from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class XmlProtectionRule(EndpointBase):
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    host: str = field(metadata=EndpointBase.post_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    block_period: int = field(metadata=EndpointBase.post_mark)
    severity: str = field(metadata=EndpointBase.post_mark)
    trigger: str = field(metadata=EndpointBase.post_mark)
    request_type: str = field(metadata=EndpointBase.post_mark)
    request_file: str = field(metadata=EndpointBase.post_mark)
    host_status: str = field(metadata=EndpointBase.post_mark)
    data_format: str = field(metadata=EndpointBase.post_mark)
    schema_file: str = field(metadata=EndpointBase.post_mark)
    wsdl_file: str = field(metadata=EndpointBase.post_mark)
    wsdl_ip_port_override: str = field(metadata=EndpointBase.post_mark)
    ws_security: str = field(metadata=EndpointBase.post_mark)
    soap_attachment: str = field(metadata=EndpointBase.post_mark)
    validate_soapaction: str = field(metadata=EndpointBase.post_mark)
    validate_soap_headers: str = field(metadata=EndpointBase.post_mark)
    allow_additional_soap_headers: str = field(metadata=EndpointBase.post_mark)
    validate_soap_body: str = field(metadata=EndpointBase.post_mark)
    xml_limit_check: str = field(metadata=EndpointBase.post_mark)
    xml_limit_attr_num: int = field(metadata=EndpointBase.post_mark)
    xml_limit_attrname_len: int = field(metadata=EndpointBase.post_mark)
    xml_limit_attrvalue_len: int = field(metadata=EndpointBase.post_mark)
    xml_limit_cdata_len: int = field(metadata=EndpointBase.post_mark)
    xml_limit_element_depth: int = field(metadata=EndpointBase.post_mark)
    xml_limit_element_name_len: int = field(metadata=EndpointBase.post_mark)
    xml_attributes_check: str = field(metadata=EndpointBase.post_mark)
    external_entity_check: str = field(metadata=EndpointBase.post_mark)
    expansion_entity_check: str = field(metadata=EndpointBase.post_mark)
    x_include_check: str = field(metadata=EndpointBase.post_mark)
    schema_location_check: str = field(metadata=EndpointBase.post_mark)
    schema_location_exempted_urls: str = field(metadata=EndpointBase.post_mark)
    ws_i_basic_profile_assertion: str = field(metadata=EndpointBase.post_mark)
    ws_i_basic_profile_wsdl_assertion: str = field(metadata=EndpointBase.post_mark)


    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()