from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class UserTrackingRule(EndpointBase):
    from .UserTrackingRuleConditionItem import UserTrackingRuleConditionItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    hostname_ip: str = field(metadata=EndpointBase.post_mark)
    host_status: str = field(metadata=EndpointBase.post_mark)
    authentication_url: str = field(metadata=EndpointBase.post_mark)
    username_parameter: str = field(metadata=EndpointBase.post_mark)
    password_parameter: str = field(metadata=EndpointBase.post_mark)
    session_id_name: str = field(metadata=EndpointBase.post_mark)
    logoff_path: str = field(metadata=EndpointBase.post_mark)
    session_fixation_protection: str = field(metadata=EndpointBase.post_mark)
    limit_users: str = field(metadata=EndpointBase.post_mark)
    maximum_users: int = field(metadata=EndpointBase.post_mark)
    session_idle_timeout: int = field(metadata=EndpointBase.post_mark)
    session_timeout_enable: str = field(metadata=EndpointBase.post_mark)
    session_timeout_enforcement: str = field(metadata=EndpointBase.post_mark)
    session_timeout: int = field(metadata=EndpointBase.post_mark)
    session_frozen_time: int = field(metadata=EndpointBase.post_mark)
    session_frozen_action: str = field(metadata=EndpointBase.post_mark)
    session_frozen_block_period: int = field(metadata=EndpointBase.post_mark)
    session_frozen_severity: str = field(metadata=EndpointBase.post_mark)
    session_frozen_trigger: str = field(metadata=EndpointBase.post_mark)
    default_action: str = field(metadata=EndpointBase.post_mark)
    credential_stuffing_protection: str = field(metadata=EndpointBase.post_mark)
    credential_stuffing_online_query: str = field(metadata=EndpointBase.post_mark)
    sz_match_condition: int = field(metadata=EndpointBase.post_mark)

    match_condition: List[UserTrackingRuleConditionItem] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()
