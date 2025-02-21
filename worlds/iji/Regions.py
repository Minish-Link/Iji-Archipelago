
from typing import Callable, Dict, List, TYPE_CHECKING, NamedTuple
from BaseClasses import MultiWorld, Region, Entrance
from worlds.generic.Rules import CollectionRule
from worlds.iji.Rules import can_access_sector, can_reach_nulldriver, can_reach_poster_nine, can_reach_sector_z, can_rocket_boost, has_weapon_stats
from .Locations import IjiLocation, location_table

if TYPE_CHECKING:
    from . import IjiWorld

def create_regions(world: "IjiWorld"):

    region_menu = create_region(world, "Menu")
    world.multiworld.regions.append(region_menu)

    region_global = create_region(world, "Global")
    world.multiworld.regions.append(region_global)
    region_menu.connect(region_global, "Menu -> Global")

    region_sector1 = create_region(world, "Sector 1")
    world.multiworld.regions.append(region_sector1)
    region_menu.connect(region_sector1, "Menu -> Sector 1")

    region_sector1_ra = create_region(world, "Sector 1 Restricted Area")
    world.multiworld.regions.append(region_sector1_ra)
    region_sector1.connect(region_sector1_ra, "Sector 1 -> Restricted Area",
                           lambda state: state.has("Strength Stat", world.player, 3))

    region_sector1_p = create_region(world, "Sector 1 Poster")
    world.multiworld.regions.append(region_sector1_p)
    region_sector1.connect(region_sector1_p, "Sector 1 -> Poster",
                           lambda state: state.has("Strength Stat", world.player, 3))

    region_sector2 = create_region(world, "Sector 2")
    world.multiworld.regions.append(region_sector2)
    region_sector1.connect(region_sector2, "Sector 1 -> Sector 2",
                           lambda state: can_access_sector(state, world.player, world.options.HealthBalancing, 2))

    region_sector2_st = create_region(world, "Sector 2 Storage Transport Top")
    world.multiworld.regions.append(region_sector2_st)
    region_sector2.connect(region_sector2_st, "Sector 2 -> Storage Transport Top",
                           lambda state: can_rocket_boost(state, world.player))

    region_sector2_p = create_region(world, "Sector 2 Poster")
    world.multiworld.regions.append(region_sector2_p)
    region_sector2.connect(region_sector2_p, "Sector 2 -> Poster",
                           lambda state: state.has("Strength Stat", world.player, 3) or \
                               has_weapon_stats("Machine Gun") or \
                               world.options.LogicDifficulty.value >= \
                               world.options.LogicDifficulty.option_obscure_logic)

    region_sector3 = create_region(world, "Sector 3")
    world.multiworld.regions.append(region_sector3)
    region_sector2.connect(region_sector3, "Sector 2 -> Sector 3",
                           lambda state: can_access_sector(state, world.player, world.options.HealthBalancing, 3))

    region_sector3_ra = create_region(world, "Sector 3 Restricted Area")
    world.multiworld.regions.append(region_sector3_ra)
    region_sector3.connect(region_sector3_ra, "Sector 3 -> Restricted Area",
                           lambda state: state.has_all_counts({"Strength Stat": 9, "Crack Stat": 9}, world.player))

    region_sector3_p = create_region(world, "Sector 3 Poster")
    world.multiworld.regions.append(region_sector3_p)
    region_sector3.connect(region_sector3_p, "Sector 3 -> POster",
                           lambda state: can_rocket_boost(state, world.player) and \
                               state.has("Strength Stat", world.player, 3))

    region_sector4 = create_region(world, "Sector 4")
    world.multiworld.regions.append(region_sector4)
    region_sector3.connect(region_sector4, "Sector 3 -> Sector 4",
                           lambda state: can_access_sector(state, world.player, world.options.HealthBalancing, 4))

    region_sector4_sc = create_region(world, "Sector 4 Surveillance Control")
    world.multiworld.regions.append(region_sector4_sc)
    region_sector4.connect(region_sector4, "Sector 4 -> Surveillance Control",
                           lambda state: has_weapon_stats(state, "Rocket Launcher", world.player))

    region_sector4_ms = create_region(world, "Sector 4 Top of Main Storage")
    world.multiworld.regions.append(region_sector4_ms)
    region_sector4.connect(region_sector4, "Sector 4 -> Top of Main Storage",
                            lambda state: has_weapon_stats(state, "Rocket Launcher", world.player) or # Rocket Method
                                can_rocket_boost(state, world.player) or # Rocket Boost Method
                                state.has("Strength Stat", world.player, 3)) # Kick the Door Method

    region_sector4_p = create_region(world, "Sector 4 Poster")
    world.multiworld.regions.append(region_sector4_p)
    region_sector4.connect(region_sector4_p, "Sector 4 -> Poster",
                           lambda state: has_weapon_stats("Rocket Launcher", world.player) or # Rocket Launcher
                           state.has("Strength Stat", world.player, 3) or # Kick the Tasen Soldier
                           world.options.LogicDifficulty.value >= # Use the Tasen Shredder
                           world.options.LogicDifficulty.option_obscure_logic)

    region_sector5 = create_region(world, "Sector 5")
    world.multiworld.regions.append(region_sector5)
    region_sector4.connect(region_sector5, "Sector 4 -> Sector 5",
                           lambda state: can_access_sector(state, world.player, world.options.HealthBalancing, 5))

    region_sector5_p = create_region(world, "Sector 5 Poster")
    world.multiworld.regions.append(region_sector5_p)
    region_sector5.connect(region_sector5_p, "Sector 5 -> Poster",
                           lambda state: has_weapon_stats(state, "Nuke", world.player))

    region_sector6 = create_region(world, "Sector 6")
    world.mutliworld.regions.append(region_sector6)
    region_sector5.connect(region_sector6, "Sector 5 -> Sector 6",
                           lambda state:can_access_sector(state, world.player, world.options.HealthBalancing, 6))

    region_sector6_p = create_region(world, "Sector 6 Poster")
    world.multiworld.regions.append(region_sector6_p)
    region_sector6.connect(region_sector6_p, "Sector 6 -> Poster",
                           lambda state: has_weapon_stats(state, "Velocithor", world.player))

    region_sector7 = create_region(world, "Sector 7")
    world.multiworld.regions.append(region_sector7)
    region_sector6.connect(region_sector7, "Sector 6 -> Sector 7",
                           lambda state: can_access_sector(state, world.player, world.options.HealthBalancing, 7))

    region_sector7_hw = create_region(world, "Sector 7 Heavy Weapon Armory")
    world.multiworld.regions.append(region_sector7_hw)
    region_sector7.connect(region_sector7_hw, "Sector 7 -> Heavy Weapon Armory",
                           lambda state: state.has("Strength Stat", world.player, 2))

    region_sector7_ht = create_region(world, "Sector 7 Hyper Turret Logbooks")
    world.multiworld.regions.append(region_sector7_ht)
    region_sector7.connect(region_sector7_ht, "Sector 7 -> Hyper Turret Logbooks",
                           lambda state: state.has("Crack Stat", world.player, 2))

    region_sector7_ch = create_region(world, "Sector 7 Crackers' Hideout")
    world.multiworld.regions.append(region_sector7_ch)
    region_sector7.connect(region_sector7_ch, "Sector 7 -> Crackers' Hideout",
                           lambda state: has_weapon_stats(state, "Rocket Launcher", world.player) or
                           has_weapon_stats(state, "Shocksplinter", world.player))

    region_sector7_p = create_region(world, "Sector 7 Poster")
    world.multiworld.regions.append(region_sector7_p)
    region_sector7.connect(region_sector7_p, "Sector 7 -> Poster",
                           lambda state: has_weapon_stats(state, "CFIS", world.player) and
                           has_weapon_stats(state, "Nuke", world.player) and
                           state.has("Attack Stat", world.player, 2))

    region_sector8 = create_region(world, "Sector 8")
    world.multiworld.regions.append(region_sector8)
    region_sector7.connect(region_sector8, "Sector 7 -> Sector 8",
                           lambda state: can_access_sector(state, world.player, world.options.HealthBalancing, 8))

    region_sector8_ss = create_region(world, "Sector 8 Staff Storage Return Trip")
    world.multiworld.regions.append(region_sector8_ss)
    region_sector8.connect(region_sector8_ss, "Sector 8 -> Staff Storage Return Trip",
                            lambda state: state.has("Crack Stat", world.player, 4))

    region_sector8_p = create_region(world, "Sector 8 Poster")
    world.multiworld.regions.append(region_sector8_p)
    region_sector8.connect(region_sector8_p, "Sector 8 -> Poster",
                           lambda state: can_rocket_boost(state, world.player))

    region_sector9 = create_region(world, "Sector 9")
    world.multiworld.regions.append(region_sector9)
    region_sector8.connect(region_sector9, "Sector 8 -> Sector 9",
                           lambda state: can_access_sector(state, world.player, world.options.HealthBalancing, 9))

    region_sector9_p = create_region("Sector 9 Poster")
    world.multiworld.regions.append(region_sector9_p)
    region_sector9.connect(region_sector9_p, "Sector 9 -> Poster",
                           lambda state: can_reach_poster_nine(state, world.player, \
                               (world.options.SpecialTraitItems.value == \
                               world.options.SpecialTraitItems.option_items_only or \
                               world.options.SpecialTraitItems.value == \
                               world.options.SpecialTraitItems.option_locations_and_items)))

    region_sector9_ds = create_region(world, "Sector 9 Deep Sector")
    world.multiworld.regions.append(region_sector9_ds)
    region_sector9.connect(region_sector9_ds, "Sector 9 -> Deep Sector",
                           lambda state: True) # No requirements... for now

    region_sectorx = create_region(world, "Sector X")
    world.multiworld.regions.append(region_sectorx)
    region_sector9.connect(region_sectorx, "Sector 9 -> Sector X",
                           lambda state: can_access_sector(state, world.player, world.options.HealthBalancing, 10))

    region_sectorx_vs = create_region(world, "Sector X Ventilation Shaft")
    world.multiworld.regions.append(region_sectorx_vs)
    region_sectorx.connect(region_sectorx, "Sector X -> Ventilation Shaft",
                           lambda state: has_weapon_stats(state, "Nuke", world.player))

    region_sectorx_p = create_region(world, "Sector X Poster")
    world.multiworld.regions.append(region_sectorx_p)
    region_sectorx_vs.connect(region_sectorx, "Sector X Ventilation Shaft -> Poster",
                              lambda state: has_weapon_stats(state, "Splintergun", world.player))

    region_sectorx_mc = create_region(world, "Sector X Maximum Charge Terminal")
    world.multiworld.regions.append(region_sectorx_mc)
    region_sectorx.connect(region_sectorx_mc, "Sector X -> Maximum Charge Terminal",
                           lambda state: True) # No requirements... for now

    region_sectorz = create_region(world, "Sector Z")
    world.multiworld.regions.append(region_sectorz)
    region_sector1.connect(region_sectorz, "Sector 1 -> Sector Z",
                           lambda state: can_reach_sector_z(state, world.player, \
                               world.options.SectorZRequirements.value, \
                               world.options.SectorZRequirementType.value == \
                               world.options.SectorZRequirementType.option_poster_locations))

    region_sectorz_ip = create_region(world, "Sector Z Inner Prey")
    world.multiworld.regions.append(region_sectorz_ip)
    region_sectorz.connect(region_sectorz_ip, "Sector Z -> Inner Prey",
                           lambda state: can_reach_nulldriver(state, world.player, \
                               world.options.NullDriverPosterRequirement.value, \
                               world.options.NullDriverPosterRequirementType.value == \
                               world.options.NullDriverPosterRequirementType.option_poster_locations, \
                               world.options.NullDriverRibbonRequirement.value, \
                               world.options.NullDriverRibbonRequirementType.value == \
                               world.options.NullDriverRibbonRequirementType.option_ribbon_locations))

    region_sectory = create_region(world, "Sector Y")
    world.multiworld.regions.append(region_sectory)
    region_sectorx.connect(region_sectory, "Sector X -> Sector Y",
                           lambda state: can_reach_sector_z(state, world.player, \
                               world.options.SectorZRequirements.value, \
                               world.options.SectorZRequirementType.value == \
                               world.options.SectorZRequirementType.option_poster_locations)
                               and can_reach_nulldriver(state, world.player, \
                               world.options.NullDriverPosterRequirement.value, \
                               world.options.NullDriverPosterRequirementType.value == \
                               world.options.NullDriverPosterRequirementType.option_poster_locations, \
                               world.options.NullDriverRibbonRequirement.value, \
                               world.options.NullDriverRibbonRequirementType.value == \
                               world.options.NullDriverRibbonRequirementType.option_ribbon_locations))



