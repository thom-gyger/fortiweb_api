from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema



@mdc(base_schema=Baseschema)
class HiddenFieldProtectionPolicy(EndpointBase):
    from .HiddenFieldProtectionPolicyItem import HiddenFieldProtectionPolicyItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    sz_hidden_fields_list: int
    flag: int

    hidden_fields_list: List[HiddenFieldProtectionPolicyItem] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()
