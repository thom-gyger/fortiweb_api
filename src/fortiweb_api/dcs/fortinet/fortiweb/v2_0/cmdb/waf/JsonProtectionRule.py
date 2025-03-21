from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class JsonProtectionRule(EndpointBase):
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    host_status: str = field(metadata=EndpointBase.post_mark)
    host: str = field(metadata=EndpointBase.post_mark)
    request_type: str = field(metadata=EndpointBase.post_mark)
    request_file: str = field(metadata=EndpointBase.post_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    block_period: int = field(metadata=EndpointBase.post_mark)
    severity: str = field(metadata=EndpointBase.post_mark)
    trigger: str = field(metadata=EndpointBase.post_mark)
    schema_type: str = field(metadata=EndpointBase.post_mark)
    schema_file: str = field(metadata=EndpointBase.post_mark)
    schema_group: str = field(metadata=EndpointBase.post_mark)
    json_limits: str = field(metadata=EndpointBase.post_mark)
    json_data_size: int = field(metadata=EndpointBase.post_mark)
    key_size: int = field(metadata=EndpointBase.post_mark)
    key_number: int = field(metadata=EndpointBase.post_mark)
    value_size: int = field(metadata=EndpointBase.post_mark)
    value_number: int = field(metadata=EndpointBase.post_mark)
    value_number_in_array: int = field(metadata=EndpointBase.post_mark)
    object_depth: int = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()