def create_region(world: "IjiWorld", name: str) -> Region:
    region = Region(name, world.player, world.multiworld)

    for name, data in location_table.items():
        if data.valid(world) and data.region == region.name:
            region.locations.append(IjiLocation(world.player, name, data.code, region))

    return region

class IjiRegionAccess(NamedTuple):
    exits: List[str] = []
    access_rule: CollectionRule = lambda state: True


region_table: Dict[str, IjiRegionAccess] = {
    "Menu": IjiRegionAccess(exits=["Global", "Sector 1"]),
    "Global": IjiRegionAccess(),
    "Sector 1": IjiRegionAccess(
        exits=["Sector 1 Restricted Area", "Sector 1 Poster", "Sector 2", "Sector Z"]
    ),
    "Sector 1 Restricted Area": IjiRegionAccess(),
    "Sector 1 Poster": IjiRegionAccess(),
    "Sector 2": IjiRegionAccess(exits=["Sector 2 Storage Transport Top", "Sector 2 Poster", "Sector 3"]),
    "Sector 2 Restricted Area": IjiRegionAccess(),
    "Sector 2 Poster": IjiRegionAccess(),
    "Sector 3": IjiRegionAccess(exits=["Sector 3 Restricted Area", "Sector 3 Poster", "Sector 4"]),
    "Sector 3 Restricted Area": IjiRegionAccess(),
    "Sector 3 Poster": IjiRegionAccess(),
    "Sector 4": IjiRegionAccess(exits=["Sector 4 Surveillance Control", "Sector 4 Top of Main Storage", "Sector 4 Poster", "Sector 5"]),
    "Sector 4 Surveillance Control": IjiRegionAccess(),
    "Sector 4 Top of Main Storage": IjiRegionAccess(),
    "Sector 4 Poster": IjiRegionAccess(),
    "Sector 5": IjiRegionAccess(exits=["Sector 5 Poster", "Sector 6"]),
    "Sector 5 Poster": IjiRegionAccess(),
    "Sector 6": IjiRegionAccess(exits=["Sector 6 Poster", "Sector 7"]),
    "Sector 6 Poster": IjiRegionAccess(),
    "Sector 7": IjiRegionAccess(exits=["Sector 7 Heavy Weapon Armory", "Sector 7 Hyper Turret Logbooks", "Sector 7 Crackers' Hideout", "Sector 7 Poster", "Sector 8"]),
    "Sector 7 Heavy Weapon Armory": IjiRegionAccess(),
    "Sector 7 Hyper Turret Logbooks": IjiRegionAccess(),
    "Sector 7 Crackers' Hideout": IjiRegionAccess(),
    "Sector 7 Poster": IjiRegionAccess(),
    "Sector 8": IjiRegionAccess(exits=["Sector 8 Staff Storage Return Trip", "Sector 8 Poster", "Sector 9"]),
    "Sector 8 Staff Storage Return Trip": IjiRegionAccess(),
    "Sector 8 Poster": IjiRegionAccess(),
    "Sector 9": IjiRegionAccess(exits=["Sector 9 Poster", "Sector 9 Deep Sector", "Sector X"]),
    "Sector 9 Poster": IjiRegionAccess(),
    "Sector 9 Deep Sector": IjiRegionAccess(),
    "Sector X": IjiRegionAccess(exits=["Sector X Ventilation Shaft", "Sector X Ultimate Charge Terminal", "Sector Y"]),
    "Sector X Ventilation Shaft": IjiRegionAccess(exits=["Sector X Poster"]),
    "Sector X Poster": IjiRegionAccess(),
    "Sector X Maximum Charge Terminal": IjiRegionAccess(),
    "Sector Z": IjiRegionAccess(exits=["Sector Z Inner Prey"]),
    "Sector Z Inner Prey": IjiRegionAccess(),
    "Sector Y": IjiRegionAccess()
}
