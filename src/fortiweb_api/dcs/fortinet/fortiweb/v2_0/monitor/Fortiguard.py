from typing import List, Optional, Dict, Any, ClassVar, Type
from marshmallow import Schema, EXCLUDE
from marshmallow_dataclass import dataclass as mdc

from fortiweb_api.dcs.EndpointBase import EndpointBase
from fortiweb_api.dcs.fortinet.fortiweb.BaseSchema import Baseschema


@mdc(base_schema=Baseschema)
class Registration:
    label: str
    label_key: str
    url: str
    text: str
    is_registered: bool

    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class SecurityService:
    expired: str
    is_valid: bool
    expired_text: Optional[str]
    expired_url: Optional[str]
    lastUpdateTime: str
    lastUpdateMethod: str
    update_url: str
    update_text: str
    buildNumber: str
    engineVersion: str
    label_key: str

    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class AntivirusService:
    expired: str
    is_valid: bool
    anti_expired_text: Optional[str]
    anti_expired_url: Optional[str]
    lastUpdateTime: str
    lastUpdateMethod: str
    engineLastUpdateTime: str
    engineLastUpdateMethod: str
    anti_update_url: str
    anti_update_text: str
    regularVirusDatabaseVersion: str
    exVirusDatabaseVersion: str
    label_key: str
    antivirusEnginVersion: str

    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class ReputationService:
    expired: str
    is_valid: bool
    reputation_expired_text: Optional[str]
    reputation_expired_url: Optional[str]
    lastUpdateTime: str
    lastUpdateMethod: str
    reputation_update_url: str
    reputation_update_text: str
    reputationBuildNumber: str
    label_key: str

    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class CredentialStuffingDefense:
    expired: str
    is_valid: bool
    expired_text: Optional[str]
    expired_url: Optional[str]
    lastUpdateTime: str
    lastUpdateMethod: str
    databaseVersion: str
    label_key: str

    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class SbclService:
    expired: str
    is_valid: bool
    expired_text: Optional[str]
    expired_url: Optional[str]
    lastUpdateTime: str
    lastUpdateMethod: str
    label_key: str
    sandboxCloudVersion: str

    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class GeodbService:
    expired: str
    is_valid: bool
    lastUpdateTime: str
    lastUpdateMethod: str
    label_key: str
    geodbVersion: str

    Schema: ClassVar[Type[Schema]] = Baseschema

@mdc(base_schema=Baseschema)
class ThreatAnalytics:
    expired: str
    is_valid: bool

    Schema: ClassVar[Type[Schema]] = Baseschema


@mdc(base_schema=Baseschema)
class Fortiguard(EndpointBase):
    registration: Registration
    securityService: SecurityService
    antivirusService: AntivirusService
    reputationService: ReputationService
    credentialStuffingDefense: CredentialStuffingDefense
    sbclService: SbclService
    geodbService: GeodbService
    ThreatAnalytics: ThreatAnalytics
    updateStatus: str
    startedAt: str
    updateDone: bool
    stop: bool
    override: bool
    scheduled: bool
    isUpdating: bool
    updateControl: List[str]
    address: str
    scheduleType: str
    everySelect: int
    dailySelect: int
    weeklyDaySelect: int
    weeklyHourSelect: int
    dbVersionType: int
    regularVersion: str
    regularIncludedSignatures: int
    regularIncludedGrayware: int
    regularDescription: str
    extendedVersion: str
    extendedIncludedSignatures: int
    extendedIncludedGrayware: int
    extendedDescription: str
    bufferSize: int
    bufferSizeMax: int
    useFSD: int
    useFSDVersion: str
    useFSDDescription: str
    _id: str

    Schema: ClassVar[Type[Schema]] = Baseschema


    @classmethod
    def get_post_json_template(cls) -> str:
        cls.post_required_fields = []
        return super().get_post_json_template()