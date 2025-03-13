from typing import Callable, Dict, Mapping, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import CollectionState, Location
from worlds.generic.Rules import CollectionRule
from worlds.iji.Rules import can_destroy_sentinel_proxima, can_kill_annihilators, can_make_bustergun, can_make_hyperpulse, can_make_nuke, can_make_plasmacannon, can_make_resonancereflector, can_make_splintergun, can_make_spreadrockets, can_make_velocithor, can_reach_cfis, can_reach_mpfbdevastator, can_reach_pulsecannon, can_reach_resonancedetonator, can_reach_rocketlauncher, can_reach_shocksplinter, can_reach_superchargesix, has_stats, has_weapon_stats

if TYPE_CHECKING:
    from . import IjiWorld

class IjiLocation(Location):
    game="Iji"

class IjiLocData(NamedTuple):
    code: int
    region: str
    valid: Callable[["IjiWorld"], bool] = lambda world: True
    weapon: str = ""
    logic: Callable[["IjiWorld", CollectionState], bool] = lambda world, state: True

def get_total_locations(world: "IjiWorld") -> int:
    total: int = 0
    for loc in world.multiworld.get_locations(world.player):
        total += 1

    return total

def get_location_names() -> Dict[str, int]:
    names = {name: data.code for name, data in location_table.items()}

locations_sectorcomplete: Dict[str,IjiLocData] = {
    "Sector 1 - Sector Complete":   IjiLocData(code=1,  region="Sector 1"),
    "Sector 2 - Sector Complete":   IjiLocData(code=2,  region="Sector 2"),
    "Sector 3 - Sector Complete":   IjiLocData(code=3,  region="Sector 3"),
    "Sector 4 - Sector Complete":   IjiLocData(code=4,  region="Sector 4"),
    "Sector 5 - Sector Complete":   IjiLocData(code=5,  region="Sector 5"),
    "Sector 6 - Sector Complete":   IjiLocData(code=6,  region="Sector 6"),
    "Sector 7 - Sector Complete":   IjiLocData(code=7,  region="Sector 7"),
    "Sector 8 - Sector Complete":   IjiLocData(code=8,  region="Sector 8"),
    "Sector 9 - Sector Complete":   IjiLocData(code=9,  region="Sector 9"),
    "Sector X - Sector Complete":   IjiLocData(code=10, region="Sector X", \
        valid=lambda world: world.options.EndGoal.value != 1),
    "Sector Z - Sector Complete":   IjiLocData(code=11, region="Sector Z", \
        valid=lambda world: (world.sector_z_allowed() and world.options.EndGoal.value != 2)),
    "Sector Y - Sector Complete":   IjiLocData(code=12, region="Sector Y", \
        valid=lambda world: (world.sector_y_allowed() and world.options.EndGoal.value != 3))
}

# levelup regions change based on difficulty (Whenever that is implemented)
locations_levelup: Dict[str, IjiLocData] = {
    "Level 1":  IjiLocData(code=101, region="Sector 1"),
    "Level 2":  IjiLocData(code=102, region="Sector 1"),
    "Level 3":  IjiLocData(code=103, region="Sector 1"),
    "Level 4":  IjiLocData(code=104, region="Sector 1"),
    "Level 5":  IjiLocData(code=105, region="Sector 1"),
    "Level 6":  IjiLocData(code=106, region="Sector 2"),
    "Level 7":  IjiLocData(code=107, region="Sector 2"),
    "Level 8":  IjiLocData(code=108, region="Sector 2"),
    "Level 9":  IjiLocData(code=109, region="Sector 2"),
    "Level 10": IjiLocData(code=110, region="Sector 2"),
    "Level 11": IjiLocData(code=111, region="Sector 3"),
    "Level 12": IjiLocData(code=112, region="Sector 3"),
    "Level 13": IjiLocData(code=113, region="Sector 3"),
    "Level 14": IjiLocData(code=114, region="Sector 3"),
    "Level 15": IjiLocData(code=115, region="Sector 3"),
    "Level 16": IjiLocData(code=116, region="Sector 4"),
    "Level 17": IjiLocData(code=117, region="Sector 4"),
    "Level 18": IjiLocData(code=118, region="Sector 4"),
    "Level 19": IjiLocData(code=119, region="Sector 4"),
    "Level 20": IjiLocData(code=120, region="Sector 4"),
    "Level 21": IjiLocData(code=121, region="Sector 5"),
    "Level 22": IjiLocData(code=122, region="Sector 5"),
    "Level 23": IjiLocData(code=123, region="Sector 5"),
    "Level 24": IjiLocData(code=124, region="Sector 5"),
    "Level 25": IjiLocData(code=125, region="Sector 5"),
    "Level 26": IjiLocData(code=126, region="Sector 6"),
    "Level 27": IjiLocData(code=127, region="Sector 6"),
    "Level 28": IjiLocData(code=128, region="Sector 6"),
    "Level 29": IjiLocData(code=129, region="Sector 6"),
    "Level 30": IjiLocData(code=130, region="Sector 6"),
    "Level 31": IjiLocData(code=131, region="Sector 7"),
    "Level 32": IjiLocData(code=132, region="Sector 7"),
    "Level 33": IjiLocData(code=133, region="Sector 7"),
    "Level 34": IjiLocData(code=134, region="Sector 7"),
    "Level 35": IjiLocData(code=135, region="Sector 7"),
    "Level 36": IjiLocData(code=136, region="Sector 8"),
    "Level 37": IjiLocData(code=137, region="Sector 8"),
    "Level 38": IjiLocData(code=138, region="Sector 8"),
    "Level 39": IjiLocData(code=139, region="Sector 8"),
    "Level 40": IjiLocData(code=140, region="Sector 8"),
    "Level 41": IjiLocData(code=141, region="Sector 9"),
    "Level 42": IjiLocData(code=142, region="Sector 9"),
    "Level 43": IjiLocData(code=143, region="Sector 9"),
    "Level 44": IjiLocData(code=144, region="Sector 9"),
    "Level 45": IjiLocData(code=145, region="Sector 9"),
    "Level 46": IjiLocData(code=146, region="Sector X"),
    "Level 47": IjiLocData(code=147, region="Sector X"),
    "Level 48": IjiLocData(code=148, region="Sector X"),
    "Level 49": IjiLocData(code=149, region="Sector X"),
    "Level 50": IjiLocData(code=150, region="Sector X"),
}

locations_tutorialpages: Dict[str, IjiLocData] = {
    "Tutorial Page 1":              IjiLocData(code=161, region="Sector 1"),
    "Tutorial Page 2":              IjiLocData(code=162, region="Sector 1"),
    "Tutorial Page 3":              IjiLocData(code=163, region="Sector 1"),
    "Tutorial Page 4":              IjiLocData(code=164, region="Sector 1"),
    "Tutorial Page 5":              IjiLocData(code=165, region="Sector 1"),
    "Tutorial Page 6":              IjiLocData(code=166, region="Sector 1"),
}

