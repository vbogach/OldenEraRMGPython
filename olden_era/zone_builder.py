from olden_era.models.biome_rules import BiomeRules
from olden_era.models.main_object import MainObject
from olden_era.models.zone import Zone


class ZoneBuilder:
    def __init__(self, zone_template: Zone):
        self._zone = zone_template.model_copy(deep=True)

    def set_ownership(self, player_idx: int) -> "ZoneBuilder":
        for main_object in self._zone.mainObjects:
            if main_object.spawn is not None:
                main_object.spawn = f"Player{player_idx}"
            if main_object.owner is not None:
                main_object.owner = f"Player{player_idx}"
        return self

    def set_name(self, name: str) -> "ZoneBuilder":
        self._zone.name = name
        return self

    def set_biomes(self, biome: BiomeRules) -> "ZoneBuilder":
        self._zone.zoneBiome = biome
        self._zone.contentBiome = biome
        self._zone.metaObjectsBiome = biome
        return self

    def remove_cities(self) -> "ZoneBuilder":
        self._zone.mainObjects = [main_object for main_object in self._zone.mainObjects if main_object.type != "City"]
        return self

    def add_main_objects(self, main_object: MainObject) -> "ZoneBuilder":
        self._zone.mainObjects.append(main_object)
        return self

    def remove_roads(self) -> "ZoneBuilder":
        self._zone.roads = []
        return self

    def build(self) -> Zone:
        return self._zone
