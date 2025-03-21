from typing import List, Dict, Type, ClassVar, Optional
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class Vdoms:
    vdoms: List[str]

    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class Visibility:
    ftp_security: bool
    traffic_mirror: bool
    mobile_app_identification: bool
    adfs_policy: bool
    acceleration_policy: bool
    web_cache: bool
    support_ajax_requests: bool
    wccp_mode: bool
    wvs: bool
    api_gateway: bool
    firewall: bool
    padding_oracle: bool
    wad: bool
    fortigate_integration: bool
    support_icap_server: bool
    debug_log: bool
    recaptcha: bool
    ztna: bool
    cryptographic_key: bool

    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class Admin:
    vdoms: list
    visibility: Visibility
    vdom_mode: bool
    language_code: str
    hostname: str
    login_name: str
    admin_name: str
    current_vdom: str
    dpdk_mode: bool
    prof_admin: bool
    remote_user: bool
    MGPORT: str
    op_mode: str
    admintimeout: int
    gui_upload: bool
    hsm_status: bool
    hsm_ha_status: bool
    fips_status: bool
    is_fips_ciphers: bool
    fds_status: bool
    sig_update_status: bool
    ha_mode: str
    is_slave: Optional[bool]
    vdom_cookie_name: str
    last_backup: str
    server_epoch: str
    timezone_offset: int

    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class Config:
    PRODUCT_NAME: str
    CONFIG_CERT_FORTINET: int
    CONFIG_FORTIWEB_IMAGE: int
    CONFIG_MAJOR_NUM: int
    CONFIG_MINOR_NUM: int
    CONFIG_PATCH_NUM: int
    CONFIG_BUILD_NUMBER: int
    CONFIG_BUILD_LABEL: str
    CONFIG_SYSTEM_MODEL: str
    CONFIG_GUI_NO: str
    HAVE_LOGDISK_EXT4: int
    HAVE_HA: int
    HAVE_VIRT: int
    HAVE_VIRT_VM: int
    HAVE_VLAN: int
    HAVE_VDOM: int
    HAVE_LICFILE: int
    CONFIG_SYSTEM_FWB_VM: int

    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class State(EndpointBase):
    admin: Admin
    config: Config

    Schema: ClassVar[Type[Schema]] = Baseschema