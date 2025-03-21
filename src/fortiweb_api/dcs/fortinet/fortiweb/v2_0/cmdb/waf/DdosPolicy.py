from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class DdosPolicy(EndpointBase):
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    enable_http_session_based_prevention: str = field(metadata=EndpointBase.post_mark)
    http_request_flood_prevention_rule: str = field(metadata=EndpointBase.post_mark)
    http_connection_flood_check_rule: str = field(metadata=EndpointBase.post_mark)
    enable_layer4_dos_prevention: str = field(metadata=EndpointBase.post_mark)
    layer4_access_limit_rule: str = field(metadata=EndpointBase.post_mark)
    layer4_connection_flood_check_rule: str = field(metadata=EndpointBase.post_mark)
    layer3_fragment_protection: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


