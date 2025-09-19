import json
import os
import re
import requests
import yaml
import importlib
from typing import Type, cast, Optional, Dict, Any
from fortiweb_api.dcs.EndpointBase import EndpointBase
from marshmallow import ValidationError
import urllib3

# Suppress only the InsecureRequestWarning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class _MockResponse:
    def __init__(self, error_message: str, reason: str):
        self.text = f"Error({reason}): {error_message}"

    def json(self):
        return {self.text}

class APIException(Exception):
    def __init__(self, response: _MockResponse, status_code):
        self.response = response
        self.status_code = status_code

    def __str__(self):
        return f"{self.response.text} with status code {self.status_code}"

    @staticmethod
    def _raise_error(e) -> "APIException":
        if isinstance(e, requests.exceptions.RequestException):
            try:
                mockresponse = _MockResponse(f"{getattr(e.response, 'text', None)}", f"RequestException")
                return APIException(mockresponse, e.response.status_code)
            except:
                mockresponse = _MockResponse(f"{e}", f"RequestException")
                return APIException(mockresponse, 500)

        elif isinstance(e, requests.exceptions.ConnectTimeout) or isinstance(e, requests.exceptions.ConnectionError):
            mockresponse = _MockResponse(f"unable to connect: {e}", "ConnectTimeout")
            return APIException(mockresponse, e.response.status_code)

        elif isinstance(e, requests.exceptions.HTTPError):
            mockresponse = _MockResponse(f"HTTPError: {e}", "HTTPError")
            return APIException(mockresponse, e.response.status_code)

        elif isinstance(e, ValidationError):
            mockresponse = _MockResponse(f"Marshmallow error: {e.messages}", "ValidationError")
            return APIException(mockresponse, 0)

        else:
            mockresponse = _MockResponse(f"Unknown Error: {e}", "unknown")
            return APIException(mockresponse, 0)

def _build_url(base_url: str, endpoint: str, mkey: Optional[str] = None, sub_mkey: Optional[str] = None, kwargs: Optional[Dict[str, Any]] = None) -> str:
    params = []
    if mkey:
        params.append(f"mkey={mkey}")
    if sub_mkey:
        params.append(f"sub_mkey={sub_mkey}")
    if kwargs:
        params.extend([f"{key}={value}" for key, value in kwargs.items()])

    query_string = "&".join(params)
    return f"{base_url}{endpoint}{'&' if '?' in endpoint else '?'}{query_string}" if query_string else f"{base_url}{endpoint}"

