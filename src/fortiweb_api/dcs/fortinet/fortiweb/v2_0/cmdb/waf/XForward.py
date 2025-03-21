from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class XForward(EndpointBase):
    from .XForwardIp import XForwardIp
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    x_forwarded_for_support: str = field(metadata=EndpointBase.post_mark)
    ip_location_add: str = field(metadata=EndpointBase.post_mark)
    add_source_port: str = field(metadata=EndpointBase.post_mark)
    x_forwarded_port: str = field(metadata=EndpointBase.post_mark)
    tracing_original_ip: str = field(metadata=EndpointBase.post_mark)
    original_ip_header: str = field(metadata=EndpointBase.post_mark)
    x_real_ip: str = field(metadata=EndpointBase.post_mark)
    x_forwarded_proto: str = field(metadata=EndpointBase.post_mark)
    x_forwarded_proto_val: str = field(metadata=EndpointBase.post_mark)
    sz_ip_list: int
    delete_headers: str = field(metadata=EndpointBase.post_mark)
    merge_headers: str = field(metadata=EndpointBase.post_mark)
    block_based_on_original_ip: str = field(metadata=EndpointBase.post_mark)
    block_based_on_original_ip_val: str = field(metadata=EndpointBase.post_mark)
    ip_location: str = field(metadata=EndpointBase.post_mark)
    skip_private_original_ip: str = field(metadata=EndpointBase.post_mark)
    skip_special_original_ip: str = field(metadata=EndpointBase.post_mark)
    block_based_on_full_scan: str = field(metadata=EndpointBase.post_mark)

    ip_list: List[XForwardIp] = field(default_factory=list)

    Schema: ClassVar[Type[Schema]] = Schema

