from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema



@mdc(base_schema=Baseschema)
class FileSecurityPolicy(EndpointBase):
    from .FileSecurityPolicyRuleItem import FileSecurityPolicyRuleItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    block_period: int = field(metadata=EndpointBase.post_mark)
    severity: str = field(metadata=EndpointBase.post_mark)
    trigger: str = field(metadata=EndpointBase.post_mark)
    av_scan: str = field(metadata=EndpointBase.post_mark)
    fortisandbox_check: str = field(metadata=EndpointBase.post_mark)
    hold_session_while_scanning_file: str = field(metadata=EndpointBase.post_mark)
    icap_server_check: str = field(metadata=EndpointBase.post_mark)
    exchange_mail_detection: str = field(metadata=EndpointBase.post_mark)
    owa_protocol: str = field(metadata=EndpointBase.post_mark)
    activesync_protocol: str = field(metadata=EndpointBase.post_mark)
    mapi_protocol: str = field(metadata=EndpointBase.post_mark)
    sz_rule: int

    rule: List[FileSecurityPolicyRuleItem] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()