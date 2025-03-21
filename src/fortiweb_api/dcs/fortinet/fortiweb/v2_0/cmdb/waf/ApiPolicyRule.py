from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class ApiPolicyRule(EndpointBase):
    from .ApiPolicyRuleAttachHttpHeaderItem import ApiPolicyRuleAttachHttpHeaderItem
    from .ApiPolicyRuleMatchUrlPrefixesItem import ApiPolicyRuleMatchUrlPrefixesItem
    from .ApiPolicyRuleSubUrlSettingItem import ApiPolicyRuleSubUrlSettingItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    api_key_verification: str = field(metadata=EndpointBase.post_mark)
    allow_user_group: str = field(metadata=EndpointBase.post_mark)
    api_key_location: str = field(metadata=EndpointBase.post_mark)
    header_field_name: str = field(metadata=EndpointBase.post_mark)
    parameter_name: str = field(metadata=EndpointBase.post_mark)
    rate_limit_period: int = field(metadata=EndpointBase.post_mark)
    rate_limit_requests: int = field(metadata=EndpointBase.post_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    block_period: int = field(metadata=EndpointBase.post_mark)
    severity: str = field(metadata=EndpointBase.post_mark)
    trigger_policy: str = field(metadata=EndpointBase.post_mark)
    host: str = field(metadata=EndpointBase.post_mark)
    host_status: str = field(metadata=EndpointBase.post_mark)
    rate_limit_user_period: int = field(metadata=EndpointBase.post_mark)
    rate_limit_user_requests: int = field(metadata=EndpointBase.post_mark)
    x_ratelimit_headers: str = field(metadata=EndpointBase.post_mark)
    sz_attach_http_header: int
    sz_match_url_prefixes: int
    sz_sub_url_setting: int

    attach_http_header: List[ApiPolicyRuleAttachHttpHeaderItem] = field(default_factory=list)
    match_url_prefixes: List[ApiPolicyRuleMatchUrlPrefixesItem] = field(default_factory=list)
    sub_url_setting: List[ApiPolicyRuleSubUrlSettingItem] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()



