from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class SnmpCommunity(EndpointBase):
    from .SnmpCommunityHostItem import SnmpCommunityHostItem
    id: int = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    q_ref: int
    name: str = field(metadata=EndpointBase.post_mark)
    status: str = field(metadata=EndpointBase.post_mark)
    query_v1_status: str = field(metadata=EndpointBase.post_mark)
    query_v1_port: int = field(metadata=EndpointBase.post_mark)
    query_v2c_status: str = field(metadata=EndpointBase.post_mark)
    query_v2c_port: int = field(metadata=EndpointBase.post_mark)
    trap_v1_status: str = field(metadata=EndpointBase.post_mark)
    trap_v1_lport: int = field(metadata=EndpointBase.post_mark)
    trap_v1_rport: int = field(metadata=EndpointBase.post_mark)
    trap_v2c_status: str = field(metadata=EndpointBase.post_mark)
    trap_v2c_lport: int = field(metadata=EndpointBase.post_mark)
    trap_v2c_rport: int = field(metadata=EndpointBase.post_mark)
    events: str = field(metadata=EndpointBase.post_mark)
    sz_hosts: int
    host_list: Optional[List[SnmpCommunityHostItem]] = field(default_factory=list)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

