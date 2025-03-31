
from typing import Callable, Dict, List, TYPE_CHECKING, NamedTuple
from BaseClasses import CollectionState, MultiWorld, Region, Entrance
from worlds.generic.Rules import CollectionRule
from worlds.iji.Rules import can_access_sector, can_reach_nulldriver, can_reach_poster_nine, can_reach_sector_z, can_rocket_boost, has_stats, has_multiple_stats, has_weapon_stats
from .Locations import IjiLocation, location_table

if TYPE_CHECKING:
    from . import IjiWorld

def create_regions(world: "IjiWorld", healthbalancing: bool, compactment: int):

    region_menu = create_region(world, "Menu")

def sector_z_available(world: "IjiWorld") -> int:
    if (world.options.EndGoal.value == world.options.EndGoal.option_sector_y or\
        world.options.EndGoal.value == world.options.EndGoal.option_sector_z):
        return 1
    else:
        return 0

def connect_region_exits(world: "IjiWorld", name: str):
    pass

def create_region(world: "IjiWorld", name: str) -> Region:
    region = Region(name, world.player, world.multiworld)
    
    region.add_locations({
        location_name: location_data.code for location_name, location_data in location_table.items()
        if location_data.region==region.name and location_data.valid(world)
    }, IjiLocation)


    return region

class IjiRegionExitData(NamedTuple):
    valid: Callable[["IjiWorld"], bool] = lambda world: True
    logic: Callable[["IjiWorld", CollectionState], bool] = lambda world, state: True

