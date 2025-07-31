from typing import List, Dict, Type, ClassVar, Optional
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class Backup(EndpointBase):
    affected: Optional[int]

    Schema: ClassVar[Type[Schema]] = Baseschema