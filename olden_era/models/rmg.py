from olden_era.models.base import Base
from olden_era.models.border import Border
from olden_era.models.content_count_limits import ContentCountLimits
from olden_era.models.content_list import ContentList
from olden_era.models.content_pool import ContentPool
from olden_era.models.game_rules import GameRules
from olden_era.models.global_bans import GlobalBans
from olden_era.models.named_content import MandatoryContent
from olden_era.models.orientation import Orientation
from olden_era.models.rmg_variant import RMGVariant
from olden_era.models.value_override import ValueOverride
from olden_era.models.zone_layout import ZoneLayout


class RMG(Base):
    border: Border | None = None
    contentCountLimits: list[ContentCountLimits]
    contentLists: list[ContentList]
    contentPools: list[ContentPool]
    description: str
    displayWinCondition: str
    gameMode: str
    gameRules: GameRules
    globalBans: GlobalBans | None = None
    mandatoryContent: list[MandatoryContent]
    name: str
    orientation: Orientation | None = None
    sizeX: int
    sizeZ: int
    valueOverrides: list[ValueOverride] | None = None
    variants: list[RMGVariant]
    zoneLayouts: list[ZoneLayout]