region_exit_table: Dict[str, Dict[str, IjiRegionExitData]] = {
    "Menu": {
        "Global",
        "Sector 1"},
    "Global": {},
    "Sector 1": {
        "Sector 1 Restricted Area": IjiRegionExitData(
            valid=lambda world: world.max_stats["Strength Stat"] >= 3,
            logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 3,
                                                 world.options.CompactStatItems.value)),
        "Sector 1 Poster": IjiRegionExitData(
            valid=lambda world: world.max_stats["Strength Stat"] >= 1,
            logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 1,
                                                 world.options.CompactStatItems.value)),
        "Sector 2": IjiRegionExitData(
            valid=lambda world: world.max_stats["Sector Access"] >= 1,
            logic=lambda world, state: can_access_sector(world, state, 2))},
    "Sector 1 Restricted Area": {
        "Sector Z": IjiRegionExitData(
            valid=lambda world: sector_z_available(world),
            logic=lambda world, state: can_reach_sector_z(state, world.player, world,
                                                          world.options.SectorZPosterLocationsRequired.value,
                                                          world.options.SectorZRibbonItemsRequired.value,
                                                          world.options.CompactStatItems.value))},
    "Sector 1 Poster": {},
    "Sector 2": {
        "Sector 2 Storage Transport Top": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Health Stat"] >= 1 or world.options.SpecialTraitItems),
            logic=lambda world, state: can_rocket_boost(state, world.player)),
        "Sector 2 Poster": IjiRegionExitData(
            valid=lambda world: (world.options.LogicDifficulty.value >= world.options.LogicDifficulty.option_obscure_logic or
                                 world.max_stats["Strength Stat"] >= 3 or world.max_stats["Tasen Stat"] >= 2),
            logic=lambda world, state: (has_stats(state, "Strength Stat", world.player, 3,
                                                  world.options.CompactStatItems.value) or \
                                        has_weapon_stats(state, "Machine Gun", world.player,
                                                         world.options.CompactStatItems.value) or \
                                        world.options.LogicDifficulty.value >= \
                                        world.options.LogicDifficulty.option_obscure_logic)),
        "Sector 3": IjiRegionExitData(
            valid=lambda world: world.max_stats["Sector Access"] >= 2,
            logic=lambda world, state: can_access_sector(world, state, 3))},
    "Sector 2 Storage Transport Top": {
        "Sector 2 Supercharge": IjiRegionExitData(
            valid=lambda world: world.max_stats["Tasen Stat"] >= 5,
            logic=lambda world, state: has_weapon_stats(state, "Rocket Launcher", world.player,
                                                        world.options.CompactStatItems.value))},
    "Sector 2 Supercharge": {},
    "Sector 2 Poster": {},
    "Sector 3": {
        "Sector 3 Restricted Area": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Strength Stat"] >= 9 and world.max_stats["Crack Stat"] >= 9),
            logic=lambda world, state: (has_multiple_stats(state, {"Strength Stat": 9, "Crack Stat": 9},
                                                           world.player, world.options.CompactStatItems.value))),
        "Sector 3 Poster": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Strength Stat"] >= 3 and\
                (world.max_stats["Health Stat"] >= 1 or world.options.SpecialTraitItems))),
        "Sector 3 Supercharge": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Komato Stat"] >= 5 and world.max_stats["Crack Stat"] >= 5),
            logic=lambda world, state: has_weapon_stats(state, "Hyper Pulse", world.player,
                                                        world.options.CompactStatItems.value)),
        "Sector 4": IjiRegionExitData(
            valid=lambda world: world.max_stats["Sector Access"] >= 3,
            logic=lambda world, state: can_access_sector(world, state, 4))},
    "Sector 3 Restricted Area": {},
    "Sector 3 Poster": {},
    "Sector 4": {
        "Sector 4 Surveillance Control": IjiRegionExitData(
            valid=lambda world: world.max_stats["Tasen Stat"] >= 5,
            logic=lambda world, state: has_weapon_stats("Rocket Launcher", world.player,
                                                        world.options.CompactStatItems.value)),
        "Sector 4 Top of Main Storage": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Tasen Stat"] >= 5 or
                                 world.max_stats["Strength Stat"] >= 3 or
                                 world.max_stats["Health Stat"] >= 1 or
                                 world.options.SpecialTraitItems),
            logic=lambda world, state: (has_weapon_stats(state, "Rocket Launcher", world.player,
                                                        world.options.CompactStatItems.value) or
                                        has_stats(state, "Strength Stat", world.player, 3,
                                                  world.options.CompactStatitems.value) or
                                        can_rocket_boost(state, world.player))),
        "Sector 4 Poster": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Tasen Stat"] >= 5 or
                                 world.max_stats["Strength Stat"] >= 3 or
                                 world.options.LogicDifficulty.value >= world.options.LogicDifficulty.option_obscure_logic),
            logic=lambda world, state: (has_weapon_stats(state, "Rocket Launcher", world.player,
                                                        world.options.CompactStatItems.value) or
                                        has_stats(state, "Strength Stat", world.player, 3,
                                                  world.options.CompactStatItems.value) or
                                        world.options.LogicDifficulty.value >= world.options.LogicDifficulty.option_obscure_logic)),
        "Sector 5": IjiRegionExitData(
            valid=lambda world: world.max_stats["Sector Access"] >= 4,
            logic=lambda world, state: can_access_sector(world, state, 5))},
    "Sector 4 Surveillance Control": {},
    "Sector 4 Top of Main Storage": {},
    "Sector 4 Poster": {},
    "Sector 5": {
        "Sector 5 Poster": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Tasen Stat"] >= 9 and
                                 (world.max_stats["Crack Stat"] >= 8 or
                                  world.options.LogicDifficulty.value >= world.options.LogicDifficulty.option_obscure_logic)),
            logic=lambda world, state: (has_weapon_stats(state, "Nuke", world.player,
                                                         world.options.CompactStatItems.value) or
                                        (has_weapon_stats(state, "MPFB Devastator", world.player,
                                                         world.options.CompactStatItems.value) and
                                         world.options.LogicDifficulty.value >= world.options.LogicDifficulty.option_obscure_logic))),
        "Sector 6": IjiRegionExitData(
            valid=lambda world: world.max_stats["Sector Access"] >= 5,
            logic=lambda world, state: can_access_sector(world, state, 6))},
    "Sector 5 Poster": {},
    "Sector 6": {
        "Sector 6 Poster": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Crack Stat"] >= 9 and
                                 world.max_stats["Tasen Stat"] >= 9 and
                                 world.max_stats["Komato Stat"] >= 9),
            logic=lambda world, state: has_weapon_stats(state, "Velocithor", world.player,
                                                        world.options.CompactStatItems.value)),
        "Sector 7": IjiRegionExitData(
            valid=lambda world: world.max_stats["Sector Access"] >= 6,
            logic=lambda world, state: can_access_sector(world, state, 7))},
    "Sector 6 Poster": {},
    "Sector 7": {
        "Sector 7 Heavy Weapon Armory": IjiRegionExitData(
            valid=lambda world: world.max_stats["Strength Stat"] >= 2,
            logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 2,
                                                 world.options.CompactStatItems.value)),
        "Sector 7 Hyper Turret Logbooks": IjiRegionExitData(
            valid=lambda world: world.max_stats["Crack Stat"] >= 2,
            logic=lambda world, state: has_stats(state, "Crack Stat", world.player, 2,
                                                 world.options.CompactStatitems.value)),
        "Sector 7 Crackers' Hideout": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Tasen Stat"] >= 5 or
                                 world.max_stats["Komato Stat"] >= 5),
            logic=lambda world, state: (has_weapon_stats(state, "Rocket Launcher", world.player,
                                                         world.options.CompactStatItems.value) or
                                        has_weapon_stats(state, "Shocksplinter", world.player,
                                                         world.options.CompactStatItems.value))),
        "Sector 7 Poster": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Komato Stat"] >= 9 and
                                 world.max_stats["Attack Stat"] >= 2 and
                                 world.max_stats["Tasen Stat"] >= 9 and
                                 world.max_stats["Crack Stat"] >= 8 and
                                 world.max_stats["Strength Stat"] >= 2),
            logic=lambda world, state: (has_weapon_stats(state, "CFIS", world.player,
                                                         world.options.CompactStatItems.value) and
                                        has_weapon_stats(state, "Nuke", world.player,
                                                         world.options.CompactStatItems.value) and
                                        has_multiple_stats(state, {"Strength Stat": 2, "Attack Stat": 2}, world.player,
                                                           world.options.CompactStatItems.value))),
        "Sector 8": IjiRegionExitData(
            valid=lambda world: world.max_stats["Sector Access"] >= 7,
            logic=lambda world, state: can_access_sector(world, state, 8))},
    "Sector 7 Heavy Weapon Armory": {},
    "Sector 7 Hyper Turret Logbooks": {},
    "Sector 7 Crackers' Hideout": {},
    "Sector 7 Poster": {},
    "Sector 8": {
        "Sector 8 Staff Storage Return Trip": IjiRegionExitData(
            valid=lambda world: world.max_stats["Crack Stat"] >= 4,
            logic=lambda world, state: has_stats(state, "Crack Stat", world.player, 4,
                                          world.options.CompactStatItems.value)),
        "Sector 8 Poster": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Health Stat"] >= 1 or
                                 world.options.SpecialTraitItems),
            logic=lambda world, state: can_rocket_boost(state, world.player)),
        "Sector 9": IjiRegionExitData(
            valid=lambda world: world.max_stats["Sector Access"] >= 8,
            logic=lambda world, state: can_access_sector(world, state, 9))},
    "Sector 8 Staff Storage Return Trip": {},
    "Sector 8 Poster": {},
    "Sector 9": {
        "Sector 9 Poster": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Health Stat"] >= 9 and
                                 world.max_stats["Tasen Stat"] >= 9),
            logic=lambda world, state: (has_stats(state, "Health Stat", world.player, 9,
                                                 world.options.CompactStatItems.value) and
                                        has_weapon_stats(state, "MPFB Devastator", world.player,
                                                         world.options.CompactStatItems.value))),
        "Sector 9 Deep Sector": IjiRegionExitData(),
        "Sector X": IjiRegionExitData(
            valid=lambda world: world.max_stats["Sector Access"] >= 9,
            logic=lambda world, state: can_access_sector(world, state, 10))},
    "Sector 9 Poster": {},
    "Sector 9 Deep Sector": {},
    "Sector X": {
        "Sector X Ventilation Shaft": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Tasen Stat"] >= 9 and
                                 world.max_stats["Crack Stat"] >= 8),
            logic=lambda world, state: has_weapon_stats(state, "Nuke", world.player,
                                                        world.options.CompactStatItems.value)),
        "Sector X Ultimate Charge Terminal": IjiRegionExitData(),
        "Sector Y": IjiRegionExitData(
            valid = lambda world: (world.options.EndGoal.value == world.options.EndGoal.option_sector_y or
                world.options.PostGameLocations.value == world.options.PostGameLocations.option_sector_y),
            logic = lambda world, state: state.can_reach_region("Sector Z Inner Prey", world.player))},
    "Sector X Ventilation Shaft": {
        "Sector X Poster": IjiRegionExitData(
            valid=lambda world: (world.max_stats["Komato Stat"] >= 5 and
                                 world.max_stats["Crack Stat"] >= 6),
            logic=lambda world, state: has_weapon_stats(state, "Splintergun", world.player,
                                                        world.options.CompactStatItems.value))},
    "Sector X Poster": {},
    "Sector X Maximum Charge Terminal": {},
    "Sector Z": {
        "Sector Z Inner Prey": IjiRegionExitData(
            valid=lambda world: sector_z_available(world),
            logic=lambda world, state: can_reach_nulldriver(state, world.player, world,
                               world.options.NullDriverPosterLocationsRequired.value,
                               world.options.NullDriverRibbonItemsRequired.value,
                               world.options.CompactStatItems.value))},
    "Sector Z Inner Prey": {},
    "Sector Y": {}
}

