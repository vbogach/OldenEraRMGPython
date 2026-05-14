from olden_era.core.biome import Biome
from olden_era.core.sid import SID
from olden_era.models.base import Base


class Content(Base):
    sid: SID
    weight: int
    variant: int | None = None
    biome: Biome | None = None


class ContentList(Base):
    name: str
    content: list[Content]
