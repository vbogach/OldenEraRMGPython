from olden_era.models.base import Base
from olden_era.models.identifiable import Identifiable


class Limit(Identifiable):
    maxCount: int
    content: list[Identifiable] | None = None


class ContentCountLimits(Base):
    name: str
    limits: list[Limit] | None = None
