from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class ServerPoolPersistence(EndpointBase):
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    type: str = field(metadata=EndpointBase.post_mark)
    cookie_name: str = field(metadata=EndpointBase.post_mark)
    timeout: int = field(metadata=EndpointBase.post_mark)
    ipv4_netmask: str = field(metadata=EndpointBase.post_mark)
    ipv6_mask_length: int = field(metadata=EndpointBase.post_mark)
    http_header: str = field(metadata=EndpointBase.post_mark)
    url_parameter: str = field(metadata=EndpointBase.post_mark)
    cookie_path: str = field(metadata=EndpointBase.post_mark)
    cookie_domain: str = field(metadata=EndpointBase.post_mark)
    secure_cookie: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

