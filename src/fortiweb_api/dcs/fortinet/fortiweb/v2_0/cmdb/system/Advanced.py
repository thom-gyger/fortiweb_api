from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field
from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


# rewrite this code to use the marshmallow_dataclass
@mdc(base_schema=Baseschema)
class Advanced(EndpointBase):
    owasp_top10_compliance: str = field(metadata=EndpointBase.post_mark)
    share_ip: str = field(metadata=EndpointBase.post_mark)
    circulate_url_decode: str = field(metadata=EndpointBase.post_mark)
    decoding_enhancement: str = field(metadata=EndpointBase.post_mark)
    max_cache_size: int = field(metadata=EndpointBase.post_mark)
    max_dos_alert_interval: int = field(metadata=EndpointBase.post_mark)
    max_dlp_cache_size: int = field(metadata=EndpointBase.post_mark)
    dlp_verdict_cache_timeout: int = field(metadata=EndpointBase.post_mark)
    anypktstream: str = field(metadata=EndpointBase.post_mark)
    max_bot_alert_interval: int = field(metadata=EndpointBase.post_mark)
    ignore_octet_stream: str = field(metadata=EndpointBase.post_mark)
    ignore_undefined_query_param: str = field(metadata=EndpointBase.post_mark)
    key_attr: str = field(metadata=EndpointBase.post_mark)
    key_max_length: int = field(metadata=EndpointBase.post_mark)
    key_printable: str = field(metadata=EndpointBase.post_mark)
    max_signature_scanning_for_upload_file_cache: int = field(metadata=EndpointBase.post_mark)

    Schema: ClassVar[Type[Schema]] = Baseschema

    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()

