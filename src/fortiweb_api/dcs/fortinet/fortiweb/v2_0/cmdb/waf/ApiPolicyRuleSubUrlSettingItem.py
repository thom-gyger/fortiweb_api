from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class ApiPolicyRuleSubUrlSettingItem(EndpointBase):
    id: Optional[int] = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    http_method: str = field(metadata=EndpointBase.post_mark)
    type: str = field(metadata=EndpointBase.post_mark)
    url_expression: str = field(metadata=EndpointBase.post_mark)
    api_key_verification: str = field(metadata=EndpointBase.post_mark)
    api_key_location: str = field(metadata=EndpointBase.post_mark)
    header_field_name: str = field(metadata=EndpointBase.post_mark)
    parameter_name: str = field(metadata=EndpointBase.post_mark)
    rate_limit_period: int = field(metadata=EndpointBase.post_mark)
    rate_limit_requests: int = field(metadata=EndpointBase.post_mark)
    allow_user_group: str = field(metadata=EndpointBase.post_mark)
    api_key_inherit: str = field(metadata=EndpointBase.post_mark)
    rate_limit_user_period: int = field(metadata=EndpointBase.post_mark)
    rate_limit_user_requests: int = field(metadata=EndpointBase.post_mark)



    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()



