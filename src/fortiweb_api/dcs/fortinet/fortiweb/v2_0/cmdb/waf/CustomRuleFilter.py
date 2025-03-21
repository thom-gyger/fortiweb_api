from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

class CustomRuleFilter:
    pass

@mdc(base_schema=Baseschema)
class CustomRuleFilterOccurrence(EndpointBase, CustomRuleFilter):
    id: str  = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    occurrence_num: int = field(metadata=EndpointBase.post_mark)
    within: int = field(metadata=EndpointBase.post_mark)
    percentage_flag: str = field(metadata=EndpointBase.post_mark)
    percentage: int = field(metadata=EndpointBase.post_mark)
    traced_by: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterCustomSignature(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    custom_signature_enable: str = field(metadata=EndpointBase.post_mark)
    custom_signature_type: str = field(metadata=EndpointBase.post_mark)
    custom_signature_name: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterSubClass(EndpointBase, CustomRuleFilter):
    sub_class_id: str = field(metadata=EndpointBase.post_mark)
    select_all: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterMainClass(EndpointBase, CustomRuleFilter):
    main_class_id: str = field(metadata=EndpointBase.post_mark)
    select_all: str = field(metadata=EndpointBase.post_mark)
    no_subclass: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterPacketInterval(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    packet_interval_timeout: int  = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterContentType(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    content_type_set: str = field(metadata=EndpointBase.post_mark)
    content_type_rev_match: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterResponseCode(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    response_code_min: int = field(metadata=EndpointBase.post_mark)
    response_code_max: int = field(metadata=EndpointBase.post_mark)
    response_code_rev_match: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterHttpTransaction(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    http_transaction_timeout: int = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterAccessLimit(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    access_rate_limit: int = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterUser(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    reverse_match: str = field(metadata=EndpointBase.post_mark)
    user_name: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterParameter(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    name_type: str = field(metadata=EndpointBase.post_mark)
    name: str = field(metadata=EndpointBase.post_mark)
    location_check: str = field(metadata=EndpointBase.post_mark)
    location: str = field(metadata=EndpointBase.post_mark)
    value_check: str = field(metadata=EndpointBase.post_mark)
    value: str = field(metadata=EndpointBase.post_mark)
    parameter_rev_match: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterHttpHeader(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    header_field_check: str = field(metadata=EndpointBase.post_mark)
    header_name_type: str = field(metadata=EndpointBase.post_mark)
    predefined_header: str = field(metadata=EndpointBase.post_mark)
    custom_header_name: str = field(metadata=EndpointBase.post_mark)
    http_hline_missing_check: str = field(metadata=EndpointBase.post_mark)
    http_hline_empty_check: str = field(metadata=EndpointBase.post_mark)
    misformatted_basic_scheme_check: str = field(metadata=EndpointBase.post_mark)
    header_value: str = field(metadata=EndpointBase.post_mark)
    pre_header_type: str = field(metadata=EndpointBase.post_mark)
    pre_header_rev_match: str = field(metadata=EndpointBase.post_mark)
    cus_header_type: str = field(metadata=EndpointBase.post_mark)
    cus_header_name_type: str = field(metadata=EndpointBase.post_mark)
    cus_header_rev_match: str = field(metadata=EndpointBase.post_mark)
    http_method_check: str = field(metadata=EndpointBase.post_mark)
    http_method_value_type: str = field(metadata=EndpointBase.post_mark)
    http_method_value: str = field(metadata=EndpointBase.post_mark)
    http_method_rev_match: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterUrl(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    reverse_match: str = field(metadata=EndpointBase.post_mark)
    request_file: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterMethod(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    method_type: str = field(metadata=EndpointBase.post_mark)
    predefined_method_set: str = field(metadata=EndpointBase.post_mark)
    custom_method_type: str = field(metadata=EndpointBase.post_mark)
    custom_method_value: str = field(metadata=EndpointBase.post_mark)
    method_reverse_match: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterTimeRange(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    range_type: str = field(metadata=EndpointBase.post_mark)
    range_start: str = field(metadata=EndpointBase.post_mark)
    range_end: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterGeo(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    match_exclusive: str = field(metadata=EndpointBase.post_mark)
    country_list: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()


@mdc(base_schema=Baseschema)
class CustomRuleFilterSourceIp(EndpointBase, CustomRuleFilter):
    id: str = field(metadata=EndpointBase.post_mark_optional | EndpointBase.key_mark)
    source_ip: str = field(metadata=EndpointBase.post_mark)
    exclusive_match: str = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()