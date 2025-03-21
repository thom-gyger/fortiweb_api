from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class UrlRewritingRule(EndpointBase):
    from .UrlRewritingRuleHeaderInsertItem import UrlRewritingRuleHeaderInsertItem
    from .UrlRewritingRuleHeaderRemovalItem import UrlRewritingRuleHeaderRemovalItem
    from .UrlRewritingRuleResponseHeaderInsertItem import UrlRewritingRuleResponseHeaderInsertItem
    from .UrlRewritingRuleResponseHeaderRemovalItem import UrlRewritingRuleResponseHeaderRemovalItem
    from .UrlRewritingRuleMatchConditionItem import UrlRewritingRuleMatchConditionItem
    q_ref: Optional[int]
    q_ref_string: Optional[str]
    name: str = field(metadata=EndpointBase.post_mark | EndpointBase.key_mark)
    action: str = field(metadata=EndpointBase.post_mark)
    host_status: str = field(metadata=EndpointBase.post_mark)
    host_use_pserver: str = field(metadata=EndpointBase.post_mark)
    host: str = field(metadata=EndpointBase.post_mark)
    url_status: str = field(metadata=EndpointBase.post_mark)
    url: str = field(metadata=EndpointBase.post_mark)
    location: str = field(metadata=EndpointBase.post_mark)
    referer_status: str = field(metadata=EndpointBase.post_mark)
    referer_use_pserver: str = field(metadata=EndpointBase.post_mark)
    referer: str = field(metadata=EndpointBase.post_mark)
    body_replace: str = field(metadata=EndpointBase.post_mark)
    location_replace: str = field(metadata=EndpointBase.post_mark)
    location_status: str = field(metadata=EndpointBase.post_mark)
    http_method_status: str = field(metadata=EndpointBase.post_mark)
    http_method: str = field(metadata=EndpointBase.post_mark)
    status_code_status: str = field(metadata=EndpointBase.post_mark)
    status_code: int = field(metadata=EndpointBase.post_mark)
    request_replace_existing_headers: str = field(metadata=EndpointBase.post_mark)
    response_replace_existing_headers: str = field(metadata=EndpointBase.post_mark)
    request_remove_duplicate_headers: str = field(metadata=EndpointBase.post_mark)
    response_remove_duplicate_headers: str = field(metadata=EndpointBase.post_mark)
    flag_operation: int = field(metadata=EndpointBase.post_mark)
    sz_header_insert: int
    sz_response_header_insert: int
    sz_header_removal: int
    sz_response_header_removal: int
    sz_match_condition: int

    header_insert: List[UrlRewritingRuleHeaderInsertItem] = field(default_factory=list)
    header_removal: List[UrlRewritingRuleHeaderRemovalItem] = field(default_factory=list)
    response_header_insert: List[UrlRewritingRuleResponseHeaderInsertItem] = field(default_factory=list)
    response_header_removal: List[UrlRewritingRuleResponseHeaderRemovalItem] = field(default_factory=list)
    match_condition: List[UrlRewritingRuleMatchConditionItem] = field(default_factory=list)



    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()