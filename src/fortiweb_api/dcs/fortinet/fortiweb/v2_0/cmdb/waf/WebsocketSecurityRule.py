from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class WebsocketSecurityRule(EndpointBase):
    from .WebsocketSecurityRuleAllowOriginItem import WebsocketSecurityRuleAllowOriginItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    host_status: str = field(metadata=EndpointBase.post_mark)
    host: str = field(metadata=EndpointBase.post_mark)
    url_type: str = field(metadata=EndpointBase.post_mark)
    url: str = field(metadata=EndpointBase.post_mark)
    block_websocket_traffic: str = field(metadata=EndpointBase.post_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    max_frame_size: int = field(metadata=EndpointBase.post_mark)
    max_message_size: int = field(metadata=EndpointBase.post_mark)
    block_extensions: str = field(metadata=EndpointBase.post_mark)
    enable_attack_signatures: str = field(metadata=EndpointBase.post_mark)
    allow_plain_text: str = field(metadata=EndpointBase.post_mark)
    allow_binary_text: str = field(metadata=EndpointBase.post_mark)
    sz_allowed_origin_list: int

    allowed_origin_list: List[Dict[str, WebsocketSecurityRuleAllowOriginItem]] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()
