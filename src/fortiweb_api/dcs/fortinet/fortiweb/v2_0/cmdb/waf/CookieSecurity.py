from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class CookieSecurity(EndpointBase):
    from .CookieSecurityExceptionItem import CookieSecurityExceptionItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    security_mode: str = field(metadata=EndpointBase.post_mark)
    security_mode_val: int = field(metadata=EndpointBase.post_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    block_period: int = field(metadata=EndpointBase.post_mark)
    severity: str = field(metadata=EndpointBase.post_mark)
    trigger: str = field(metadata=EndpointBase.post_mark)
    cookie_replay_protection_type: str = field(metadata=EndpointBase.post_mark)
    max_age: int = field(metadata=EndpointBase.post_mark)
    secure_cookie: str = field(metadata=EndpointBase.post_mark)
    http_only: str = field(metadata=EndpointBase.post_mark)
    allow_suspicious_cookies: str = field(metadata=EndpointBase.post_mark)
    allow_time: str = field(metadata=EndpointBase.post_mark)
    samesite: str = field(metadata=EndpointBase.post_mark)
    samesite_value: str = field(metadata=EndpointBase.post_mark)
    sz_cookie_security_exception_list: int

    cookie_security_exception_list: List[CookieSecurityExceptionItem] = field(default_factory=list)

    Schema: ClassVar[Type[Schema]] = Baseschema


    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

