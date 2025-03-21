from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class SignatureAdvancedDetail(EndpointBase):
    id: Optional[str] = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    status: int = field(metadata=EndpointBase.post_mark)
    has_filter: int = field(metadata=EndpointBase.post_mark)
    global_status: int = field(metadata=EndpointBase.post_mark)
    group_status: int = field(metadata=EndpointBase.post_mark)
    desc: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class SignatureAdvancedFpm(EndpointBase):
    status: int = field(metadata=EndpointBase.post_mark)
    fpm: int = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class SignatureAdvancedAlertOnly(EndpointBase):
    status: int = field(metadata=EndpointBase.post_mark)
    alert_only: int = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class SignatureAdvancedStatus(EndpointBase):
    status: int = field(metadata=EndpointBase.post_mark)
    has_filter: int = field(metadata=EndpointBase.post_mark)
    global_status: int = field(metadata=EndpointBase.post_mark)
    group_status: int = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema


