from typing import List, Dict, Type, ClassVar
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class Vdoms(EndpointBase):
    name: str
    can_delete: int

    Schema: ClassVar[Type[Schema]] = Baseschema