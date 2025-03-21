from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class SignatureDisable(EndpointBase):
    id: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    signature_id: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Schema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


