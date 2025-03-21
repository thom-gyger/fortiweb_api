from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class UrlAccessRuleMatchConditionItem(EndpointBase):
    id: Optional[int] = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    reg_exp: str = field(metadata=EndpointBase.post_mark)
    type: str = field(metadata=EndpointBase.post_mark)
    reverse_match: str = field(metadata=EndpointBase.post_mark)
    sip_address_check: str = field(metadata=EndpointBase.post_mark)
    sip_address_type: str = field(metadata=EndpointBase.post_mark)
    reverse_dns_timeout: int = field(metadata=EndpointBase.post_mark)
    sip_address_value: str = field(metadata=EndpointBase.post_mark)
    sip_address_domain: str = field(metadata=EndpointBase.post_mark)
    sdomain_type: str = field(metadata=EndpointBase.post_mark)
    source_domain: str = field(metadata=EndpointBase.post_mark)
    source_domain_type: str = field(metadata=EndpointBase.post_mark)
    url_access_parameter: str = field(metadata=EndpointBase.post_mark)
    only_method_check: str = field(metadata=EndpointBase.post_mark)
    only_protocol_check: str = field(metadata=EndpointBase.post_mark)
    only_method: str = field(metadata=EndpointBase.post_mark)
    only_protocol: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema


    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()
