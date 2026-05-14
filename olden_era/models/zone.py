from olden_era.models.base import Base
from olden_era.models.biome_rules import BiomeRules
from olden_era.models.encounter_holes_settings import EncounterHolesSettings
from olden_era.models.main_object import MainObject
from olden_era.models.road import Road


class Zone(Base):
    name: str
    size: float
    zoneBiome: BiomeRules
    contentBiome: BiomeRules
    metaObjectsBiome: BiomeRules
    mainObjects: list[MainObject]
    resourcesValuePerArea: int
    resourcesValue: int
    unguardedContentValue: int
    unguardedContentValuePerArea: int
    guardedContentValue: int
    guardedContentValuePerArea: int
    contentCountLimits: list[str] | str
    mandatoryContent: list[str]
    resourcesContentPool: list[str]
    unguardedContentPool: list[str]
    guardedContentPool: list[str]
    randomHireInitialUnitIncrement: list[int] | None = None
    randomHireEnableWeeklyUnitIncrement: list[bool] | None = None
    diplomacyModifier: float | None = None
    guardReactionDistribution: list[int]
    guardWeeklyIncrement: float
    guardMultiplier: float | None = None
    guardRandomization: float
    guardCutoffValue: int
    layout: str
    encounterHolesSettings: EncounterHolesSettings | None = None
    roads: list[Road] | None = None
    crossroadsPosition: int | None = None
