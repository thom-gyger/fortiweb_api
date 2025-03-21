from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field, fields

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class AccelerationPolicy(EndpointBase):
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    exception: str = field(metadata=EndpointBase.post_mark)
    html_minify: str = field(metadata=EndpointBase.post_mark)
    html_combine_heads: str = field(metadata=EndpointBase.post_mark)
    html_css2head: str = field(metadata=EndpointBase.post_mark)
    js_minify: str = field(metadata=EndpointBase.post_mark)
    css_minify: str = field(metadata=EndpointBase.post_mark)


    Schema: ClassVar[Type[Schema]] = Baseschema


    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

