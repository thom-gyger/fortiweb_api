from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class CertificateVerify(EndpointBase):
    id: Optional[int]
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    ca: str = field(metadata=EndpointBase.post_mark)
    crl: str = field(metadata=EndpointBase.post_mark)
    publish_dn: str = field(metadata=EndpointBase.post_mark)
    strictly_need_cert: str = field(metadata=EndpointBase.post_mark)
    partial_chain: str = field(metadata=EndpointBase.post_mark)
    crl_allow_expired: str = field(metadata=EndpointBase.post_mark)


    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()



