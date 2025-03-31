from typing import Dict, TYPE_CHECKING
import copy

from worlds.generic.Rules import set_rule

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import IjiWorld


def has_stats(state: CollectionState, itemname: str, player: int, itemsneeded: int, compactment: int) -> bool:
    return (state.count(itemname, player) * compactment) >= itemsneeded

def has_multiple_stats(state: CollectionState, itemsneeded: Dict[str, int], player: int, compactment: int) -> bool:
    for itemname, itemamount in itemsneeded.items():
        if not has_stats(state, itemname, player, itemamount, compactment):
            return False

    return True

def get_supercharge_count(world: "IjiWorld", state: CollectionState):
    return state.count("Supercharge", world.player)

def get_sector_max_level(world: "IjiWorld", state: CollectionState, sector: int):
    if world.options.GameDifficulty.value == world.options.GameDifficulty.option_normal:
        return (5 * sector) + get_supercharge_count(world, state)
    elif world.options.GameDifficulty.value == world.options.GameDifficulty.option_hard:
        return (4 * sector) + get_supercharge_count(world, state)
    else:
        return (3 * sector) + get_supercharge_count(world, state)

def get_max_level(world: "IjiWorld", state: CollectionState):
    get_sector_max_level(world, state, min(state.count("Sector Access", world.player)+1, 9))

def can_access_sector(world: "IjiWorld", state: CollectionState, targetsector: int) -> bool:
    if targetsector == 1:
        return True
    return state.has("Sector Access", world.player, targetsector-1) and \
        (not world.options.HealthBalancing or\
        has_stats(state, "Health Stat", world.player,
                  min(targetsector-1,world.max_stats["Health Stat"]), world.options.CompactStatItems.value))

def can_rocket_boost(state: CollectionState, player: int) -> bool: 
    return state.has("Health Stat", player) or state.has("SUPPRESSION", player)

def can_reach_superchargesix(state: CollectionState, world: "IjiWorld", compactment: int) -> bool:
    return (has_weapon_stats(state, "Splintergun", world.player, compactment) or 
        has_weapon_stats(state, "Nuke", world.player, compactment) or 
        (has_multiple_stats(state, {"Tasen Stat": 9, "Komato Stat": 9, "Crack Stat": 3}, 
                            world.player, compactment) and 
        can_rocket_boost(state, world.player) and 
        world.options.LogicDifficulty.value >= world.options.LogicDifficulty.option_obscure_logic) or 
        (has_weapon_stats(state, "Shocksplinter", world.player, compactment) and 
        world.options.LogicDifficulty.value == world.options.LogicDifficulty.option_extreme_logic))

def can_destroy_sentinel_proxima(state: CollectionState, world: "IjiWorld") -> bool:
    return has_multiple_stats(state, {"Health Stat": 9, "Attack Stat": 9, "Assimilate Stat": 3, "Tasen Stat": 9},
                              world.player, world.options.CompactStatItems.value)

