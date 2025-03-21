from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

from uuid import UUID

@mdc(base_schema=Baseschema)
class ApiUser(EndpointBase):
    from .ApiUserIpAccessListItem import ApiUserIpAccessListItem
    from .ApiUserHttpRefererItem import ApiUserHttpRefererItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    email: str = field(metadata=EndpointBase.post_mark)
    comments: str = field(metadata=EndpointBase.post_mark)
    uuid: UUID = field(metadata=EndpointBase.post_mark)
    api_key: str = field(metadata=EndpointBase.post_mark)
    create_time: str = field(metadata=EndpointBase.post_mark)
    key_mode: str = field(metadata=EndpointBase.post_mark)
    key_mode_val: str = field(metadata=EndpointBase.post_mark)
    url: str = field(metadata=EndpointBase.post_mark)
    headers: str = field(metadata=EndpointBase.post_mark)
    params: str = field(metadata=EndpointBase.post_mark)
    phantom_token_name: str = field(metadata=EndpointBase.post_mark)
    token_name: str = field(metadata=EndpointBase.post_mark)
    headers_verification: str = field(metadata=EndpointBase.post_mark)
    payload_validation: str = field(metadata=EndpointBase.post_mark)
    rsa_key: str = field(metadata=EndpointBase.post_mark)
    sz_ip_access_list: int
    sz_http_referer_list: int

    ip_access_list: List[ApiUserIpAccessListItem] = field(default_factory=list)
    http_referer_list: List[ApiUserHttpRefererItem] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()



