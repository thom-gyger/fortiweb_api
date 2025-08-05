from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class CertificateSNIItem(EndpointBase):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    domain: str = field(metadata=EndpointBase.post_mark)
    domain_type: str = field(metadata=EndpointBase.post_mark)
    multi_local_cert: str = field(metadata=EndpointBase.post_mark)
    multi_local_cert_group: str = field(metadata=EndpointBase.post_mark)
    local_cert: str = field(metadata=EndpointBase.post_mark)
    local_cert_val: str = field(metadata=EndpointBase.post_mark)
    certificate_type: str = field(metadata=EndpointBase.post_mark)
    lets_certificate: str = field(metadata=EndpointBase.post_mark)
    inter_group: str = field(metadata=EndpointBase.post_mark)
    verify: str = field(metadata=EndpointBase.post_mark)


    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()



