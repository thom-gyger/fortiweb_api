from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class GlobalAllowListCustom(EndpointBase):
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    type: str = field(metadata=EndpointBase.post_mark)
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    header_type: str = field(metadata=EndpointBase.post_mark)
    request_type: str = field(metadata=EndpointBase.post_mark)
    domain_type: str = field(metadata=EndpointBase.post_mark)
    name_type: str = field(metadata=EndpointBase.post_mark)
    request_file_status: str = field(metadata=EndpointBase.post_mark)
    domain_status: str = field(metadata=EndpointBase.post_mark)
    request_file: str = field(metadata=EndpointBase.post_mark)
    domain: str = field(metadata=EndpointBase.post_mark)
    path : str = field(metadata=EndpointBase.post_mark)
    status: str = field(metadata=EndpointBase.post_mark)
    value_type: str = field(metadata=EndpointBase.post_mark)
    value: str = field(metadata=EndpointBase.post_mark)
    value_status: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()