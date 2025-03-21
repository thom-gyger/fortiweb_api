from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class MitbRule(EndpointBase):
    from .MitbRuleDomainItem import MitbRuleDomainItem
    from .MitbRuleParameterItem import MitbRuleParameterItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    severity: str = field(metadata=EndpointBase.post_mark)
    trigger: str = field(metadata=EndpointBase.post_mark)
    host_status: str = field(metadata=EndpointBase.post_mark)
    host: str = field(metadata=EndpointBase.post_mark)
    request_type: str = field(metadata=EndpointBase.post_mark)
    request_url: str = field(metadata=EndpointBase.post_mark)
    post_url: str = field(metadata=EndpointBase.post_mark)
    sz_protected_parameter_list: int
    sz_allowed_external_domains_list: int

    protected_parameter_list: List[MitbRuleParameterItem] = field(default_factory=list)
    allowed_external_domains_list: List[MitbRuleDomainItem] = field(default_factory=list)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

