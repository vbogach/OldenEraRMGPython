from olden_era.core.sid import SID
from olden_era.models.base import Base


class Identifiable(Base):
    sid: SID | None = None
    includeLists: list[str] | None = None
    variant: int | None = None
