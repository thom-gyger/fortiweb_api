from typing import List, Dict, Type, ClassVar, Optional
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema

@mdc(base_schema=Baseschema)
class PolicyStatusDetail(EndpointBase):
    id: int
    pool: str
    type: int
    ipDomainName: str
    port: int
    healthCheckStatus: str
    sessionCount: int
    backupServer: int
    status: int
    server_rtt: int
    app_response_time: int

    Schema: ClassVar[Type[Schema]] = Baseschema