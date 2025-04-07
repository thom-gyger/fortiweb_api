from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class Syslogd(EndpointBase):
    status: str = field(metadata=EndpointBase.post_mark)
    severity: str = field(metadata=EndpointBase.post_mark)
    facility: str = field(metadata=EndpointBase.post_mark)
    policy: str = field(metadata=EndpointBase.post_mark)
    sz_custom_field: int = field(metadata=EndpointBase.post_mark)
    logtype: str = field(metadata=EndpointBase.post_mark)


    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

