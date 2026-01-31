from enum import Enum
from math import floor, ceil
from typing import Dict, TYPE_CHECKING, List, NamedTuple
from Data.DoorData import DoorData
from .Options import combined_weapons_indices

from BaseClasses import CollectionState
from .Names import RegNames, ItemNames, EventNames
from ..stardew_valley.stardew_rule import true_

if TYPE_CHECKING:
    from . import IjiWorld

class WeaponData(NamedTuple):
    tasen: int = 0
    komato: int = 0
    crack: int = 0
    points_needed: int = 0

    def clamp_tasen(self, max_value) -> bool: # returns True if tasen was reduced, False if not
        temp = self.tasen
        self.tasen = min(max_value, self.tasen)
        self.calculate_points_needed()
        return temp > self.tasen

    def clamp_komato(self, max_value) -> bool: # returns True if komato was reduced, False if not
        temp = self.komato
        self.komato = min(max_value, self.komato)
        self.calculate_points_needed()
        return temp > self.komato

    def clamp_crack(self, max_value) -> bool: # returns True if crack was reduced, False if not
        temp = self.crack
        self.crack = min(max_value, self.crack)
        self.calculate_points_needed()
        return temp > self.crack

    def calculate_points_needed(self):
        self.points_needed = self.tasen + self.komato + self.crack

def is_difficulty_in_logic(world: "IjiWorld", difficulty: int) -> bool:
    if world.multiworld.state.has(ItemNames.Glitch, world.player):
        return True
    else:
        return world.options.logic_difficulty.value >= difficulty

def can_access_sector(state: CollectionState, world: "IjiWorld", target_sector: int) -> bool:
    if target_sector == 1:
        return True
    else:
        return (
            (state.has(ItemNames.Sector_Access[target_sector], world.player) or
            state.has(ItemNames.Sector_Access[0], world.player, target_sector-1)) and
            meets_hb_requirement(state, world, target_sector)
        )

def meets_hb_requirement(state: CollectionState, world: "IjiWorld", target_sector: int) -> bool:
    return (
        has_stats(world, ItemNames.Stat_Health, world.health_balancing_values[target_sector-2]) or
        (state.has(ItemNames.Glitch, world.player) and not world.options.enforce_health_balancing)
    )

def meets_goal_req(state: CollectionState, world: "IjiWorld") -> bool:
    ribbons_needed = world.options.ribbon_items.value * (world.options.goal_ribbons.value / 100.0)
    return state.has_all_counts({EventNames.Posters[0]: world.options.goal_posters.value,
                                 ItemNames.Ribbon: ribbons_needed}, world.player)

def has_xp(state: CollectionState, world: "IjiWorld", sector: int, level: int) -> bool:
    return state.has(EventNames.XP_Collected[sector-1],
                     world.player,
                     xp_table[world.options.game_difficulty.value][sector-1][level-1])

xp_table: List[List[List[int]]] = [
    [
        [4, 12, 24, 40, 60],
        [24, 52, 84, 120, 160],
        [44, 92, 144, 200, 260],
        [64, 132, 204, 280, 360],
        [84, 172, 264, 360, 460],
        [104, 212, 324, 440, 560],
        [124, 252, 384, 520, 660],
        [144, 292, 444, 600, 760],
        [164, 332, 504, 680, 860],
        [184, 372, 564, 760, 960]
    ],
    [
        [6, 18, 36, 60],
        [30, 66, 108, 156],
        [54, 114, 180, 252],
        [78, 162, 252, 348],
        [102, 210, 324, 444],
        [126, 258, 396, 540],
        [150, 306, 468, 636],
        [174, 354, 540, 732],
        [198, 402, 612, 828],
        [222, 450, 684, 924]
    ],
    [
        [8, 24, 48],
        [32, 72, 120],
        [56, 120, 192],
        [80, 168, 264],
        [104, 216, 336],
        [128, 264, 408],
        [152, 312, 480],
        [176, 360, 552],
        [200, 408, 624],
        [224, 456, 696]
    ]
]

#def get_stat_points(state: CollectionState, world: "IjiWorld") -> int:
#    if state.has(EventNames.Weapons[0], world.player): # If Null Driver can be obtained
#        return 99
#    else:
#        return world.current_stat_items[ItemNames.Supercharge]

