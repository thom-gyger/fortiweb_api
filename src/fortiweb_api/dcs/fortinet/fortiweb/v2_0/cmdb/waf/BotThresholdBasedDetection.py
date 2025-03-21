from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class BotThresholdBasedDetection(EndpointBase):
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    bot_recognition: str = field(metadata=EndpointBase.post_mark)
    mobile_app_identification: str = field(metadata=EndpointBase.post_mark)
    bot_confirmation: str = field(metadata=EndpointBase.post_mark)
    validation_timeout: int = field(metadata=EndpointBase.post_mark)
    max_attempt_times: int = field(metadata=EndpointBase.post_mark)
    recaptcha_server: str = field(metadata=EndpointBase.post_mark)
    crawler_detection: str = field(metadata=EndpointBase.post_mark)
    crawler_action: str = field(metadata=EndpointBase.post_mark)
    crawler_severity: str = field(metadata=EndpointBase.post_mark)
    crawler_trigger: str = field(metadata=EndpointBase.post_mark)
    crawler_occurrence_num: int = field(metadata=EndpointBase.post_mark)
    crawler_within: int = field(metadata=EndpointBase.post_mark)
    crawler_block_period: int = field(metadata=EndpointBase.post_mark)
    scanner_detection: str = field(metadata=EndpointBase.post_mark)
    scanner_action: str = field(metadata=EndpointBase.post_mark)
    scanner_severity: str = field(metadata=EndpointBase.post_mark)
    scanner_trigger: str = field(metadata=EndpointBase.post_mark)
    scanner_occurrence_num: int = field(metadata=EndpointBase.post_mark)
    scanner_within: int = field(metadata=EndpointBase.post_mark)
    scanner_block_period: int = field(metadata=EndpointBase.post_mark)
    slow_attack_detection: str = field(metadata=EndpointBase.post_mark)
    slow_attack_action: str = field(metadata=EndpointBase.post_mark)
    slow_attack_severity: str = field(metadata=EndpointBase.post_mark)
    slow_attack_trigger: str = field(metadata=EndpointBase.post_mark)
    slow_attack_occurrence_num: int = field(metadata=EndpointBase.post_mark)
    slow_attack_within: int = field(metadata=EndpointBase.post_mark)
    slow_attack_http_transaction_timeout: int = field(metadata=EndpointBase.post_mark)
    slow_attack_packet_interval_timeout: int = field(metadata=EndpointBase.post_mark)
    slow_attack_block_period: int = field(metadata=EndpointBase.post_mark)
    content_scraping_detection: str = field(metadata=EndpointBase.post_mark)
    content_scraping_action: str = field(metadata=EndpointBase.post_mark)
    content_scraping_severity: str = field(metadata=EndpointBase.post_mark)
    content_scraping_trigger: str = field(metadata=EndpointBase.post_mark)
    content_scraping_occurrence_num: int = field(metadata=EndpointBase.post_mark)
    content_scraping_within: int = field(metadata=EndpointBase.post_mark)
    content_scraping_block_period: int = field(metadata=EndpointBase.post_mark)
    brute_login_detection: str = field(metadata=EndpointBase.post_mark)
    brute_login_action: str = field(metadata=EndpointBase.post_mark)
    brute_login_severity: str = field(metadata=EndpointBase.post_mark)
    brute_login_trigger: str = field(metadata=EndpointBase.post_mark)
    brute_login_occurrence_num: int = field(metadata=EndpointBase.post_mark)
    brute_login_within: int = field(metadata=EndpointBase.post_mark)
    brute_login_request_file: str = field(metadata=EndpointBase.post_mark)
    brute_login_block_period: int = field(metadata=EndpointBase.post_mark)
    exception: str = field(metadata=EndpointBase.post_mark)


    Schema: ClassVar[Type[Schema]] = Baseschema


    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()



