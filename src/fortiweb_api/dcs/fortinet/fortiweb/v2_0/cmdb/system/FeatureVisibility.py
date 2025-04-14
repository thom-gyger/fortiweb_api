from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class FeatureVisibility(EndpointBase):
    ftp_security: str = field(metadata=EndpointBase.post_mark)
    ztna: str = field(metadata=EndpointBase.post_mark)
    traffic_mirror: str = field(metadata=EndpointBase.post_mark)
    mobile_app_identification: str = field(metadata=EndpointBase.post_mark)
    adfs_policy: str = field(metadata=EndpointBase.post_mark)
    acceleration_policy: str = field(metadata=EndpointBase.post_mark)
    web_cache: str = field(metadata=EndpointBase.post_mark)
    support_ajax_requests: str = field(metadata=EndpointBase.post_mark)
    wccp_mode: str = field(metadata=EndpointBase.post_mark)
    wvs: str = field(metadata=EndpointBase.post_mark)
    wvs_val: str = field(metadata=EndpointBase.post_mark)
    api_gateway: str = field(metadata=EndpointBase.post_mark)
    firewall: str = field(metadata=EndpointBase.post_mark)
    padding_oracle: str = field(metadata=EndpointBase.post_mark)
    wad: str = field(metadata=EndpointBase.post_mark)
    fortigate_integration: str = field(metadata=EndpointBase.post_mark)
    support_icap_server: str = field(metadata=EndpointBase.post_mark)
    debug_log: str = field(metadata=EndpointBase.post_mark)
    recaptcha: str = field(metadata=EndpointBase.post_mark)
    cryptographic_key: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