class API:
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'endpoints.yaml')
    with open(file_path, 'r') as file:
        endpoint_data = yaml.safe_load(file)

    def __init__(self, device_ip: str, api_version: str = "v2.0", vdom=None, username=None, password=None):

        if username and password:
            self.username = username
            self.password = password
        else:
            self.username = os.getenv("FORTIWEB_USERNAME")
            self.password = os.getenv("FORTIWEB_PASSWORD")

        self.device_ip = device_ip
        self.vdom = vdom
        self.firmware = None
        self.api_version = api_version
        self.base_url = f"https://{device_ip}"
        self.url = None
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})
        self.session.verify = False  # Disable SSL verification for simplicity

        if api_version == "v2.0":
            self.base_url = f"{self.base_url}/api/v2.0/"

            # determ the firmware version of the waf
            try:
                system_status = self.get("system_status")[0]
            except APIException:
                return

            match = re.search(r"(\d+\.\d+)", system_status.firmwareVersion)
            if match:
                self.firmware = float(match.group(1))


        else:
            raise APIException(_MockResponse(f"API version {api_version} for device {device_ip} not supported", "APIException"), 0)

    def _gettoken(self):
        import json
        import base64
        if self.vdom:
            auth_dict = {"username": self.username, "password": self.password, "vdom": self.vdom}
        else:
            auth_dict = {"username": self.username, "password": self.password}

        json_string = json.dumps(auth_dict, separators=(',', ':')) + "\n"
        token = base64.b64encode(json_string.encode()).decode()
        return token

    def get(self, endpoint_name, mkey=None, sub_mkey=None, kwargs=None, raw_output=None) -> [EndpointBase]:
        endpoint = self.endpoint_data.get(self.api_version, {}).get("endpoints", {}).get(endpoint_name, {}).get("urn")
        class_path = self.endpoint_data.get(self.api_version, {}).get("endpoints", {}).get(endpoint_name, {}).get("class_path")
        *module_path, class_name = class_path.split(".")
        module = importlib.import_module(".".join(module_path))
        cls = cast(Type[EndpointBase], getattr(module, class_name))

        self.url = _build_url(self.base_url, endpoint, mkey, sub_mkey, kwargs)
        self.session.headers.update({"Authorization": self._gettoken()})
        try:
            response = self.session.get(self.url, timeout=10)
            response.raise_for_status()# Raise an exception for HTTP errors
            if raw_output:
                return response.content # for API endpoints that return Content-Type: application/raw
            if response.json().get("resutls"): # bug fix from fortiweb API response
                data = response.json()["resutls"]
            else:
                data = response.json()["results"]
            object_list = []

            if isinstance(data, list):
                for item in data:
                    item["firmware"] = self.firmware
                    endpoint_obj = cls.Schema().load(item)
                    object_list.append(endpoint_obj)
            else:
                data["firmware"] = self.firmware
                endpoint_obj = cls.Schema().load(data)
                object_list.append(endpoint_obj)

            return object_list

        except Exception as e:
            raise APIException._raise_error(e)

    def post(self, endpoint_name, data, mkey=None, sub_mkey=None, kwargs=None, isfile=False, files=None, skip_schema=None, data_workaround=None):
        endpoint = self.endpoint_data.get(self.api_version, {}).get("endpoints", {}).get(endpoint_name, {}).get("urn")
        class_path = self.endpoint_data.get(self.api_version, {}).get("endpoints", {}).get(endpoint_name, {}).get("class_path")
        *module_path, class_name = class_path.split(".")
        module = importlib.import_module(".".join(module_path))
        cls = cast(Type[EndpointBase], getattr(module, class_name))

        self.url = _build_url(self.base_url, endpoint, mkey, sub_mkey, kwargs)
        self.session.headers.update({"Authorization": self._gettoken()})
        try:
            if not isfile:
                self.session.headers.update({"Content-Type": "application/json"})
                if data_workaround:
                # Workaround for endpoints that do not accept data encapsuled inside "data": {data}, example /system/replacemessage
                    json_data = json.dumps(data)
                else:
                    json_data = json.dumps({"data": data})
                response = self.session.post(self.url, data=json_data, timeout=10)
                response.raise_for_status()  # Raise an exception for HTTP errors
                data = response.json()["results"]
                if skip_schema:
                    # # Workaround for endpoints that do not return the object as a response to a put, example /system/replacemessage
                    endpoint_obj = data
                else:
                    data["firmware"] = self.firmware
                    endpoint_obj = cls.Schema().load(data)
                return endpoint_obj
            else:
                if "Content-Type" in self.session.headers:
                    del self.session.headers["Content-Type"]
                if files:

                    response = self.session.post(self.url, files=files, data=data, timeout=10)
                else:
                    response = self.session.post(self.url, files=data, timeout=10)
                response.raise_for_status()

        except Exception as e:
            raise APIException._raise_error(e)

    def put(self, endpoint_name, data, mkey=None, sub_mkey=None, kwargs=None, skip_schema=None, data_workaround=None):
        endpoint = self.endpoint_data.get(self.api_version, {}).get("endpoints", {}).get(endpoint_name, {}).get("urn")
        class_path = self.endpoint_data.get(self.api_version, {}).get("endpoints", {}).get(endpoint_name, {}).get("class_path")
        *module_path, class_name = class_path.split(".")
        module = importlib.import_module(".".join(module_path))
        cls = cast(Type[EndpointBase], getattr(module, class_name))

        self.url = _build_url(self.base_url, endpoint, mkey, sub_mkey, kwargs)
        self.session.headers.update({"Authorization": self._gettoken(), "Content-Type": "application/json"})
        try:
            if data_workaround:
                # Workaround for endpoints that do not accept data encapsuled inside "data": {data}, example /system/config.fortiguard
                json_data = json.dumps(data)
            else:
                json_data = json.dumps({"data": data})
            response = self.session.put(self.url, data=json_data, timeout=10)
            data = response.json()["results"]
            response.raise_for_status()  # Raise an exception for HTTP errors
            if skip_schema:
                # Workaround for endpoints that do not return the object as a response to a put, example /system/maintenance.systemtime
                endpoint = data
            else:
                data["firmware"] = self.firmware
                endpoint = cls.Schema().load(data)

            return endpoint

        except Exception as e:
            raise APIException._raise_error(e)
        
    def delete(self, endpoint_name, mkey=None, sub_mkey=None, kwargs=None) -> None:
        endpoint = self.endpoint_data.get(self.api_version, {}).get("endpoints", {}).get(endpoint_name, {}).get("urn")
        class_path = self.endpoint_data.get(self.api_version, {}).get("endpoints", {}).get(endpoint_name, {}).get("class_path")
        *module_path, class_name = class_path.split(".")
        module = importlib.import_module(".".join(module_path))
        cls = cast(Type[EndpointBase], getattr(module, class_name))

        self.url = _build_url(self.base_url, endpoint, mkey, sub_mkey, kwargs)
        self.session.headers.update({"Authorization": self._gettoken()})
        try:
            response = self.session.delete(self.url, timeout=10)
            response.raise_for_status()  # Raise an exception for HTTP errors

        except Exception as e:
            raise APIException._raise_error(e)

    def get_endpoint_url(self, endpoint_name) -> str:
        endpoint = self.endpoint_data.get(self.api_version, {}).get("endpoints", {}).get(endpoint_name, {}).get("urn")
        url = f"{self.base_url}{endpoint}"
        return url