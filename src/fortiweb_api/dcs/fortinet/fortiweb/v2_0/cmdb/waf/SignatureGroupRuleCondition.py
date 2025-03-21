from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class SignatureGroupRuleCondition(EndpointBase):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    operator: str = field(metadata=EndpointBase.post_mark)
    request_target: str = field(metadata=EndpointBase.post_mark)
    response_target: str = field(metadata=EndpointBase.post_mark)
    threshold: int = field(metadata=EndpointBase.post_mark)
    case_sensitive: str = field(metadata=EndpointBase.post_mark)
    expression: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()