normal_level_regions: Dict[str, List[str]] = {
    "Sector 1": ["Level 1", "Level 2", "Level 3", "Level 4", "Level 5",
        "Reach Health Level 2",
        "Reach Health Level 3",
        "Reach Health Level 4",
        "Reach Health Level 5",
        "Reach Health Level 6",
        "Reach Attack Level 2",
        "Reach Attack Level 3",
        "Reach Attack Level 4",
        "Reach Attack Level 5",
        "Reach Attack Level 6",
        "Reach Assmilate Level 2",
        "Reach Assmilate Level 3",
        "Reach Assmilate Level 4",
        "Reach Assmilate Level 5",
        "Reach Assmilate Level 6",
        "Reach Strength Level 2",
        "Reach Strength Level 3",
        "Reach Strength Level 4",
        "Reach Strength Level 5",
        "Reach Strength Level 6",
        "Reach Crack Level 2",
        "Reach Crack Level 3",
        "Reach Crack Level 4",
        "Reach Crack Level 5",
        "Reach Crack Level 6",
        "Reach Tasen Level 2",
        "Reach Tasen Level 3",
        "Reach Tasen Level 4",
        "Reach Tasen Level 5",
        "Reach Tasen Level 6",
        "Reach Komato Level 2",
        "Reach Komato Level 3",
        "Reach Komato Level 4",
        "Reach Komato Level 5",
        "Reach Komato Level 6"
        ],
    "Sector 2": ["Level 6", "Level 7", "Level 8", "Level 9", "Level 10",
        "Reach Health Level 7",
        "Reach Health Level 8",
        "Reach Health Level 9",
        "Reach Health Level 10",
        "Reach Attack Level 7",
        "Reach Attack Level 8",
        "Reach Attack Level 9",
        "Reach Attack Level 10",
        "Reach Assmilate Level 7",
        "Reach Assmilate Level 8",
        "Reach Assmilate Level 9",
        "Reach Assmilate Level 10",
        "Reach Strength Level 7",
        "Reach Strength Level 8",
        "Reach Strength Level 9",
        "Reach Strength Level 10",
        "Reach Crack Level 7",
        "Reach Crack Level 8",
        "Reach Crack Level 9",
        "Reach Crack Level 10",
        "Reach Tasen Level 7",
        "Reach Tasen Level 8",
        "Reach Tasen Level 9",
        "Reach Tasen Level 10",
        "Reach Komato Level 7",
        "Reach Komato Level 8",
        "Reach Komato Level 9",
        "Reach Komato Level 10"
        ],
    "Sector 3": ["Level 11", "Level 12", "Level 13", "Level 14", "Level 15"],
    "Sector 4": ["Level 16", "Level 17", "Level 18", "Level 19", "Level 20"],
    "Sector 5": ["Level 21", "Level 22", "Level 23", "Level 24", "Level 25"],
    "Sector 6": ["Level 26", "Level 27", "Level 28", "Level 29", "Level 30"],
    "Sector 7": ["Level 31", "Level 32", "Level 33", "Level 34", "Level 35"],
    "Sector 8": ["Level 36", "Level 37", "Level 38", "Level 39", "Level 40"],
    "Sector 9": ["Level 41", "Level 42", "Level 43", "Level 44", "Level 45"],
    "Sector X": ["Level 46", "Level 47", "Level 48", "Level 49", "Level 50"]
}

