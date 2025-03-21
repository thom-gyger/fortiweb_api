from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema



@mdc(base_schema=Baseschema)
class ServerPoolPserverItem(EndpointBase):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    server_type: str = field(metadata=EndpointBase.post_mark)
    ip: str = field(metadata=EndpointBase.post_mark)
    domain: str = field(metadata=EndpointBase.post_mark)
    adfs_username: str = field(metadata=EndpointBase.post_mark)
    adfs_password: str = field(metadata=EndpointBase.post_mark)
    sdn_addr_type: str = field(metadata=EndpointBase.post_mark)
    sdn: str = field(metadata=EndpointBase.post_mark)
    filter: str = field(metadata=EndpointBase.post_mark)
    port: int = field(metadata=EndpointBase.post_mark)
    weight: int = field(metadata=EndpointBase.post_mark)
    status: str = field(metadata=EndpointBase.post_mark)
    server_id: int
    backup_server: str = field(metadata=EndpointBase.post_mark)
    proxy_protocol: str = field(metadata=EndpointBase.post_mark)
    proxy_protocol_version: str = field(metadata=EndpointBase.post_mark)
    ssl: str = field(metadata=EndpointBase.post_mark)
    implicit_ssl: str = field(metadata=EndpointBase.post_mark)
    ssl_quiet_shutdown: str = field(metadata=EndpointBase.post_mark)
    ssl_session_timeout: int = field(metadata=EndpointBase.post_mark)
    server_side_sni: str = field(metadata=EndpointBase.post_mark)
    multi_certificate: str = field(metadata=EndpointBase.post_mark)
    certificate: str = field(metadata=EndpointBase.post_mark)
    certificate_group: str = field(metadata=EndpointBase.post_mark)
    certificate_type: str = field(metadata=EndpointBase.post_mark)
    lets_certificate: str = field(metadata=EndpointBase.post_mark)
    intermediate_certificate_group: str = field(metadata=EndpointBase.post_mark)
    certificate_verify: str = field(metadata=EndpointBase.post_mark)
    client_certificate_proxy: str = field(metadata=EndpointBase.post_mark)
    client_certificate_proxy_sign_ca: str = field(metadata=EndpointBase.post_mark)
    client_certificate: str = field(metadata=EndpointBase.post_mark)
    server_certificate_verify: str = field(metadata=EndpointBase.post_mark)
    server_certificate_verify_policy: str = field(metadata=EndpointBase.post_mark)
    server_certificate_verify_action: str = field(metadata=EndpointBase.post_mark)
    session_ticket_reuse: str = field(metadata=EndpointBase.post_mark)
    session_id_reuse: str = field(metadata=EndpointBase.post_mark)
    sni: str = field(metadata=EndpointBase.post_mark)
    sni_certificate: str = field(metadata=EndpointBase.post_mark)
    sni_strict: str = field(metadata=EndpointBase.post_mark)
    urlcert: str = field(metadata=EndpointBase.post_mark)
    urlcert_group: str = field(metadata=EndpointBase.post_mark)
    urlcert_hlen: int = field(metadata=EndpointBase.post_mark)
    use_ciphers_group: str = field(metadata=EndpointBase.post_mark)
    ssl_ciphers_group: str = field(metadata=EndpointBase.post_mark)
    tls_v10: str = field(metadata=EndpointBase.post_mark)
    tls_v11: str = field(metadata=EndpointBase.post_mark)
    tls_v12: str = field(metadata=EndpointBase.post_mark)
    tls_v13: str = field(metadata=EndpointBase.post_mark)
    ssl_noreg: str = field(metadata=EndpointBase.post_mark)
    ssl_cipher: str = field(metadata=EndpointBase.post_mark)
    ssl_custom_cipher: str = field(metadata=EndpointBase.post_mark)
    tls13_custom_cipher: str = field(metadata=EndpointBase.post_mark)
    rfc7919_comply: str = field(metadata=EndpointBase.post_mark)
    supported_groups: str = field(metadata=EndpointBase.post_mark)
    hsts_header: str = field(metadata=EndpointBase.post_mark)
    hsts_max_age: int = field(metadata=EndpointBase.post_mark)
    hsts_include_subdomains: str = field(metadata=EndpointBase.post_mark)
    hsts_preload: str = field(metadata=EndpointBase.post_mark)
    hpkp_header: str = field(metadata=EndpointBase.post_mark)
    client_certificate_forwarding: str = field(metadata=EndpointBase.post_mark)
    client_certificate_forwarding_sub_header: str = field(metadata=EndpointBase.post_mark)
    client_certificate_forwarding_cert_header: str = field(metadata=EndpointBase.post_mark)
    health_check_inherit: str = field(metadata=EndpointBase.post_mark)
    health: str = field(metadata=EndpointBase.post_mark)
    conn_limit: int = field(metadata=EndpointBase.post_mark)
    recover: int = field(metadata=EndpointBase.post_mark)
    warm_up: int = field(metadata=EndpointBase.post_mark)
    warm_rate: int = field(metadata=EndpointBase.post_mark)
    http2: str = field(metadata=EndpointBase.post_mark)
    hlck_domain: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()