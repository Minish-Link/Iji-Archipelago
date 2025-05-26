from typing import Dict, TYPE_CHECKING, List

from worlds.generic.Rules import set_rule

from BaseClasses import CollectionState
from .Names import RegNames, ItemNames, EventNames

if TYPE_CHECKING:
    from . import IjiWorld

def can_access_sector(state: CollectionState, world: "IjiWorld",targetsector: int) -> bool:
    if targetsector == 1:
        return True
    elif world.options.out_of_order_sectors:
        return state.has(ItemNames.Sector_Access[targetsector], world.player) and \
            (world.options.health_balancing == False or has_stats(state, world, ItemNames.Stat_Health, targetsector-1))
    else:
        return state.has(ItemNames.Sector_Access[0], world.player, targetsector-1) and \
            (world.options.health_balancing == False or has_stats(state, world, ItemNames.Stat_Health, targetsector-1))

def meets_goal_req(state: CollectionState, world: "IjiWorld") -> bool:
    return state.has_all_counts({EventNames.Posters[0]: world.options.goal_posters.value,
                                 ItemNames.Ribbon: world.options.goal_ribbons.value}, world.player)
    pass

def has_xp(state: CollectionState, world: "IjiWorld", sector: int, level: int) -> bool:
    current_xp: int = 0
    n = sector-1
    x = level + (5*n)
    current_xp += (4 * (state.count(EventNames.XP[n][0], world.player)))
    current_xp += (8 * (state.count(EventNames.XP[n][1], world.player)))
    current_xp += (16 * (state.count(EventNames.XP[n][2], world.player)))
    current_xp += (32 * (state.count(EventNames.XP[n][3], world.player)))
    current_xp += (64 * (state.count(EventNames.XP[n][4], world.player)))
    current_xp += (128 * (state.count(EventNames.XP[n][5], world.player)))

    if current_xp >= 2*((x*x) + x - (25*n*n) - (5*n)):
        return True
    else:
        return False

#xp_table: List[int] = [
#    4, 12, 24, 40, 60,
#    24, 52, 84, 120, 160,
#    44, 92, 144, 200, 260,
#    64, 132, 204, 280, 360,
#    84, 172, 264, 360, 460,
#    104, 212, 324, 440, 560,
#    124, 252, 384, 520, 660,
#    144, 292, 444, 600, 760,
#    164, 332, 504, 680, 860,
#    184, 372, 564, 760, 960
#]

def get_stat_points(state: CollectionState, world: "IjiWorld") -> int:
    if state.has(EventNames.Weapons[0], world.player): # If Null Driver can be obtained
        return 99
    else:
        return state.count_from_list([EventNames.Levels[0], ItemNames.Supercharge], world.player)

def has_enough_points(state: CollectionState, world: "IjiWorld", points_needed: int) -> bool:
        return get_stat_points(state, world) >= points_needed

def has_stats(state: CollectionState, world: "IjiWorld", stat_needed: str, amount_needed: int) -> bool:
    return (state.has(stat_needed, world.player, amount_needed) and has_enough_points(state, world, amount_needed))

def has_multiple_stats(state: CollectionState, world: "IjiWorld", stats_needed: Dict[str, int]) -> bool:
    points_needed = 0
    for value in stats_needed.values():
        points_needed += value

    return state.has_all_counts(stats_needed, world.player) and has_enough_points(state, world, points_needed)


def can_rocket_boost(state: CollectionState, world: "IjiWorld") -> bool: 
    return (state.has(ItemNames.Stat_Health, world.player) and has_enough_points(state, world, 1)) or\
        state.has(ItemNames.Special_Health, world.player)

def can_mpfb_boost(state: CollectionState, world: "IjiWorld") -> bool:
    return (state.has(ItemNames.Stat_Health, world.player, 1) and state.has(EventNames.Weapons[4], world.player) and
            has_enough_points(state, world, 10))

