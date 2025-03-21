from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class HttpContentRoutingMatchItem(EndpointBase):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    match_object: str = field(metadata=EndpointBase.post_mark)
    match_condition: str = field(metadata=EndpointBase.post_mark)
    x509_subject_name: str = field(metadata=EndpointBase.post_mark)
    match_expression: str = field(metadata=EndpointBase.post_mark)
    name: str = field(metadata=EndpointBase.post_mark)
    value: str = field(metadata=EndpointBase.post_mark)
    name_match_condition: str = field(metadata=EndpointBase.post_mark)
    value_match_condition: str = field(metadata=EndpointBase.post_mark)
    start_ip: str = field(metadata=EndpointBase.post_mark)
    end_ip: str = field(metadata=EndpointBase.post_mark)
    reverse: str = field(metadata=EndpointBase.post_mark)
    country_list: str = field(metadata=EndpointBase.post_mark)
    ip_list: str = field(metadata=EndpointBase.post_mark)
    ip_range: str = field(metadata=EndpointBase.post_mark)
    ip_list_file: str = field(metadata=EndpointBase.post_mark)
    ztna_ems_tag: str = field(metadata=EndpointBase.post_mark)
    ztna_ems_tag_combine: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()





