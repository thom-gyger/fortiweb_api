from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class XmlProtectionWsSecurityRule(EndpointBase):
    from .XmlProtectionWsSecurityRuleElementItem import XmlProtectionWsSecurityRuleElementItem
    from .XmlProtectionWsSecurityRuleNamespaceItem import XmlProtectionWsSecurityRuleNamespaceItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    request_security_status: str = field(metadata=EndpointBase.post_mark)
    request_operation: str = field(metadata=EndpointBase.post_mark)
    response_security_status: str = field(metadata=EndpointBase.post_mark)
    response_operation: str = field(metadata=EndpointBase.post_mark)
    encryption_part: str = field(metadata=EndpointBase.post_mark)
    signature_algorithm: str = field(metadata=EndpointBase.post_mark)
    encryption_algorithm: str = field(metadata=EndpointBase.post_mark)
    key_transport_algorithm: str = field(metadata=EndpointBase.post_mark)
    xml_server_certificate: str = field(metadata=EndpointBase.post_mark)
    xml_client_certificate_group: str = field(metadata=EndpointBase.post_mark)
    sz_namespace_mapping: int
    sz_element_list: int

    namespace_mapping: List[XmlProtectionWsSecurityRuleNamespaceItem] = field(default_factory=list)
    element_list: List[XmlProtectionWsSecurityRuleElementItem] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()