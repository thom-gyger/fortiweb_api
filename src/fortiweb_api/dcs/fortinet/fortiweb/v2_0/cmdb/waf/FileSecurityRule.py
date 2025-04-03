from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class FileSecurityRule(EndpointBase):
    from .FileSecurityRuleCustomFileTypeItem import FileSecurityRuleCustomFileTypeItem
    from .FileSecurityRuleFileTypeItem import FileSecurityRuleFileTypeItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    host_status: str = field(metadata=EndpointBase.post_mark)
    host: str = field(metadata=EndpointBase.post_mark)
    request_type: str = field(metadata=EndpointBase.post_mark)
    request_file: str = field(metadata=EndpointBase.post_mark)
    file_size_limit: int = field(metadata=EndpointBase.post_mark)
    flag: int
    type: str = field(metadata=EndpointBase.post_mark)
    file_uncompress: str = field(metadata=EndpointBase.post_mark)
    uncompress_oversize_limit: int = field(metadata=EndpointBase.post_mark)
    uncompress_nest_limit: int = field(metadata=EndpointBase.post_mark)
    json_file_support: str = field(metadata=EndpointBase.post_mark)
    json_key_for_filename: str = field(metadata=EndpointBase.post_mark)
    json_key_field: str = field(metadata=EndpointBase.post_mark)
    enable_base64_decode: str = field(metadata=EndpointBase.post_mark)
    octet_stream_filename_headers: str = field(metadata={"firmware":"<7.6"} | EndpointBase.post_mark)
    sz_file_types: int
    sz_custom_file_types: int

    file_types: List[FileSecurityRuleFileTypeItem] = field(default_factory=list)
    custom_file_types: List[FileSecurityRuleCustomFileTypeItem] = field(default_factory=list)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()