from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class CorsProtectionRule(EndpointBase):
    from .CorsProtectionRuleAllowedHeadersItem import CorsProtectionRuleAllowedHeadersItem
    from .CorsProtectionRuleExposedHeadersItem import CorsProtectionRuleExposedHeadersItem
    from .CorsProtectionRuleAllowedMethodsItem import CorsProtectionRuleAllowedMethodsItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    host_status: str = field(metadata=EndpointBase.post_mark)
    host: str = field(metadata=EndpointBase.post_mark)
    request_type: str = field(metadata=EndpointBase.post_mark)
    request_file: str = field(metadata=EndpointBase.post_mark)
    block_cors_traffic: str = field(metadata=EndpointBase.post_mark)
    allowed_origins_list: str = field(metadata=EndpointBase.post_mark)
    allowed_methods: str = field(metadata=EndpointBase.post_mark)
    sz_allowed_methods_list: int
    allowed_headers: str = field(metadata=EndpointBase.post_mark)
    sz_allowed_headers_list: int
    exposed_headers: str  = field(metadata=EndpointBase.post_mark)
    sz_exposed_headers_list: int
    remove_other_headers: str  = field(metadata=EndpointBase.post_mark)
    allowed_credentials: str  = field(metadata=EndpointBase.post_mark)
    allowed_maximum_age: int  = field(metadata=EndpointBase.post_mark)

    allowed_methods_list: List[CorsProtectionRuleAllowedMethodsItem] = field(default_factory=list)
    allowed_headers_list: List[CorsProtectionRuleAllowedHeadersItem] = field(default_factory=list)
    exposed_headers_list: List[CorsProtectionRuleExposedHeadersItem] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()