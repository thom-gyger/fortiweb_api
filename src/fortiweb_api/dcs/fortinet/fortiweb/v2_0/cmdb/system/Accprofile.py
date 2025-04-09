from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class Accprofile(EndpointBase):
    id: Optional[int]
    q_ref: Optional[int]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    mntgrp: str = field(metadata=EndpointBase.post_mark)
    admingrp: str = field(metadata=EndpointBase.post_mark)
    sysgrp: str = field(metadata=EndpointBase.post_mark)
    netgrp: str = field(metadata=EndpointBase.post_mark)
    loggrp: str = field(metadata=EndpointBase.post_mark)
    authusergrp: str = field(metadata=EndpointBase.post_mark)
    traroutegrp: str = field(metadata=EndpointBase.post_mark)
    wafgrp: str = field(metadata=EndpointBase.post_mark)
    wadgrp: str = field(metadata=EndpointBase.post_mark)
    wvsgrp: str = field(metadata=EndpointBase.post_mark)
    mlgrp: str = field(metadata=EndpointBase.post_mark)



    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