def has_enough_points(world: "IjiWorld", points_needed: int) -> bool:
        return world.current_stat_items[ItemNames.Supercharge] >= points_needed

def has_stats(world: "IjiWorld", stat_needed: str, amount_needed: int) -> bool:
    return world.current_stat_items[stat_needed] >= amount_needed and has_enough_points(world, amount_needed)

def has_multiple_stats(world: "IjiWorld", stats_needed: Dict[str, int]) -> bool:
    points_needed = 0
    for value in stats_needed.values():
        points_needed += value

    if not has_enough_points(world, points_needed):
        return False

    for stat, amount in stats_needed.items():
        if min(world.current_stat_items[stat], world.max_stats[stat]) < amount:
            return False

    return True

def can_rocket_boost(state: CollectionState, world: "IjiWorld") -> bool:
    health_needed = 0 if state.has(ItemNames.Special_Health, world.player) else 1
    return (
        (
            has_stats(world, ItemNames.Stat_Health, health_needed) and
            has_any_weapons_plus_points(state, world, [3,7], health_needed)
        ) or
        can_mpfb_boost(state, world)
    )

def can_shock_boost(state: CollectionState, world: "IjiWorld") -> bool:
    # Shocksplinter blasts launch Iji farther, and may be needed when rockets won't cut it
    health_needed = 0 if state.has(ItemNames.Special_Health, world.player) else 1
    return (
        has_stats(world, ItemNames.Stat_Health, health_needed) and
        has_weapon_plus_points(state, world, 7, health_needed)
    )

def can_mpfb_boost(state: CollectionState, world: "IjiWorld") -> bool:
    return (
        has_stats(world, ItemNames.Stat_Health, 1) and
        has_weapon_plus_points(state, world, 4, 1)
    )

def can_banana_boost(state: CollectionState, world: "IjiWorld") -> bool:
    return (
        has_stats(world, ItemNames.Stat_Health, 1) and
        has_weapon_plus_points(state, world, 17, 1)
    )

def get_max_health(state: CollectionState, world: "IjiWorld") -> int:
    return min(20,(state.count(ItemNames.Stat_Health, world.player) + 1) * 2)

def can_reach_superchargesix(state: CollectionState, world: "IjiWorld") -> bool:
    return (((state.has(EventNames.Weapons[10], world.player)) or # Splintergun
           (state.has(EventNames.Weapons[12], world.player)) or # Nuke
           (can_retribution(state, world) and world.options.logic_difficulty >= 1) or # Retribution
           (state.has(EventNames.Weapons[7], world.player) and state.has(ItemNames.Glitch, world.player)) or # Shocksplinter
           state.has(ItemNames.Debug, world.player)) and # Shoot the glass midair
            state.has(ItemNames.Upgrade_Jump, world.player, 1))

def can_retribution(state: CollectionState, world: "IjiWorld") -> bool:
    return (state.has_all([EventNames.Weapons[1],
                          EventNames.Weapons[2],
                          EventNames.Weapons[3],
                          EventNames.Weapons[4],
                          EventNames.Weapons[5],
                          EventNames.Weapons[6],
                          EventNames.Weapons[7],
                          EventNames.Weapons[8]], world.player) and
            can_rocket_boost(state, world) and
            has_enough_points(world, world.weapon_stats_needed["Banana Gun"].points_needed + 1))

def can_destroy_sentinel_proxima(state: CollectionState, world: "IjiWorld") -> bool:
    return (
        (
            has_multiple_stats(world, {
                ItemNames.Stat_Health: 9,
                ItemNames.Stat_Attack: 9,
                ItemNames.Stat_Assimilate: 3
            }) and
            has_weapon_plus_points(state, world, 4, 21)
        ) or
        (
            is_difficulty_in_logic(world, 1) and
            has_multiple_stats(world, {
                ItemNames.Stat_Health: 3,
                ItemNames.Stat_Attack: 9,
                ItemNames.Stat_Assimilate: 3
            }) and
            has_weapon_plus_points(state, world, 4, 15)
            #state.has_all_counts({ EventNames.Stat_Health: 3,
            #                      EventNames.Stat_Attack: 9,
            #                      EventNames.Stat_Assimilate: 3,
            #                      EventNames.Weapons[4]: 1}, world.player) and
            #has_weapon_stats(state, ItemNames.Weapons[4],world,15)
        ) # TODO add additional glitched logic for sentinel proxima AKA a major pain in my ass
    )

