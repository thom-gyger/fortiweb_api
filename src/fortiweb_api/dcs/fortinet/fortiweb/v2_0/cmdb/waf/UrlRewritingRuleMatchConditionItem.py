from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class UrlRewritingRuleMatchConditionItem(EndpointBase):
    id: Optional[int] = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    object: str = field(metadata=EndpointBase.post_mark)
    reg_exp: str = field(metadata=EndpointBase.post_mark)
    is_essential: str = field(metadata=EndpointBase.post_mark)
    reverse_match: str = field(metadata=EndpointBase.post_mark)
    protocol_filter: str = field(metadata=EndpointBase.post_mark)
    HTTP_protocol: str = field(metadata=EndpointBase.post_mark)
    content_type_filter: str = field(metadata=EndpointBase.post_mark)
    content_type_set: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()