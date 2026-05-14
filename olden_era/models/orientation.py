from olden_era.models.base import Base


class Orientation(Base):
    zeroAngleZone: str | None = None
    baseAngleMin: int | None = None
    baseAngleMax: int | None = None
    randomAngleAmplitude: int | None = None
    randomAngleStep: int | None = None
    mode: str | None = None
