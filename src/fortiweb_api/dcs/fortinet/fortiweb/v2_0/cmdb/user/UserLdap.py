from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class UserLdap(EndpointBase):
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    server: str = field(metadata=EndpointBase.post_mark)
    port: int = field(metadata=EndpointBase.post_mark)
    common_name_id: str = field(metadata=EndpointBase.post_mark)
    distinguished_name: str = field(metadata=EndpointBase.post_mark)
    bind_type: str = field(metadata=EndpointBase.post_mark)
    ssl_connection: str = field(metadata=EndpointBase.post_mark)
    protocol: str = field(metadata=EndpointBase.post_mark)
    ca_cert: str = field(metadata=EndpointBase.post_mark)
    ca_cert_val: int = field(metadata=EndpointBase.post_mark)
    username: str = field(metadata=EndpointBase.post_mark)
    password: str = field(metadata=EndpointBase.post_mark)
    filter: str = field(metadata=EndpointBase.post_mark)
    group_authentication: str = field(metadata=EndpointBase.post_mark)
    group_type: str = field(metadata=EndpointBase.post_mark)
    group_dn: str = field(metadata=EndpointBase.post_mark)


    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()



