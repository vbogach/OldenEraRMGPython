from olden_era.models.base import Base


class PlacementRule(Base):
    type: str
    args: list[str | int]
    target: float | None = None
    targetMin: float | None = None
    targetMax: float | None = None
    weight: float