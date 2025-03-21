from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class SignatureSigDetail(EndpointBase):
    sample: str
    sample2: str
    protocol: int
    meet_target: str
    attack_reference: str
    alert_only: int = field(metadata=EndpointBase.put_mark)
    fpm_disable: int = field(metadata=EndpointBase.put_mark)
    fpm_mitigation: int
    score: int = field(metadata=EndpointBase.put_mark)
    override: int
    default_score: int
    concat: str
    filters: List[Any] = field(default_factory=list)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


