import json
from collections import defaultdict
from itertools import combinations
from pathlib import Path

from olden_era.connection_builder import ConnectionBuilder
from olden_era.models.biome_rules import BiomeRules
from olden_era.models.connection import Connection
from olden_era.models.faction import Faction
from olden_era.models.main_object import MainObject
from olden_era.models.orientation import Orientation
from olden_era.models.rmg import RMG
from olden_era.models.road import Road, RoadJunction
from olden_era.zone_builder import ZoneBuilder

TEMPLATE_PATH = Path(
    r"C:\Program Files (x86)\Steam\steamapps\common\Heroes of Might and Magic Olden Era\HeroesOldenEra_Data\StreamingAssets\map_templates"
)
SYMPHONY_PATH = TEMPLATE_PATH / "Symphony.rmg.json"

with open(SYMPHONY_PATH, "r") as f:
    data = json.load(f)

rmg = RMG.model_validate(data)
spawn_template = rmg.variants[0].zones[0]
side_template = rmg.variants[0].zones[4]
treasure_template = rmg.variants[0].zones[28]
supertreasure_template = rmg.variants[0].zones[32]
spawn_template.size = 1.0
side_template.size = 1.0
supertreasure_template.size = 1.0
treasure_template.size = 1.0

# for idx, zone in enumerate(rmg.variants[0].zones):
#     print(idx)
#     print(zone)

zones = {}
connections = []

supertreasure_builder = ZoneBuilder(supertreasure_template)
supertreasure = supertreasure_builder.remove_cities().remove_roads().set_name("SupertreasureMid").build()
zones[supertreasure.name] = supertreasure

spawn_side_template = Connection(
    name="",
    start="",
    end="",
    connectionType="Direct",
    road=True,
    simTurnSquad=True,
    guardValue=3000,
    guardWeeklyIncrement=0.20,
)
side_treasure_template = Connection(
    name="",
    start="",
    end="",
    connectionType="Direct",
    road=True,
    simTurnSquad=True,
    guardValue=9000,
    guardWeeklyIncrement=0.20,
)
treasure_supertreasure_template = Connection(
    name="",
    start="",
    end="",
    connectionType="Direct",
    road=True,
    simTurnSquad=True,
    guardValue=18000,
    guardWeeklyIncrement=0.20,
)
spawn_supertreasure_template = Connection(
    name="",
    start="",
    end="",
    connectionType="Direct",
    road=True,
    simTurnSquad=True,
    guardValue=48000,
    guardWeeklyIncrement=0.10,
)

player_indices = list(range(1, 4))
for player_idx in player_indices:
    spawn = (
        ZoneBuilder(spawn_template)
        .set_ownership(player_idx)
        .remove_cities()
        .set_name(f"Spawn{player_idx}")
        .remove_roads()
        .build()
    )
    match_biome = BiomeRules(type="MatchZone", args=[spawn.name])
    city = MainObject(
        type="City",
        faction=Faction(type="Match", args=["0", spawn.name]),
        removeGuardIfHasOwner=True,
        guardChance=1.0,
        guardValue=2000,
        guardRandomization=0.2,
        guardWeeklyIncrement=0.1,
        buildingsConstructionSid="poor_buildings_construction",
        placement="Center",
    )
    side = (
        ZoneBuilder(side_template)
        .remove_cities()
        .set_name(f"Side{player_idx}")
        .remove_roads()
        .set_biomes(match_biome)
        .add_main_objects(city)
        .build()
    )
    nonmatch_biome_rule = f"differentFrom: Spawn{player_idx}"
    nonmatch_biome = BiomeRules(
        type="FromList", args=["Grass", "Deathland", "Snow", "Autumn", "Lava", "Dirt", nonmatch_biome_rule]
    )
    treasure = (
        ZoneBuilder(treasure_template)
        .remove_cities()
        .remove_roads()
        .set_name(f"Treasure{player_idx}")
        .set_biomes(nonmatch_biome)
        .build()
    )
    zones[spawn.name] = spawn
    zones[side.name] = side
    zones[treasure.name] = treasure

    connection_spawn_side = ConnectionBuilder(spawn_side_template).from_to(spawn, side).build()
    connections.append(connection_spawn_side)
    connection_side_treasure = ConnectionBuilder(side_treasure_template).from_to(side, treasure).build()
    connections.append(connection_side_treasure)
    connection_treasure_supertreasure = (
        ConnectionBuilder(treasure_supertreasure_template).from_to(treasure, supertreasure).build()
    )
    connections.append(connection_treasure_supertreasure)

