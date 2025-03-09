
from typing import Callable, Dict, List, TYPE_CHECKING, NamedTuple
from BaseClasses import MultiWorld, Region, Entrance
from worlds.generic.Rules import CollectionRule
from worlds.iji.Rules import can_access_sector, can_reach_nulldriver, can_reach_poster_nine, can_reach_sector_z, can_rocket_boost, has_stats, has_multiple_stats, has_weapon_stats
from .Locations import IjiLocation, location_table

if TYPE_CHECKING:
    from . import IjiWorld

def create_regions(world: "IjiWorld", healthbalancing: bool, compactment: int):

    region_menu = create_region(world, "Menu")

    region_global = create_region(world, "Global")
    region_sector1 = create_region(world, "Sector 1")
    region_sector1_ra = create_region(world, "Sector 1 Restricted Area")
    region_sector1_p = create_region(world, "Sector 1 Poster")
    region_sector2 = create_region(world, "Sector 2")
    region_sector2_st = create_region(world, "Sector 2 Storage Transport Top")
    region_sector2_p = create_region(world, "Sector 2 Poster")
    region_sector3 = create_region(world, "Sector 3")
    region_sector3_ra = create_region(world, "Sector 3 Restricted Area")
    region_sector3_p = create_region(world, "Sector 3 Poster")
    region_sector4 = create_region(world, "Sector 4")
    region_sector4_sc = create_region(world, "Sector 4 Surveillance Control")
    region_sector4_ms = create_region(world, "Sector 4 Top of Main Storage")
    region_sector4_p = create_region(world, "Sector 4 Poster")
    region_sector5 = create_region(world, "Sector 5")
    region_sector5_p = create_region(world, "Sector 5 Poster")
    region_sector6 = create_region(world, "Sector 6")
    region_sector6_p = create_region(world, "Sector 6 Poster")
    region_sector7 = create_region(world, "Sector 7")
    region_sector7_hw = create_region(world, "Sector 7 Heavy Weapon Armory")
    region_sector7_ht = create_region(world, "Sector 7 Hyper Turret Logbooks")
    region_sector7_ch = create_region(world, "Sector 7 Crackers' Hideout")
    region_sector7_p = create_region(world, "Sector 7 Poster")
    region_sector8 = create_region(world, "Sector 8")
    region_sector8_ss = create_region(world, "Sector 8 Staff Storage Return Trip")
    region_sector8_p = create_region(world, "Sector 8 Poster")
    region_sector9 = create_region(world, "Sector 9")
    region_sector9_p = create_region(world, "Sector 9 Poster")
    region_sector9_ds = create_region(world, "Sector 9 Deep Sector")
    region_sectorx = create_region(world, "Sector X")
    region_sectorx_vs = create_region(world, "Sector X Ventilation Shaft")
    region_sectorx_p = create_region(world, "Sector X Poster")
    region_sectorx_mc = create_region(world, "Sector X Maximum Charge Terminal")
    region_sectorz = create_region(world, "Sector Z")
    region_sectorz_ip = create_region(world, "Sector Z Inner Prey")
    region_sectory = create_region(world, "Sector Y")

    region_menu.connect(region_global, "Menu -> Global",
                        lambda state: True)
    region_menu.connect(region_sector1, "Menu -> Sector 1",
                        lambda state: True)
    region_sector1.connect(region_sector1_ra, "Sector 1 -> Restricted Area",
                           lambda state: has_stats(state, "Strength Stat", world.player, 3, compactment))
    region_sector1.connect(region_sector1_p, "Sector 1 -> Poster",
                           lambda state: has_stats(state, "Strength Stat", world.player, 1, compactment))
    region_sector1.connect(region_sector2, "Sector 1 -> Sector 2",
                           lambda state: can_access_sector(state, world.player, healthbalancing, 2, compactment))
    region_sector2.connect(region_sector2_st, "Sector 2 -> Storage Transport Top",
                           lambda state: can_rocket_boost(state, world.player))
    region_sector2.connect(region_sector2_p, "Sector 2 -> Poster",
                           lambda state: (has_stats(state, "Strength Stat", world.player, 3, compactment) or \
                               has_weapon_stats(state, "Machine Gun", world.player, compactment) or \
                               world.options.LogicDifficulty.value >= \
                               world.options.LogicDifficulty.option_obscure_logic))
    region_sector2.connect(region_sector3, "Sector 2 -> Sector 3",
                           lambda state: can_access_sector(state, world.player, healthbalancing, 3, compactment))
    region_sector3.connect(region_sector3_ra, "Sector 3 -> Restricted Area",
                           lambda state: has_multiple_stats(state, {"Strength Stat": 9, "Crack Stat": 9}, world.player, compactment))
    region_sector3.connect(region_sector3_p, "Sector 3 -> Poster",
                           lambda state: (can_rocket_boost(state, world.player) and \
                               has_stats(state, "Strength Stat", world.player, 3, compactment)))
    region_sector3.connect(region_sector4, "Sector 3 -> Sector 4",
                           lambda state: can_access_sector(state, world.player, healthbalancing, 4, compactment))
    region_sector4.connect(region_sector4, "Sector 4 -> Surveillance Control",
                           lambda state: has_weapon_stats(state, "Rocket Launcher", world.player, compactment))
    region_sector4.connect(region_sector4, "Sector 4 -> Top of Main Storage",
                            lambda state: (has_weapon_stats(state, "Rocket Launcher", world.player, compactment) or # Rocket Method
                                can_rocket_boost(state, world.player) or # Rocket Boost Method
                                has_stats(state, "Strength Stat", world.player, 3, compactment))) # Kick the Door Method
    region_sector4.connect(region_sector4_p, "Sector 4 -> Poster",
                           lambda state: (has_weapon_stats(state, "Rocket Launcher", world.player, compactment) or # Rocket Launcher
                           has_stats(state, "Strength Stat", world.player, 3, compactment) or # Kick the Tasen Soldier
                           world.options.LogicDifficulty.value >= # Use the Tasen Shredder
                           world.options.LogicDifficulty.option_obscure_logic))
    region_sector4.connect(region_sector5, "Sector 4 -> Sector 5",
                           lambda state: can_access_sector(state, world.player, healthbalancing, 5, compactment))
    region_sector5.connect(region_sector5_p, "Sector 5 -> Poster",
                           lambda state: (has_weapon_stats(state, "Nuke", world.player, compactment) or \
                               (has_weapon_stats(state, "MPFB Devastator", world.player, compactment) and \
                               world.options.LogicDifficulty.value >= world.options.LogicDifficulty.option_obscure_logic)))
    region_sector5.connect(region_sector6, "Sector 5 -> Sector 6",
                           lambda state: can_access_sector(state, world.player, healthbalancing, 6, compactment))
    region_sector6.connect(region_sector6_p, "Sector 6 -> Poster",
                           lambda state: has_weapon_stats(state, "Velocithor", world.player, compactment))
    region_sector6.connect(region_sector7, "Sector 6 -> Sector 7",
                           lambda state: can_access_sector(state, world.player, healthbalancing, 7, compactment))
    region_sector7.connect(region_sector7_hw, "Sector 7 -> Heavy Weapon Armory",
                           lambda state: has_stats(state, "Strength Stat", world.player, 2, compactment))
    region_sector7.connect(region_sector7_ht, "Sector 7 -> Hyper Turret Logbooks",
                           lambda state: has_stats(state, "Crack Stat", world.player, 2, compactment))
    region_sector7.connect(region_sector7_ch, "Sector 7 -> Crackers' Hideout",
                           lambda state: (has_weapon_stats(state, "Rocket Launcher", world.player, compactment) or
                           has_weapon_stats(state, "Shocksplinter", world.player, compactment)))
    region_sector7.connect(region_sector7_p, "Sector 7 -> Poster",
                           lambda state: (has_weapon_stats(state, "CFIS", world.player, compactment) and
                           has_weapon_stats(state, "Nuke", world.player, compactment) and
                           has_stats(state, "Attack Stat", world.player, 2, compactment)))
    region_sector7.connect(region_sector8, "Sector 7 -> Sector 8",
                           lambda state: can_access_sector(state, world.player, healthbalancing, 8, compactment))
    region_sector8.connect(region_sector8_ss, "Sector 8 -> Staff Storage Return Trip",
                            lambda state: has_stats(state, "Crack Stat", world.player, 4, compactment))
    region_sector8.connect(region_sector8_p, "Sector 8 -> Poster",
                           lambda state: can_rocket_boost(state, world.player))
    region_sector8.connect(region_sector9, "Sector 8 -> Sector 9",
                           lambda state: can_access_sector(state, world.player, healthbalancing, 9, compactment))
    region_sector9.connect(region_sector9_p, "Sector 9 -> Poster",
                           lambda state: can_reach_poster_nine(state, world.player, \
                               world.options.SpecialTraitItems.value, \
                               world.options.CompactStatItems.value))
    region_sector9.connect(region_sector9_ds, "Sector 9 -> Deep Sector",
                           lambda state: True) # No requirements... for now
    region_sector9.connect(region_sectorx, "Sector 9 -> Sector X",
                           lambda state: can_access_sector(state, world.player, healthbalancing, 10, compactment))
    region_sectorx.connect(region_sectorx_vs, "Sector X -> Ventilation Shaft",
                           lambda state: has_weapon_stats(state, "Nuke", world.player, compactment))
    region_sectorx_vs.connect(region_sectorx_p, "Sector X Ventilation Shaft -> Poster",
                              lambda state: has_weapon_stats(state, "Splintergun", world.player, compactment))
    region_sectorx.connect(region_sectorx_mc, "Sector X -> Maximum Charge Terminal",
                           lambda state: True) # No requirements... for now
    world.multiworld.regions.append(region_menu)
    world.multiworld.regions.append(region_global)
    world.multiworld.regions.append(region_sector1)
    world.multiworld.regions.append(region_sector1_ra)
    world.multiworld.regions.append(region_sector1_p)
    world.multiworld.regions.append(region_sector2)
    world.multiworld.regions.append(region_sector2_st)
    world.multiworld.regions.append(region_sector2_p)
    world.multiworld.regions.append(region_sector3)
    world.multiworld.regions.append(region_sector3_ra)
    world.multiworld.regions.append(region_sector3_p)
    world.multiworld.regions.append(region_sector4)
    world.multiworld.regions.append(region_sector4_sc)
    world.multiworld.regions.append(region_sector4_ms)
    world.multiworld.regions.append(region_sector4_p)
    world.multiworld.regions.append(region_sector5)
    world.multiworld.regions.append(region_sector5_p)
    world.multiworld.regions.append(region_sector6)
    world.multiworld.regions.append(region_sector6_p)
    world.multiworld.regions.append(region_sector7)
    world.multiworld.regions.append(region_sector7_hw)
    world.multiworld.regions.append(region_sector7_ht)
    world.multiworld.regions.append(region_sector7_ch)
    world.multiworld.regions.append(region_sector7_p)
    world.multiworld.regions.append(region_sector8)
    world.multiworld.regions.append(region_sector8_ss)
    world.multiworld.regions.append(region_sector8_p)
    world.multiworld.regions.append(region_sector9)
    world.multiworld.regions.append(region_sector9_p)
    world.multiworld.regions.append(region_sector9_ds)
    world.multiworld.regions.append(region_sectorx)
    world.multiworld.regions.append(region_sectorx_vs)
    world.multiworld.regions.append(region_sectorx_p)
    world.multiworld.regions.append(region_sectorx_mc)

    region_sector1.connect(region_sectorz, "Sector 1 -> Sector Z",
                           lambda state: can_reach_sector_z(state, world.player, world, \
                               world.options.SectorZPosterLocationsRequired.value, \
                               world.options.SectorZRibbonItemsRequired.value, \
                               world.options.CompactStatItems.value))
    world.multiworld.regions.append(region_sectorz)

    region_sectorz.connect(region_sectorz_ip, "Sector Z -> Inner Prey",
                           lambda state: can_reach_nulldriver(state, world.player, world, \
                               world.options.NullDriverPosterLocationsRequired.value, \
                               world.options.NullDriverRibbonItemsRequired.value, \
                               world.options.CompactStatItems.value))
    world.multiworld.regions.append(region_sectorz_ip)

    region_sectorx.connect(region_sectory, "Sector X -> Sector Y",
                           lambda state: can_reach_nulldriver(state, world.player, world, \
                               world.options.NullDriverPosterLocationsRequired.value, \
                               world.options.NullDriverRibbonItemsRequired.value, \
                               world.options.CompactStatItems.value))
    world.multiworld.regions.append(region_sectory)



