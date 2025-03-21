from typing import Optional, Dict, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from BaseSchema import Baseschema


from fortiweb_api.dcs.fortinet.fortiweb.v2_0.cmdb.system.Vip import Vip
from SystemInfo import SystemInfo
from Vdom import Vdom
from fortiweb_api.dcs.fortinet.generic.FortinetGenericInterface import FortinetGenericInterface

@mdc(base_schema=Baseschema)
class ConfigItems:
    interfaces: Dict[str, FortinetGenericInterface] = field(default_factory=dict)
    vips: Dict[str, Vip] = field(default_factory=dict)
    vdoms: Dict[str, Vdom] = field(default_factory=dict)
    system_infos: SystemInfo
    Schema: ClassVar[Type[Schema]] = Schema

@mdc(base_schema=Baseschema)
class IpAddress:
    name: str
    address: str
    sot_id: str

@mdc(base_schema=Baseschema)
class FortiwebGenericDevices:
    name: str
    sot_id: str
    location: str
    role: str
    platform: str
    tenant: str
    manufacturer: str
    serial: Optional[str]
    device_type: str
    ip_address: IpAddress
    config_items: ConfigItems
    Schema: ClassVar[Type[Schema]] = Schema

