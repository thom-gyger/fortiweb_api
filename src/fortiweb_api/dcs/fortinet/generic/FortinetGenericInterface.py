from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class Interface(EndpointBase):
    id: int
    can_view: int
    q_ref: int
    q_ref_string: Optional[str]
    can_clone: int
    q_type: int
    name: str
    type: str
    ip: str
    ip6: str
    allowaccess: str
    status: str
    mode: str
    ip6_mode: str
    vlanid: int
    vlanproto: str
    interface: str
    description: str
    lacp_speed: str
    algorithm: str
    intf: str
    modename: str
    ip6_allowaccess: str
    adom: str
    wccp: str
    azure_endpoint: int
    mtu: int
    dynamic_gateway: str
    dynamic_dns1: str
    dynamic_dns2: str

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


