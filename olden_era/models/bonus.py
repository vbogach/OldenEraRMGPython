from olden_era.core.sid import SID
from olden_era.models.base import Base


class Bonus(Base):
    sid: SID | None = None
    receiverSide: int
    receiverFilter: str | None = None
    parameters: list[str]