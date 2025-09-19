import os
import yaml
from ttp import ttp
from jinja2 import Environment, FileSystemLoader
from netmiko import ConnectHandler
import re


class Helpers:
    @classmethod
    def parse_data(cls, data, ttp_template_name: str)-> dict:

        def unpacker(d):
            if isinstance(d, list) and len(d) == 1:
                return unpacker(d[0])
            else:
                return d

        file_path = f"{os.path.dirname(__file__)}/templates/ttp/{ttp_template_name}"
        with open(file_path, 'r') as file:
            ttp_template = file.read()
        parser = ttp(data=data, template=ttp_template)
        parser.parse()
        result = parser.result()[0]
        unpacked = unpacker(result)
        return unpacked

    @classmethod
    def render_data(cls, data, config_template: str) -> str:
        env = Environment(loader=FileSystemLoader(f"{os.path.dirname(__file__)}/templates/config"))
        template = env.get_template(config_template)
        rendered = template.render(item=data)
        return rendered

class CliAPI:
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, 'endpoints.yaml')

    with open(file_path, 'r') as file:
        endpoint_data = yaml.safe_load(file)

    def __init__(self, waf_ip: str, vdom=None, username=None, password=None, fast_cli=None, debug=None):
        self.waf_ip = re.sub(r":\d+$", "", waf_ip)

        if username and password:
            self.username = username
            self.password = password
        else:
            self.username = os.getenv("FORTIWEB_USERNAME")
            self.password = os.getenv("FORTIWEB_PASSWORD")
        self.vdom = vdom
        if fast_cli:
            self.fast_cli = fast_cli
            self.device = {"device_type": "terminal_server","host": self.waf_ip,"username": self.username,"password": self.password, "fast_cli": True,}
        else:
            self.fast_cli = False
        if debug:
            self.device = {"device_type": "terminal_server","host": self.waf_ip,"username": self.username,"password": self.password,"session_log": "./cliapi_output_log.txt"}
        else:
            self.device = {"device_type": "terminal_server","host": self.waf_ip,"username": self.username,"password": self.password,}
    def get(self, endpoint_name:str, sub_element=None):
        endpoint = self.endpoint_data["default"].get(endpoint_name)
        command = endpoint.get("command")
        if sub_element:
            command = f"{command} {sub_element}"
        ttp_template_name = endpoint.get("ttp_template")

        connection = ConnectHandler(**self.device)
        connection.find_prompt()
        expect_string = r".*\# "

        try:
            if self.vdom:
                expect_string = r".*\(.*\) \# "
                if self.vdom == "global":
                    connection.send_command("config global\n", expect_string=expect_string)
                else:
                    connection.send_command("config vdom\n", expect_string=expect_string)
                    connection.send_command(f"edit {self.vdom}\n", expect_string=expect_string)

            output = connection.send_command(command, expect_string=expect_string)
            connection.disconnect()

            parsed_data= Helpers.parse_data(output, ttp_template_name)
            return parsed_data

        except Exception as e:
            connection.disconnect()
            print(f"get CLI Errror!!:{e}")
            raise e

    def post(self, endpoint_name:str, data, direct_command=False):

        connection = ConnectHandler(**self.device)
        connection.find_prompt()
        expect_configmode_string = r".*\(.*\) \# "
        expect_normalmode_string = r".*\# "

        try:
            if self.vdom:
                if self.vdom == "global":
                    connection.send_command("config global\n", expect_string=expect_configmode_string)
                else:
                    connection.send_command("config vdom\n", expect_string=expect_configmode_string)
                    connection.send_command(f"edit {self.vdom}\n", expect_string=expect_configmode_string)

            if not direct_command:
                endpoint = self.endpoint_data["default"].get(endpoint_name)
                config = Helpers.render_data(data, endpoint.get("config_template"))
                output = connection.send_config_set(config, exit_config_mode=False, enter_config_mode=False, terminator= expect_normalmode_string, cmd_verify=False, error_pattern="Command fail. CLI parsing error.")
            elif self.fast_cli:
                output = connection.send_config_set(data, exit_config_mode=False, enter_config_mode=False, terminator= expect_normalmode_string, cmd_verify=False, error_pattern="Command fail. CLI parsing error.",
                                                    delay_factor=0.1,
                                                    max_loops=50,
                                                    strip_command=False,
                                                    strip_prompt=False,
                                                    read_timeout=10)
            else:
                output = connection.send_config_set(data, exit_config_mode=False, enter_config_mode=False, terminator= expect_normalmode_string, cmd_verify=False, error_pattern="Command fail. CLI parsing error.")

            connection.disconnect()
            return output

        except Exception as e:
            connection.disconnect()
            print(f"post CLI Errror!!:{e}")
            raise e

