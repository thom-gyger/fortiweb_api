from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class SSLCypherPredefined(EndpointBase):
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    tls_v10: str = field(metadata=EndpointBase.post_mark)
    tls_v11: str = field(metadata=EndpointBase.post_mark)
    tls_v12: str = field(metadata=EndpointBase.post_mark)
    tls_v13: str = field(metadata=EndpointBase.post_mark)
    ssl_cipher: str = field(metadata=EndpointBase.post_mark)
    ssl_custom_cipher: str = field(metadata=EndpointBase.post_mark)
    tls13_custom_cipher: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()