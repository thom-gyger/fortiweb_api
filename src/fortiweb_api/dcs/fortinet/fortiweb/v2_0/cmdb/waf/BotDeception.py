from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class BotDeception(EndpointBase):
    from .BotDeceptionUrlItem import BotDeceptionUrlItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    deception_url: str = field(metadata=EndpointBase.post_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    block_period: int = field(metadata=EndpointBase.post_mark)
    severity: str = field(metadata=EndpointBase.post_mark)
    trigger: str = field(metadata=EndpointBase.post_mark)
    exception: str = field(metadata=EndpointBase.post_mark)
    sz_url_list: int

    url_list: List[BotDeceptionUrlItem] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema


    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()



