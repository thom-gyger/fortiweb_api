from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class ServerPoolHealthCheckItem(EndpointBase):
    id: Optional[str] = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    type: str = field(metadata=EndpointBase.post_mark)
    timeout: int = field(metadata=EndpointBase.post_mark)
    retry_times: int = field(metadata=EndpointBase.post_mark)
    interval: int = field(metadata=EndpointBase.post_mark)
    url_path: str = field(metadata=EndpointBase.post_mark)
    method: str = field(metadata=EndpointBase.post_mark)
    match_type: str = field(metadata=EndpointBase.post_mark)
    response_code: int = field(metadata=EndpointBase.post_mark)
    match_content: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = ['protocol']
        return super().get_post_json_template()