hard_level_regions: Dict[str, List[str]] = {
    "Sector 1": ["Level 1", "Level 2", "Level 3", "Level 4",
        "Reach Health Level 2",
        "Reach Health Level 3",
        "Reach Health Level 4",
        "Reach Health Level 5",
        "Reach Attack Level 2",
        "Reach Attack Level 3",
        "Reach Attack Level 4",
        "Reach Attack Level 5",
        "Reach Assmilate Level 2",
        "Reach Assmilate Level 3",
        "Reach Assmilate Level 4",
        "Reach Assmilate Level 5",
        "Reach Strength Level 2",
        "Reach Strength Level 3",
        "Reach Strength Level 4",
        "Reach Strength Level 5",
        "Reach Crack Level 2",
        "Reach Crack Level 3",
        "Reach Crack Level 4",
        "Reach Crack Level 5",
        "Reach Tasen Level 2",
        "Reach Tasen Level 3",
        "Reach Tasen Level 4",
        "Reach Tasen Level 5",
        "Reach Komato Level 2",
        "Reach Komato Level 3",
        "Reach Komato Level 4",
        "Reach Komato Level 5"
        ],
    "Sector 2": ["Level 5","Level 6", "Level 7", "Level 8",
        "Reach Health Level 6",
        "Reach Health Level 7",
        "Reach Health Level 8",
        "Reach Health Level 9",
        "Reach Attack Level 6",
        "Reach Attack Level 7",
        "Reach Attack Level 8",
        "Reach Attack Level 9",
        "Reach Assmilate Level 6",
        "Reach Assmilate Level 7",
        "Reach Assmilate Level 8",
        "Reach Assmilate Level 9",
        "Reach Strength Level 6",
        "Reach Strength Level 7",
        "Reach Strength Level 8",
        "Reach Strength Level 9",
        "Reach Crack Level 6",
        "Reach Crack Level 7",
        "Reach Crack Level 8",
        "Reach Crack Level 9",
        "Reach Tasen Level 6",
        "Reach Tasen Level 7",
        "Reach Tasen Level 8",
        "Reach Tasen Level 9",
        "Reach Komato Level 6",
        "Reach Komato Level 7",
        "Reach Komato Level 8",
        "Reach Komato Level 9"
        ],
    "Sector 3": ["Level 9", "Level 10", "Level 11", "Level 12",
        "Reach Health Level 10",
        "Reach Attack Level 10",
        "Reach Assimilate Level 10",
        "Reach Strength Level 10",
        "Reach Crack Level 10",
        "Reach Tasen Level 10",
        "Reach Komato Level 10"
        ],
    "Sector 4": ["Level 13", "Level 14", "Level 15", "Level 16"],
    "Sector 5": ["Level 17", "Level 18", "Level 19", "Level 20"],
    "Sector 6": ["Level 21", "Level 22", "Level 23", "level 24"],
    "Sector 7": ["Level 25", "Level 26", "Level 27", "Level 28"],
    "Sector 8": ["Level 29", "Level 30", "Level 31", "Level 32"],
    "Sector 9": ["Level 33", "Level 34", "Level 35", "Level 36"],
    "Sector X": ["Level 37", "Level 38", "Level 39", "Level 40"]
}

