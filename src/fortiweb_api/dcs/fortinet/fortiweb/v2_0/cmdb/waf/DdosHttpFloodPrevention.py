from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class DdosHttpFloodPrevention(EndpointBase):
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    access_limit_in_http_session: int = field(metadata=EndpointBase.post_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    block_period: int = field(metadata=EndpointBase.post_mark)
    severity: str = field(metadata=EndpointBase.post_mark)
    trigger_policy: str = field(metadata=EndpointBase.post_mark)
    bot_confirmation: str = field(metadata=EndpointBase.post_mark)
    bot_recognition: str = field(metadata=EndpointBase.post_mark)
    validation_timeout: int = field(metadata=EndpointBase.post_mark)
    max_attempt_times: int = field(metadata=EndpointBase.post_mark)
    recaptcha_server: str = field(metadata=EndpointBase.post_mark)
    mobile_app_identification: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


