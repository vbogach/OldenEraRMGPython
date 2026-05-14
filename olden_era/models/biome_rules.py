from olden_era.models.base import Base


class BiomeRules(Base):
    type: str
    args: list[str]