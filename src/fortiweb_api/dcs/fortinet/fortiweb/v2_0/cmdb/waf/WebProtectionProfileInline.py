from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

from fortiweb_api.dcs.EndpointBase import EndpointBase


#rewrite the schema to use marshmallow_dataclass
@mdc(base_schema=Baseschema)
class WebProtectionProfileInline(EndpointBase):
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    client_management: str = field(metadata=EndpointBase.post_mark)
    threat_score_profile: str = field(metadata=EndpointBase.post_mark)
    http_session_cookie: str = field(metadata=EndpointBase.post_mark)
    http_session_timeout: int = field(metadata=EndpointBase.post_mark)
    url_access_policy: str = field(metadata=EndpointBase.post_mark)
    signature_rule: str = field(metadata=EndpointBase.post_mark)
    x_forwarded_for_rule: str = field(metadata=EndpointBase.post_mark)
    parameter_validation_rule: str = field(metadata=EndpointBase.post_mark)
    hidden_fields_protection: str = field(metadata=EndpointBase.post_mark)
    allow_method_policy: str = field(metadata=EndpointBase.post_mark)
    url_rewrite_policy: str = field(metadata=EndpointBase.post_mark)
    http_authen_policy: str = field(metadata=EndpointBase.post_mark)
    file_upload_policy: str = field(metadata=EndpointBase.post_mark)
    webshell_detection_policy: str = field(metadata=EndpointBase.post_mark)
    file_exception_policy: str = field(metadata=EndpointBase.post_mark)
    http_protocol_parameter_restriction: str = field(metadata=EndpointBase.post_mark)
    redirect_url: str = field(metadata=EndpointBase.post_mark)
    amf3_protocol_detection: str = field(metadata=EndpointBase.post_mark)
    rdt_reason: str = field(metadata=EndpointBase.post_mark)
    ip_list_policy: str = field(metadata=EndpointBase.post_mark)
    file_compress_rule: str = field(metadata=EndpointBase.post_mark)
    application_layer_dos_prevention: str = field(metadata=EndpointBase.post_mark)
    geo_block_list_policy: str = field(metadata=EndpointBase.post_mark)
    custom_access_policy: str = field(metadata=EndpointBase.post_mark)
    ip_intelligence: str = field(metadata=EndpointBase.post_mark)
    mobile_app_identification: str = field(metadata=EndpointBase.post_mark)
    token_secret: str = field(metadata=EndpointBase.post_mark)
    token_header: str = field(metadata=EndpointBase.post_mark)
    mobile_api_protection: str = field(metadata=EndpointBase.post_mark)
    site_publish_helper: str = field(metadata=EndpointBase.post_mark)
    cookie_security_policy: str = field(metadata=EndpointBase.post_mark)
    padding_oracle: str = field(metadata=EndpointBase.post_mark)
    # profile_id: str
    comment: str = field(metadata=EndpointBase.post_mark)
    fortigate_quarantined_ips: str = field(metadata=EndpointBase.post_mark)
    quarantined_ip_action: str = field(metadata=EndpointBase.post_mark)
    quarantined_ip_severity: str = field(metadata=EndpointBase.post_mark)
    quarantined_ip_trigger: str = field(metadata=EndpointBase.post_mark)
    csrf_protection: str = field(metadata=EndpointBase.post_mark)
    mitb_protection: str = field(metadata=EndpointBase.post_mark)
    user_tracking_policy: str = field(metadata=EndpointBase.post_mark)
    http_header_security: str = field(metadata=EndpointBase.post_mark)
    xml_validation_policy: str = field(metadata=EndpointBase.post_mark)
    json_validation_policy: str = field(metadata=EndpointBase.post_mark)
    openapi_validation_policy: str = field(metadata=EndpointBase.post_mark)
    websocket_security_policy: str = field(metadata=EndpointBase.post_mark)
    cors_protection_policy: str = field(metadata=EndpointBase.post_mark)
    custom_response: str = field(metadata=EndpointBase.post_mark)
    bot_mitigate_policy: str = field(metadata=EndpointBase.post_mark)
    api_management_policy: str = field(metadata=EndpointBase.post_mark)
    url_encryption_policy: str = field(metadata=EndpointBase.post_mark)
    syntax_based_attack_detection: str = field(metadata=EndpointBase.post_mark)
    link_cloaking_policy: str = field(metadata=EndpointBase.post_mark)
    owasp_api_top10_log_field: str = field(metadata=EndpointBase.post_mark)
    grpc_policy: Optional[str] = None

    Schema: ClassVar[Type[Schema]] = Baseschema


    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()