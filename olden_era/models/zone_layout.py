from olden_era.models.base import Base


class AmbientPickupDistribution(Base):
    groupSizeWeights: list[int]
    obstacleAttraction: float
    roadAttraction: float
    noise: float
    repulsion: float


class GuardedEncounterResourceFractions(Base):
    fractions: list[float]
    countBounds: list[None]


class ElevationModes(Base):
    weight: float
    minElevatedFraction: float
    maxElevatedFraction: float


class ZoneLayout(Base):
    ambientPickupDistribution: AmbientPickupDistribution
    guardedEncounterResourceFractions: GuardedEncounterResourceFractions
    roadClusterArea: int
    elevationModes: list[ElevationModes] | None = None
    elevationClusterScale: float
    minLakeArea: int | None = None
    lakesFill: float
    obstaclesFillVoid: float
    obstaclesFill: float
    name: str