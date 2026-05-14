from olden_era.models.base import Base


class BorderNoise(Base):
    amp: float
    freq: float


class Border(Base):
    cornerRadius: float
    obstaclesWidth: int
    waterWidth: int
    waterType: str
    obstaclesNoise: list[BorderNoise]
    waterNoise: list[BorderNoise]
