from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class ServerPoolHealthCheck(EndpointBase):
    from .ServerPoolHealthCheckItem import ServerPoolHealthCheckItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    trigger_policy: str = field(metadata=EndpointBase.post_mark)
    relationship: str = field(metadata=EndpointBase.post_mark)
    role: str = field(metadata=EndpointBase.post_mark)
    group_id: int = field(metadata=EndpointBase.post_mark)
    sz_health_list: int = field(metadata=EndpointBase.post_mark)

    healt_list: Optional[List[ServerPoolHealthCheckItem]] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema


    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = ['protocol']
        return super().get_post_json_template()



