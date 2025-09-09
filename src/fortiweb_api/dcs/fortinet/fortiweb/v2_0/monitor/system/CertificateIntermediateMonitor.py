from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class CertificateIntermediateMonitor(EndpointBase):
    name: Optional[str]
    status: Optional[str]
    issuer: Optional[str]
    validFrom: Optional[str]
    validTo: Optional[str]
    version: Optional[int]
    subject: Optional[str]
    serialNumber: Optional[str]

    Schema: ClassVar[Type[Schema]] = Baseschema



    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()
    

