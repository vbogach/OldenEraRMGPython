from olden_era.models.base import Base
from olden_era.models.bonus import Bonus
from olden_era.models.global_bans import GlobalBans
from olden_era.models.value_override import ValueOverride


class GameRules(Base):
    astrologyExpModifier: float | None = None
    bonuses: Bonus | list[Bonus] | None = None
    championSelectRule: str | None = None
    encounterHoles: bool
    factionLawsExpModifier: float | None = None
    gladiatorArena: bool | None = None
    gladiatorArenaCountDay: int | None = None
    gladiatorArenaDaysDelayStart: int | None = None
    gladiatorArenaRegistrationStartFight: bool | None = None
    gladiatorArenaRegistrationStartWork: bool | None = None
    globalBans: GlobalBans | None = None
    heroCountIncrement: int
    heroCountMax: int
    heroCountMin: int
    heroHireBan: bool
    tournamentRules: bool | None = None
    valueOverrides: list[ValueOverride] | None = None
    winConditions: dict