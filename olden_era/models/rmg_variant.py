from olden_era.models.base import Base
from olden_era.models.border import Border
from olden_era.models.connection import Connection
from olden_era.models.orientation import Orientation
from olden_era.models.zone import Zone


class RMGVariant(Base):
    orientation: Orientation
    border: Border | None = None
    zones: list[Zone]
    connections: list[Connection]
