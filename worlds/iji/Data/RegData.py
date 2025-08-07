from typing import Callable, Dict, List, TYPE_CHECKING, NamedTuple
from ..Rules import can_access_sector, can_reach_poster_nine, can_reach_superchargesix, can_rocket_boost, has_stats, has_multiple_stats, has_weapon_stats, has_enough_points, can_mpfb_boost, meets_goal_req
from BaseClasses import CollectionState
from ..Names import RegNames, ItemNames, EventNames

if TYPE_CHECKING:
    from .. import IjiWorld

class ExitData(NamedTuple):
    valid: Callable[["IjiWorld"], bool] = lambda world: True
    logic: Callable[["IjiWorld", CollectionState], bool] = lambda world, state: True

region_exit_table: Dict[str, Dict[str, ExitData]] = {
    RegNames.Menu: {
        RegNames.Global: ExitData(),
        RegNames.Sector1_Main[0]: ExitData(
            logic=lambda world, state: can_access_sector(state, world, 1)
        ),
        RegNames.Sector2_Main[0]: ExitData(
            logic=lambda world, state: can_access_sector(state, world, 2)
        ),
        RegNames.Sector3_Main[0]: ExitData(
            logic=lambda world, state: can_access_sector(state, world, 3)
        ),
        RegNames.Sector4_Main[0]: ExitData(
            valid=lambda world: world.options.end_goal.value >= 5,
            logic=lambda world, state: can_access_sector(state, world, 4)
        ),
        RegNames.Sector5_Main[0]: ExitData(
            valid=lambda world: world.options.end_goal.value >= 5,
            logic=lambda world, state: can_access_sector(state, world, 5)
        ),
        RegNames.Sector6_Main[0]: ExitData(
            valid=lambda world: world.options.end_goal.value >= 7,
            logic=lambda world, state: can_access_sector(state, world, 6)
        ),
        RegNames.Sector7_Main[0]: ExitData(
            valid=lambda world: world.options.end_goal.value >= 7,
            logic=lambda world, state: can_access_sector(state, world, 7)
        ),
        RegNames.Sector8_Main[0]: ExitData(
            valid=lambda world: world.options.end_goal.value >= 9,
            logic=lambda world, state: can_access_sector(state, world, 8)
        ),
        RegNames.Sector9_Main[0]: ExitData(
            valid=lambda world: world.options.end_goal.value >= 9,
            logic=lambda world, state: can_access_sector(state, world, 9)
        ),
        RegNames.SectorX_Main[0]: ExitData(
            valid=lambda world: world.options.end_goal.value >= 10,
            logic=lambda world, state: can_access_sector(state, world, 10)
        )
    },
    RegNames.Global: {},
    # Sector 1
    # Main Path
    RegNames.Sector1_Main[0]: {
        RegNames.Sector1_Poster: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 1)
            )
        ),
        RegNames.Sector1_Main[1]: ExitData()
    },
    RegNames.Sector1_Main[1]: {
        RegNames.Sector1_Main[2]: ExitData(),
        RegNames.Sector1_Super: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 3) or
                state.has_any([EventNames.Weapons[3], EventNames.Weapons[7]], world.player)
            )
        ),
        RegNames.Sector1_Side[0]: ExitData(),
        RegNames.Sector1_Side[1]: ExitData()
    },
    RegNames.Sector1_Main[2]: {
        RegNames.Sector1_Main[3]: ExitData()
    },
    RegNames.Sector1_Main[3]: {},
    # Side Paths
    RegNames.Sector1_Poster: {},
    RegNames.Sector1_Super: {
        RegNames.SectorZ: ExitData(
            valid=lambda world: (
                (world.options.end_goal.value >= 11 or world.options.allow_sector_z.value > 0)
            ),
            logic=lambda world, state: (
                (meets_goal_req(state, world) or 
                 (world.options.end_goal.value < 11 and world.options.allow_sector_z.value & 4 == 0))
            )
        )
    },
    RegNames.Sector1_Side[0]: {},
    RegNames.Sector1_Side[1]: {},
    # Sector Z
    RegNames.SectorZ: {
        RegNames.SectorZ_Null: ExitData(
            valid=lambda world: (
                world.options.end_goal.value == 12 or world.options.allow_sector_z.value & 2 == 2)
        )
    },
    RegNames.SectorZ_Null: {},
    # Sector 2
    # Main Path
    RegNames.Sector2_Main[0]: {
        RegNames.Sector2_Main[1]: ExitData()
    },
    RegNames.Sector2_Main[1]: {
        RegNames.Sector2_Main[2]: ExitData(),
        RegNames.Sector2_Side[0]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 1)
            )
        ),
        RegNames.Sector2_Side[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        )
    },
    RegNames.Sector2_Main[2]: {
        RegNames.Sector2_Main[7]: ExitData(),
        RegNames.Sector2_Super: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        ),
        RegNames.Sector2_Main[5]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        )
    },
    RegNames.Sector2_Main[3]: {
        RegNames.Sector2_Main[4]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        )
    },
    RegNames.Sector2_Main[4]: {
        RegNames.Sector2_Side[2]: ExitData(
            logic=lambda world, state: (
                can_rocket_boost(state, world)
            )
        )
    },
    RegNames.Sector2_Main[5]: {
        RegNames.Sector2_Main[6]: ExitData(),
        RegNames.Sector2_Side[3]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 2)
            )
        )
    },
    RegNames.Sector2_Main[6]: {
        RegNames.Sector2_Side[5]: ExitData(),
        RegNames.Sector2_Poster: ExitData(
            logic=lambda world, state: (
                world.options.logic_difficulty.value >= 2 or
                has_stats(state, world, ItemNames.Stat_Strength, 3) or
                state.has_any([EventNames.Weapons[2], EventNames.Weapons[6]], world.player)
            )
        )
    },

    RegNames.Sector2_Main[7]: {
        RegNames.Sector2_Main[3]: ExitData(),
        RegNames.Sector2_Main[2]: ExitData(
            logic=lambda world, state: (
                state.has_any([EventNames.Weapons[3], EventNames.Weapons[7]], world.player)
            )
        )
    },
    # Side Paths
    RegNames.Sector2_Side[0]: {},
    RegNames.Sector2_Side[1]: {
        RegNames.Sector2_Main[7]: ExitData()
    },
    RegNames.Sector2_Side[2]: {
        RegNames.Sector2_Side[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        )
    },
    RegNames.Sector2_Side[3]: {
        RegNames.Sector2_Side[4]: ExitData()
    },
    RegNames.Sector2_Side[4]: {},
    RegNames.Sector2_Side[5]: {},
    RegNames.Sector2_Poster: {},
    RegNames.Sector2_Super: {},
    # Sector 3
    # Main Path
    RegNames.Sector3_Main[0]: {
        RegNames.Sector3_Main[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        ),
        RegNames.Sector3_Side[0]: ExitData(),
        RegNames.Sector3_Side[2]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 1)
            )
        )
    },
    RegNames.Sector3_Main[1]: {
        RegNames.Sector3_Main[2]: ExitData(),
        RegNames.Sector3_Side[4]: ExitData(),
        RegNames.Sector3_Side[9]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 3)
            )
        )
    },
    RegNames.Sector3_Main[2]: {
        RegNames.Sector3_Main[3]: ExitData(),
        RegNames.Sector3_Side[10]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 1)
            )
        ),
        RegNames.Sector3_Super[0]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Weapons[14], world.player)
            )
        )
    },
    RegNames.Sector3_Main[3]: {
        RegNames.Sector3_Main[4]: ExitData(
            logic=lambda world, state: (
                world.options.end_goal.value != 3 or meets_goal_req(state, world)
            )
        ),
        RegNames.Sector3_Poster[0]: ExitData(
            logic=lambda world, state: (
                (can_rocket_boost(state, world) and
                 (has_stats(state, world, ItemNames.Stat_Strength, 3) or state.has(EventNames.Weapons[3], world.player))) or
                (state.has(ItemNames.Upgrade_Jump, world.player, 2) and
                 (state.has_any([EventNames.Weapons[11], EventNames.Weapons[10]], world.player)))
            )
        )
    },
    RegNames.Sector3_Main[4]: {},
    # Side Paths
    RegNames.Sector3_Side[0]: {
        RegNames.Sector3_Side[1]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 2)
            )
        )
    },
    RegNames.Sector3_Side[1]: {},
    RegNames.Sector3_Side[2]: {
        RegNames.Sector3_Side[3]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 1)
            )
        )
    },
    RegNames.Sector3_Side[3]: {},
    RegNames.Sector3_Side[4]: {
        RegNames.Sector3_Side[5]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 1)
            )
        ),
        RegNames.Sector3_Side[7]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 9)
            )
        )
    },
    RegNames.Sector3_Side[5]: {
        RegNames.Sector3_Side[6]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 1)
            )
        )
    },
    RegNames.Sector3_Side[6]: {},
    RegNames.Sector3_Side[7]: {
        RegNames.Sector3_Side[8]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 9)
            )
        )
    },
    RegNames.Sector3_Side[8]: {},
    RegNames.Sector3_Side[9]: {},
    RegNames.Sector3_Side[10]: {},
    RegNames.Sector3_Super[0]: {
        RegNames.Sector3_Super[1]: ExitData()
    },
    RegNames.Sector3_Super[1]: {},
    RegNames.Sector3_Poster[0]: {
        RegNames.Sector3_Poster[1]: ExitData()
    },
    RegNames.Sector3_Poster[1]: {},
    # Sector 4
    # Main Path
    RegNames.Sector4_Main[0]: {
        RegNames.Sector4_Main[1]: ExitData(),
        RegNames.Sector4_Super[0]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2) or

                (can_rocket_boost(state, world) and
                    (state.has(ItemNames.Upgrade_Jump, world.player, 1) or
                    world.options.logic_difficulty.value >= 1)) or

                has_stats(state, world, ItemNames.Stat_Strength, 3)
            )
        ),
        RegNames.Sector4_Side[0]: ExitData(
            logic=lambda world, state: (
                state.has_any([EventNames.Weapons[3], EventNames.Weapons[7]], world.player) and
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        )
    },
    RegNames.Sector4_Main[1]: {
        RegNames.Sector4_Main[2]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        ),
        RegNames.Sector4_Main[3]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Sector4_Terminals, world.player)
            )
        ),
        RegNames.Sector4_Side[2]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        ),
        RegNames.Sector4_Side[3]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 2)
            )
        )
    },
    RegNames.Sector4_Main[2]: {
        RegNames.Sector4_Super[1]: ExitData(
            logic=lambda world, state: (
                state.has_any([EventNames.Weapons[3], EventNames.Weapons[7]], world.player)
            )
        ),
        RegNames.Sector4_Side[4]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 5)
            )
        )
    },
    RegNames.Sector4_Main[3]: {
        RegNames.Sector4_Main[4]: ExitData(),
        RegNames.Sector4_Main[5]: ExitData(),
        RegNames.Sector4_Side[4]: ExitData(
            valid=lambda world: (
                world.options.logic_difficulty.value >= 1
            ),
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    RegNames.Sector4_Main[4]: {},
    RegNames.Sector4_Main[5]: {
        RegNames.Sector4_Main[6]: ExitData(),
        RegNames.Sector4_Main[7]: ExitData()
    },
    RegNames.Sector4_Main[6]: {
        RegNames.Sector4_Poster[0]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        )
    },
    RegNames.Sector4_Main[7]: {
        RegNames.Sector4_Main[8]: ExitData()
    },
    RegNames.Sector4_Main[8]: {},
    #Side Paths
    RegNames.Sector4_Side[0]: {
        RegNames.Sector4_Side[1]: ExitData()
    },
    RegNames.Sector4_Side[1]: {},
    RegNames.Sector4_Side[2]: {
        RegNames.Sector4_Main[3]: ExitData()
    },
    RegNames.Sector4_Side[3]: {},
    RegNames.Sector4_Side[4]: {
        RegNames.Sector4_Main[3]: ExitData()
    },
    RegNames.Sector4_Poster[0]: {
        RegNames.Sector4_Poster[1]: ExitData(
            logic=lambda world, state: (
                world.options.logic_difficulty.value >= 2 or
                (world.options.logic_difficulty.value >= 1 and
                has_stats(state, world, ItemNames.Stat_Strength, 3)) or
                state.has_any([EventNames.Weapons[3], EventNames.Weapons[7]], world.player)
            )
        )
    },
    RegNames.Sector4_Poster[1]: {},
    RegNames.Sector4_Super[0]: {
        RegNames.Sector4_Super[1]: ExitData()
    },
    RegNames.Sector4_Super[1]: {
        RegNames.Sector4_Super[2]: ExitData()
    },
    RegNames.Sector4_Super[2]: {},
    # Sector 5
    # Main Path
    RegNames.Sector5_Main[0]: {
        RegNames.Sector5_Main[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1) or
                (state.has(ItemNames.Stat_Health, world.player, 1) and
                state.has(EventNames.Weapons[4], world.player) and
                world.options.logic_difficulty.value >= 1 and
                has_enough_points(state, world, 10))
            )
        ),
        RegNames.Sector5_Side[0]: ExitData()
    },
    RegNames.Sector5_Main[1]: {
        RegNames.Sector5_Main[2]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        ),
        RegNames.Sector5_Side[2]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 1)
            )
        )
    },
    RegNames.Sector5_Main[2]: {
        RegNames.Sector5_Main[3]: ExitData(),
        RegNames.Sector5_Main[7]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2) or
                (world.options.logic_difficulty.value >= 4 and
                 state.has_all([EventNames.Weapons[12], ItemNames.Stat_Health], world.player) and
                 has_enough_points(state, world, 18))
            )
        ),
        RegNames.Sector5_Main[6]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Weapons[11], world.player)
            )
        ),
        RegNames.Sector5_Side[3]: ExitData(
            logic=lambda world, state: (
                state.has_any([EventNames.Weapons[3], EventNames.Weapons[7]], world.player) or
                has_stats(state, world, ItemNames.Stat_Strength, 6) or
                world.options.logic_difficulty.value >= 1
            )
        ),
        RegNames.Sector5_Side[4]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 4)
            )
        ),
        RegNames.Sector5_Side[5]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 2) or

                state.has(ItemNames.Upgrade_Jump, world.player, 2) or

                (world.options.logic_difficulty.value >= 2 and state.has(EventNames.Weapons[4], world.player) and
                 state.has(ItemNames.Stat_Health, world.player, 1) and has_enough_points(state, world, 10)) or

                (can_rocket_boost(state, world) and ((world.options.logic_difficulty.value >= 3 and
                 state.has(ItemNames.Stat_Strength, world.player, 5) and has_enough_points(state, world, 6)) or
                 world.options.logic_difficulty.value >= 4))
            )
        ),
        RegNames.Sector5_Poster[0]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2) or

                (world.options.logic_difficulty.value >= 2 and state.has(EventNames.Weapons[4], world.player) and
                 state.has(ItemNames.Stat_Health, world.player, 1) and has_enough_points(state, world, 10)) or

                (can_rocket_boost(state, world) and
                 ((world.options.logic_difficulty.value >= 3 and
                   state.has(ItemNames.Stat_Strength, world.player, 5) and has_enough_points(state, world, 6)) or
                 world.options.logic_difficulty.value >= 4))
            )
        ),
        RegNames.Sector5_Ribbon: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    RegNames.Sector5_Main[3]: {
        RegNames.Sector5_Main[4]: ExitData(),
        RegNames.Sector5_Main[6]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        ),
        RegNames.Sector5_Side[6]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 2)
            )
        )
    },
    RegNames.Sector5_Main[4]: {
        RegNames.Sector5_Main[5]: ExitData(),
        RegNames.Sector5_Side[7]: ExitData(),
        RegNames.Sector5_Side[8]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 3)
            )
        ),
        RegNames.Sector5_Side[9]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 3)
            )
        )
    },
    RegNames.Sector5_Main[5]: {
        RegNames.Sector5_Main[6]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    RegNames.Sector5_Main[6]: {
        RegNames.Sector5_Main[2]: ExitData(),
        RegNames.Sector5_Main[3]: ExitData(),
        RegNames.Sector5_Main[5]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    RegNames.Sector5_Main[7]: {
        RegNames.Sector5_Main[8]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2) and
                (world.options.end_goal.value != 5 or meets_goal_req(state, world))
            )
        )
    },
    RegNames.Sector5_Main[8]: {},
    # Side Paths
    RegNames.Sector5_Side[0]: {
        RegNames.Sector5_Side[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        )
    },
    RegNames.Sector5_Side[1]: {},
    RegNames.Sector5_Side[2]: {},
    RegNames.Sector5_Side[3]: {},
    RegNames.Sector5_Side[4]: {},
    RegNames.Sector5_Side[5]: {},
    RegNames.Sector5_Side[6]: {},
    RegNames.Sector5_Side[7]: {},
    RegNames.Sector5_Side[8]: {},
    RegNames.Sector5_Side[9]: {},
    RegNames.Sector5_Poster[0]: {
        RegNames.Sector5_Poster[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    RegNames.Sector5_Poster[1]: {
        RegNames.Sector5_Poster[2]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Weapons[12], world.player) or
                (world.options.logic_difficulty.value >= 2 and state.has(EventNames.Weapons[4], world.player))
            )
        )
    },
    RegNames.Sector5_Poster[2]: {},
    RegNames.Sector5_Ribbon: {},
    # Sector 6
    # Main Path
    RegNames.Sector6_Main[0]: {
        RegNames.Sector6_Main[1]: ExitData(),
        RegNames.Sector6_Side[0]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 2)
            )
        ),
        RegNames.Sector6_Side[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        )
    },
    RegNames.Sector6_Main[1]: {
        RegNames.Sector6_Main[2]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1) or 

                (world.options.logic_difficulty.value >= 1 and
                 can_mpfb_boost(state, world))
            )
        ),
        RegNames.Sector6_Side[4]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Sector6_Shredders, world.player)
            )
        ),
        RegNames.Sector6_Side[5]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Sector6_Shredders, world.player)
            )
        )
    },
    RegNames.Sector6_Main[2]: {
        RegNames.Sector6_Main[3]: ExitData(),
        RegNames.Sector6_Side[3]: ExitData()
    },
    RegNames.Sector6_Main[3]: {
        RegNames.Sector6_Main[4]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1) or 
               (world.options.logic_difficulty.value >= 2 and
                can_mpfb_boost(state, world))
            )
        )
    },
    RegNames.Sector6_Main[4]: {
        RegNames.Sector6_Main[5]: ExitData(),
        RegNames.Sector6_Side[6]: ExitData(),
        RegNames.Sector6_Side[7]: ExitData(),
        RegNames.Sector6_Side[14]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        ),
        RegNames.Sector6_Side[15]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 1)
            )
        ),
        RegNames.Sector6_Poster[0]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 3)
            )
        )
    },
    RegNames.Sector6_Main[5]: {
        RegNames.Sector6_Main[6]: ExitData()
    },
    RegNames.Sector6_Main[6]: {
        RegNames.Sector6_Main[7]: ExitData(),
        RegNames.Sector6_Main[12]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        ),
        RegNames.Sector6_Side[10]: ExitData(),
        RegNames.Sector6_Side[11]: ExitData(),
        RegNames.Sector6_Ribbon: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Sector6_Terminal_Ribbon, world.player)
            )
        ),
        RegNames.Sector6_Main[9]: ExitData(
            valid=lambda world: (
                world.options.logic_difficulty.value >= 4
            ),
            logic=lambda world, state: (
                can_mpfb_boost(state, world)
            )
        ),
        RegNames.Sector6_Super: ExitData(
            logic=lambda world, state: (
                can_reach_superchargesix(state, world)
            )
        )
    },
    RegNames.Sector6_Main[7]: {},
    RegNames.Sector6_Main[8]: {
        RegNames.Sector6_Main[9]: ExitData()
    },
    RegNames.Sector6_Main[9]: {
        RegNames.Sector6_Main[10]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        ),
        RegNames.Sector6_Side[12]: ExitData()
    },
    RegNames.Sector6_Main[10]: {
        RegNames.Sector6_Main[11]: ExitData()
    },
    RegNames.Sector6_Main[11]: {},
    RegNames.Sector6_Main[12]: {
        RegNames.Sector6_Main[8]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Sector6_Terminal_BlackOps, world.player) and
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    # Side Paths
    RegNames.Sector6_Side[0]: {},
    RegNames.Sector6_Side[1]: {
        RegNames.Sector6_Side[2]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    RegNames.Sector6_Side[2]: {},
    RegNames.Sector6_Side[3]: {},
    RegNames.Sector6_Side[4]: {},
    RegNames.Sector6_Side[5]: {
        RegNames.Sector6_Side[14]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 9)
            )
        )
    },
    RegNames.Sector6_Side[6]: {},
    RegNames.Sector6_Side[7]: {},
    RegNames.Sector6_Side[8]: {
        RegNames.Sector6_Side[9]: ExitData(),
        RegNames.Sector6_Poster[1]: ExitData(
            valid=lambda world: (
                world.options.logic_difficulty.value >= 1
            ),
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1) and can_rocket_boost(state, world)
            )
        )
    },
    RegNames.Sector6_Side[9]: {},
    RegNames.Sector6_Side[10]: {},
    RegNames.Sector6_Side[11]: {},
    RegNames.Sector6_Side[12]: {
        RegNames.Sector6_Side[13]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    RegNames.Sector6_Side[13]: {
        RegNames.Sector6_Side[12]: ExitData()
    },
    RegNames.Sector6_Side[14]: {
        RegNames.Sector6_Side[5]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 9)
            )
        ),
        RegNames.Sector6_Main[4]: ExitData()
    },
    RegNames.Sector6_Side[15]: {},
    RegNames.Sector6_Poster[0]: {
        RegNames.Sector6_Poster[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2) or
                (can_mpfb_boost(state, world) and world.options.logic_difficulty.value >= 2)
            )
        ),
        RegNames.Sector6_Side[8]: ExitData(
            valid=lambda world: (
                world.options.logic_difficulty.value >= 2 and
                world.options.debug_item.value >= 1
            ),
            logic=lambda world, state: (
                state.has(ItemNames.Debug, world.player) and
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        )
    },
    RegNames.Sector6_Poster[1]: {
        RegNames.Sector6_Poster[2]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Sector6_Terminal_Poster, world.player)
            )
        ),
        RegNames.Sector6_Side[8]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    RegNames.Sector6_Poster[2]: {
        RegNames.Sector6_Poster[3]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Weapons[16], world.player) and
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    RegNames.Sector6_Poster[3]: {},
    RegNames.Sector6_Super: {},
    RegNames.Sector6_Ribbon: {},
    # Sector 7
    # Main Path
    RegNames.Sector7_Main[0]: {
        RegNames.Sector7_Main[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        ),
        RegNames.Sector7_Side[0]: ExitData()
    },
    RegNames.Sector7_Main[1]: {
        RegNames.Sector7_Main[2]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        ),
        RegNames.Sector7_Side[1]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 5)
            )
        ),
        RegNames.Sector7_Side[2]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 2)
            )
        ),
        RegNames.Sector7_Side[3]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 7)
            )
        )
    },
    RegNames.Sector7_Main[2]: {
        RegNames.Sector7_Main[3]: ExitData(),
        RegNames.Sector7_Side[3]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Weapons[11], world.player) or
                (can_rocket_boost(state, world) and
                 world.options.logic_difficulty.value >= 1)
            )
        )
    },
    RegNames.Sector7_Main[3]: {
        RegNames.Sector7_Main[4]: ExitData(),
        RegNames.Sector7_Main[7]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Sector7_Terminal_CFIS, world.player)
            )
        ),
        RegNames.Sector7_Side[5]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Sector7_Terminal_CFIS, world.player)
            )
        ),
        RegNames.Sector7_Side[4]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 2)
            )
        )
    },
    RegNames.Sector7_Main[4]: {
        RegNames.Sector7_Main[5]: ExitData(),
        RegNames.Sector7_Main[6]: ExitData(
            valid=lambda world: (
                world.options.logic_difficulty.value >= 1 and
                world.options.debug_item.value >= 1
            ),
            logic=lambda world, state: (
                state.has_all([ItemNames.Debug, EventNames.Weapons[5]], world.player)
            )
        ),
        RegNames.Sector7_Side[7]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 7)
            )
        )
    },
    RegNames.Sector7_Main[5]: {
        RegNames.Sector7_Main[6]: ExitData(),
        RegNames.Sector7_Side[8]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 2)
            )
        ),
        RegNames.Sector7_Side[9]: ExitData()
    },
    RegNames.Sector7_Main[6]: {
        RegNames.Sector7_Side[10]: ExitData()
    },
    RegNames.Sector7_Main[7]: {
        RegNames.Sector7_Main[8]: ExitData(),
        RegNames.Sector7_Poster: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Weapons[8], world.player) and
                state.has(ItemNames.Stat_Attack, world.player, 2) and
                has_enough_points(state, world, 11) and
                (state.has(EventNames.Weapons[12], world.player) or
                (world.options.logic_difficulty.value >= 2 and
                state.has_all([ItemNames.Debug, EventNames.Weapons[3]], world.player)))
            )
        )
    },
    RegNames.Sector7_Main[8]: {
        RegNames.Sector7_Main[9]: ExitData()
    },
    RegNames.Sector7_Main[9]: {
        RegNames.Sector7_Main[10]: ExitData()
    },
    RegNames.Sector7_Main[10]: {
        RegNames.Sector7_Main[11]: ExitData(
            logic=lambda world, state: (
                world.options.end_goal.value != 7 or meets_goal_req(state, world)
            )
        ),
        RegNames.Sector7_Ribbon: ExitData(),
        RegNames.Sector7_Side[11]: ExitData(
            valid=lambda world: (
                world.options.debug_item.value >= 1
            ),
            logic=lambda world, state: (
                state.has_all([EventNames.Weapons[12], ItemNames.Debug], world.player)
            )
        ),
        RegNames.Sector7_Side[12]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 3)
            )
        ),
        RegNames.Sector7_Side[13]: ExitData(),
        RegNames.Sector7_Side[14]: ExitData(
            logic=lambda world, state: (
                state.has_any([EventNames.Weapons[3], EventNames.Weapons[7]], world.player)
            )
        )
    },
    RegNames.Sector7_Main[11]: {},
    # Side Paths
    RegNames.Sector7_Side[0]: {},
    RegNames.Sector7_Side[1]: {},
    RegNames.Sector7_Side[2]: {},
    RegNames.Sector7_Side[3]: {},
    RegNames.Sector7_Side[4]: {},
    RegNames.Sector7_Side[5]: {
        RegNames.Sector7_Side[6]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 2)
            )
        )
    },
    RegNames.Sector7_Side[6]: {},
    RegNames.Sector7_Side[7]: {},
    RegNames.Sector7_Side[8]: {},
    RegNames.Sector7_Side[9]: {},
    RegNames.Sector7_Side[10]: {},
    RegNames.Sector7_Side[11]: {},
    RegNames.Sector7_Side[12]: {},
    RegNames.Sector7_Side[13]: {},
    RegNames.Sector7_Side[14]: {},
    RegNames.Sector7_Poster: {},
    RegNames.Sector7_Ribbon: {},
    # Sector 8
    # Main Path
    RegNames.Sector8_Main[0]: {
        RegNames.Sector8_Main[1]: ExitData(),
        RegNames.Sector8_Side[0]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        )
    },
    RegNames.Sector8_Main[1]: {
        RegNames.Sector8_Main[2]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        ),
        RegNames.Sector8_Side[0]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        ),
        RegNames.Sector8_Side[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        ),
        RegNames.Sector8_Side[2]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 8)
            )
        )
    },
    RegNames.Sector8_Main[2]: {
        RegNames.Sector8_Main[3]: ExitData(),
        RegNames.Sector8_Side[3]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 4)
            )
        ),
        RegNames.Sector8_Poster: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Weapons[12], world.player) or can_rocket_boost(state, world)
            )
        )
    },
    RegNames.Sector8_Main[3]: {
        RegNames.Sector8_Side[4]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 7)
            )
        ),
        RegNames.Sector8_Side[5]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 4)
            )
        ),
        RegNames.Sector8_Side[6]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Stat_Strength, world.player, 2) and
                ((state.has(EventNames.Weapons[14], world.player) and
                 has_enough_points(state, world, 10)) or
                 (state.has_all([ItemNames.Debug, EventNames.Weapons[5]], world.player) and
                  has_enough_points(state, world, 2)))
            )
        )
    },
    # Side Paths
    RegNames.Sector8_Side[0]: {
        RegNames.Sector8_Side[1]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 3)
            )
        ),
        RegNames.Sector8_Main[1]: ExitData()
    },
    RegNames.Sector8_Side[1]: {},
    RegNames.Sector8_Side[2]: {},
    RegNames.Sector8_Side[3]: {},
    RegNames.Sector8_Side[4]: {},
    RegNames.Sector8_Side[5]: {},
    RegNames.Sector8_Side[6]: {},
    RegNames.Sector8_Poster: {},
    # Sector 9
    # Main Path
    RegNames.Sector9_Main[0]: {
        RegNames.Sector9_Main[1]: ExitData(),
        RegNames.Sector9_Side[0]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Weapons[12], world.player)
            )
        ),
        RegNames.Sector9_Side[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        ),
        RegNames.Sector9_Side[12]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1) or
                (can_mpfb_boost(state, world) and world.options.logic_difficulty.value >= 2)
            )
        )
    },
    RegNames.Sector9_Main[1]: {
        RegNames.Sector9_Main[2]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    RegNames.Sector9_Main[2]: {
        RegNames.Sector9_Main[3]: ExitData()
    },
    RegNames.Sector9_Main[3]: {
        RegNames.Sector9_Main[4]: ExitData(
            logic=lambda world, state: (
                state.has_all([EventNames.Sector9_Bulkhead[0], EventNames.Sector9_Bulkhead[1],
                               EventNames.Sector9_Bulkhead[2], EventNames.Sector9_Bulkhead[3]], world.player)
            )
        ),
        RegNames.Sector9_Bulkhead[0]: ExitData(),
        RegNames.Sector9_Bulkhead[1]: ExitData(),
        RegNames.Sector9_Bulkhead[2]: ExitData(),
        RegNames.Sector9_Bulkhead[3]: ExitData(),
        RegNames.Sector9_Side[2]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 5)
            )
        ),
        RegNames.Sector9_Side[13]: ExitData(
            logic=lambda world, state: (
                state.has_any([EventNames.Weapons[3], EventNames.Weapons[7]], world.player) or
                world.options.logic_difficulty.value >= 1
            )
        )
    },
    RegNames.Sector9_Main[4]: {
        RegNames.Sector9_Main[5]: ExitData(),
        RegNames.Sector9_Poster[0]: ExitData(),
        RegNames.Sector9_Side[5]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 4)
            )
        ),
        RegNames.Sector9_Side[14]: ExitData()
    },
    RegNames.Sector9_Main[5]: {
        RegNames.Sector9_Main[6]: ExitData()
    },
    RegNames.Sector9_Main[6]: {
        RegNames.Sector9_Main[7]: ExitData(),
        RegNames.Sector9_Side[4]: ExitData(),
        RegNames.Sector9_Side[6]: ExitData(),
        RegNames.Sector9_Side[15]: ExitData()
    },
    RegNames.Sector9_Main[7]: {
        RegNames.Sector9_Main[8]: ExitData()
    },
    RegNames.Sector9_Main[8]: {
        RegNames.Sector9_Side[8]: ExitData(),
        RegNames.Sector9_Side[7]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 4)
            )
        )
    },
    RegNames.Sector9_Main[9]: {
        RegNames.Sector9_Main[10]: ExitData(),
        RegNames.Sector9_Main[11]: ExitData(),
        RegNames.Sector9_Side[9]: ExitData()
    },
    RegNames.Sector9_Main[10]: {},
    RegNames.Sector9_Main[11]: {
        RegNames.Sector9_Main[12]: ExitData()
    },
    RegNames.Sector9_Main[12]: {
        RegNames.Sector9_Main[13]: ExitData()
    },
    RegNames.Sector9_Main[13]: {
        RegNames.Sector9_Main[14]: ExitData(
            logic=lambda world, state: (
                world.options.end_goal.value != 9 or meets_goal_req(state, world)
            )
        ),
        RegNames.Sector9_Deep[0]: ExitData(),
        RegNames.Sector9_Side[10]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Weapons[14], world.player) and
                state.has(ItemNames.Stat_Strength, world.player, 4) and
                has_enough_points(state, world, 14)
            )
        )
    },
    RegNames.Sector9_Main[14]: {},
    RegNames.Sector9_Bulkhead[0]: {
        RegNames.Sector9_Side[13]: ExitData()
    },
    RegNames.Sector9_Bulkhead[1]: {},
    RegNames.Sector9_Bulkhead[2]: {},
    RegNames.Sector9_Bulkhead[3]: {},
    # Side Paths
    RegNames.Sector9_Side[0]: {
        RegNames.Sector9_Side[1]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 2)
            )
        )
    },
    RegNames.Sector9_Side[1]: {
        RegNames.Sector9_Side[12]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 2)
            )
        )
    },
    RegNames.Sector9_Side[2]: {},
    RegNames.Sector9_Side[3]: {},
    RegNames.Sector9_Side[4]: {},
    RegNames.Sector9_Side[5]: {
        RegNames.Sector9_Main[6]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 8)
            )
        )
    },
    RegNames.Sector9_Side[6]: {
        RegNames.Sector9_Main[8]: ExitData()
    },
    RegNames.Sector9_Side[7]: {
        RegNames.Sector9_Side[8]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 8)
            )
        )
    },
    RegNames.Sector9_Side[8]: {
        RegNames.Sector9_Main[9]: ExitData()
    },
    RegNames.Sector9_Side[9]: {},
    RegNames.Sector9_Side[10]: {
        RegNames.Sector9_Side[11]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 4)
            )
        )
    },
    RegNames.Sector9_Side[11]: {},
    RegNames.Sector9_Side[12]: {
        RegNames.Sector9_Side[0]: ExitData()
    },
    RegNames.Sector9_Side[13]: {},
    RegNames.Sector9_Side[14]: {
        RegNames.Sector9_Main[6]: ExitData()
    },
    RegNames.Sector9_Side[15]: {
        RegNames.Sector9_Side[7]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 4)
            )
        )
    },
    RegNames.Sector9_Poster[0]: {
        RegNames.Sector9_Main[6]: ExitData(),
        RegNames.Sector9_Side[3]: ExitData(),
        RegNames.Sector9_Poster[1]: ExitData(
            logic=lambda world, state: (
                can_reach_poster_nine(state, world)
            )
        )
    },
    RegNames.Sector9_Poster[1]: {
        RegNames.Sector9_Poster[2]: ExitData()
    },
    RegNames.Sector9_Poster[2]: {
        RegNames.Sector9_Poster[3]: ExitData()
    },
    RegNames.Sector9_Poster[3]: {},
    RegNames.Sector9_Deep[0]: {
        RegNames.Sector9_Deep[1]: ExitData()
    },
    RegNames.Sector9_Deep[1]: {
        RegNames.Sector9_Deep[2]: ExitData()
    },
    RegNames.Sector9_Deep[2]: {
        RegNames.Sector9_Deep[3]: ExitData()
    },
    RegNames.Sector9_Deep[3]: {
        RegNames.Sector9_Deep[4]: ExitData()
    },
    RegNames.Sector9_Deep[4]: {
        RegNames.Sector9_Deep[5]: ExitData()
    },
    RegNames.Sector9_Deep[5]: {
        RegNames.Sector9_Deep[6]: ExitData()
    },
    RegNames.Sector9_Deep[6]: {
        RegNames.Sector9_Deep[7]: ExitData(),
        RegNames.Sector9_Deep[9]: ExitData()
    },
    RegNames.Sector9_Deep[7]: {
        RegNames.Sector9_Deep[8]: ExitData()
    },
    RegNames.Sector9_Deep[8]: {},
    RegNames.Sector9_Deep[9]: {},
    # Sector X
    # Main Path
    RegNames.SectorX_Main[0]: {
        RegNames.SectorX_Main[1]: ExitData()
    },
    RegNames.SectorX_Main[1]: {
        RegNames.SectorX_Main[2]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 1)
            )
        ),
        RegNames.SectorX_Poster[0]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Weapons[12], world.player) or
                (world.options.logic_difficulty.value >= 3 and
                state.has(ItemNames.Debug, world.player) and
                state.has_any([EventNames.Weapons[3], EventNames.Weapons[7]], world.player) and
                can_rocket_boost(state, world) and
                has_enough_points(state, world, 6))
            )
        ),
        RegNames.SectorX_Side[7]: ExitData()
    },
    RegNames.SectorX_Main[2]: {
        RegNames.SectorX_Main[3]: ExitData()
    },
    RegNames.SectorX_Main[3]: {
        RegNames.SectorX_Main[4]: ExitData()
    },
    RegNames.SectorX_Main[4]: {
        RegNames.SectorX_Core[0]: ExitData(),
        RegNames.SectorX_Main[7]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.SectorX_Megacore, world.player)
            )
        )
    },
    RegNames.SectorX_Main[5]: {
        RegNames.SectorX_Main[6]: ExitData()
    },
    RegNames.SectorX_Main[6]: {},
    RegNames.SectorX_Main[7]: {
        RegNames.SectorX_Main[8]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        ),
        RegNames.SectorX_Main[9]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Sector8_Terminal_AnnihilatorBeta, world.player)
            )
        ),
        RegNames.SectorX_Main[12]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 5)
            )
        )
    },
    RegNames.SectorX_Main[8]: {
        RegNames.SectorX_Main[12]: ExitData(),
        RegNames.SectorX_Side[1]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 6)
            )
        )
    },
    RegNames.SectorX_Main[9]: {
        RegNames.SectorX_Main[10]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    RegNames.SectorX_Main[10]: {
        RegNames.SectorX_Main[11]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 9)
            )
        ),
        RegNames.SectorX_Side[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    RegNames.SectorX_Main[11]: {
        RegNames.SectorX_Final[0]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2) or
                (state.has(ItemNames.Debug, world.player) and world.options.logic_difficulty.value >= 3 and
                 state.has_any([EventNames.Weapons[3], EventNames.Weapons[7]], world.player) and
                 can_rocket_boost(state, world) and has_enough_points(state, world, 6))
            )
        )
    },
    RegNames.SectorX_Main[12]: {
        RegNames.SectorX_Main[9]: ExitData(),
        RegNames.SectorX_Main[10]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 7)
            )
        )
    },
    RegNames.SectorX_Core[0]: {
        RegNames.SectorX_Core[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        ),
        RegNames.SectorX_Core[4]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        ),
        RegNames.SectorX_Main[5]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.SectorX_Megacore, world.player)
            )
        )
    },
    RegNames.SectorX_Core[1]: {
        RegNames.SectorX_Core[2]: ExitData(),
        RegNames.SectorX_Core[3]: ExitData()
    },
    RegNames.SectorX_Core[2]: {},
    RegNames.SectorX_Core[3]: {},
    RegNames.SectorX_Core[4]: {
        RegNames.SectorX_Core[5]: ExitData(),
        RegNames.SectorX_Side[0]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Strength, 6)
            )
        )
    },
    RegNames.SectorX_Core[5]: {
        RegNames.SectorX_Core[6]: ExitData()
    },
    RegNames.SectorX_Core[6]: {
        RegNames.SectorX_Core[7]: ExitData()
    },
    RegNames.SectorX_Core[7]: {
        RegNames.SectorX_Core[8]: ExitData()
    },
    RegNames.SectorX_Core[8]: {},
    RegNames.SectorX_Final[0]: {
        RegNames.SectorX_Final[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2) or
                (world.options.logic_difficulty.value >= 3 and can_mpfb_boost(state, world))
            )
        ),
        RegNames.SectorX_Side[2]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 9)
            )
        ),
        RegNames.SectorX_Side[3]: ExitData(
            logic=lambda world, state: (
                has_stats(state, world, ItemNames.Stat_Crack, 9)
            )
        )
    },
    RegNames.SectorX_Final[1]: {
        RegNames.SectorX_Final[2]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2) or
                (world.options.logic_difficulty.value >= 3 and can_mpfb_boost(state, world) and
                 state.has(ItemNames.Stat_Health, world.player, 3) and has_enough_points(state, world, 12))
           )
       )
   },
    RegNames.SectorX_Final[2]: {
        RegNames.SectorX_Final[3]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        ),
        RegNames.SectorX_Side[4]: ExitData(),
        RegNames.SectorX_Side[5]: ExitData()
    },
    RegNames.SectorX_Final[3]: {
        RegNames.SectorX_Final[4]: ExitData()
    },
    RegNames.SectorX_Final[4]: {
        RegNames.SectorX_Final[5]: ExitData(),
        RegNames.SectorX_Side[6]: ExitData()
    },
    RegNames.SectorX_Final[5]: {
        RegNames.SectorX_Final[6]: ExitData(
            logic=lambda world, state: (
                world.options.end_goal.value != 10 or meets_goal_req(state, world)
            )
        )
    },
    RegNames.SectorX_Final[6]: {
        RegNames.SectorY: ExitData(
            valid=lambda world: (
                (world.options.end_goal.value == 12 or world.options.allow_sector_z.value & 2 == 2)
            ),
            logic=lambda world, state: (
                state.has(EventNames.Weapons[0], world.player)
            )
        )
    },
    # Side Paths
    RegNames.SectorX_Side[0]: {},
    RegNames.SectorX_Side[1]: {
        RegNames.SectorX_Main[10]: ExitData(),
        RegNames.SectorX_Main[11]: ExitData()
    },
    RegNames.SectorX_Side[2]: {
        RegNames.SectorX_Final[1]: ExitData()
    },
    RegNames.SectorX_Side[3]: {
        RegNames.SectorX_Final[1]: ExitData()
    },
    RegNames.SectorX_Side[4]: {},
    RegNames.SectorX_Side[5]: {},
    RegNames.SectorX_Side[6]: {},
    RegNames.SectorX_Side[7]: {},
    RegNames.SectorX_Poster[0]: {
        RegNames.SectorX_Poster[1]: ExitData(
            logic=lambda world, state: (
                state.has(ItemNames.Upgrade_Jump, world.player, 2)
            )
        )
    },
    RegNames.SectorX_Poster[1]: {
        RegNames.SectorX_Poster[2]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Weapons[10], world.player) or
                state.has(ItemNames.Debug, world.player)
            )
        )
    },
    RegNames.SectorX_Poster[2]: {
        RegNames.SectorX_Poster[3]: ExitData(
            logic=lambda world, state: (
                state.has(EventNames.Weapons[12], world.player) or
                (world.options.logic_difficulty.value >= 3 and
                 state.has(ItemNames.Debug, world.player) and
                 state.has_any([EventNames.Weapons[3], EventNames.Weapons[7]], world.player) and
                 can_rocket_boost(state, world)) and
                 has_enough_points(state, world, 6)
             )
        )
    },
    RegNames.SectorX_Poster[3]: {
        RegNames.SectorX_Core[0]: ExitData(),
        RegNames.SectorX_Core[6]: ExitData()
    },
    RegNames.SectorX_Super: {},
    # Sector Y
    RegNames.SectorY: {}
}