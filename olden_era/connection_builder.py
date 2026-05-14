from olden_era.models.connection import Connection
from olden_era.models.zone import Zone


class ConnectionBuilder:
    def __init__(self, connection_template: Connection):
        self._connection = connection_template.model_copy(deep=True)

    def from_to(self, start: Zone, end: Zone) -> "ConnectionBuilder":
        self._connection.start = start.name
        self._connection.end = end.name
        self._connection.name = f"{start.name}{end.name}"
        return self

    def build(self) -> Connection:
        return self._connection
