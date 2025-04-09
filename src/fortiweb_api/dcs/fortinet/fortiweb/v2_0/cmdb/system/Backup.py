from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class Backup(EndpointBase):
    q_ref: Optional[int] = field(metadata=EndpointBase.post_mark)
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    config_type: str = field(metadata=EndpointBase.post_mark)
    schedule_type: str = field(metadata=EndpointBase.post_mark)
    schedule_days: str = field(metadata=EndpointBase.post_mark)
    schedule_time: str = field(metadata=EndpointBase.post_mark)
    ftp_server: str = field(metadata=EndpointBase.post_mark)
    ftp_dir: str = field(metadata=EndpointBase.post_mark)
    ftp_auth: str = field(metadata=EndpointBase.post_mark)
    ftp_user: str = field(metadata=EndpointBase.post_mark)
    ftp_passwd: str = field(metadata=EndpointBase.post_mark)
    protocol_type: str = field(metadata=EndpointBase.post_mark)
    encryption: str = field(metadata=EndpointBase.post_mark)
    encryption_passwd: str = field(metadata=EndpointBase.post_mark)
    ml_flag: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

