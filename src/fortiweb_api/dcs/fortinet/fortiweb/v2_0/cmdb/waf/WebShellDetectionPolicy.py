from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema



@mdc(base_schema=Baseschema)
class WebShellDetectionPolicy(EndpointBase):
    from .WebShellDetectionPolicyFuzzyItem import WebShellDetectionPolicyFuzzyItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    block_period: int = field(metadata=EndpointBase.post_mark)
    severity: str = field(metadata=EndpointBase.post_mark)
    trigger: str = field(metadata=EndpointBase.post_mark)
    fuzzy_similarity_threshold: int = field(metadata=EndpointBase.post_mark)
    fuzzy_php_status: str = field(metadata=EndpointBase.post_mark)
    fuzzy_asp_status: str = field(metadata=EndpointBase.post_mark)
    fuzzy_jsp_status: str = field(metadata=EndpointBase.post_mark)
    fuzzy_python_status: str = field(metadata=EndpointBase.post_mark)
    fuzzy_perl_status: str = field(metadata=EndpointBase.post_mark)
    known_php_status: str = field(metadata=EndpointBase.post_mark)
    known_php_short_open_tag: str = field(metadata=EndpointBase.post_mark)
    known_asp_status: str = field(metadata=EndpointBase.post_mark)
    known_jsp_status: str = field(metadata=EndpointBase.post_mark)
    known_python_status: str = field(metadata=EndpointBase.post_mark)
    known_perl_status: str = field(metadata=EndpointBase.post_mark)
    sz_fuzzy_disable_list: int

    fuzzy_disable_list: List[WebShellDetectionPolicyFuzzyItem] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()
