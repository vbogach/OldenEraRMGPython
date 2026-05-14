from olden_era.core.sid import SID
from olden_era.models.base import Base


class ContentPoolValueDistribution(Base):
    priceBounds: list[int]
    weights: list[int]


class ContentPoolWeightedContent(Base):
    sid: SID
    variant: int | None = None
    weight: int


class ContentPoolGroup(Base):
    weight: int
    includeLists: list[str]
    content: list[ContentPoolWeightedContent] | None = None


class ContentPoolBan(Base):
    sid: SID
    variant: int | None = None


class ContentPool(Base):
    name: str
    valueDistribution: ContentPoolValueDistribution | None = None
    groups: list[ContentPoolGroup]
    bans: list[ContentPoolBan] | None = None