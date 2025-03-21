from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class SystemInfo:
    fortiguard: Dict[str, Any] = field(default_factory=dict)
    state : Dict[str, Any] = field(default_factory=dict)
    Schema: ClassVar[Type[Schema]] = Schema