def can_reach_superchargesix(state: CollectionState, world: "IjiWorld") -> bool:
    return ((state.has(EventNames.Weapons[15], world.player) and has_enough_points(state, world, 13)) or \
           (state.has(EventNames.Weapons[12], world.player) and has_enough_points(state, world, 17)) or \
           (can_retribution(state, world) and has_enough_points(state, world, 19)
            and world.options.logic_difficulty >= 1) or \
           (state.has(EventNames.Weapons[6], world.player) and has_enough_points(state, world, 5)
            and world.options.logic_difficulty >= 3) or \
           state.has(ItemNames.Debug, world.player)) and \
                state.has(ItemNames.Upgrade_Jump, world.player, 1)

def can_retribution(state: CollectionState, world: "IjiWorld") -> bool:
    return (state.has_all([EventNames.Weapons[1],
                          EventNames.Weapons[2],
                          EventNames.Weapons[3],
                          EventNames.Weapons[4],
                          EventNames.Weapons[5],
                          EventNames.Weapons[6],
                          EventNames.Weapons[7],
                          EventNames.Weapons[8]], world.player) and
            can_rocket_boost(state, world))

def can_destroy_sentinel_proxima(state: CollectionState, world: "IjiWorld") -> bool:
    return (
        state.has_all_counts({ItemNames.Stat_Health: 9,
                                 ItemNames.Stat_Attack: 9,
                                 ItemNames.Stat_Assimilate: 3,
                                 ItemNames.Stat_Tasen: 9}, world.player) and
        has_enough_points(state, world, 30)
    )

def has_weapon_stats(state: CollectionState, weaponname: str, world: "IjiWorld", extra_points: int = 0) -> bool:
    if weaponname == ItemNames.Weapons[1]:
        return True
    elif weaponname == ItemNames.Weapons[2]:
        return state.has(ItemNames.Stat_Tasen, world.player, 2) and has_enough_points(state, world, 2 + extra_points)
    elif weaponname == ItemNames.Weapons[3]:
        return state.has(ItemNames.Stat_Tasen, world.player, 5) and has_enough_points(state, world, 5 + extra_points)
    elif weaponname == ItemNames.Weapons[4]:
        return state.has(ItemNames.Stat_Tasen, world.player, 9) and has_enough_points(state, world, 9 + extra_points)
    elif weaponname == ItemNames.Weapons[5]:
        return True
    elif weaponname == ItemNames.Weapons[6]:
        return state.has(ItemNames.Stat_Komato, world.player, 2) and has_enough_points(state, world, 2 + extra_points)
    elif weaponname == ItemNames.Weapons[7]:
        return state.has(ItemNames.Stat_Komato, world.player, 5) and has_enough_points(state, world, 5 + extra_points)
    elif weaponname == ItemNames.Weapons[8]:
        return state.has(ItemNames.Stat_Komato, world.player, 9) and has_enough_points(state, world, 9 + extra_points)
    elif weaponname == ItemNames.Weapons[9]:
        return state.has_all_counts({ItemNames.Stat_Tasen: 2,
                                     ItemNames.Stat_Crack: 2}, world.player) and has_enough_points(state, world, 4 + extra_points)
    elif weaponname == ItemNames.Weapons[10]:
        return state.has_all_counts({ItemNames.Stat_Tasen: 2,
                                     ItemNames.Stat_Komato: 5,
                                     ItemNames.Stat_Crack: 6}, world.player) and has_enough_points(state, world, 13 + extra_points)
    elif weaponname == ItemNames.Weapons[11]:
        return state.has_all_counts({ItemNames.Stat_Tasen: 5,
                                     ItemNames.Stat_Crack: 4}, world.player) and has_enough_points(state, world, 9 + extra_points)
    elif weaponname == ItemNames.Weapons[12]:
        return state.has_all_counts({ItemNames.Stat_Tasen: 9,
                                     ItemNames.Stat_Crack: 8}, world.player) and has_enough_points(state, world, 17 + extra_points)
    elif weaponname == ItemNames.Weapons[13]:
        return state.has(ItemNames.Stat_Crack, world.player, 3) and has_enough_points(state, world, 3 + extra_points)
    elif weaponname == ItemNames.Weapons[14]:
        return state.has_all_counts({ItemNames.Stat_Komato: 2,
                                     ItemNames.Stat_Crack: 5}, world.player) and has_enough_points(state, world, 7 + extra_points)
    elif weaponname == ItemNames.Weapons[15]:
        return state.has_all_counts({ItemNames.Stat_Komato: 5,
                                     ItemNames.Stat_Crack: 7}, world.player) and has_enough_points(state, world, 12 + extra_points)
    elif weaponname == ItemNames.Weapons[16]:
        return state.has_all_counts({ItemNames.Stat_Tasen: 9,
                                     ItemNames.Stat_Komato: 9,
                                     ItemNames.Stat_Crack: 9}, world.player) and has_enough_points(state, world, 27 + extra_points)
    elif weaponname == ItemNames.Weapons[17]:
        return state.has_all_counts({ItemNames.Stat_Tasen: 9,
                                     ItemNames.Stat_Komato: 9}, world.player) and has_enough_points(state, world, 18 + extra_points)
    elif weaponname == ItemNames.Weapons[18]: # requires using a Velocithor V2-10 to obtain
        return state.has_all_counts({ItemNames.Stat_Tasen: 9,
                                     ItemNames.Stat_Komato: 9,
                                     ItemNames.Stat_Crack: 9}, world.player) and has_enough_points(state, world, 27 + extra_points)
    elif weaponname == ItemNames.Weapons[0]:
        return True
    else:
        return False # should not happen, but just in case

