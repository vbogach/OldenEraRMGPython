from olden_era.models.base import Base


class Faction(Base):
    type: str
    args: list[str]