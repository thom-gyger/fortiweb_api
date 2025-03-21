from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class InputRuleList(EndpointBase):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    argument_type: str = field(metadata=EndpointBase.post_mark)
    type_checked: str = field(metadata=EndpointBase.post_mark)
    argument_name_type: str = field(metadata=EndpointBase.post_mark)
    argument_name: str = field(metadata=EndpointBase.post_mark)
    argument_expression: str = field(metadata=EndpointBase.post_mark)
    max_length: int = field(metadata=EndpointBase.post_mark)
    location: str = field(metadata=EndpointBase.post_mark)
    from_json: str = field(metadata=EndpointBase.post_mark)
    is_essential: str = field(metadata=EndpointBase.post_mark)
    data_type: str = field(metadata=EndpointBase.post_mark)
    custom_data_type: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Schema

@mdc(base_schema=Baseschema)
class InputRule(EndpointBase):
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

    rule_list: List[InputRuleList] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Schema

