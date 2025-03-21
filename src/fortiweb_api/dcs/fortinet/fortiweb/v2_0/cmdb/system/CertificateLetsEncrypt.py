from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class CertificateLetsEncrypt(EndpointBase):
    from .CertificateLetsEncryptSanItem import CertificateLetsEncryptSanItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    domain: str = field(metadata=EndpointBase.post_mark)
    status: int = field(metadata=EndpointBase.post_mark)
    validation_method: str = field(metadata=EndpointBase.post_mark)
    key_type: str = field(metadata=EndpointBase.post_mark)
    expire_date: str = field(metadata=EndpointBase.post_mark)
    certificate: str = field(metadata=EndpointBase.post_mark)
    private_key: str = field(metadata=EndpointBase.post_mark)
    renew_period: int = field(metadata=EndpointBase.post_mark)
    sz_san_list: int = field(metadata=EndpointBase.post_mark)

    san_list: Optional[List[CertificateLetsEncryptSanItem]] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


