from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class BotKnownBots(EndpointBase):
    from .BotKnownBotsMaliciousBotsDisableItem import BotKnownBotsMaliciousBotsDisableItem
    from .BotKnownBotsKnownGoodBotsDisableItem import BotKnownBotsKnownGoodBotsDisableItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    dos_status: str = field(metadata=EndpointBase.post_mark)
    dos_action: str = field(metadata=EndpointBase.post_mark)
    dos_block_period: int = field(metadata=EndpointBase.post_mark)
    dos_severity: str = field(metadata=EndpointBase.post_mark)
    dos_trigger: str = field(metadata=EndpointBase.post_mark)
    dos_threat_weight: str = field(metadata=EndpointBase.post_mark)
    spam_status: str = field(metadata=EndpointBase.post_mark)
    spam_action: str = field(metadata=EndpointBase.post_mark)
    spam_block_period: int = field(metadata=EndpointBase.post_mark)
    spam_severity: str = field(metadata=EndpointBase.post_mark)
    spam_trigger: str = field(metadata=EndpointBase.post_mark)
    spam_threat_weight: str = field(metadata=EndpointBase.post_mark)
    trojan_status: str = field(metadata=EndpointBase.post_mark)
    trojan_action: str = field(metadata=EndpointBase.post_mark)
    trojan_block_period: int = field(metadata=EndpointBase.post_mark)
    trojan_severity: str = field(metadata=EndpointBase.post_mark)
    trojan_trigger: str = field(metadata=EndpointBase.post_mark)
    trojan_threat_weight: str = field(metadata=EndpointBase.post_mark)
    scanner_status: str = field(metadata=EndpointBase.post_mark)
    scanner_action: str = field(metadata=EndpointBase.post_mark)
    scanner_block_period: int = field(metadata=EndpointBase.post_mark)
    scanner_severity: str = field(metadata=EndpointBase.post_mark)
    scanner_trigger: str = field(metadata=EndpointBase.post_mark)
    scanner_threat_weight: str = field(metadata=EndpointBase.post_mark)
    crawler_status: str = field(metadata=EndpointBase.post_mark)
    crawler_action: str = field(metadata=EndpointBase.post_mark)
    crawler_block_period: int = field(metadata=EndpointBase.post_mark)
    crawler_severity: str = field(metadata=EndpointBase.post_mark)
    crawler_trigger: str = field(metadata=EndpointBase.post_mark)
    crawler_threat_weight: str = field(metadata=EndpointBase.post_mark)
    known_engines_status: str = field(metadata=EndpointBase.post_mark)
    known_engines_action: str = field(metadata=EndpointBase.post_mark)
    known_engines_block_period: int = field(metadata=EndpointBase.post_mark)
    known_engines_severity: str = field(metadata=EndpointBase.post_mark)
    known_engines_trigger: str = field(metadata=EndpointBase.post_mark)
    known_engines_threat_weight: str = field(metadata=EndpointBase.post_mark)
    sz_malicious_bot_disable_list: int
    sz_known_good_bots_disable_list: int
    exception: str = field(metadata=EndpointBase.post_mark)
    malicious_bot_disable_list: List[BotKnownBotsMaliciousBotsDisableItem] = field(default_factory=list)
    known_good_bots_disable_list: List[BotKnownBotsKnownGoodBotsDisableItem] = field(default_factory=list)



    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()



