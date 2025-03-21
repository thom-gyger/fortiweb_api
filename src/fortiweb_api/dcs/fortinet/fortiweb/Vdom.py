from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from BaseSchema import Baseschema

# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class Vdom:
    name : str
    can_delete : str

    # Policy
    server_policies : Dict[str, PolicySchema] = field(default_factory=dict)
    web_protection_profiles : Dict[str, WebProtectionProfileSchema]

    # Server objects
    virtual_servers : Optional[Dict[str, VirtualServerSchema]] = field(default_factory=dict)
    server_pools : Optional[Dict[str, PoolSchema]] = field(default_factory=dict)
    health_checks : Optional[Dict[str, PoolHealthCheckSchema]] = field(default_factory=dict)
    persistence_policies : Optional[Dict[str, PoolPersistanceSchema]] = field(default_factory=dict)
    http_content_routing_policies : Optional[Dict[str, HttpContentRoutingSchema]] = field(default_factory=dict)
    protected_hostnames : Optional[Dict[str, ProtectedHostnamesSchema]] = field(default_factory=dict)
    services : Optional[Dict[str, ServiceSchema]] = field(default_factory=dict)
    certificates : Optional[str]
    ssl_ciphers : Optional[Dict[str, SSLCypherSchema]] = field(default_factory=dict)
    global_allow_lists : Optional[List[GlobalAllowListItemsSchema]] = field(default_factory=list)
    policy_based_allow_lists : Optional[List[PolicyBasedAllowListSchema]] = field(default_factory=list)
    data_types : Optional[Dict[str, DataTypeSchema]] = field(default_factory=dict)
    url_replacer_policies : Optional[Dict[str, UrlReplacerPolicySchema]] = field(default_factory=dict)
    url_replacer_rules : Optional[Dict[str, UrlReplacerRuleSchema]] = field(default_factory=dict)
    x_forwarder : Optional[Dict[str, XForwarderSchema]] = field(default_factory=dict)
    ip_groups : Optional[Dict[str, IpGroupSchema]] = field(default_factory=dict)

    #TODO
    # Application delivery
    url_rewrite_policy : Optional[str]
    url_rewrite_rule : Optional[str]
    authentication_policy : Optional[str]
    authentication_rule : Optional[str]
    file_compression_policy : Optional[str]
    file_compression_exclusion_rule : Optional[str]
    scripts : Optional[str]

    # Web protection
    signature_groups : Optional[Dict[str, SignatureGroupSchema]] = field(default_factory=dict)
    signatures : Optional[Dict[str, SignatureSchema]] = field(default_factory=dict)
    custom_policies : Optional[Dict[str, CustomPolicySchema]] = field(default_factory=dict)
    custom_policy_rules : Optional[Dict[str, CustomPolicyRuleSchema]] = field(default_factory=dict)
    padding_oracle : Optional[Dict[str, PaddingOracleSchema]] = field(default_factory=dict)
    csrf_protection : Optional[Dict[str, CsrfProtectionSchema]] = field(default_factory=dict)
    http_header_security_policies : Optional[Dict[str, HttpHeaderSecuritySchema]] = field(default_factory=dict)
    http_header_security_policy_exceptions : Optional[Dict[str, HttpHeaderSecurityExceptionSchema]] = field(default_factory=dict)
    mitb_protection_policies : Optional[Dict[str, MitbPolicySchema]] = field(default_factory=dict)
    mitb_protection_rules : Optional[Dict[str, MitbRuleSchema]] = field(default_factory=dict)
    url_encryption_policies : Optional[Dict[str, UrlEncryptionPolicySchema]] = field(default_factory=dict)
    url_encryption_rules : Optional[Dict[str, UrlEncryptionRuleSchema]] = field(default_factory=dict)
    link_cloaking_policies : Optional[Dict[str, LinkCloakingPolicySchema]] = field(default_factory=dict)
    link_cloaking_rules : Optional[Dict[str, LinkCloakingRuleSchema]] = field(default_factory=dict)
    syntax_based_detection : Optional[Dict[str, SyntaxBasedDetectionSchema]] = field(default_factory=dict)
    cookie_security : Optional[Dict[str, CookieSecuritySchema]] = field(default_factory=dict)
    parameter_validation_policies : Optional[Dict[str, ParameterValidationPolicySchema]] = field(default_factory=dict)
    input_rules : Optional[Dict[str, InputRuleSchema]] = field(default_factory=dict)
    hidden_field_policies : Optional[Dict[str, HiddenFieldSchema]] = field(default_factory=dict)
    hidden_field_rules : Optional[Dict[str, HiddenFieldRuleSchema]] = field(default_factory=dict)
    file_security_policies : Optional[Dict[str, FileSecuritySchema]] = field(default_factory=dict)
    file_security_rules : Optional[Dict[str, FileSecurityRuleSchema]] = field(default_factory=dict)
    custom_file_types : Optional[Dict[str, FileSecurityFileTypeSchema]] = field(default_factory=dict)
    web_shell_detection : Optional[Dict[str, WebShellDetectionPolicySchema]] = field(default_factory=dict)
    file_exception_policies : Optional[Dict[str, FileExceptionPolicySchema]] = field(default_factory=dict)
    http_constraints : Optional[Dict[str, HttpConstraintSchema]] = field(default_factory=dict)
    http_constraints_exceptions : Optional[Dict[str, HttpConstraintExceptionSchema]] = field(default_factory=dict)

    ### TODO
    websocket_security_policies : Optional[str]
    websocket_security_rules : Optional[str]
    grpc_security_policies : Optional[str]
    grpc_security_rules : Optional[str]
    grpc_idl_files : Optional[str]
    url_access_policies : Optional[str]
    url_access_rules : Optional[str]
    url_access_rules_parameters : Optional[str]
    allow_method_policies : Optional[str]
    allow_method_exceptions : Optional[str]
    cors_protection_policies : Optional[str]
    allow_origins : Optional[str]

    # bot mitigation
    bot_mitigation_policies : Optional[str]
    biometric_based_detections : Optional[str]
    threshold_based_detections : Optional[str]
    bot_descriptions : Optional[str]
    known_bots : Optional[str]
    exception_policy : Optional[str]

    # api protection
    json_protection_policies : Optional[str]
    json_protection_rules : Optional[str]
    json_schemas : Optional[str]
    json_schema_groups : Optional[str]
    xml_protection_policies : Optional[str]
    xml_protection_rules : Optional[str]
    xml_schemas : Optional[str]
    wsdl : Optional[str]
    exempted_urls : Optional[str]
    ws_security_rule : Optional[str]
    open_api_validation_policies : Optional[str]
    open_api_files : Optional[str]

    # ddos protection
    http_access_limits : Optional[str]
    malicious_ips : Optional[str]
    http_flood_preventions : Optional[str]
    tcp_flood_preventions : Optional[str]
    dos_protection_policies : Optional[str]

    # ip protection
    ip_lists : Optional[str]
    geo_ips : Optional[str]
    geo_ip_exceptions : Optional[str]
    ip_reputation_policies : Optional[str]
    ip_reputation_exceptions : Optional[str]

    Schema: ClassVar[Type[Schema]] = Schema
