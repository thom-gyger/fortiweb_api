from typing import List, ClassVar, Type, Optional
from marshmallow import Schema
from marshmallow_dataclass import dataclass as mdc
from dataclasses import field

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class StatusMonitor(EndpointBase):
    """
    Example JSON from API:
    {
        "status": 1,
        "cpu": 36,
        "memory": 25,
        "log_disk": 55,
        "tcp_concurrent_connection": 10,
        "tcp_connection_per_second": 6,
        "throughput_in": 27336,
        "throughput_out": 2272819,
        "threat_by_countries": [
            {
                "count": "2232",
                "country": "Reserved"
            }
        ],
        "threat": 2232,
        "threat_by_attack_type": [
            {
                "count": "2209",
                "type": "Information Disclosure"
            },
            {
                "count": "22",
                "type": "Threshold Based Detection"
            },
            {
                "count": "1",
                "type": "HTTP Access Limit"
            }
        ],
        "policy": [
            {
                "name": "serverpolicy2",
                "info": {
                    "tcp_concurrent_connection": 10,
                    "tcp_connection_per_second": 6,
                    "throughput_in": 27336,
                    "throughput_out": 2272819,
                    "threat_by_countries": [
                        {
                            "count": "2232",
                            "country": "Reserved"
                        }
                    ],
                    "threat_by_attack_type": [
                        {
                            "count": "2209",
                            "type": "Information Disclosure"
                        },
                        {
                            "count": "22",
                            "type": "Threshold Based Detection"
                        },
                        {
                            "count": "1",
                            "type": "HTTP Access Limit"
                        }
                    ]
                }
            }]}
    """

    @mdc(base_schema=Baseschema)
    class ThreatByCountry(EndpointBase):
        count: str  # Using str as the count is represented as a string in the JSON
        country: str

    @mdc(base_schema=Baseschema)
    class ThreatByAttackType(EndpointBase):
        count: str  # Using str as the count is represented as a string in the JSON
        type: str

    @mdc(base_schema=Baseschema)
    class PolicyInfo(EndpointBase):
        tcp_concurrent_connection: int
        tcp_connection_per_second: int
        throughput_in: int
        throughput_out: int
        threat_by_countries: List["StatusMonitor.ThreatByCountry"] = field(default_factory=list)  # Default to empty list
        threat_by_attack_type: List["StatusMonitor.ThreatByAttackType"] = field(default_factory=list)  # Default to empty list



    @mdc(base_schema=Baseschema)
    class Policy(EndpointBase):
        name: str
        info: "StatusMonitor.PolicyInfo"

    status: int
    cpu: int
    memory: int
    log_disk: int
    tcp_concurrent_connection: int
    tcp_connection_per_second: int
    throughput_in: int
    throughput_out: int
    threat: int
    threat_by_countries: List["StatusMonitor.ThreatByCountry"] = field(default_factory=list)
    threat_by_attack_type: List["StatusMonitor.ThreatByAttackType"] = field(default_factory=list)
    policy: List[Policy] = field(default_factory=list)

    Schema: ClassVar[Type[Schema]] = Baseschema


@mdc(base_schema=Baseschema)
class SessionDataByPolicy(EndpointBase):
    """
    Example JSON from API:
    {
        "details": [
            {
                "policies": "serverpolicy2",
                "sources": "",
                "Bytes": "6446708",
                "Request": "77720",
                "Response": "6368988",
                "requests": "580",
                "sessions": "10"
            }
        ],
        "summary": {}
    }
    """

    @mdc(base_schema=Baseschema)
    class Detail(EndpointBase):
        policies: str
        sources: str
        Bytes: str
        Request: str
        Response: str
        requests: str
        sessions: str

    summary: dict
    details: List[Detail] = field(default_factory=list)
    Schema: ClassVar[Type[Schema]] = Baseschema


@mdc(base_schema=Baseschema)
class GlobalResource(EndpointBase):
    name: str
    current_usage: int
    max_capacity: int
    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class SystemResource(EndpointBase):
    cpu: int
    mem: int
    logDisk: str
    dbStatus: str
    diskUsage: int
    sessionCount: int
    connCntPerSec: int
    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class SystemStatus(EndpointBase):

    cluster: Optional[str]
    haMultiGroup: Optional[bool]
    cluster_members: Optional[List[dict]]
    serialNumber: str
    operationMode: str
    haStatus: str
    systemTime: str
    firmwareVersion: str
    up_days: str
    up_hrs: str
    up_mins: str
    firmware_partition: int
    administrativeDomain: str
    threatanalytics: str
    vmLicense: Optional[str]
    registration: dict
    readonly: bool
    bufferSizeMax: int
    fileUploadLimitMax: int

    Schema: ClassVar[Type[Schema]] = Baseschema
