from typing import TYPE_CHECKING

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import IjiWorld

def can_access_sector(state: CollectionState, player: int, healthbalancing: bool, targetsector: int) -> bool:
    return state.has("Sector Access", player, targetsector-1) and \
        (healthbalancing == False or state.has("Health Stat", player, targetsector-1))

def can_rocket_boost(state: CollectionState, player: int) -> bool: 
    return state.has("Health Stat", player) or state.has("SUPPRESSION", player)

def has_weapon_stats(state: CollectionState, weaponname: str, player: int) -> bool:
    if weaponname == "Shotgun":
        return True
    elif weaponname == "Machine Gun":
        return state.has("Tasen Stat", player, 2)
    elif weaponname == "Rocket Launcher":
        return state.has("Tasen Stat", player, 5)
    elif weaponname == "MPFB Devastator":
        return state.has("Tasen Stat", player, 9)
    elif weaponname == "Resonance Detonator":
        return True
    elif weaponname == "Pulse Cannon":
        return state.has("Komato Stat", player, 2)
    elif weaponname == "Shocksplinter":
        return state.has("Komato Stat", player, 5)
    elif weaponname == "CFIS":
        return state.has("Komato Stat", player, 9)
    elif weaponname == "Buster Gun":
        return state.has_all_counts({"Tasen Stat": 2, "Crack Stat": 2}, player)
    elif weaponname == "Splintergun":
        return state.has_all_counts({"Tasen Stat": 2, "Komato Stat": 5, "Crack Stat": 6}, player)
    elif weaponname == "Spread Rockets":
        return state.has_all_counts({"Tasen Stat": 5, "Crack Stat": 4}, player)
    elif weaponname == "Nuke":
        return state.has_all_counts({"Tasen Stat": 9, "Crack Stat": 8}, player)
    elif weaponname == "Resonance Reflector":
        return state.has("Crack Stat", player, 3)
    elif weaponname == "Hyper Pulse Cannon":
        return state.has_all_counts({"Komato Stat": 2, "Crack Stat": 5})
    elif weaponname == "Plasma Cannon":
        return state.has_all_counts({"Komato Stat": 5, "Crack Stat": 7})
    elif weaponname == "Velocithor":
        return state.has_all_counts({"Tasen Stat": 9, "Komato Stat": 9, "Crack Stat": 9})
    elif weaponname == "Banana Gun":
        return state.has_all_counts({"Tasen Stat": 9, "Komato Stat": 9}, player)
    elif weaponname == "Massacre":
        return True
    elif weaponname == "Null Driver":
        return True
    else:
        return False # should not happen, but just in case

def can_kill_annihilators(state: CollectionState, player: int) -> bool:
    return (state.has("Tasen Stat", player, 5) or state.has("Komato Stat", player, 5)) and \
        state.has("Attack Stat", player, 4)

def can_reach_poster_nine(state: CollectionState, player: int, suppressionshuffle: bool) -> bool:
    return state.has("Health Stat", player, 9) and (not suppressionshuffle or state.has("SUPPRESSION", player))

def can_reach_sector_z(state: CollectionState, player: int, posterrequirement: int, posterlocations: bool) -> bool:
    if posterlocations:
        return state.has("Strength Stat", player, 3) and posterrequirement <= get_poster_location_count(state, player)
    else:
        return state.has("Strength Stat", player, 3) and state.has("Poster", player, posterrequirement)

def can_reach_nulldriver(state: CollectionState, player: int,
                         posterrequirement: int, posterlocations: bool,
                         ribbonrequirement: int, ribbonlocations: bool) -> bool:
    if posterlocations:
        if ribbonlocations:
            return posterrequirement <= get_poster_location_count(state, player) and \
                state.has("Sector Access", player, max(0, ribbonrequirement - 1))
        else:
            return posterrequirement <= get_poster_location_count(state, player) and \
                state.has("Ribbon", player, ribbonrequirement)
    else:
        if ribbonlocations:
            return state.has("Poster", player, posterrequirement) and \
                state.has("Sector Access", player, max(0, ribbonrequirement - 1))
        else:
            return state.has("Poster", player, posterrequirement) and \
                state.has("Ribbon", player, ribbonrequirement)


def get_poster_location_count(state: CollectionState, player: int) -> int:
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