from pydantic import Field

from olden_era.models.base import Base
from olden_era.models.placement_rule import PlacementRule


class Connection(Base):
    guardValue: int | None = None
    guardRandomization: float | None = None
    guardWeeklyIncrement: float | None = None
    gatePlacement: str | None = None
    guardZone: str | None = None
    guardEscape: bool | None = None
    name: str | None = None
    start: str = Field(validation_alias="from", serialization_alias="from")
    end: str = Field(validation_alias="to", serialization_alias="to")
    connectionType: str
    simTurnSquad: bool | None = None
    road: bool | None = None
    length: float | None = None
    portalPlacementRulesFrom: list[PlacementRule] | None = None
    portalPlacementRulesTo: list[PlacementRule] | None = None
    guardMatchGroup: str | None = None
