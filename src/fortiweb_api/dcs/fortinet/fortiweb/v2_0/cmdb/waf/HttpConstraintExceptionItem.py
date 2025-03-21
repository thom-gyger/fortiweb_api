from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class HttpConstraintExceptionItem(EndpointBase):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    host: str = field(metadata=EndpointBase.post_mark)
    request_file: str = field(metadata=EndpointBase.post_mark)
    request_type: str = field(metadata=EndpointBase.post_mark)
    host_status: str = field(metadata=EndpointBase.post_mark)
    source_ip_status: str = field(metadata=EndpointBase.post_mark)
    source_ip: str = field(metadata=EndpointBase.post_mark)
    max_http_header_length: str = field(metadata=EndpointBase.post_mark)
    max_http_content_length: str = field(metadata=EndpointBase.post_mark)
    max_http_body_length: str = field(metadata=EndpointBase.post_mark)
    max_http_request_filename_length: str = field(metadata=EndpointBase.post_mark)
    max_http_request_length: str = field(metadata=EndpointBase.post_mark)
    max_url_parameter_length: str = field(metadata=EndpointBase.post_mark)
    max_cookie_in_request: str = field(metadata=EndpointBase.post_mark)
    max_header_line_request: str = field(metadata=EndpointBase.post_mark)
    Illegal_http_request_method_check: str = field(metadata=EndpointBase.post_mark)
    max_url_parameter: str = field(metadata=EndpointBase.post_mark)
    Illegal_host_name_check: str = field(metadata=EndpointBase.post_mark)
    number_of_ranges_in_range_header: str = field(metadata=EndpointBase.post_mark)
    http2_max_requests: str = field(metadata=EndpointBase.post_mark)
    block_malformed_request: str = field(metadata=EndpointBase.post_mark)
    Illegal_content_length_check: str = field(metadata=EndpointBase.post_mark)
    Illegal_content_type_check: str = field(metadata=EndpointBase.post_mark)
    Post_request_ctype_check: str = field(metadata=EndpointBase.post_mark)
    max_http_header_name_length: str = field(metadata=EndpointBase.post_mark)
    max_http_header_value_length: str = field(metadata=EndpointBase.post_mark)
    parameter_name_check: str = field(metadata=EndpointBase.post_mark)
    parameter_value_check: str = field(metadata=EndpointBase.post_mark)
    Illegal_header_name_check: str = field(metadata=EndpointBase.post_mark)
    Illegal_header_value_check: str = field(metadata=EndpointBase.post_mark)
    max_http_body_parameter_length: str = field(metadata=EndpointBase.post_mark)
    max_url_param_name_len: str = field(metadata=EndpointBase.post_mark)
    max_url_param_value_len: str = field(metadata=EndpointBase.post_mark)
    url_param_name_check: str = field(metadata=EndpointBase.post_mark)
    url_param_value_check: str = field(metadata=EndpointBase.post_mark)
    redundant_header_check: str = field(metadata=EndpointBase.post_mark)
    duplicate_paramname_check: str = field(metadata=EndpointBase.post_mark)
    null_byte_in_url_check: str = field(metadata=EndpointBase.post_mark)
    Illegal_byte_in_url_check: str = field(metadata=EndpointBase.post_mark)
    web_socket_protocol_check: str = field(metadata=EndpointBase.post_mark)
    odd_and_even_space_attack_check: str = field(metadata=EndpointBase.post_mark)
    Internal_resource_limits_check: str = field(metadata=EndpointBase.post_mark)
    rpc_protocol_check: str = field(metadata=EndpointBase.post_mark)
    cl_te_coexist_check: str = field(metadata=EndpointBase.post_mark)
    inconsistent_cl_check: str = field(metadata=EndpointBase.post_mark)
    missing_host_check: str = field(metadata=EndpointBase.post_mark)
    range_overlapping_check: str = field(metadata=EndpointBase.post_mark)
    multipart_formdata_bad_request_check: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema


    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()