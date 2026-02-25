# Introduction
This package provides an abstraction of the FortiWeb WAF API to easily interact with the devices.
Each API call returns a list of objects that represent a configuration object of the WAF.

# Usage

## REST API

**GET**
```python
from fortiweb_api.API import API
device = "10.10.10.10"
waf = API(device, vdom="root", username="yourusername", password="yourpassword")
serverpolicy = waf.get("server_policy", mkey="sp_abc") # returns one Object [<ServerPolicy>]
serverpolicies = waf.get("server_policy") # returns all Objects [<ServerPolicy>, <ServerPolicy> ...]

#serialize
#==========================================================
#each object inherits from <EnpointBase> which provides the serialize() method
#there are 3 serialization possibilities

#1
#====================
serverpolicy[0].serialize() #This is serializing with all the fields that are post/put relevant. So, for example q_ref field is NOT in the output.

#2
#====================
serverpolicy[0].serialize(all_fields=True) # This is serializing all fields.

#3
#====================
serverpolicy[0].serialize(all_fields_nested=True) # This is serializing all fields, even there are nested objects.

```

**POST**
```python
from fortiweb_api.API import API
device = "10.10.10.10"
waf = API(device, vdom="root", username="yourusername", password="yourpassword")
bmp = waf.get("bot_mitigation_policy", mkey="bmp_abc") # returns one Object
bmp[0].name = "cloned_bmp" # instead of making a new object we are getting an existing one, change the name and post it. In fact, we are cloning it.

waf.post("bot_mitigation_policy", bmp[0].serialize())

#of course, if you want to create a new endpoint instead of cloning an existing one you can do it as follows:
data = {"name": "bmpX",
        "bot_deception": "bdX",
        "biometrics_based_detection": "bbdX",
        "threshold_based_detection": "tbdX",
        "known_bots": "kbX",
        "exception": "exX"
    }
#creat a new Endpoint Object, validate it and POST it
from fortiweb_api.dcs.fortinet.fortiweb.v2_0.cmdb.waf.BotMitigationPolicy import BotMitigationPolicy
bmp_schema = BotMitigationPolicy
bmp = bmp_schema.Schema().load(json.dumps(data)) # Schema is verified and Endpointobject is instantiated
waf.post("bot_mitigation_policy", bmp.serialize())

#do not validate and POST it
waf.post("bot_mitigation_policy", json.dumps(data))
```


**PUT**

You are about to edit an existing object. To perform a PUT request, you need to use the `mkey=` parameter when invoking the `put()` method.

The endpoint object provides a method `key_field()` that returns the relevant attribute name to be used for the `mkey` parameter.
```python
from fortiweb_api.API import API
device = "10.10.10.10"
waf = API(device, vdom="root", username="yourusername", password="yourpassword")
bmp = waf.get("bot_mitigation_policy", mkey="bmp_abc") # returns one Object

#make the Change
bmp[0].biometrics_based_detection = "bbdY"

#get the key field value used for mkey param
key_field = bmp[0].key_field()
key_field_value = gettattr(bmp[0], key_field)

#apply the change
changed_bmp = waf.put("bot_mitigation_policy", mkey=key_field_value) # this will return a list with the changed Endpoint

```

**DELETE**
```python
from fortiweb_api.API import API
device = "10.10.10.10"
waf = API(device, vdom="root", username="yourusername", password="yourpassword")
waf.delete("bot_mitigation_policy", mkey="bmp_abc")
```

**about endpointnames**
in folder ```src/fortiweb_api``` you can view all the available endpoint names

```yaml
server_policy: #<---- ep_name
      urn: "cmdb/server-policy/policy"
      class_path: "fortiweb_api.dcs.fortinet.fortiweb.v2_0.cmdb.server_policy.ServerPolicy.ServerPolicy"
server_policy_content_routing_item: #<---- ep_name
    urn: "cmdb/server-policy/policy/http-content-routing-list"
    class_path: "fortiweb_api.dcs.fortinet.fortiweb.v2_0.cmdb.server_policy.ServerPolicyContentRoutingItem.ServerPolicyContentRoutingItem"
...

```
<br>

**Specialities**

<u>Firmware compatibility:</u>
Due to the variety of FortiWeb releases, some endpoints may have different or additional fields. For example, the endpoint "FileSecurityRule" includes the attribute "octet_stream_filename_headers", which does not exist in all FortiWeb firmware versions.

The data class uses metadata to declare the firmware release for which an attribute is relevant. Consider the following file:
 `src/fortinet/fortiweb_api/v2_0/cmdb/waf/FileSecurityRule.py`:

```python
octet_stream_filename_headers: str = field(metadata={"firmware":"<7.6"} | EndpointBase.post_mark)
```

To ensure safe validation during Schema().load() of an API.get() call, the base schema checks the firmware attribute in the received JSON to determine whether a missing attribute is acceptable.

The firmware version is evaluated during the initialization of the API and is added to each JSON response during get().

Process flow:
API initialization -> get firmware -> get(file_security_rule) -> add firmware field to JSON -> Schema().load(JSON)

what if you now want to post the endpoint object (resceived from Fortiweb 7.6) to another Fortiweb which is running a Firmware lowe than 7.6?
You first need, to add the desired attribute(s) to that Object:
```python
setattr(ep_object_from_v7_6, "octet_stream_filename_headers", "your value")
configured_object = Device_v7_4.post("file_security_rule", ep_object_from_v7_4.serialize())
```

<u>File Uploading</u>
... to be described


## CLI API
There are things you cant do with regular RestAPI calls. For example, if you want to access a complete Certificate including the Private-Key. For this, you can use the CLI-API.

... to be dercibed