def can_make_bustergun(state: CollectionState, world: "IjiWorld") -> bool:
    return has_weapon_stats(state, ItemNames.Weapons[9], world) and \
        state.has_all([EventNames.Weapons[1], EventNames.Weapons[2]], world.player)

def can_make_splintergun(state: CollectionState, world: "IjiWorld") -> bool:
    return has_weapon_stats(state, ItemNames.Weapons[10], world) and \
        state.has_all([EventNames.Weapons[2], EventNames.Weapons[7]], world.player)

def can_make_spreadrockets(state: CollectionState, world: "IjiWorld") -> bool:
    return has_weapon_stats(state, ItemNames.Weapons[11], world) and \
        state.has_all([EventNames.Weapons[1], EventNames.Weapons[3]], world.player)

def can_make_nuke(state: CollectionState, world: "IjiWorld") -> bool:
    return has_weapon_stats(state, ItemNames.Weapons[12], world) and \
        state.has_all([EventNames.Weapons[3], EventNames.Weapons[4]], world.player)

def can_make_resonancereflector(state: CollectionState, world: "IjiWorld") -> bool:
    return (has_weapon_stats(state, ItemNames.Weapons[13], world) and \
        state.has_all([EventNames.Weapons[1], EventNames.Weapons[5]], world.player))

def can_make_hyperpulse(state: CollectionState, world: "IjiWorld") -> bool:
    return has_weapon_stats(state, ItemNames.Weapons[14], world) and \
        state.has_all([EventNames.Weapons[5], EventNames.Weapons[6]], world.player)

def can_make_plasmacannon(state: CollectionState, world: "IjiWorld") -> bool:
    return has_weapon_stats(state, ItemNames.Weapons[15], world) and \
        state.has_all([EventNames.Weapons[6], EventNames.Weapons[7]], world.player)

def can_make_velocithor(state: CollectionState, world: "IjiWorld") -> bool:
    return has_weapon_stats(state, ItemNames.Weapons[16], world)\
       and state.has_all([EventNames.Weapons[4], EventNames.Weapons[8]], world.player)



def can_kill_annihilators(state: CollectionState, world: "IjiWorld") -> bool:
    return (state.has_any([EventNames.Weapons[3], EventNames.Weapons[7]], world.player)) and \
        state.has(ItemNames.Stat_Attack, world.player, 4) and \
        state.has(ItemNames.Stat_Health, world.player, 4) and \
        has_enough_points(state, world, 13)

def can_reach_poster_nine(state: CollectionState, world: "IjiWorld") -> bool:
    return state.has(ItemNames.Stat_Health, world.player, 9)\
       and (not world.options.special_trait_items or state.has(ItemNames.Special_Health, world.player))\
      and state.has(EventNames.Weapons[4], world.player) and has_enough_points(state, world, 18)