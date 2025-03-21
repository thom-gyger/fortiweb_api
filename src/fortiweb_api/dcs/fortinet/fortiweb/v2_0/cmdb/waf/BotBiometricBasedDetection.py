from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class BotBiometricBasedDetection(EndpointBase):
    from .BotBiometricBasedDetectionUrlItem import BotBiometricBasedDetectionUrlItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    mouse_movement: str = field(metadata=EndpointBase.post_mark)
    page_focus: str = field(metadata=EndpointBase.post_mark)
    click: str = field(metadata=EndpointBase.post_mark)
    keyboard: str = field(metadata=EndpointBase.post_mark)
    screen_touch: str = field(metadata=EndpointBase.post_mark)
    scroll: str = field(metadata=EndpointBase.post_mark)
    bot_traits: str = field(metadata=EndpointBase.post_mark)
    bot_traits_num: int
    event_collection_time: int = field(metadata=EndpointBase.post_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    bot_effective_time: int = field(metadata=EndpointBase.post_mark)
    severity: str = field(metadata=EndpointBase.post_mark)
    trigger: str = field(metadata=EndpointBase.post_mark)
    exception: str = field(metadata=EndpointBase.post_mark)
    sz_url_list: int

    url_list: List[BotBiometricBasedDetectionUrlItem] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema


    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()



