from olden_era.models.base import Base
from olden_era.models.faction import Faction


class MainObject(Base):
    type: str | None = None
    spawn: str | None = None
    faction: Faction | None = None
    removeGuardIfHasOwner: bool | None = None
    guardChance: float | None = None
    guardValue: int | None = None
    guardRandomization: float | None = None
    guardWeeklyIncrement: float | None = None
    buildingsConstructionSid: str | None = None
    placement: str | None = None
    placementArgs: list[str] | None = None
    holdCityWinCon: bool | None = None
    factions: list[Faction] | None = None
    owner: str | None = None
    isKeyObject: bool | None = None
    initialUnitIncrement: int | None = None
    enableWeeklyUnitIncrement: bool | None = None