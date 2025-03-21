from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class ServerPool(EndpointBase):
    from .ServerPoolPserverItem import ServerPoolPserverItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    type: str = field(metadata=EndpointBase.post_mark)
    protocol: str = field(metadata=EndpointBase.post_mark)
    server_balance: str = field(metadata=EndpointBase.post_mark)
    health: str = field(metadata=EndpointBase.post_mark)
    hlck_sip: str = field(metadata=EndpointBase.post_mark)
    hlck_sip6: str = field(metadata=EndpointBase.post_mark)
    lb_algo: str = field(metadata=EndpointBase.post_mark)
    persistence: str = field(metadata=EndpointBase.post_mark)
    comment: str = field(metadata=EndpointBase.post_mark)
    flag: int
    #server_pool_id: str
    sub_table_id: int
    sub_table_action: str
    http_reuse: str = field(metadata=EndpointBase.post_mark)
    reuse_conn_total_time: int = field(metadata=EndpointBase.post_mark)
    reuse_conn_idle_time: int = field(metadata=EndpointBase.post_mark)
    reuse_conn_max_request: int = field(metadata=EndpointBase.post_mark)
    reuse_conn_max_count: int = field(metadata=EndpointBase.post_mark)
    adfs_server_name: str = field(metadata=EndpointBase.post_mark)
    sz_pserver_list: int

    pserver_list: Optional[List[ServerPoolPserverItem]] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()
