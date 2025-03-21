from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class MitbRuleParameterItem(EndpointBase):
    #id: str = field(metadata=EndpointBase.post_mark_optional )
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    type: str = field(metadata=EndpointBase.post_mark)
    obfuscate: str = field(metadata=EndpointBase.post_mark)
    encrypt: str = field(metadata=EndpointBase.post_mark)
    anti_keyLogger: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()