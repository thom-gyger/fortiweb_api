from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class UserRadius(EndpointBase):
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    server: str = field(metadata=EndpointBase.post_mark)
    server_port: int = field(metadata=EndpointBase.post_mark)
    secret: str = field(metadata=EndpointBase.post_mark)
    secondary_server: str = field(metadata=EndpointBase.post_mark)
    secondary_server_port: int = field(metadata=EndpointBase.post_mark)
    secondary_secret: str = field(metadata=EndpointBase.post_mark)
    nas_ip: str = field(metadata=EndpointBase.post_mark)
    auth_type: str = field(metadata=EndpointBase.post_mark)
    fac_push: str = field(metadata=EndpointBase.post_mark)


    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()



