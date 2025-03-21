from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class ParameterInputRule(EndpointBase):
    from .ParameterInputRuleItem import ParameterInputRuleItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    host: str = field(metadata=EndpointBase.post_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    block_period: int = field(metadata=EndpointBase.post_mark)
    severity: str = field(metadata=EndpointBase.post_mark)
    trigger: str = field(metadata=EndpointBase.post_mark)
    request_type: str = field(metadata=EndpointBase.post_mark)
    request_file: str = field(metadata=EndpointBase.post_mark)
    host_status: str = field(metadata=EndpointBase.post_mark)
    flag: int
    maximum_parameter_number: int = field(metadata=EndpointBase.post_mark)
    json_parameter_support: str = field(metadata=EndpointBase.post_mark)
    sz_rule_list: int

    rule_list: List[ParameterInputRuleItem] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()
