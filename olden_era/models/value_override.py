from olden_era.models.base import Base
from olden_era.models.identifiable import Identifiable


class ValueOverride(Identifiable):
    guardValue: int