locations_statlevels: Dict[str, IjiLocData] = {
    "Reach Health Level 2":         IjiLocData(code = 411, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Health Stat", world.player, 1, world.options.CompactStatItems.value)),
    "Reach Health Level 3":         IjiLocData(code = 412, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Health Stat", world.player, 2, world.options.CompactStatItems.value)),
    "Reach Health Level 4":         IjiLocData(code = 413, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Health Stat", world.player, 3, world.options.CompactStatItems.value)),
    "Reach Health Level 5":         IjiLocData(code = 414, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Health Stat", world.player, 4, world.options.CompactStatItems.value)),
    "Reach Health Level 6":         IjiLocData(code = 415, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Health Stat", world.player, 5, world.options.CompactStatItems.value)),
    "Reach Health Level 7":         IjiLocData(code = 416, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Health Stat", world.player, 6, world.options.CompactStatItems.value)),
    "Reach Health Level 8":         IjiLocData(code = 417, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Health Stat", world.player, 7, world.options.CompactStatItems.value)),
    "Reach Health Level 9":         IjiLocData(code = 418, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Health Stat", world.player, 8, world.options.CompactStatItems.value)),
    "Reach Health Level 10":        IjiLocData(code = 419, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Health Stat", world.player, 9, world.options.CompactStatItems.value)),

    "Reach Attack Level 2":         IjiLocData(code = 421, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Attack Stat", world.player, 1, world.options.CompactStatItems.value)),
    "Reach Attack Level 3":         IjiLocData(code = 422, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Attack Stat", world.player, 2, world.options.CompactStatItems.value)),
    "Reach Attack Level 4":         IjiLocData(code = 423, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Attack Stat", world.player, 3, world.options.CompactStatItems.value)),
    "Reach Attack Level 5":         IjiLocData(code = 424, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Attack Stat", world.player, 4, world.options.CompactStatItems.value)),
    "Reach Attack Level 6":         IjiLocData(code = 425, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Attack Stat", world.player, 5, world.options.CompactStatItems.value)),
    "Reach Attack Level 7":         IjiLocData(code = 426, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Attack Stat", world.player, 6, world.options.CompactStatItems.value)),
    "Reach Attack Level 8":         IjiLocData(code = 427, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Attack Stat", world.player, 7, world.options.CompactStatItems.value)),
    "Reach Attack Level 9":         IjiLocData(code = 428, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Attack Stat", world.player, 8, world.options.CompactStatItems.value)),
    "Reach Attack Level 10":        IjiLocData(code = 429, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Attack Stat", world.player, 9, world.options.CompactStatItems.value)),

    "Reach Assimilate Level 2":     IjiLocData(code = 431, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Assimilate Stat", world.player, 1, world.options.CompactStatItems.value)),
    "Reach Assimilate Level 3":     IjiLocData(code = 432, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Assimilate Stat", world.player, 2, world.options.CompactStatItems.value)),
    "Reach Assimilate Level 4":     IjiLocData(code = 433, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Assimilate Stat", world.player, 3, world.options.CompactStatItems.value)),
    "Reach Assimilate Level 5":     IjiLocData(code = 434, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Assimilate Stat", world.player, 4, world.options.CompactStatItems.value)),
    "Reach Assimilate Level 6":     IjiLocData(code = 435, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Assimilate Stat", world.player, 5, world.options.CompactStatItems.value)),
    "Reach Assimilate Level 7":     IjiLocData(code = 436, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Assimilate Stat", world.player, 6, world.options.CompactStatItems.value)),
    "Reach Assimilate Level 8":     IjiLocData(code = 437, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Assimilate Stat", world.player, 7, world.options.CompactStatItems.value)),
    "Reach Assimilate Level 9":     IjiLocData(code = 438, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Assimilate Stat", world.player, 8, world.options.CompactStatItems.value)),
    "Reach Assimilate Level 10":    IjiLocData(code = 439, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Assimilate Stat", world.player, 9, world.options.CompactStatItems.value)),

    "Reach Strength Level 2":       IjiLocData(code = 441, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 1, world.options.CompactStatItems.value)),
    "Reach Strength Level 3":       IjiLocData(code = 442, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 2, world.options.CompactStatItems.value)),
    "Reach Strength Level 4":       IjiLocData(code = 443, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 3, world.options.CompactStatItems.value)),
    "Reach Strength Level 5":       IjiLocData(code = 444, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 4, world.options.CompactStatItems.value)),
    "Reach Strength Level 6":       IjiLocData(code = 445, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 5, world.options.CompactStatItems.value)),
    "Reach Strength Level 7":       IjiLocData(code = 446, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 6, world.options.CompactStatItems.value)),
    "Reach Strength Level 8":       IjiLocData(code = 447, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 7, world.options.CompactStatItems.value)),
    "Reach Strength Level 9":       IjiLocData(code = 448, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 8, world.options.CompactStatItems.value)),
    "Reach Strength Level 10":      IjiLocData(code = 449, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 9, world.options.CompactStatItems.value)),

    "Reach Crack Level 2":          IjiLocData(code = 451, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Crack Stat", world.player, 1, world.options.CompactStatItems.value)),
    "Reach Crack Level 3":          IjiLocData(code = 452, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Crack Stat", world.player, 2, world.options.CompactStatItems.value)),
    "Reach Crack Level 4":          IjiLocData(code = 453, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Crack Stat", world.player, 3, world.options.CompactStatItems.value)),
    "Reach Crack Level 5":          IjiLocData(code = 454, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Crack Stat", world.player, 4, world.options.CompactStatItems.value)),
    "Reach Crack Level 6":          IjiLocData(code = 455, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Crack Stat", world.player, 5, world.options.CompactStatItems.value)),
    "Reach Crack Level 7":          IjiLocData(code = 456, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Crack Stat", world.player, 6, world.options.CompactStatItems.value)),
    "Reach Crack Level 8":          IjiLocData(code = 457, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Crack Stat", world.player, 7, world.options.CompactStatItems.value)),
    "Reach Crack Level 9":          IjiLocData(code = 458, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Crack Stat", world.player, 8, world.options.CompactStatItems.value)),
    "Reach Crack Level 10":         IjiLocData(code = 459, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Crack Stat", world.player, 9, world.options.CompactStatItems.value)),

    "Reach Tasen Level 2":          IjiLocData(code = 461, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Tasen Stat", world.player, 1, world.options.CompactStatItems.value)),
    "Reach Tasen Level 3":          IjiLocData(code = 462, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Tasen Stat", world.player, 2, world.options.CompactStatItems.value)),
    "Reach Tasen Level 4":          IjiLocData(code = 463, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Tasen Stat", world.player, 3, world.options.CompactStatItems.value)),
    "Reach Tasen Level 5":          IjiLocData(code = 464, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Tasen Stat", world.player, 4, world.options.CompactStatItems.value)),
    "Reach Tasen Level 6":          IjiLocData(code = 465, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Tasen Stat", world.player, 5, world.options.CompactStatItems.value)),
    "Reach Tasen Level 7":          IjiLocData(code = 466, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Tasen Stat", world.player, 6, world.options.CompactStatItems.value)),
    "Reach Tasen Level 8":          IjiLocData(code = 467, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Tasen Stat", world.player, 7, world.options.CompactStatItems.value)),
    "Reach Tasen Level 9":          IjiLocData(code = 468, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Tasen Stat", world.player, 8, world.options.CompactStatItems.value)),
    "Reach Tasen Level 10":         IjiLocData(code = 469, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Tasen Stat", world.player, 9, world.options.CompactStatItems.value)),

    "Reach Komato Level 2":         IjiLocData(code = 471, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Komato Stat", world.player, 1, world.options.CompactStatItems.value)),
    "Reach Komato Level 3":         IjiLocData(code = 472, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Komato Stat", world.player, 2, world.options.CompactStatItems.value)),
    "Reach Komato Level 4":         IjiLocData(code = 473, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Komato Stat", world.player, 3, world.options.CompactStatItems.value)),
    "Reach Komato Level 5":         IjiLocData(code = 474, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Komato Stat", world.player, 4, world.options.CompactStatItems.value)),
    "Reach Komato Level 6":         IjiLocData(code = 475, region = "Sector 1",\
        logic=lambda world, state: has_stats(state, "Komato Stat", world.player, 5, world.options.CompactStatItems.value)),
    "Reach Komato Level 7":         IjiLocData(code = 476, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Komato Stat", world.player, 6, world.options.CompactStatItems.value)),
    "Reach Komato Level 8":         IjiLocData(code = 477, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Komato Stat", world.player, 7, world.options.CompactStatItems.value)),
    "Reach Komato Level 9":         IjiLocData(code = 478, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Komato Stat", world.player, 8, world.options.CompactStatItems.value)),
    "Reach Komato Level 10":        IjiLocData(code = 479, region = "Sector 2",\
        logic=lambda world, state: has_stats(state, "Komato Stat", world.player, 9, world.options.CompactStatItems.value)),

}

locations_poster: Dict[str, IjiLocData] = {
    "Sector 1 - Poster":            IjiLocData(code=201, region="Sector 1 Poster", \
        valid=lambda world: world.options.PosterLocations),
    "Sector 2 - Poster":            IjiLocData(code=202, region="Sector 2 Poster", \
        valid=lambda world: world.options.PosterLocations),
    "Sector 3 - Poster":            IjiLocData(code=203, region="Sector 3 Poster", \
        valid=lambda world: world.options.PosterLocations),
    "Sector 4 - Poster":            IjiLocData(code=204, region="Sector 4 Poster", \
        valid=lambda world: world.options.PosterLocations),
    "Sector 5 - Poster":            IjiLocData(code=205, region="Sector 5 Poster", \
        valid=lambda world: world.options.PosterLocations),
    "Sector 6 - Poster":            IjiLocData(code=206, region="Sector 6 Poster", \
        valid=lambda world: world.options.PosterLocations),
    "Sector 7 - Poster":            IjiLocData(code=207, region="Sector 7 Poster", \
        valid=lambda world: world.options.PosterLocations),
    "Sector 8 - Poster":            IjiLocData(code=208, region="Sector 8 Poster", \
        valid=lambda world: world.options.PosterLocations),
    "Sector 9 - Poster":            IjiLocData(code=209, region="Sector 9 Poster", \
        valid=lambda world: world.options.PosterLocations),
    "Sector X - Poster":            IjiLocData(code=210, region="Sector X Poster", \
        valid=lambda world: world.options.PosterLocations),
    "Sector Z - Epic Poster":       IjiLocData(code=211, region="Sector Z", \
        valid=lambda world: world.options.PosterLocations and world.sector_z_allowed()),
    "Sector Y - Poster of Doom":    IjiLocData(code=212, region="Sector Y", \
        valid=lambda world: world.options.PosterLocations and world.sector_y_allowed())
}

locations_ribbon: Dict[str, IjiLocData] = {
    "Sector 1 - Ribbon":    IjiLocData(code=221, region="Sector 1", \
        valid=lambda world: world.options.RibbonLocations),
    "Sector 2 - Ribbon":    IjiLocData(code=222, region="Sector 2", \
        valid=lambda world: world.options.RibbonLocations),
    "Sector 3 - Ribbon":    IjiLocData(code=223, region="Sector 3", \
        valid=lambda world: world.options.RibbonLocations),
    "Sector 4 - Ribbon":    IjiLocData(code=224, region="Sector 4", \
        valid=lambda world: world.options.RibbonLocations),
    "Sector 5 - Ribbon":    IjiLocData(code=225, region="Sector 5", \
        valid=lambda world: world.options.RibbonLocations),
    "Sector 6 - Ribbon":    IjiLocData(code=226, region="Sector 6", \
        valid=lambda world: world.options.RibbonLocations),
    "Sector 7 - Ribbon":    IjiLocData(code=227, region="Sector 7", \
        valid=lambda world: world.options.RibbonLocations),
    "Sector 8 - Ribbon":    IjiLocData(code=228, region="Sector 8", \
        valid=lambda world: world.options.RibbonLocations),
    "Sector 9 - Ribbon":    IjiLocData(code=229, region="Sector 9", \
        valid=lambda world: world.options.RibbonLocations),
    "Sector X - Ribbon":    IjiLocData(code=230, region="Sector X", \
        valid=lambda world: world.options.RibbonLocations)
}

locations_supercharge: Dict[str,IjiLocData] = {
    "Sector 1 - Supercharge":   IjiLocData(code=231, region="Sector 1 Restricted Area", \
        valid=lambda world: world.options.SuperchargeLocations,\
        logic=lambda world, state: has_weapon_stats(state, "Rocket Launcher", world.player, world.options.CompactStatItems.value)),
    "Sector 2 - Supercharge":   IjiLocData(code=232, region="Sector 2 Storage Transport Top", \
        valid=lambda world: world.options.SuperchargeLocations,\
        logic=lambda world, state: has_weapon_stats(state, "Hyper Pulse Cannon", world.player, world.options.CompactStatItems.value)),
    "Sector 3 - Supercharge":   IjiLocData(code=233, region="Sector 3", \
        valid=lambda world: world.options.SuperchargeLocations),
    "Sector 4 - Supercharge":   IjiLocData(code=234, region="Sector 4 Top of Main Storage", \
        valid=lambda world: world.options.SuperchargeLocations),
    "Sector 5 - Supercharge":   IjiLocData(code=235, region="Sector 5", \
        valid=lambda world: world.options.SuperchargeLocations,\
        logic=lambda world, state: has_weapon_stats(state, "Nuke", world.player, world.options.CompactStatItems.value)),
    "Sector 6 - Supercharge":   IjiLocData(code=236, region="Sector 6", \
        valid=lambda world: world.options.SuperchargeLocations,\
        logic=lambda world, state: can_reach_superchargesix(state, world, world.options.CompactStatItems.value)),
    "Sector 7 - Supercharge":   IjiLocData(code=237, region="Sector 7", \
        valid=lambda world: world.options.SuperchargeLocations,\
        logic=lambda world, state: can_destroy_sentinel_proxima(state, world)),
    "Sector 8 - Supercharge":   IjiLocData(code=238, region="Sector 8 Staff Storage Return Trip", \
        valid=lambda world: world.options.SuperchargeLocations,\
        logic=lambda world, state: can_kill_annihilators(state, world.player, world.options.CompactStatItems.value)),
    "Sector 9 - Supercharge":   IjiLocData(code=239, region="Sector 9 Deep Sector", \
        valid=lambda world: (world.options.SuperchargeLocations) and world.options.PacifistLocations),
    "Sector X - Supercharge":   IjiLocData(code=240, region="Sector X", \
        valid=lambda world: world.options.SuperchargeLocations,\
        logic=lambda world, state: has_weapon_stats(state, "Velocithor", world.player, world.options.CompactStatItems.value))
}

locations_uniquebasicweapons: Dict[str, IjiLocData] = {
    "Obtain Machine Gun":                   IjiLocData(code=241, region="Global", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_time, \
        logic=lambda world, state: has_weapon_stats(state, "Machine Gun", world.player, world.options.CompactStatItems.value)),
    "Obtain Rocket Launcher":               IjiLocData(code=242, region="Global", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_time,\
        logic=lambda world, state: can_reach_rocketlauncher(state, world.player, world.options.CompactStatItems.value)),
    "Obtain MPFB Devastator":               IjiLocData(code=243, region="Global", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_time,\
        logic=lambda world, state: can_reach_mpfbdevastator(state, world.player, world.options.CompactStatItems.value)),
    "Obtain Resonance Detonator":           IjiLocData(code=244, region="Global", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_time,\
        logic=lambda world, state: can_reach_resonancedetonator(state, world.player, world.options.CompactStatItems.value)),
    "Obtain Pulse Cannon":                  IjiLocData(code=245, region="Global", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_time,\
        logic=lambda world, state: can_reach_pulsecannon(state, world.player, world.options.CompactStatItems.value)),
    "Obtain Shocksplinter":                 IjiLocData(code=246, region="Global", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_time,\
        logic=lambda world, state: can_reach_shocksplinter(state, world.player, world.options.CompactStatItems.value)),
    "Obtain Cyclic Fusion Ignition System": IjiLocData(code=247, region="Global", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_time,\
        logic=lambda world, state: can_reach_cfis(state, world.player, world.options.CompactStatItems.value))
}

locations_uniquespecialweapons: Dict[str, IjiLocData] = {
    "Obtain Banana Gun":    IjiLocData(code=248, region="Sector 9 Poster", \
        valid=lambda world: world.options.UniqueWeaponLocations, \
        logic=lambda world, state: has_weapon_stats(state,"Banana Gun",world.player,world.options.CompactStatItems.value)),
    "Obtain Massacre":      IjiLocData(code=249, region="Sector X", \
        valid=lambda world: (world.options.UniqueWeaponLocations and world.options.PacifistLocations), \
        logic=lambda world, state: has_weapon_stats(state,"Massacre",world.player,world.options.CompactStatItems.value)),
    "Obtain Null Driver":   IjiLocData(code=250, region="Sector Z Inner Prey", \
        valid=lambda world: world.options.UniqueWeaponLocations and world.sector_z_allowed(), \
        logic=lambda world, state: has_weapon_stats(state,"Null Driver",world.player,world.options.CompactStatItems.value))
}

locations_combinedweapons: Dict[str,IjiLocData] = {
    "Obtain Buster Gun":            IjiLocData(code=251, region="Global", \
        valid=lambda world: world.options.CombinedWeaponLocations,\
        logic=lambda world, state: can_make_bustergun(state, world.player, world.options.CompactStatItems.value)),
    "Obtain Splintergun":           IjiLocData(code=252, region="Global", \
        valid=lambda world: world.options.CombinedWeaponLocations,\
        logic=lambda world, state: can_make_splintergun(state, world.player, world.options.CompactStatItems.value)),
    "Obtain Spread Rockets":        IjiLocData(code=253, region="Global", \
        valid=lambda world: world.options.CombinedWeaponLocations,\
        logic=lambda world, state: can_make_spreadrockets(state, world.player, world.options.CompactStatItems.value)),
    "Obtain Nuke":                  IjiLocData(code=254, region="Global", \
        valid=lambda world: world.options.CombinedWeaponLocations,\
        logic=lambda world, state: can_make_nuke(state, world.player, world.options.CompactStatItems.value)),
    "Obtain Resonance Reflector":   IjiLocData(code=255, region="Global", \
        valid=lambda world: world.options.CombinedWeaponLocations,\
        logic=lambda world, state: can_make_resonancereflector(state, world.player, world.options.CompactStatItems.value)),
    "Obtain Hyper Pulse Cannon":    IjiLocData(code=256, region="Global", \
        valid=lambda world: world.options.CombinedWeaponLocations,\
        logic=lambda world, state: can_make_hyperpulse(state, world.player, world.options.CompactStatItems.value)),
    "Obtain Plasma Cannon":         IjiLocData(code=257, region="Global", \
        valid=lambda world: world.options.CombinedWeaponLocations,\
        logic=lambda world, state: can_make_plasmacannon(state, world.player, world.options.CompactStatItems.value)),
    "Obtain Velocithor V2-10":      IjiLocData(code=258, region="Global", \
        valid=lambda world: world.options.CombinedWeaponLocations,\
        logic=lambda world, state: can_make_velocithor(state, world.player, world.options.CompactStatItems.value))
}

locations_upgrades: Dict[str, IjiLocData] = {
    "Sector 2 - Jump Upgrade":  IjiLocData(code=261, region="Sector 2", \
        valid=lambda world: world.options.UpgradeLocations),
    "Sector 3 - Armor Upgrade": IjiLocData(code=262, region="Sector 3", \
        valid=lambda world: world.options.UpgradeLocations),
    "Sector 5 - Jump Upgrade":  IjiLocData(code=263, region="Sector 5", \
        valid=lambda world: world.options.UpgradeLocations),
    "Sector 7 - Armor Upgrade": IjiLocData(code=264, region="Sector 7", \
        valid=lambda world: world.options.UpgradeLocations),
    "Sector 8 - Armor Upgrade": IjiLocData(code=265, region="Sector 8", \
        valid=lambda world: world.options.UpgradeLocations),
    "Sector 9 - Armor Upgrade": IjiLocData(code=266, region="Sector 9", \
        valid=lambda world: world.options.UpgradeLocations),
    "Sector X - Armor Upgrade": IjiLocData(code=267, region="Sector X", \
        valid=lambda world: world.options.UpgradeLocations)
}

locations_sectorweapons: Dict[str, IjiLocData] = {
    "Sector 1 - Machine Gun":                   IjiLocData(code=311, region="Sector 1", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 2 - Machine Gun":                   IjiLocData(code=321, region="Sector 2", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 2 - Rocket Launcher":               IjiLocData(code=322, region="Sector 2 Storage Transport Top", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 2 - Resonance Detonator":           IjiLocData(code=324, region="Sector 2", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 3 - Machine Gun":                   IjiLocData(code=331, region="Sector 3", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 3 - Rocket Launcher":               IjiLocData(code=332, region="Sector 3", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 3 - Resonance Detonator":           IjiLocData(code=334, region="Sector 3", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 3 - Pulse Cannon":                  IjiLocData(code=335, region="Sector 3", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector,\
        logic=lambda world, state: (has_weapon_stats(state, "Pulse Cannon", world.player, world.options.CompactStatItems.value) and
                                    has_stats(state, "Crack Stat", world.player, 1, world.options.CompactStatItems.value))),
    "Sector 4 - Machine Gun":                   IjiLocData(code=341, region="Sector 4", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 4 - Rocket Launcher":               IjiLocData(code=342, region="Sector 4", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 4 - MPFB Devastator":               IjiLocData(code=343, region="Sector 4 Top of Main Storage", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector 4 - Resonance Detonator":           IjiLocData(code=344, region="Sector 4", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 4 - Pulse Cannon":                  IjiLocData(code=345, region="Sector 4", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 5 - Machine Gun":                   IjiLocData(code=351, region="Sector 5", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 5 - Rocket Launcher":               IjiLocData(code=352, region="Sector 5", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 5 - MPFB Devastator":               IjiLocData(code=353, region="Sector 5", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector 5 - Resonance Detonator":           IjiLocData(code=354, region="Sector 5", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 5 - Pulse Cannon":                  IjiLocData(code=355, region="Sector 5", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 5 - Shocksplinter":                 IjiLocData(code=356, region="Sector 5", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Machine Gun":                   IjiLocData(code=361, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Rocket Launcher":               IjiLocData(code=362, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - MPFB Devastator":               IjiLocData(code=363, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Resonance Detonator":           IjiLocData(code=364, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Pulse Cannon":                  IjiLocData(code=365, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Shocksplinter":                 IjiLocData(code=366, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Cyclic Fusion Ignition System": IjiLocData(code=367, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector,\
        logic=lambda world, state: (has_weapon_stats(state, "CFIS", world.player, world.options.CompactStatItems.value) and
                                    has_stats(state, "Crack Stat", world.player, 3, world.options.CompactStatItems.value))),
    "Sector 7 - Machine Gun":                   IjiLocData(code=371, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Rocket Launcher":               IjiLocData(code=372, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - MPFB Devastator":               IjiLocData(code=373, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Resonance Detonator":           IjiLocData(code=374, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Pulse Cannon":                  IjiLocData(code=375, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Shocksplinter":                 IjiLocData(code=376, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Cyclic Fusion Ignition System": IjiLocData(code=377, region="Sector 7 Heavy Weapon Armory", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"CFIS",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - Machine Gun":                   IjiLocData(code=381, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - Rocket Launcher":               IjiLocData(code=382, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - MPFB Devastator":               IjiLocData(code=383, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - Resonance Detonator":           IjiLocData(code=384, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - Pulse Cannon":                  IjiLocData(code=385, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - Shocksplinter":                 IjiLocData(code=386, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - Cyclic Fusion Ignition System": IjiLocData(code=387, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"CFIS",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Machine Gun":                   IjiLocData(code=391, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Rocket Launcher":               IjiLocData(code=392, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - MPFB Devastator":               IjiLocData(code=393, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Resonance Detonator":           IjiLocData(code=394, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Pulse Cannon":                  IjiLocData(code=395, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Shocksplinter":                 IjiLocData(code=396, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Cyclic Fusion Ignition System": IjiLocData(code=397, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"CFIS",world.player,world.options.CompactStatItems.value)),
    "Sector X - Machine Gun":                   IjiLocData(code=301, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector X - Rocket Launcher":               IjiLocData(code=302, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector X - MPFB Devastator":               IjiLocData(code=303, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector X - Resonance Detonator":           IjiLocData(code=304, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector X - Pulse Cannon":                  IjiLocData(code=305, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector X - Shocksplinter":                 IjiLocData(code=306, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector X - Cyclic Fusion Ignition System": IjiLocData(code=307, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"CFIS",world.player,world.options.CompactStatItems.value)),
    "Sector X - Resonance Reflector":           IjiLocData(code=308, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value >= \
        world.options.BasicWeaponLocations.option_first_per_sector, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Reflector",world.player,world.options.CompactStatItems.value))
}

locations_allbasicweapons: Dict[str, IjiLocData] = {
    "Sector 3 - Machine Gun 1/3":                   IjiLocData(code=3311, region="Sector 3", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 3 - Machine Gun 2/3":                   IjiLocData(code=3312, region="Sector 3", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 3 - Machine Gun 3/3":                   IjiLocData(code=3313, region="Sector 3", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 3 - Rocket Launcher 1/2":               IjiLocData(code=3321, region="Sector 3", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 3 - Rocket Launcher 2/2":               IjiLocData(code=3322, region="Sector 3", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 4 - Rocket Launcher 1/2":               IjiLocData(code=3421, region="Sector 4", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 4 - Rocket Launcher 2/2":               IjiLocData(code=3422, region="Sector 4", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 5 - Machine Gun 1/2":                   IjiLocData(code=3511, region="Sector 5", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 5 - Machine Gun 2/2":                   IjiLocData(code=3512, region="Sector 5", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 5 - Rocket Launcher 1/2":               IjiLocData(code=3521, region="Sector 5", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 5 - Rocket Launcher 2/2":               IjiLocData(code=3522, region="Sector 5", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 5 - Pulse Cannon 1/3":                  IjiLocData(code=3551, region="Sector 5", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 5 - Pulse Cannon 2/3":                  IjiLocData(code=3552, region="Sector 5", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 5 - Pulse Cannon 3/3":                  IjiLocData(code=3553, region="Sector 5", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Machine Gun 1/2":                   IjiLocData(code=3611, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Machine Gun 2/2":                   IjiLocData(code=3612, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Rocket Launcher 1/3":               IjiLocData(code=3621, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Rocket Launcher 2/3":               IjiLocData(code=3622, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Rocket Launcher 3/3":               IjiLocData(code=3623, region="Sector6", \
        valid=lambda world: world.options.BasicWeaponLocations.value== \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - MPFB Devastator 1/2":               IjiLocData(code=3631, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - MPFB Devastator 2/2":               IjiLocData(code=3632, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances,\
        logic=lambda world, state: (has_weapon_stats(state, "MPFB Devastator", world.player, world.options.CompactStatItems.value) and
                                    has_stats(state, "Crack Stat", world.player, 3, world.options.CompactStatItems.value))),
    "Sector 6 - Pulse Cannon 1/2":                  IjiLocData(code=3651, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Pulse Cannon 2/2":                  IjiLocData(code=3652, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Shocksplinter 1/3":                 IjiLocData(code=3661, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Shocksplinter 2/3":                 IjiLocData(code=3662, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 6 - Shocksplinter 3/3":                 IjiLocData(code=3663, region="Sector 6", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Rocket Launcher 1/3":               IjiLocData(code=3721, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Rocket Launcher 2/3":               IjiLocData(code=3722, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Rocket Launcher 3/3":               IjiLocData(code=3723, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Resonance Detonator 1/2":           IjiLocData(code=3741, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Resonance Detonator 2/2":           IjiLocData(code=3742, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Pulse Cannon 1/2":                  IjiLocData(code=3751, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Pulse Cannon 2/2":                  IjiLocData(code=3752, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Shocksplinter 1/3":                 IjiLocData(code=3761, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Shocksplinter 2/3":                 IjiLocData(code=3762, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 7 - Shocksplinter 3/3":                 IjiLocData(code=3763, region="Sector 7", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - Rocket Launcher 1/3":               IjiLocData(code=3821, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - Rocket Launcher 2/3":               IjiLocData(code=3822, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - Rocket Launcher 3/3":               IjiLocData(code=3823, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - Pulse Cannon 1/2":                  IjiLocData(code=3851, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - Pulse Cannon 2/2":                  IjiLocData(code=3852, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - Shocksplinter 1/2":                 IjiLocData(code=3861, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 8 - Shocksplinter 2/2":                 IjiLocData(code=3862, region="Sector 8", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Machine Gun 1/4":                   IjiLocData(code=3911, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Machine Gun 2/4":                   IjiLocData(code=3912, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Machine Gun 3/4":                   IjiLocData(code=3913, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Machine Gun 4/4":                   IjiLocData(code=3914, region="Sector 9 Poster", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Rocket Launcher 1/5":               IjiLocData(code=3921, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Rocket Launcher 2/5":               IjiLocData(code=3922, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Rocket Launcher 3/5":               IjiLocData(code=3923, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Rocket Launcher 4/5":               IjiLocData(code=3924, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Rocket Launcher 5/5":               IjiLocData(code=3925, region="Sector 9 Poster", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - MPFB Devastator 1/4":               IjiLocData(code=3931, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - MPFB Devastator 2/4":               IjiLocData(code=3932, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - MPFB Devastator 3/4":               IjiLocData(code=3933, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - MPFB Devastator 4/4":               IjiLocData(code=3934, region="Sector 9 Poster", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Resonance Detonator 1/4":           IjiLocData(code=3941, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Resonance Detonator 2/4":           IjiLocData(code=3942, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Resonance Detonator 3/4":           IjiLocData(code=3943, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Resonance Detonator 4/4":           IjiLocData(code=3944, region="Sector 9 Poster", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Pulse Cannon 1/4":                  IjiLocData(code=3951, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Pulse Cannon 2/4":                  IjiLocData(code=3952, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Pulse Cannon 3/4":                  IjiLocData(code=3953, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Pulse Cannon 4/4":                  IjiLocData(code=3954, region="Sector 9 Poster", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Shocksplinter 1/4":                 IjiLocData(code=3961, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Shocksplinter 2/4":                 IjiLocData(code=3962, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Shocksplinter 3/4":                 IjiLocData(code=3963, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Shocksplinter 4/4":                 IjiLocData(code=3964, region="Sector 9 Poster", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Cyclic Fusion Ignition System 1/3": IjiLocData(code=3971, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"CFIS",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Cyclic Fusion Ignition System 2/3": IjiLocData(code=3972, region="Sector 9", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"CFIS",world.player,world.options.CompactStatItems.value)),
    "Sector 9 - Cyclic Fusion Ignition System 3/3": IjiLocData(code=3973, region="Sector 9 Poster", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"CFIS",world.player,world.options.CompactStatItems.value)),
    "Sector X - Machine Gun 1/3":                   IjiLocData(code=3011, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector X - Machine Gun 2/3":                   IjiLocData(code=3012, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector X - Machine Gun 3/3":                   IjiLocData(code=3013, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Machine Gun",world.player,world.options.CompactStatItems.value)),
    "Sector X - Rocket Launcher 1/3":               IjiLocData(code=3021, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector X - Rocket Launcher 2/3":               IjiLocData(code=3022, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector X - Rocket Launcher 3/3":               IjiLocData(code=3023, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Rocket Launcher",world.player,world.options.CompactStatItems.value)),
    "Sector X - MPFB Devastator 1/4":               IjiLocData(code=3031, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector X - MPFB Devastator 2/4":               IjiLocData(code=3032, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector X - MPFB Devastator 3/4":               IjiLocData(code=3033, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"MPFB Devastator",world.player,world.options.CompactStatItems.value)),
    "Sector X - MPFB Devastator 4/4":               IjiLocData(code=3034, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances,\
        logic=lambda world, state: (has_weapon_stats(state, "MPFB Devastator", world.player, world.options.CompactStatItems.value) and
                                    has_stats(state, "Strength Stat", world.player, 6, world.options.CompactStatItems.value))),
    "Sector X - Resonance Detonator 1/2":           IjiLocData(code=3041, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector X - Resonance Detonator 2/2":           IjiLocData(code=3042, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Resonance Detonator",world.player,world.options.CompactStatItems.value)),
    "Sector X - Pulse Cannon 1/4":                  IjiLocData(code=3051, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector X - Pulse Cannon 2/4":                  IjiLocData(code=3052, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector X - Pulse Cannon 3/4":                  IjiLocData(code=3053, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector X - Pulse Cannon 4/4":                  IjiLocData(code=3054, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Pulse Cannon",world.player,world.options.CompactStatItems.value)),
    "Sector X - Shocksplinter 1/3":                 IjiLocData(code=3061, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector X - Shocksplinter 2/3":                 IjiLocData(code=3062, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector X - Shocksplinter 3/3":                 IjiLocData(code=3063, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"Shocksplinter",world.player,world.options.CompactStatItems.value)),
    "Sector X - Cyclic Fusion Ignition System 1/4": IjiLocData(code=3071, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"CFIS",world.player,world.options.CompactStatItems.value)),
    "Sector X - Cyclic Fusion Ignition System 2/4": IjiLocData(code=3072, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"CFIS",world.player,world.options.CompactStatItems.value)),
    "Sector X - Cyclic Fusion Ignition System 3/4": IjiLocData(code=3073, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"CFIS",world.player,world.options.CompactStatItems.value)),
    "Sector X - Cyclic Fusion Ignition System 4/4": IjiLocData(code=3074, region="Sector X", \
        valid=lambda world: world.options.BasicWeaponLocations.value == \
        world.options.BasicWeaponLocations.option_all_instances, \
        logic=lambda world, state: has_weapon_stats(state,"CFIS",world.player,world.options.CompactStatItems.value))
}

locations_logbooks: Dict[str, IjiLocData] = {
    "Sector 1 - Logbook 1":  IjiLocData(code=1101, region="Sector 1", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 2":  IjiLocData(code=1102, region="Sector 1", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 3":  IjiLocData(code=1103, region="Sector 1", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 4":  IjiLocData(code=1104, region="Sector 1", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 5":  IjiLocData(code=1105, region="Sector 1", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 6":  IjiLocData(code=1106, region="Sector 1", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 7":  IjiLocData(code=1107, region="Sector 1", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 8":  IjiLocData(code=1108, region="Sector 1", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 9":  IjiLocData(code=1109, region="Sector 1", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 10": IjiLocData(code=1110, region="Sector 1", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 11": IjiLocData(code=1111, region="Sector 1 Poster", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 12": IjiLocData(code=1112, region="Sector 1 Poster", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 13": IjiLocData(code=1113, region="Sector 1 Poster", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 14": IjiLocData(code=1114, region="Sector 1 Poster", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 1 - Logbook 15": IjiLocData(code=1115, region="Sector 1 Restricted Area", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 1":  IjiLocData(code=1201, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 2":  IjiLocData(code=1202, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 3":  IjiLocData(code=1203, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 4":  IjiLocData(code=1204, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 5":  IjiLocData(code=1205, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 6":  IjiLocData(code=1206, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 7":  IjiLocData(code=1207, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 8":  IjiLocData(code=1208, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 9":  IjiLocData(code=1209, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 10": IjiLocData(code=1210, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 11": IjiLocData(code=1211, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 12": IjiLocData(code=1212, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 13": IjiLocData(code=1213, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 14": IjiLocData(code=1214, region="Sector 2", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 15": IjiLocData(code=1215, region="Sector 2 Poster", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 2 - Logbook 16": IjiLocData(code=1216, region="Sector 2 Poster", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 1":  IjiLocData(code=1301, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 2":  IjiLocData(code=1302, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 3":  IjiLocData(code=1303, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 4":  IjiLocData(code=1304, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 5":  IjiLocData(code=1305, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 6":  IjiLocData(code=1306, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 7":  IjiLocData(code=1307, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 8":  IjiLocData(code=1308, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 9":  IjiLocData(code=1309, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 10": IjiLocData(code=1310, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 11": IjiLocData(code=1311, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 12": IjiLocData(code=1312, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 13": IjiLocData(code=1313, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 14": IjiLocData(code=1314, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 15": IjiLocData(code=1315, region="Sector 3", \
        valid=lambda world: world.options.LogbookLocations,\
        logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 1, world.options.CompactStatItems.value)),
    "Sector 3 - Logbook 16": IjiLocData(code=1316, region="Sector 3 Restricted Area", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 17": IjiLocData(code=1317, region="Sector 3 Restricted Area", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 3 - Logbook 18": IjiLocData(code=1318, region="Sector 3 Poster", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 4 - Logbook 1":  IjiLocData(code=1401, region="Sector 4", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 4 - Logbook 2":  IjiLocData(code=1402, region="Sector 4", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 4 - Logbook 3":  IjiLocData(code=1403, region="Sector 4", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 4 - Logbook 4":  IjiLocData(code=1404, region="Sector 4", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 4 - Logbook 5":  IjiLocData(code=1405, region="Sector 4", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 4 - Logbook 6":  IjiLocData(code=1406, region="Sector 4", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 4 - Logbook 7":  IjiLocData(code=1407, region="Sector 4", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 4 - Logbook 8":  IjiLocData(code=1408, region="Sector 4", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 4 - Logbook 9":  IjiLocData(code=1409, region="Sector 4", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 4 - Logbook 10": IjiLocData(code=1410, region="Sector 4 Surveillance Control", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 4 - Logbook 11": IjiLocData(code=1411, region="Sector 4 Top of Main Storage", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 4 - Logbook 12": IjiLocData(code=1412, region="Sector 4", \
        valid=lambda world: world.options.LogbookLocations,\
        logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 5, world.options.CompactStatItems.value)),
    "Sector 4 - Logbook 13": IjiLocData(code=1413, region="Sector 4 Poster", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 5 - Logbook 1":  IjiLocData(code=1501, region="Sector 5", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 5 - Logbook 2":  IjiLocData(code=1502, region="Sector 5", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 5 - Logbook 3":  IjiLocData(code=1503, region="Sector 5", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 5 - Logbook 4":  IjiLocData(code=1504, region="Sector 5", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 5 - Logbook 5":  IjiLocData(code=1505, region="Sector 5", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 5 - Logbook 6":  IjiLocData(code=1506, region="Sector 5", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 5 - Logbook 7":  IjiLocData(code=1507, region="Sector 5", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 5 - Logbook 8":  IjiLocData(code=1508, region="Sector 5", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 5 - Logbook 9":  IjiLocData(code=1509, region="Sector 5", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 5 - Logbook 10": IjiLocData(code=1510, region="Sector 5", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 6 - Logbook 1":  IjiLocData(code=1601, region="Sector 6", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 6 - Logbook 2":  IjiLocData(code=1602, region="Sector 6", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 6 - Logbook 3":  IjiLocData(code=1603, region="Sector 6", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 6 - Logbook 4":  IjiLocData(code=1604, region="Sector 6", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 6 - Logbook 5":  IjiLocData(code=1605, region="Sector 6", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 6 - Logbook 6":  IjiLocData(code=1606, region="Sector 6", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 6 - Logbook 7":  IjiLocData(code=1607, region="Sector 6", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 6 - Logbook 8":  IjiLocData(code=1608, region="Sector 6", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 6 - Logbook 9":  IjiLocData(code=1609, region="Sector 6", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 6 - Logbook 10": IjiLocData(code=1610, region="Sector 6", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 6 - Logbook 11": IjiLocData(code=1611, region="Sector 6 Poster", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 1":  IjiLocData(code=1701, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 2":  IjiLocData(code=1702, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 3":  IjiLocData(code=1703, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 4":  IjiLocData(code=1704, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 5":  IjiLocData(code=1705, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 6":  IjiLocData(code=1706, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 7":  IjiLocData(code=1707, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 8":  IjiLocData(code=1708, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 9":  IjiLocData(code=1709, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 10": IjiLocData(code=1710, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 11": IjiLocData(code=1711, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 12": IjiLocData(code=1712, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 13": IjiLocData(code=1713, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 14": IjiLocData(code=1714, region="Sector 7", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 15": IjiLocData(code=1715, region="Sector 7 Heavy Weapon Armory", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 16": IjiLocData(code=1716, region="Sector 7 Hyper Turret Logbooks", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 17": IjiLocData(code=1717, region="Sector 7 Hyper Turret Logbooks", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 18": IjiLocData(code=1718, region="Sector 7 Poster", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 19": IjiLocData(code=1719, region="Sector 7 Poster", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 20": IjiLocData(code=1720, region="Sector 7 Crackers' Hideout", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 21": IjiLocData(code=1721, region="Sector 7 Crackers' Hideout", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 7 - Logbook 22": IjiLocData(code=1722, region="Sector 7 Crackers' Hideout", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 1":  IjiLocData(code=1801, region="Sector 8", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 2":  IjiLocData(code=1802, region="Sector 8", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 3":  IjiLocData(code=1803, region="Sector 8", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 4":  IjiLocData(code=1804, region="Sector 8", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 5":  IjiLocData(code=1805, region="Sector 8", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 6":  IjiLocData(code=1806, region="Sector 8", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 7":  IjiLocData(code=1807, region="Sector 8", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 8":  IjiLocData(code=1808, region="Sector 8", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 9":  IjiLocData(code=1809, region="Sector 8", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 10": IjiLocData(code=1810, region="Sector 8", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 11": IjiLocData(code=1811, region="Sector 8", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 12": IjiLocData(code=1812, region="Sector 8", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 13": IjiLocData(code=1813, region="Sector 8 Staff Storage Return Trip", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 14": IjiLocData(code=1814, region="Sector 8 Poster", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 8 - Logbook 15": IjiLocData(code=1815, region="Sector 8", \
        valid=lambda world: world.options.LogbookLocations,\
        logic=lambda world, state: has_stats(state, "Strength Stat", world.player, 4, world.options.CompactStatItems.value)),
    "Sector 9 - Logbook 1":  IjiLocData(code=1901, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 2":  IjiLocData(code=1902, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 3":  IjiLocData(code=1903, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 4":  IjiLocData(code=1904, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 5":  IjiLocData(code=1905, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 6":  IjiLocData(code=1906, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 7":  IjiLocData(code=1907, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 8":  IjiLocData(code=1908, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 9":  IjiLocData(code=1909, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 10": IjiLocData(code=1910, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 11": IjiLocData(code=1911, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 12": IjiLocData(code=1912, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 13": IjiLocData(code=1913, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 14": IjiLocData(code=1914, region="Sector 9 Poster", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector 9 - Logbook 15": IjiLocData(code=1915, region="Sector 9", \
        valid=lambda world: world.options.LogbookLocations,\
        logic=lambda world, state: (has_weapon_stats(state, "Hyper Pulse Cannon", world.player, world.options.CompactStatItems.value) and
                                    has_stats(state, "Strength Stat", world.player, 4, world.options.CompactStatItems.value))),
    "Sector 9 - Logbook 16": IjiLocData(code=1916, region="Sector 9 Deep Sector", \
        valid=lambda world: world.options.LogbookLocations ),
    "Sector 9 - Logbook 17": IjiLocData(code=1917, region="Sector 9 Deep Sector", \
        valid=lambda world: (world.options.LogbookLocations and world.options.PacifistLocations)),
    "Sector 9 - Logbook 18": IjiLocData(code=1918, region="Sector 9 Deep Sector", \
        valid=lambda world: (world.options.LogbookLocations and world.options.PacifistLocations)),
    "Sector 9 - Logbook 19": IjiLocData(code=1919, region="Sector 9 Deep Sector", \
        valid=lambda world: (world.options.LogbookLocations and world.options.PacifistLocations)),
    "Sector X - Logbook 1":  IjiLocData(code=1001, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 2":  IjiLocData(code=1002, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 3":  IjiLocData(code=1003, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 4":  IjiLocData(code=1004, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 5":  IjiLocData(code=1005, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 6":  IjiLocData(code=1006, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 7":  IjiLocData(code=1007, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 8":  IjiLocData(code=1008, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 9":  IjiLocData(code=1009, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 10": IjiLocData(code=1010, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 11": IjiLocData(code=1011, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 12": IjiLocData(code=1012, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 13": IjiLocData(code=1013, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 14": IjiLocData(code=1014, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 15": IjiLocData(code=1015, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 16": IjiLocData(code=1016, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 17": IjiLocData(code=1017, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 18": IjiLocData(code=1018, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 19": IjiLocData(code=1019, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 20": IjiLocData(code=1020, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 21": IjiLocData(code=1021, region="Sector X", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 22": IjiLocData(code=1022, region="Sector X Ventilation Shaft", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 23": IjiLocData(code=1023, region="Sector X Maximum Charge Terminal", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 24": IjiLocData(code=1024, region="Sector X Maximum Charge Terminal", \
        valid=lambda world: world.options.LogbookLocations),
    "Sector X - Logbook 25": IjiLocData(code=1025, region="Sector X Maximum Charge Terminal", \
        valid=lambda world: world.options.LogbookLocations)
}

locations_logbooks_z: Dict[str, IjiLocData] = {
    "Sector Z - Logbook 1":  IjiLocData(code=1116, region="Sector Z", \
        valid=lambda world: world.options.LogbookLocations and world.sector_z_allowed()),
    "Sector Z - Logbook 2":  IjiLocData(code=1117, region="Sector Z", \
        valid=lambda world: world.options.LogbookLocations and world.sector_z_allowed())
}

locations_logbooks_y: Dict[str, IjiLocData] = {
    "Sector Y - Logbook 1":  IjiLocData(code=1118, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 2":  IjiLocData(code=1119, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 3":  IjiLocData(code=1120, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 4":  IjiLocData(code=1121, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 5":  IjiLocData(code=1122, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 6":  IjiLocData(code=1123, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 7":  IjiLocData(code=1124, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 8":  IjiLocData(code=1125, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 9":  IjiLocData(code=1126, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 10": IjiLocData(code=1127, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 11": IjiLocData(code=1128, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 12": IjiLocData(code=1129, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 13": IjiLocData(code=1130, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 14": IjiLocData(code=1131, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed()),
    "Sector Y - Logbook 15": IjiLocData(code=1132, region="Sector Y", \
        valid=lambda world: world.options.LogbookLocations and world.sector_y_allowed())
}

# location_doorsanity: IjiLocData = {501->699}
locations_doors: Dict[str, IjiLocData] ={
    "Sector 1 - Kick Door After Tutorial":                      IjiLocData(code=501, region = "Sector 1 Start"),
    "Sector 1 - Kick Door Left of Start (2 Strength)":          IjiLocData(code=502, region = "Sector 1 Start"),
    "Sector 1 - Kick Door to Tutorial Sideroom":                IjiLocData(code=503, region = "Sector 1 Used Materials Access"),
    "Sector 1 - Kick Door to Guard Post":                       IjiLocData(code=505, region = "Sector 1 Used Materials Access"),
    "Sector 1 - Kick Door Next to Ribbon":                      IjiLocData(code=506, region = "Sector 1 Used Materials Access"),
    "Sector 1 - Kick Door to Emergency Armory":                 IjiLocData(code=507, region = "Sector 1 Used Materials Access"),
    "Sector 1 - Kick Door to Medical Surplus":                  IjiLocData(code=508, region = "Sector 1 Emergency Armory"),

    "Sector 2 - Crack Door at Start":                           IjiLocData(code=509, region = "Sector 2 Start"),
    "Sector 2 - Kick Door to Supplies A (2 Strength)":          IjiLocData(code=510, region = "Sector 2 Storage Transport"),
    "Sector 2 - Kick Door to Doctors' Offices":                 IjiLocData(code=511, region = "Sector 2 Storage Transport"),
    "Sector 2 - Activate Medical Bay Door Terminal":            IjiLocData(code=512, region = "Sector 2 Doctors' Offices"),
    "Sector 2 - Crack Door to Security Station (3 Crack)":      IjiLocData(code=513, region = "Sector 2 Medical Access Top"),
    "Sector 2 - Crack Door to Ventilation":                     IjiLocData(code=514, region = "Sector 2 Security Station"),
    "Sector 2 - Activate Break Room Door Terminal":             IjiLocData(code=515, region = "Sector 2 Medical Access Top"),
    "Sector 2 - Kick Door to Storeroom":                        IjiLocData(code=516, region = "Sector 2 Break Room"),

    "Sector 3 - Kick Top Left Software Development Door":       IjiLocData(code=517, region = "Sector 3 Start"),
    "Sector 3 - Kick Bottom Left Software Development Door":    IjiLocData(code=518, region = "Sector 3 Start"),
    "Sector 3 - Kick Top Right Software Development Door (2 Strength)":\
                                                                IjiLocData(code=519, region = "Sector 3 Start"),
    "Sector 3 - Kick Bottom Right Software Development Door (2 Strength)":\
                                                                IjiLocData(code=520, region = "Sector 3 Start"),
    "Sector 3 - Crack Door to Storeroom Left (3 Crack)":        IjiLocData(code=521, region = "Sector 3 Software Development Left"),
    "Sector 3 - Kick Door to Storeroom Right (2 Strength)":     IjiLocData(code=522, region = "Sector 3 Software Development Right"),
    "Sector 3 - Kick Door to Storage Elevator":                 IjiLocData(code=523, region = "Sector 3 Storage A Top"),
    "Sector 3 - Kick First Door to Storage B (2 Strength)":     IjiLocData(code=524, region = "Sector 3 Storage Elevator"),
    "Sector 3 - Crack Second Door to Storage B (2 Crack)":      IjiLocData(code=525, region = "Sector 3 Storage B Interim"),
    "Sector 3 - Kick First Door to Restricted Area (10 Strength)":\
                                                                IjiLocData(code=526, region = "Sector 3 Storage Elevator"),
    "Sector 3 - Crack Second Door to Restricted Area (10 Crack)":\
                                                                IjiLocData(code=527, region = "Sector 3 Restricted Area Interim"),
    "Sector 3 - Kick Door to Main Entrance from Elevator":      IjiLocData(code=528, region = "Sector 3 Storage A Top"),
    "Sector 3 - Kick Left Outside Door":                        IjiLocData(code=529, region = "Sector 3 Storage A Top"),
    "Sector 3 - Kick Right Outside Door":                       IjiLocData(code=530, region = "Sector 3 Storage A Top"),
    "Sector 3 - Kick Bottom Door to Reception (4 Strength)":    IjiLocData(code=531, region = "Sector 3 Storage A Top"),
    "Sector 3 - Kick Top Door to Reception (4 Strength)":       IjiLocData(code=532, region = "Sector 3 Storage A Top"),
    "Sector 3 - Kick Door to Teleporter":                       IjiLocData(code=533, region = "Sector 3 Storage A Top"),
    "Sector 3 - Crack Door to Pulse Cannon (2 Crack)":          IjiLocData(code=534, region = "Sector 3 Guards' Quarters"),
    "Sector 3 - Hyper Pulse First Door to Supercharge":         IjiLocData(code=535, region = "Sector 3 Guards' Quarters"),
    "Sector 3 - Kick Second Door to Supercharge":               IjiLocData(code=536, region = "Sector 3 Heavy Weapons Storage Interim"),
    "Sector 3 - Kick Door to Krotera":                          IjiLocData(code=537, region = "Sector 3 Guards' Quarters"),
    "Sector 3 - Crack Door to Poster":                          IjiLocData(code=538, region = "Sector 3 Outside Guard Tower"),

    "Sector 4 - Crack Door in Surveillance Control":            IjiLocData(code=539, region = "Sector 4 Surveillance Control"),
    "Sector 4 - Activate Main Storage Door Terminal":           IjiLocData(code=540, region = "Sector 4 Start"),
    "Sector 4 - Kick Door to Storage Hub Right (4 Strength)":   IjiLocData(code=541, region = "Sector 4 Start"),
    "Sector 4 - Break Door at Top of Main Storage (Shredder)":  IjiLocData(code=542, region = "Sector 4 Main Storage Top Shredders"),
    "Sector 4 - Crack Door to Main Storage Overload (3 Crack)": IjiLocData(code=543, region = "Sector 4 Main Storage"),
    "Sector 4 - Activate First Main Storage Door Terminal":     IjiLocData(code=544, region = "Sector 4 Shaft to Terminals"),
    "Sector 4 - Activate Second Main Storage Door Terminal":    IjiLocData(code=545, region = "Sector 4 Shaft to Terminals"),
    "Sector 4 - Kick Door to Guard Post (6 Strength)":          IjiLocData(code=546, region = "Sector 4 Shaft to Terminals"),
    "Sector 4 - Kick Door to Reactor Core":                     IjiLocData(code=547, region = "Sector 4 Restricted Storage Access"),
    "Sector 4 - Activate Terminal next to Reactor Core":        IjiLocData(code=548, region = "Sector 4 Reactor Core"),
    "Sector 4 - Activate Door to Communicator Terminal":        IjiLocData(code=549, region = "Sector 4 Final Terminal"),

    "Sector 5 - Kick Door to First Storeroom":                  IjiLocData(code=550, region = "Sector 5 Start"),
    "Sector 5 - Crack Door to Second Storeroom (3 Crack)":      IjiLocData(code=551, region = "Sector 5 Main Region"),
    "Sector 5 - Kick Door to Storage Control Sideroom (7 Strength)":\
                                                                IjiLocData(code=552, region = "Sector 5 Main Region"),
    "Sector 5 - Kick Door to Incoming Goods Sideroom (5 Strength)":\
                                                                IjiLocData(code=553, region = "Sector 5 Main Region"),
    "Sector 5 - Kick Door to Shocksplinter (3 Strength)":       IjiLocData(code=554, region = "Sector 5 Main Region"),
    "Sector 5 - Kick Door Right of Komato Assault Carrier (8 Strength)":\
                                                                IjiLocData(code=555, region = "Sector 5 Main Region"),
    "Sector 5 - Active Door between Tasen and Komato Terminal": IjiLocData(code=556, region = "Sector 5 Main Region"),
    "Sector 5 - Activate Terminal on Floor 9":                  IjiLocData(code=557, region = "Sector 5 Main Region"),
    "Sector 5 - Activate Terminal on Floor 6":                  IjiLocData(code=558, region = "Sector 5 Main Region"),
    "Sector 5 - Activate Terminal on Floor 3":                  IjiLocData(code=559, region = "Sector 5 Classified Materials Control"),
    "Sector 5 - Kick Door to Third Storeroom":                  IjiLocData(code=560, region = "Sector 5 Classified Materials Control"),
    "Sector 5 - Kick Door Below Jump Upgrade":                  IjiLocData(code=561, region = "Sector 5 Classified Materials Storage"),
    "Sector 5 - Kick Door to Jump Upgrade":                     IjiLocData(code=562, region = "Sector 5 Classified Materials Storage"),
    "Sector 5 - Crack Door to Classified Materials Storage Crack Boxes (4 Crack)":\
                                                                IjiLocData(code=563, region = "Sector 5 Classified Materials Storage"),
    "Sector 5 - Kick Door to Sideroom below Classified Materials Storage Crack Boxes (4 Strength)":\
                                                                IjiLocData(code=564, region = "Sector 5 Classified Materials Storage"),

    "Sector 6 - Crack Door to First Sideroom (3 Crack)":        IjiLocData(code=565, region = "Sector 6 Start"),
    "Sector 6 - Kick Door to Ventilation Shaft":                IjiLocData(code=566, region = "Sector 6 Start"),
    "Sector 6 - Kick Door to Ventilation Shaft Shocksplinter":  IjiLocData(code=567, region = "Sector 6 Ventilation Shaft"),
    "Sector 6 - Break Door to Ventilation Shaft Sideroom (Shredder)":\
                                                                IjiLocData(code=568, region = "Sector 6 Ventilation Shaft"),
    "Sector 6 - Activate Terminal Left of Assassin":            IjiLocData(code=569, region = "Sector 6 Neoweapons Storage"),
    "Sector 6 - Activate Terminal below Poster Door":           IjiLocData(code=570, region = "Sector 6 Security Network Admin"),
    "Sector 6 - Crack Door below Poster Door (10 Crack)":       IjiLocData(code=571, region = "Sector 6 Security Network Admin"),
    "Sector 6 - Kick Door at Bottom of Main Elevator":          IjiLocData(code=572, region = "Sector 6 Main Sector Elevator"),
    "Sector 6 - Kick Door to Elevator Shocksplinter":           IjiLocData(code=573, region = "Sector 6 Main Sector Elevator"),
    "Sector 6 - Crack Door at Top of Elevator (4 Crack)":       IjiLocData(code=574, region = "Sector 6 Main Sector Elevator"),
    "Sector 6 - Kick Door to Exit CFIS Room":                   IjiLocData(code=575, region = "Sector 6 Genetic Research"),
    "Sector 6 - Kick Door Left of CFIS":                        IjiLocData(code=576, region = "Sector 6 Genetic Research"),
    "Sector 6 - Kick Door Right of CFIS":                       IjiLocData(code=577, region = "Sector 6 Genetic Research"),
    "Sector 6 - Activate Terminal Between Two Turrets":         IjiLocData(code=578, region = "Sector 6 Main Elevator"),
    "Sector 6 - Kick Door to Neoweapons Research A Sideroom (2 Strength)":\
                                                                IjiLocData(code=579, region = "Sector 6 Main Elevtor")

}


## location_killsanity: IjiLocData = {4001->4999}
#locations_killsanity: Dict[str, IjiLocData] = {
#    # Sector 1 Tasen
#    "Kill Tasen Scout Tuva":                    IjiLocData(code=4001),
#    "Kill Tasen Scout Ogrensie Tayu":           IjiLocData(code=4002),
#    "Kill Tasen Scout Favi Savakrie":           IjiLocData(code=4003),
#    "Kill Tasen Scout Zonrak":                  IjiLocData(code=4004),
#    "Kill Tasen Scout Xutei":                   IjiLocData(code=4005),
#    "Kill Tasen Soldier Iri":                   IjiLocData(code=4006),
#    "Kill Tasen Soldier Elsa Haukti":           IjiLocData(code=4007),
#    "Kill Tasen Scout Lofeito Hel":             IjiLocData(code=4008),
#    "Kill Tasen Scout Shohaka":                 IjiLocData(code=4009),
#    "Kill Tasen Scout Uzon":                    IjiLocData(code=4010),
#    "Kill Tasen Soldier Tajasun":               IjiLocData(code=4011),
#    "Kill Tasen Scout Jao Viy":                 IjiLocData(code=4012),
#    "Kill Tasen Scout Sunsak":                  IjiLocData(code=4013),
#    "Kill Tasen Scout Mari":                    IjiLocData(code=4014),
#    "Kill Tasen Scout Fahel":                   IjiLocData(code=4015),
#    "Kill Tasen Soldier Tusun Tuvaxu":          IjiLocData(code=4016),
#    # Sector 2 Tasen
#    # Sector 3 Tasen
#    "Kill Tasen Elite Krotera":                 IjiLocData(code=4095),
#    # Sector 4 Tasen
#    # Sector 5 Tasen
#    # Sector 6 Tasen
#    # Sector 7 Tasen
#    # Sector 8 Tasen
#    # Sector 9 Tasen
#    # Sector 3 Komato
#    # Sector 5 Komato
#    # Sector 6 Komato
#    # Sector 7 Komato
#    # Sector 8 Komato
#    # Sector 9 Komato
#    "Kill Komato Annihilator Iosa Sakera":      IjiLocData(code=4720),
#    # Sector X Komato
#    "Kill Komato Annhilator Saejao Buhastahel": IjiLocData(code=4771),
#    "Kill Komato Assassin Asha":                IjiLocData(code=4755),
#    "Kill Komato General Tor":                  IjiLocData(code=4798)
#}

location_table = {
    **locations_sectorcomplete,
    **locations_levelup,
    **locations_tutorialpages,
    **locations_statlevels,
    **locations_ribbon,
    **locations_poster,
    **locations_supercharge,
    **locations_upgrades,
    **locations_uniquebasicweapons,
    **locations_sectorweapons,
    **locations_allbasicweapons,
    **locations_combinedweapons,
    **locations_uniquespecialweapons,
    **locations_logbooks,
    **locations_logbooks_z,
    **locations_logbooks_y
}

location_groups_table = {
    group: locations
    for group in [data.region[:8] for _, data in locations_sectorcomplete.items()]
    for locations in [[location for location, data in location_table.items() if data.region[:8] == group]]
}
