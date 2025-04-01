from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class FortianalyzerPolicy(EndpointBase):
    from .FortianalyzerPolicyList import FortianalyzerPolicyList
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark)
    sz_fortianalyzer_server_list: int = field(metadata=EndpointBase.post_mark)

    fortianalyzer_server_list: Optional[List[FortianalyzerPolicyList]] = field(default_factory=list)

    
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