def has_weapon_stats(state: CollectionState, weaponname: str, player: int, compactment: int) -> bool:
    if weaponname == "Shotgun":
        return True
    elif weaponname == "Machine Gun":
        return has_stats(state, "Tasen Stat", player, 2, compactment)
    elif weaponname == "Rocket Launcher":
        return has_stats(state, "Tasen Stat", player, 5, compactment)
    elif weaponname == "MPFB Devastator":
        return has_stats(state, "Tasen Stat", player, 9, compactment)
    elif weaponname == "Resonance Detonator":
        return True
    elif weaponname == "Pulse Cannon":
        return has_stats(state, "Komato Stat", player, 2, compactment)
    elif weaponname == "Shocksplinter":
        return has_stats(state, "Komato Stat", player, 5, compactment)
    elif weaponname == "CFIS":
        return has_stats(state, "Komato Stat", player, 9, compactment)
    elif weaponname == "Buster Gun":
        return has_multiple_stats(state, {"Tasen Stat": 2, "Crack Stat": 2}, player, compactment)
    elif weaponname == "Splintergun":
        return has_multiple_stats(state, {"Tasen Stat": 2, "Komato Stat": 5, "Crack Stat": 6}, player, compactment)
    elif weaponname == "Spread Rockets":
        return has_multiple_stats(state, {"Tasen Stat": 5, "Crack Stat": 4}, player, compactment)
    elif weaponname == "Nuke":
        return has_multiple_stats(state, {"Tasen Stat": 9, "Crack Stat": 8}, player, compactment)
    elif weaponname == "Resonance Reflector":
        return has_stats(state, "Crack Stat", player, 3, compactment)
    elif weaponname == "Hyper Pulse":
        return has_multiple_stats(state, {"Komato Stat": 2, "Crack Stat": 5}, player, compactment)
    elif weaponname == "Plasma Cannon":
        return has_multiple_stats(state, {"Komato Stat": 5, "Crack Stat": 7}, player, compactment)
    elif weaponname == "Velocithor":
        return has_multiple_stats(state, {"Tasen Stat": 9, "Komato Stat": 9, "Crack Stat": 9}, player, compactment)
    elif weaponname == "Banana Gun":
        return has_multiple_stats(state, {"Tasen Stat": 9, "Komato Stat": 9}, player, compactment)
    elif weaponname == "Massacre": # requires using a Velocithor V2-10 to obtain
        return has_multiple_stats(state, {"Tasen Stat": 9, "Komato Stat": 9, "Crack Stat": 9}, player, compactment)
    elif weaponname == "Null Driver":
        return True
    else:
        return False # should not happen, but just in case

def can_reach_machinegun(state: CollectionState, player: int, compactment: int) -> bool:
    return has_weapon_stats(state, "Machine Gun", player, compactment)

def can_reach_rocketlauncher(state: CollectionState, player: int, compactment: int) -> bool:
    return has_weapon_stats(state, "Rocket Launcher", player, compactment) and \
        (state.can_reach_region("Sector 2 Storage Transport Top", player) or \
        state.can_reach_region("Sector 3", player))

def can_reach_mpfbdevastator(state: CollectionState, player: int, compactment: int) -> bool:
    return has_weapon_stats(state, "MPFB Devastator", player, compactment) and \
        (state.can_reach_region("Sector 4 Top of Main Storage", player) or \
        state.can_reach_region("Sector 5", player))

def can_reach_resonancedetonator(state: CollectionState, player: int, compactment: int) -> bool:
    return state.can_reach_region("Sector 2", player)

def can_reach_pulsecannon(state: CollectionState, player: int, compactment: int) -> bool:
    return has_weapon_stats(state, "Pulse Cannon", player, compactment) and \
        ((state.can_reach_region("Sector 3", player) and has_stats(state, "Crack Stat", player, 1, compactment)) or\
        state.can_reach_region("Sector 4", player))

def can_reach_shocksplinter(state: CollectionState, player: int, compactment: int) -> bool:
    return has_weapon_stats(state, "Shocksplinter", player, compactment) and \
        state.can_reach_region("Sector 5", player)

def can_reach_cfis(state: CollectionState, player: int, compactment: int) -> bool:
    return has_weapon_stats(state, "CFIS", player, compactment) and \
        ((state.can_reach_region("Sector 6", player) and has_stats(state, "Crack Stat", player, 3, compactment)) or \
        (state.can_reach_region("Sector 7", player) and has_stats(state, "Strength Stat", player, 2, compactment)) or \
        (state.can_reach_region("Sector 8", player)))

def can_make_bustergun(state: CollectionState, player: int, compactment: int) -> bool:
    return has_weapon_stats(state, "Buster Gun", player, compactment)

def can_make_splintergun(state: CollectionState, player: int, compactment: int) -> bool:
    return has_weapon_stats(state, "Splintergun", player, compactment) and \
        can_reach_shocksplinter(state, player, compactment)

