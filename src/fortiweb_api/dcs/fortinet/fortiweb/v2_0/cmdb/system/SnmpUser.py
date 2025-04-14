from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class SnmpUser(EndpointBase):
    from .SnmpUserHostItem import SnmpUserHostItem
    q_ref: int
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    status: str = field(metadata=EndpointBase.post_mark)
    security_level: str = field(metadata=EndpointBase.post_mark)
    auth_proto: str = field(metadata=EndpointBase.post_mark)
    auth_pwd: str = field(metadata=EndpointBase.post_mark)
    priv_proto: str = field(metadata=EndpointBase.post_mark)
    priv_pwd: str = field(metadata=EndpointBase.post_mark)
    query_status: str = field(metadata=EndpointBase.post_mark)
    query_port: int = field(metadata=EndpointBase.post_mark)
    trap_status: str = field(metadata=EndpointBase.post_mark)
    trapport_local: int = field(metadata=EndpointBase.post_mark)
    trapport_remote: int = field(metadata=EndpointBase.post_mark)
    trapevent: str = field(metadata=EndpointBase.post_mark)
    sz_hosts: int
    host_list: Optional[List[SnmpUserHostItem]] = field(default_factory=list)

    
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

