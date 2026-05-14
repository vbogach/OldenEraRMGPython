from olden_era.models.main_object import MainObject
from olden_era.models.zone import Zone


def strip_roads(zone: Zone):
    zone_copy = zone.model_copy(deep=True)
    zone_copy.roads = []
    return zone_copy

def find_spawn(zone: Zone) -> MainObject:
    return next(candidate for candidate in zone.mainObjects if candidate.type == "Spawn")

def replace_ownership(zone: Zone, player_idx: int) -> Zone:
    zone_copy = zone.model_copy(deep=True)
    zone_copy.name = f"Spawn{player_idx}"
    for main_object in zone_copy.mainObjects:
        if main_object.spawn is not None:
            main_object.spawn = f"Player{player_idx}"
        if main_object.owner is not None:
            main_object.owner = f"Player{player_idx}"
    return zone_copy

def remove_cities(zone: Zone) -> Zone:
    zone_copy = zone.model_copy(deep=True)
    zone_copy.mainObjects = [main_object for main_object in zone_copy.mainObjects if main_object.type != "City"]
    return Zone