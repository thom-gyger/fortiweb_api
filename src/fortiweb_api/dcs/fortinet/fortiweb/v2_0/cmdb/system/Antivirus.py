from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class Antivirus(EndpointBase):
    default_db: str = field(metadata=EndpointBase.post_mark)
    scan_bzip2: str = field(metadata=EndpointBase.post_mark)
    uncomp_size_limit: int = field(metadata=EndpointBase.post_mark)
    uncomp_nest_limit: int = field(metadata=EndpointBase.post_mark)
    use_fsa: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