for p1, p2 in combinations(player_indices, 2):
    supertreasure_side = (
        ZoneBuilder(supertreasure_template)
        .remove_cities()
        .remove_roads()
        .set_name(f"SupertreasureSide{p1}{p2}")
        .build()
    )
    zones[supertreasure_side.name] = supertreasure_side

    spawn_p1 = zones[f"Spawn{p1}"]
    spawn_p2 = zones[f"Spawn{p2}"]
    supertreasure_mid = zones["SupertreasureMid"]
    connection_p1 = ConnectionBuilder(spawn_supertreasure_template).from_to(supertreasure_side, spawn_p1).build()
    connections.append(connection_p1)
    connection_p2 = ConnectionBuilder(spawn_supertreasure_template).from_to(supertreasure_side, spawn_p2).build()
    connections.append(connection_p2)
    # connection_mid = (ConnectionBuilder(treasure_supertreasure_template).from_to(supertreasure_side, supertreasure_mid).build())
    # connections.append(connection_mid)


zone_to_connection_list = defaultdict(list)

for connection in connections:
    zone_to_connection_list[connection.start].append(connection)
    zone_to_connection_list[connection.end].append(connection)

for zone_name, connection_list in zone_to_connection_list.items():
    zone = zones[zone_name]
    if len(zone.mainObjects) > 0:
        for connection in connection_list:
            zone.roads.append(
                Road(
                    type="Stone",
                    start=RoadJunction(type="MainObject", args=["0"]),
                    end=RoadJunction(type="Connection", args=[connection.name]),
                )
            )
        for idx in range(1, len(zone.mainObjects)):
            zone.roads.append(
                Road(
                    type="Stone",
                    start=RoadJunction(type="MainObject", args=["0"]),
                    end=RoadJunction(type="MainObject", args=[f"{idx}"]),
                )
            )
    else:
        for c1, c2 in combinations(connection_list, 2):
            zone.roads.append(
                Road(
                    type="Stone",
                    start=RoadJunction(type="Connection", args=[c1.name]),
                    end=RoadJunction(type="Connection", args=[c2.name]),
                )
            )
rmg_copy = rmg.model_copy(deep=True)
rmg_copy.variants[0].zones = list(zones.values())
rmg_copy.variants[0].connections = connections
rmg_copy.name = "Test1"
rmg_copy.description = "Test1"
orientation = Orientation(
    zeroAngleZone="Spawn1",
    mode="MinimalBoundingSquare",
    baseAngleMin=120,
    baseAngleMax=120,
    randomAngleAmplitude=0,
    randomAngleStep=120,
)
rmg_copy.variants[0].orientation = orientation
rmg_copy.sizeX = 128
rmg_copy.sizeZ = 128
rmg_copy.gameRules.heroCountMin = 2
rmg_copy.gameRules.heroCountMax = 2
rmg_copy.gameRules.heroCountIncrement = 0
with open(
    r"C:\Program Files (x86)\Steam\steamapps\common\Heroes of Might and Magic Olden Era\HeroesOldenEra_Data\StreamingAssets\map_templates\template.rmg.json",
    "w",
) as f:
    f.write(rmg_copy.model_dump_json(exclude_none=True, by_alias=True))
