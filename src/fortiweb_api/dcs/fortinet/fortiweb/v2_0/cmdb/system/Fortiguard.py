from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class Fortiguard(EndpointBase):
    update_server_location: str = field(metadata=EndpointBase.post_mark)
    fortiguard_anycast: str = field(metadata=EndpointBase.post_mark)
    fortiguard_anycast_source: str = field(metadata=EndpointBase.post_mark)
    update_dldb: str = field(metadata=EndpointBase.post_mark)
    db_integrity_autorecover: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