def can_make_spreadrockets(state: CollectionState, player: int, compactment: int) -> bool:
    return has_weapon_stats(state, "Spread Rockets", player, compactment) and \
        can_reach_rocketlauncher(state, player, compactment)

def can_make_nuke(state: CollectionState, player: int, compactment: int) -> bool:
    return has_weapon_stats(state, "Nuke", player, compactment) and \
        can_reach_mpfbdevastator(state, player, compactment)

def can_make_resonancereflector(state: CollectionState, player: int, compactment: int) -> bool:
    return (has_weapon_stats(state, "Resonance Reflector", player, compactment) and \
        can_reach_resonancedetonator(state, player, compactment)) or \
        state.can_reach_region("Sector X", player) # Could you imagine having Sector X access before having 4 Crack

def can_make_hyperpulse(state: CollectionState, player: int, compactment: int) -> bool:
    return has_weapon_stats(state, "Hyper Pulse", player, compactment) and \
        can_reach_pulsecannon(state, player, compactment)

def can_make_plasmacannon(state: CollectionState, player: int, compactment: int) -> bool:
    return has_weapon_stats(state, "Plasma Cannon", player, compactment) and \
        can_reach_shocksplinter(state, player, compactment)

def can_make_velocithor(state: CollectionState, player: int, compactment: int) -> bool:
    return has_weapon_stats(state, "Velocithor", player, compactment) and \
        can_reach_cfis(state, player, compactment)



def can_kill_annihilators(state: CollectionState, player: int, compactment: int) -> bool:
    return (has_weapon_stats(state, "Rocket Launcher", player, compactment) or\
        has_weapon_stats(state, "Shocksplinter", player, compactment)) and \
        has_stats(state, "Attack Stat", player, 4, compactment)

def can_reach_poster_nine(state: CollectionState, player: int, suppressionshuffle: bool, compactment: int) -> bool:
    return has_stats(state, "Health Stat", player, 9, compactment) and\
        (suppressionshuffle == False or state.has("SUPPRESSION", player)) and\
        has_weapon_stats(state, "MPFB Devastator", player, compactment)

def can_reach_sector_z(state: CollectionState, player: int, world: "IjiWorld",
                       posterrequirement: int, ribbonrequirement: int, compactment: int) -> bool:
    return (posterrequirement <= get_poster_location_count(state, player, world, compactment) and\
        state.has("Ribbon", player, ribbonrequirement))

def can_reach_nulldriver(state: CollectionState, player: int, world: "IjiWorld",
                         posterrequirement: int, ribbonrequirement: int, compactment: int) -> bool:
    return (can_reach_sector_z(state, player, world, world.options.SectorZPosterLocationsRequired.value,
                               world.options.SectorZRibbonItemsRequired.value, compactment) and
            posterrequirement <= get_poster_location_count(state,player, world, compactment) and
            state.has("Ribbon", player, ribbonrequirement))

def get_poster_location_count(state: CollectionState, player: int, world: "IjiWorld", compactment: int) -> int:
    poster_total: int = 0
    if state.can_reach_region("Sector 1 Poster", player):
        poster_total += 1
    if state.can_reach_region("Sector 2 Poster", player):
        poster_total += 1
    if state.can_reach_region("Sector 3 Poster", player):
        poster_total += 1
    if state.can_reach_region("Sector 4 Poster", player):
        poster_total += 1
    if state.can_reach_region("Sector 5 Poster", player):
        poster_total += 1
    if state.can_reach_region("Sector 6 Poster", player):
        poster_total += 1
    if state.can_reach_region("Sector 7 Poster", player):
        poster_total += 1
    if state.can_reach_region("Sector 8 Poster", player):
        poster_total += 1
    if state.can_reach_region("Sector 9 Poster", player):
        poster_total += 1
    if state.can_reach_region("Sector X Poster", player):
        poster_total += 1

    return poster_total