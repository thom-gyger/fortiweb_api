from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class Replacemsg(EndpointBase):
    from .ReplacemsgPageListItem import ReplacemsgPageListItem
    id: int
    q_ref: int
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    ajax_block_support: str = field(metadata=EndpointBase.post_mark)
    sz_page_list: int = field(metadata=EndpointBase.post_mark)
    page_list: Optional[List[ReplacemsgPageListItem]] = field(default_factory=list)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

