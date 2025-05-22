from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field, fields

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class Policy(EndpointBase):
    id: int = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    src: str = field(metadata=EndpointBase.post_mark)
    dst: str = field(metadata=EndpointBase.post_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    gateway: str = field(metadata=EndpointBase.post_mark)
    iif: str = field(metadata=EndpointBase.post_mark)
    oif: str = field(metadata=EndpointBase.post_mark)
    priority: int = field(metadata=EndpointBase.post_mark)
    fwmark: int = field(metadata=EndpointBase.post_mark)

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

