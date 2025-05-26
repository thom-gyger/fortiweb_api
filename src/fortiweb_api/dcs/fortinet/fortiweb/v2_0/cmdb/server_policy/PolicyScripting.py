from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class PolicyScripting(EndpointBase):
    text: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    scripting_name:str = field(metadata=EndpointBase.post_mark_optional)

    Schema: ClassVar[Type[Schema]] = Baseschema



    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()