from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class ParameterInputRuleItem(EndpointBase):
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

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()