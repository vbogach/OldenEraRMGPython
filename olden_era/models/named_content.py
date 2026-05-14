from olden_era.models.identifiable import Identifiable
from olden_era.models.placement_rule import PlacementRule


class MandatoryContent(Identifiable):
    name: str | None = None
    isMine: bool | None = None
    isGuarded: bool | None = None
    road: bool | None = None
    guardValue: int | None = None
    designatedEncounter: bool | None = None
    soloEncounter: bool | None = None
    rules: list[PlacementRule] | None = None
    weight: int | None = None
    owner: str | None = None
    content: list["MandatoryContent"] | None = None
