from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class AdminUserGroup(EndpointBase):
    from .AdminUserGroupMemberItem import AdminUserGroupMemberItem
    q_ref: Optional[int]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    sz_members: int

    members: List[AdminUserGroupMemberItem] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()



