from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class Signature(EndpointBase):
    from .SignatureClassItem import SignatureClassItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    custom_protection_group: str = field(metadata=EndpointBase.post_mark)
    credit_card_detection_threshold: int = field(metadata=EndpointBase.post_mark)
    sub_table_type: str
    sub_table_id: int
    sub_table_action: str
    filter_id: int
    flag_operation: int
    comment: str = field(metadata=EndpointBase.post_mark)
    sz_main_class_list: int
    sz_sub_class_disable_list: int
    sz_signature_disable_list: int
    sz_alert_only_list: int
    sz_fpm_disable_list: int
    sz_scoring_override_disable_list: int
    sz_score_grade_list: int
    sz_filter_list: int
    sensitivity_level: str = field(metadata=EndpointBase.post_mark)

    main_class_list: List[SignatureClassItem] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


