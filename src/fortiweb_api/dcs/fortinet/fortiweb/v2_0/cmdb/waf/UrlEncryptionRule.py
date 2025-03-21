from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class UrlEncryptionRule(EndpointBase):
    from .UrlEncryptionRuleUrlItem import UrlEncryptionRuleUrlItem
    from .UrlEncryptionRuleExceptionItem import UrlEncryptionRuleExceptionItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    host_status: str = field(metadata=EndpointBase.post_mark)
    host: str = field(metadata=EndpointBase.post_mark)
    allow_unencrypted: str = field(metadata=EndpointBase.post_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    block_period: int = field(metadata=EndpointBase.post_mark)
    severity: str = field(metadata=EndpointBase.post_mark)
    trigger: str = field(metadata=EndpointBase.post_mark)
    sz_url_list: int
    sz_exceptions: int

    url_list: List[UrlEncryptionRuleUrlItem] = field(default_factory=list)
    exceptions: List[UrlEncryptionRuleExceptionItem] = field(default_factory=list)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()