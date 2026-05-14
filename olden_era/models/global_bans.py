from olden_era.models.base import Base


class GlobalBans(Base):
    magics: list[str] | None = None
    items: list[str] | None = None
    heroes: list[str] | None = None
