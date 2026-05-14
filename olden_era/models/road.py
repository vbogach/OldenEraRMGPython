from pydantic import Field

from olden_era.models.base import Base


class RoadJunction(Base):
    type: str
    args: list[str] | None = None


class Road(Base):
    start: RoadJunction = Field(validation_alias="from", serialization_alias="from")
    end: RoadJunction =  Field(validation_alias="to", serialization_alias="to")
    type: str | None = None