from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class TriggerPolicy(EndpointBase):
    id: Optional[int] = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    q_ref: Optional[int] 
    q_type: Optional[int] 
    name: str = field(metadata=EndpointBase.post_mark)
    email_policy: str = field(metadata=EndpointBase.post_mark)
    email_policy_val: str = field(metadata=EndpointBase.post_mark)
    syslog_policy: str = field(metadata=EndpointBase.post_mark)
    syslog_policy_val: str = field(metadata=EndpointBase.post_mark)
    analyzer_policy: str = field(metadata=EndpointBase.post_mark)
    analyzer_policy_val: str = field(metadata=EndpointBase.post_mark)
    siem_policy: str = field(metadata=EndpointBase.post_mark)
    siem_policy_val: str = field(metadata=EndpointBase.post_mark)
    application_name: str = field(metadata=EndpointBase.post_mark)
    region: str = field(metadata=EndpointBase.post_mark)
    vendor: str = field(metadata=EndpointBase.post_mark)
    product: str = field(metadata=EndpointBase.post_mark)
    
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()