def create_region(world: "IjiWorld", name: str) -> Region:
    region = Region(name, world.player, world.multiworld)

    
    region.add_locations({
        location_name: location_data.code for location_name, location_data in location_table.items()
        if location_data.region==region.name and location_data.valid(world)
    }, IjiLocation)


    return region


region_exit_table: Dict[str, List[str]] = { # unused, currently
    "Menu": ["Global", "Sector 1"],
    "Global": [],
    "Sector 1": ["Sector 1 Restricted Area", "Sector 1 Poster", "Sector 2", "Sector Z"],
    "Sector 1 Restricted Area": [],
    "Sector 1 Poster": [],
    "Sector 2": ["Sector 2 Storage Transport Top", "Sector 2 Poster", "Sector 3"],
    "Sector 2 Storage Transport Top": [],
    "Sector 2 Poster": [],
    "Sector 3": ["Sector 3 Restricted Area", "Sector 3 Poster", "Sector 4"],
    "Sector 3 Restricted Area": [],
    "Sector 3 Poster": [],
    "Sector 4": ["Sector 4 Surveillance Control", "Sector 4 Top of Main Storage", "Sector 4 Poster", "Sector 5"],
    "Sector 4 Surveillance Control": [],
    "Sector 4 Top of Main Storage": [],
    "Sector 4 Poster": [],
    "Sector 5": ["Sector 5 Poster", "Sector 6"],
    "Sector 5 Poster": [],
    "Sector 6": ["Sector 6 Poster", "Sector 7"],
    "Sector 6 Poster": [],
    "Sector 7": ["Sector 7 Heavy Weapon Armory", "Sector 7 Hyper Turret Logbooks", "Sector 7 Crackers' Hideout", "Sector 7 Poster", "Sector 8"],
    "Sector 7 Heavy Weapon Armory": [],
    "Sector 7 Hyper Turret Logbooks": [],
    "Sector 7 Crackers' Hideout": [],
    "Sector 7 Poster": [],
    "Sector 8": ["Sector 8 Staff Storage Return Trip", "Sector 8 Poster", "Sector 9"],
    "Sector 8 Staff Storage Return Trip": [],
    "Sector 8 Poster": [],
    "Sector 9": ["Sector 9 Poster", "Sector 9 Deep Sector", "Sector X"],
    "Sector 9 Poster": [],
    "Sector 9 Deep Sector": [],
    "Sector X": ["Sector X Ventilation Shaft", "Sector X Ultimate Charge Terminal", "Sector Y"],
    "Sector X Ventilation Shaft": ["Sector X Poster"],
    "Sector X Poster": [],
    "Sector X Maximum Charge Terminal": [],
    "Sector Z": ["Sector Z Inner Prey"],
    "Sector Z Inner Prey": [],
    "Sector Y": []
}