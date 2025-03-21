from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class Admin(EndpointBase):
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    access_profile: str = field(metadata=EndpointBase.post_mark)
    trusthostv4: str = field(metadata=EndpointBase.post_mark)
    trusthostv6: str = field(metadata=EndpointBase.post_mark)
    last_name: str = field(metadata=EndpointBase.post_mark)
    first_name: str = field(metadata=EndpointBase.post_mark)
    email_address: str = field(metadata=EndpointBase.post_mark)
    phone_number: str = field(metadata=EndpointBase.post_mark)
    mobile_number: str = field(metadata=EndpointBase.post_mark)
    hidden: int = field(metadata=EndpointBase.post_mark)
    domains: str = field(metadata=EndpointBase.post_mark)
    sz_dashboard: int = field(metadata=EndpointBase.post_mark)
    sz_gui_dashboard: int = field(metadata=EndpointBase.post_mark)
    type: str = field(metadata=EndpointBase.post_mark)
    admin_usergrp: str = field(metadata=EndpointBase.post_mark)
    password: str = field(metadata=EndpointBase.post_mark)
    wildcard: str = field(metadata=EndpointBase.post_mark)
    accprofile_override: str = field(metadata=EndpointBase.post_mark)
    sshkey: str = field(metadata=EndpointBase.post_mark)
    passwd_set_time: int = field(metadata=EndpointBase.post_mark)
    history_password_pos: int = field(metadata=EndpointBase.post_mark)
    history_password0: str = field(metadata=EndpointBase.post_mark)
    history_password1: str = field(metadata=EndpointBase.post_mark)
    history_password2: str = field(metadata=EndpointBase.post_mark)
    history_password3: str = field(metadata=EndpointBase.post_mark)
    history_password4: str = field(metadata=EndpointBase.post_mark)
    history_password5: str = field(metadata=EndpointBase.post_mark)
    history_password6: str = field(metadata=EndpointBase.post_mark)
    history_password7: str = field(metadata=EndpointBase.post_mark)
    history_password8: str = field(metadata=EndpointBase.post_mark)
    history_password9: str = field(metadata=EndpointBase.post_mark)
    force_password_change: str = field(metadata=EndpointBase.post_mark)
    feature_info_ver: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