def has_special_trait(state: CollectionState, world: "IjiWorld", trait_index: int) -> tuple:
    # Return value is (bool,int): bool is whether they have access to the trait, int is how many stat points are needed
    if state.has(ItemNames.Special_Traits[trait_index], world.player):
            return True, 0

    elif not world.options.special_trait_items:
        points_needed: int = world.max_stats[ItemNames.Stats[trait_index]]
        return has_stats(world, ItemNames.Stats[trait_index], points_needed), points_needed

    return False, 0

def has_weapon_stats(state: CollectionState, weapon_name: str, world: "IjiWorld", extra_points: int = 0) -> bool:
    weapon_data = world.weapon_stats_needed[weapon_name]
    has_multiple_stats(world,
                       {
                           ItemNames.Stat_Tasen: weapon_data.tasen,
                           ItemNames.Stat_Komato: weapon_data.komato,
                           ItemNames.Stat_Crack: weapon_data.crack
                       })

def can_make_weapon(state: CollectionState, world: "IjiWorld", weapon_name: str) -> bool:
    if not state.has_all(["Has "+combined_weapons_indices[weapon_name][0],
                          "Has "+combined_weapons_indices[weapon_name][0]], world.player):
        return False

    return has_weapon_stats(state, weapon_name, world)

def can_kill_annihilators(state: CollectionState, world: "IjiWorld") -> bool:
    return (
        (
            is_difficulty_in_logic(world, 2) # Glitched Logic. Nothing but a shotgun and a dream
        ) or
        (
            is_difficulty_in_logic(world, 1) and
            has_stats(world, ItemNames.Stat_Health, 4) and
            (
                has_any_weapons_plus_points(state, world, [3,4,7,8,13], 4)
            )
        ) or
        (
            state.has(ItemNames.Stat_Attack, world.player, 4) and
            state.has(ItemNames.Stat_Health, world.player, 4) and
            has_any_weapons_plus_points(state, world, [3,4,7,8], 8)
        )
    )

def can_kill_yukabacera(state: CollectionState, world: "IjiWorld") -> bool:
    # TODO
    return True

def has_any_weapons_plus_points(state: CollectionState, world: "IjiWorld", weapon_indices: List[int], extra_points: int = 0) -> bool:
    for i in weapon_indices:
        if has_weapon_plus_points(state, world, i, extra_points):
            return True
    return False

def has_weapon_plus_points(state: CollectionState, world: "IjiWorld", weapon_index: int, extra_points: int = 0) -> bool:
    if not state.has(EventNames.Weapons[weapon_index], world.player):
        return False
    points_needed = world.weapon_stats_needed[ItemNames.Weapons[weapon_index]].points_needed
    return has_enough_points(world, points_needed + extra_points)

def can_reach_poster_nine(state: CollectionState, world: "IjiWorld") -> bool:
    # Glitched Mid-air logic
    if is_difficulty_in_logic(world, 2) and state.has(ItemNames.Debug, world.player):
        # Midair MPFB blasts
        health_needed: int = 3 if state.has(ItemNames.Special_Health, world.player) else 4
        if (has_stats(world, ItemNames.Stat_Health, health_needed) and
                has_weapon_plus_points(state, world, 4, health_needed)):
            return True
        # TODO: Other Glitched methods to reach the poster
    # The intended method
    if not has_special_trait(state, world, 0)[0]:
        return False
    return (
        has_stats(world, ItemNames.Stat_Health, 9) and
        has_weapon_plus_points(state, world, 4, 9)
    )

def can_open_door(state: CollectionState, world: "IjiWorld", door_id: int, from_terminal: bool = False) -> bool:
    #TODO
    if from_terminal:
        return world.door_stats[door_id].can_open(state, world, from_terminal)
    else:
        if world.door_stats[door_id].terminal > 0 and state.has(EventNames.Terminals[door_id], world.player):
            return True
        return world.door_stats[door_id].can_open(state, world, from_terminal)

    return True
