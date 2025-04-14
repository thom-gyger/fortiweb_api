from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class NetworkOption(EndpointBase):
    tcp_timestamp: str = field(metadata=EndpointBase.post_mark)
    ip_src_balance: str = field(metadata=EndpointBase.post_mark)
    ip6_src_balance: str = field(metadata=EndpointBase.post_mark)
    tcp_buffer: str = field(metadata=EndpointBase.post_mark)
    arp_ignore: str = field(metadata=EndpointBase.post_mark)
    loopback_mtu: int = field(metadata=EndpointBase.post_mark)
    tcp_usertimeout: int = field(metadata=EndpointBase.post_mark)
    tcp_keepcnt: int = field(metadata=EndpointBase.post_mark)
    tcp_keepidle: int = field(metadata=EndpointBase.post_mark)
    tcp_keepintvl: int = field(metadata=EndpointBase.post_mark)
    loopback_tso_gso: str = field(metadata=EndpointBase.post_mark)
    route_priority: str = field(metadata=EndpointBase.post_mark)
    dns_priority: str = field(metadata=EndpointBase.post_mark)
    dns_cache_timeout: int = field(metadata=EndpointBase.post_mark)
    tcp_mtu_probing: str = field(metadata=EndpointBase.post_mark)
    ipfrag_high_thresh: int = field(metadata=EndpointBase.post_mark)
    ipfrag_low_thresh: int = field(metadata=EndpointBase.post_mark)
    ipfrag_timeout: int = field(metadata=EndpointBase.post_mark)
    ip6frag_high_thresh: int = field(metadata=EndpointBase.post_mark)
    ip6frag_low_thresh: int = field(metadata=EndpointBase.post_mark)
    ip6frag_timeout: int = field(metadata=EndpointBase.post_mark)
    ip_local_port_warning_threshold: str = field(metadata=EndpointBase.post_mark)
    ip_local_port_assign_ex: str = field(metadata=EndpointBase.post_mark)
    nf_conntrack_tcp_timeout_established: int = field(metadata=EndpointBase.post_mark)
    gro_normal_batch: int = field(metadata=EndpointBase.post_mark)
    
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