extreme_level_regions: Dict[str, List[str]] = {
    "Sector 1": ["Level 1", "Level 2", "Level 3",
        "Reach Health Level 2",
        "Reach Health Level 3",
        "Reach Health Level 4",
        "Reach Attack Level 2",
        "Reach Attack Level 3",
        "Reach Attack Level 4",
        "Reach Assmilate Level 2",
        "Reach Assmilate Level 3",
        "Reach Assmilate Level 4",
        "Reach Strength Level 2",
        "Reach Strength Level 3",
        "Reach Strength Level 4",
        "Reach Crack Level 2",
        "Reach Crack Level 3",
        "Reach Crack Level 4",
        "Reach Tasen Level 2",
        "Reach Tasen Level 3",
        "Reach Tasen Level 4",
        "Reach Komato Level 2",
        "Reach Komato Level 3",
        "Reach Komato Level 4"
        ],
    "Sector 2": ["Level 4", "Level 5", "Level 6",
        "Reach Health Level 5",
        "Reach Health Level 6",
        "Reach Health Level 7",
        "Reach Attack Level 5",
        "Reach Attack Level 6",
        "Reach Attack Level 7",
        "Reach Assmilate Level 5",
        "Reach Assmilate Level 6",
        "Reach Assmilate Level 7",
        "Reach Strength Level 5",
        "Reach Strength Level 6",
        "Reach Strength Level 7",
        "Reach Crack Level 5",
        "Reach Crack Level 6",
        "Reach Crack Level 7",
        "Reach Tasen Level 5",
        "Reach Tasen Level 6",
        "Reach Tasen Level 7",
        "Reach Komato Level 5",
        "Reach Komato Level 6",
        "Reach Komato Level 7"
        ],
    "Sector 3": ["Level 7", "Level 8", "Level 9",
        "Reach Health Level 8",
        "Reach Health Level 9",
        "Reach Health Level 10",
        "Reach Attack Level 8",
        "Reach Attack Level 9",
        "Reach Attack Level 10",
        "Reach Assmilate Level 8",
        "Reach Assmilate Level 9",
        "Reach Assmilate Level 10",
        "Reach Strength Level 8",
        "Reach Strength Level 9",
        "Reach Strength Level 10",
        "Reach Crack Level 8",
        "Reach Crack Level 9",
        "Reach Crack Level 10",
        "Reach Tasen Level 8",
        "Reach Tasen Level 9",
        "Reach Tasen Level 10",
        "Reach Komato Level 8",
        "Reach Komato Level 9",
        "Reach Komato Level 10"
        ],
    "Sector 4": ["Level 10", "Level 11", "Level 12"],
    "Sector 5": ["Level 13", "Level 14", "Level 15"],
    "Sector 6": ["Level 16", "Level 17", "Level 18"],
    "Sector 7": ["Level 19", "Level 20", "Level 21"],
    "Sector 8": ["Level 22", "Level 23", "Level 24"],
    "Sector 9": ["Level 25", "Level 26", "Level 27"],
    "Sector X": ["Level 28", "Level 29", "Level 30"]
}