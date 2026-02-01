from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING
from BaseClasses import CollectionState
from ..Rules import can_destroy_sentinel_proxima, can_kill_annihilators, has_stats, has_weapon_stats, has_xp, \
    can_make_weapon, has_weapon_plus_points, can_kill_yukabacera
from ..Names import LocNames, RegNames, ItemNames, EventNames
from ..Valid import could_destroy_sentinel_proxima, enemy_is_valid

if TYPE_CHECKING:
    from .. import IjiWorld

class IjiLocData(NamedTuple):
    region: str
    code: Optional[int] = None
    valid: Callable[["IjiWorld"], bool] = lambda world: True
    logic: Callable[["IjiWorld", CollectionState], bool] = lambda world, state: True
    locked_item: Callable[["IjiWorld"], str] = lambda world: None
    on_added: Callable[["IjiWorld"], None] = lambda world: None

locations_sector_complete: Dict[str,IjiLocData] = {
    LocNames.Sector_Complete[i]: IjiLocData(
        code=i+1, region=RegNames.Sector_Ends[i],
        valid=lambda world,temp_i=i: world.options.end_goal.value != temp_i+1
    ) for i in range(len(LocNames.Sector_Complete))
}

locations_checkpoints: Dict[str, IjiLocData] = {
    LocNames.Checkpoints[i]: IjiLocData(
        code=13+i, region=RegNames.Sector_Checkpoints[i]
    ) for i in range(len(RegNames.Sector_Checkpoints))
}

locations_level_up: Dict[str, IjiLocData] = {
    LocNames.Levels[i][j]: IjiLocData(
        code=100+(i*5)+j+1, region = RegNames.Sector_Globals[i],
        valid = lambda world,level=j+1: world.options.game_difficulty.levels_per_sector() >= level,
        logic = lambda world,state,sector=i+1,level=j+1: has_xp(state,world,sector,level),
        on_added = lambda world: world.add_max_stats(ItemNames.Supercharge, 1) if (
            world.options.levelsanity) else None
    ) for i in range(10) for j in range(5)
}

locations_stat_levels: Dict[str, IjiLocData] = {
    LocNames.Stat_Levels[i][j]: IjiLocData(
        code = 400+(i*10)+j, region = RegNames.Global,
        valid = (
            lambda world: False) if j == 0 else (
            lambda world,stat=i,items=j: (world.current_stat_items[ItemNames.Stats[stat]] < items)),
        logic = lambda world, state,stat=i,items=j: has_stats(world,ItemNames.Stats[stat],items)
    ) for i in range(7) for j in range(10)
} | {
    LocNames.Stat_Levels[i][10]: IjiLocData(
        code = 470+i, region = RegNames.Global,
        valid = lambda world: world.options.special_trait_items,
        logic = (
            lambda world, state, stat=i: (has_stats(world,ItemNames.Stats[stat],
                                                    world.max_stats[ItemNames.Stats[stat]]))
        )
    ) for i in range(7)
}

locations_poster: Dict[str, IjiLocData] = {
    LocNames.Posters[i]: IjiLocData(
        code=200+i+1, region = RegNames.Sector_Posters[i],
        valid = lambda world: world.options.poster_locations
    ) for i in range(10)
} | {
    LocNames.Posters[10]: IjiLocData(
        code=211, region = RegNames.Sector_Posters[10],
        valid = lambda world: world.options.poster_locations,
        on_added = lambda world: (
            world.increment_post_goal_locations() if (
                    world.options.end_goal.value >= 11 or
                    world.options.allow_sector_z.has_requirement()
            ) else None
        )
    ),
    LocNames.Posters[11]: IjiLocData(
        code=212,region = RegNames.Sector_Posters[11],
        valid = lambda world: world.options.poster_locations,
        on_added = lambda world: world.increment_post_goal_locations()
    )
}

locations_ribbon: Dict[str, IjiLocData] = {
    LocNames.Ribbons[i]: IjiLocData(
        code=220+i+1, region=RegNames.Sector_Ribbons[i]
    ) for i in range(10)
}

locations_supercharge: Dict[str,IjiLocData] = {
    LocNames.Supercharges[0]: IjiLocData(
        code=231, region=RegNames.Sector1_Super,
        valid=lambda world: world.options.supercharge_locations.has_locations(),
        on_added=lambda world: world.add_max_stats(ItemNames.Supercharge, 1) if (
            not world.options.supercharge_locations.awards_points()) else None
    ),
    LocNames.Supercharges[1]: IjiLocData(
        code=232, region=RegNames.Sector2_Super,
        valid=lambda world: world.options.supercharge_locations.has_locations(),
        on_added=lambda world: world.add_max_stats(ItemNames.Supercharge, 1) if (
            not world.options.supercharge_locations.awards_points()) else None
    ),
    LocNames.Supercharges[2]: IjiLocData(
        code=233, region=RegNames.Sector3_Super[1],
        valid=lambda world: world.options.supercharge_locations.has_locations(),
        on_added=lambda world: world.add_max_stats(ItemNames.Supercharge, 1) if (
            not world.options.supercharge_locations.awards_points()) else None
    ),
    LocNames.Supercharges[3]: IjiLocData(
        code=234, region=RegNames.Sector4_Super[2],
        valid=lambda world: world.options.supercharge_locations.has_locations(),
        on_added=lambda world: world.add_max_stats(ItemNames.Supercharge, 1) if (
            not world.options.supercharge_locations.awards_points()) else None
    ),
    LocNames.Supercharges[4]: IjiLocData(
        code=235, region=RegNames.Sector5_Main[8],
        valid=lambda world: world.options.supercharge_locations.has_locations(),
        logic=lambda world, state: state.has(EventNames.Weapons[12], world.player),
        on_added=lambda world: world.increment_post_goal_locations() if (
                world.options.end_goal.value == 5) else world.add_max_stats(ItemNames.Supercharge, 1) if (
            not world.options.supercharge_locations.awards_points()
        ) else None
    ),
    LocNames.Supercharges[5]: IjiLocData(
        code=236, region=RegNames.Sector6_Super,
        valid=lambda world: world.options.supercharge_locations.has_locations(),
        on_added=lambda world: world.add_max_stats(ItemNames.Supercharge, 1) if (
            not world.options.supercharge_locations.awards_points()) else None
    ),
    LocNames.Supercharges[6]: IjiLocData(
        code=237, region=RegNames.Sector7_Main[11],
        valid=lambda world: (
                world.options.supercharge_locations.has_locations() and
                could_destroy_sentinel_proxima(world)
        ),
        logic=lambda world, state: can_destroy_sentinel_proxima(state, world),
        on_added=lambda world: world.increment_post_goal_locations() if (
                world.options.end_goal.value == 7) else world.add_max_stats(ItemNames.Supercharge, 1) if (
            not world.options.supercharge_locations.awards_points()
        ) else None
    ),
    LocNames.Supercharges[7]: IjiLocData(
        code=238, region=RegNames.Sector8_Side[3],
        valid=lambda world: world.options.supercharge_locations.has_locations(),
        logic=lambda world, state: can_kill_annihilators(state, world),
        on_added=lambda world: world.add_max_stats(ItemNames.Supercharge, 1) if (
            not world.options.supercharge_locations.awards_points()) else None
    ),
    LocNames.Supercharges[8]: IjiLocData(
        code=239, region=RegNames.Sector9_Deep[9],
        valid=lambda world: world.options.supercharge_locations.has_locations(),
        on_added=lambda world: world.add_max_stats(ItemNames.Supercharge, 1) if (
            not world.options.supercharge_locations.awards_points()) else None
    ),
    LocNames.Supercharges[9]: IjiLocData(
        code=240, region=RegNames.SectorX_Core[0],
        valid=lambda world: world.options.supercharge_locations.has_locations(),
        logic=lambda world, state: (
            state.has(EventNames.SectorX_Megacore, world.player) and
            has_weapon_plus_points(state, world, 16, 0)),
        on_added=lambda world: world.add_max_stats(ItemNames.Supercharge, 1) if (
            not world.options.supercharge_locations.awards_points()) else None
    )
}

locations_upgrades: Dict[str, IjiLocData] = {
    LocNames.Upgrades_Jump[0]: IjiLocData(
        code=261, region=RegNames.Sector2_Main[3],
        locked_item=lambda world: (
            ItemNames.Upgrade_Jump if world.options.jump_upgrades.value == 0 else None
        )
    ),
    LocNames.Upgrades_Armor[0]: IjiLocData(
        code=262, region=RegNames.Sector3_Main[1],
        locked_item=lambda world: (
            ItemNames.Upgrade_Armor if (world.options.armor_upgrades.value & 1) == 0 else None
        )
    ),
    LocNames.Upgrades_Jump[1]:  IjiLocData(
        code=263, region=RegNames.Sector5_Main[5],
        locked_item=lambda world: (
            ItemNames.Upgrade_Jump if world.options.jump_upgrades.value == 0 else None
        )
    ),
    LocNames.Upgrades_Armor[1]: IjiLocData(
        code=264, region=RegNames.Sector7_Main[3],
        locked_item=lambda world: (
            ItemNames.Upgrade_Armor if (world.options.armor_upgrades.value & 1) == 0 else None
        )
    ),
    LocNames.Upgrades_Armor[2]: IjiLocData(
        code=265, region=RegNames.Sector8_Main[3],
        locked_item=lambda world: (
            ItemNames.Upgrade_Armor if (world.options.armor_upgrades.value & 1) == 0 else None
        )
    ),
    LocNames.Upgrades_Armor[3]: IjiLocData(
        code=266, region=RegNames.Sector9_Main[4],
        locked_item=lambda world: (
            ItemNames.Upgrade_Armor if (world.options.armor_upgrades.value & 1) == 0 else None
        )
    ),
    LocNames.Upgrades_Armor[4]: IjiLocData(
        code=267, region=RegNames.SectorX_Core[2],
        locked_item=lambda world: (
            ItemNames.Upgrade_Armor if (world.options.armor_upgrades.value & 1) == 0 else None
        )
    )
}

locations_unique_basic_weapons: Dict[str, IjiLocData] = {
    LocNames.Weapons_First[0]: IjiLocData(
        code=241, region=RegNames.Global,
        valid=lambda world: world.options.basic_weapon_locations.value == 1,
        logic=lambda world, state: state.has(EventNames.Weapons[2], world.player)
    ),
    LocNames.Weapons_First[1]: IjiLocData(
        code=242, region=RegNames.Global,
        valid=lambda world: world.options.basic_weapon_locations.value == 1,
        logic=lambda world, state: state.has(EventNames.Weapons[3], world.player)
    ),
    LocNames.Weapons_First[2]: IjiLocData(
        code=243, region=RegNames.Global,
        valid=lambda world: (
            world.options.basic_weapon_locations.value == 1 and
            world.options.end_goal.value >= 5
        ),
        logic=lambda world, state: state.has(EventNames.Weapons[4], world.player)
    ),
    LocNames.Weapons_First[3]: IjiLocData(
        code=244, region=RegNames.Global,
        valid=lambda world: world.options.basic_weapon_locations.value == 1,
        logic=lambda world, state: state.has(EventNames.Weapons[5], world.player)
    ),
    LocNames.Weapons_First[4]: IjiLocData(
        code=245, region=RegNames.Global,
        valid=lambda world: world.options.basic_weapon_locations.value == 1,
        logic=lambda world, state: state.has(EventNames.Weapons[6], world.player)
    ),
    LocNames.Weapons_First[5]: IjiLocData(
        code=246, region=RegNames.Global,
        valid=lambda world: (
            world.options.basic_weapon_locations.value == 1 and
            world.options.end_goal.value >= 5
        ),
        logic=lambda world, state: state.has(EventNames.Weapons[7], world.player)
    ),
    LocNames.Weapons_First[6]: IjiLocData(
        code=247, region=RegNames.Global,
        valid=lambda world: (
            world.options.basic_weapon_locations.value == 1 and
            world.options.end_goal.value >= 7
        ),
        logic=lambda world, state: state.has(EventNames.Weapons[8], world.player)
    )
}

locations_uniquespecialweapons: Dict[str, IjiLocData] = {
    LocNames.Weapon_Banana: IjiLocData(
        code=248, region=RegNames.Sector9_Poster[3],
        valid=lambda world: True,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[17],world)
    ),
    LocNames.Weapon_Massacre: IjiLocData(
        code=249, region=RegNames.SectorX_Final[6],
        valid=lambda world: False,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[18],world)
    ),
    LocNames.Weapon_Null: IjiLocData(
        code=250, region=RegNames.SectorZ_Null,
        valid=lambda world: True,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[0],world),
        on_added=lambda world: world.increment_post_goal_locations() if (
            world.options.allow_sector_z.is_post_game(world)) else None
    )
}

locations_combinedweapons: Dict[str,IjiLocData] = {
    LocNames.Weapons_Combined[0]: IjiLocData(
        code=251, region=RegNames.Global,
        logic=lambda world, state: can_make_weapon(state, world, ItemNames.Weapons[9])
    ),
    LocNames.Weapons_Combined[1]: IjiLocData(
        code=252, region=RegNames.Global,
        valid=lambda world: world.options.end_goal.value >= 5,
        logic=lambda world, state: can_make_weapon(state, world, ItemNames.Weapons[10])
    ),
    LocNames.Weapons_Combined[2]: IjiLocData(
        code=253, region=RegNames.Global,
        logic=lambda world, state: can_make_weapon(state, world, ItemNames.Weapons[11])
    ),
    LocNames.Weapons_Combined[3]: IjiLocData(
        code=254, region=RegNames.Global,
        valid=lambda world: world.options.end_goal.value >= 5,
        logic=lambda world, state: can_make_weapon(state, world, ItemNames.Weapons[12])
    ),
    LocNames.Weapons_Combined[4]: IjiLocData(
        code=255, region=RegNames.Global,
        logic=lambda world, state: (
            can_make_weapon(state, world, ItemNames.Weapons[13]) or
            state.has(EventNames.Weapons[13], world.player)
        )
    ),
    LocNames.Weapons_Combined[5]: IjiLocData(
        code=256, region=RegNames.Global,
        logic=lambda world, state: can_make_weapon(state, world, ItemNames.Weapons[14])
    ),
    LocNames.Weapons_Combined[6]: IjiLocData(
        code=257, region=RegNames.Global,
        valid=lambda world: world.options.end_goal.value >= 5,
        logic=lambda world, state: can_make_weapon(state, world, ItemNames.Weapons[15])
    ),
    LocNames.Weapons_Combined[7]: IjiLocData(
        code=258, region=RegNames.Global,
        valid=lambda world: world.options.end_goal.value >= 7,
        logic=lambda world, state: can_make_weapon(state, world, ItemNames.Weapons[16])
    )
}

locations_sector_weapons: Dict[str, IjiLocData] = {
    LocNames.Weapons_Per_Sector[0][0]: IjiLocData(
        code=311, region=RegNames.Sector1_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state, ItemNames.Weapons[2], world)
    ),
    LocNames.Weapons_Per_Sector[1][0]: IjiLocData(
        code=321, region=RegNames.Sector2_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state, ItemNames.Weapons[2], world)
    ),
    LocNames.Weapons_Per_Sector[1][1]: IjiLocData(
        code=322, region=RegNames.Sector2_Side[1],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state, ItemNames.Weapons[3], world)
    ),
    LocNames.Weapons_Per_Sector[1][2]: IjiLocData(
        code=324, region=RegNames.Sector2_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state, ItemNames.Weapons[5], world)
    ),
    LocNames.Weapons_Per_Sector[2][0]: IjiLocData(
        code=331, region=RegNames.Sector3_Main[0],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state, ItemNames.Weapons[2], world)
    ),
    LocNames.Weapons_Per_Sector[2][1]: IjiLocData(
        code=332, region=RegNames.Sector3_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state, ItemNames.Weapons[3], world)
    ),
    LocNames.Weapons_Per_Sector[2][2]: IjiLocData(
        code=334, region=RegNames.Sector3_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state, ItemNames.Weapons[5], world)
    ),
    LocNames.Weapons_Per_Sector[2][3]: IjiLocData(
        code=335, region=RegNames.Sector3_Side[10],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state, ItemNames.Weapons[6], world)
    ),
    LocNames.Weapons_Per_Sector[3][0]: IjiLocData(
        code=341, region=RegNames.Sector4_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state, ItemNames.Weapons[2], world)
    ),
    LocNames.Weapons_Per_Sector[3][1]: IjiLocData(
        code=342, region=RegNames.Sector4_Main[0],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_Per_Sector[3][2]: IjiLocData(
        code=343, region=RegNames.Sector4_Super[2],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state, ItemNames.Weapons[4], world)
    ),
    LocNames.Weapons_Per_Sector[3][3]: IjiLocData(
        code=344, region=RegNames.Sector4_Main[0],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_Per_Sector[3][4]: IjiLocData(
        code=345, region=RegNames.Sector4_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_Per_Sector[4][0]: IjiLocData(
        code=351, region=RegNames.Sector5_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_Per_Sector[4][1]: IjiLocData(
        code=352, region=RegNames.Sector5_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_Per_Sector[4][2]: IjiLocData(
        code=353, region=RegNames.Sector5_Main[6],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_Per_Sector[4][3]: IjiLocData(
        code=354, region=RegNames.Sector5_Ribbon,
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_Per_Sector[4][4]: IjiLocData(
        code=355, region=RegNames.Sector5_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_Per_Sector[4][5]: IjiLocData(
        code=356, region=RegNames.Sector5_Side[5],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_Per_Sector[5][0]: IjiLocData(
        code=361, region=RegNames.Sector6_Main[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_Per_Sector[5][1]: IjiLocData(
        code=362, region=RegNames.Sector6_Main[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_Per_Sector[5][2]: IjiLocData(
        code=363, region=RegNames.Sector6_Side[10],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_Per_Sector[5][3]: IjiLocData(
        code=364, region=RegNames.Sector6_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_Per_Sector[5][4]: IjiLocData(
        code=365, region=RegNames.Sector6_Main[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_Per_Sector[5][5]: IjiLocData(
        code=366, region=RegNames.Sector6_Side[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_Per_Sector[5][6]: IjiLocData(
        code=367, region=RegNames.Sector6_Side[9],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state, ItemNames.Weapons[8], world)
    ),
    LocNames.Weapons_Per_Sector[6][0]: IjiLocData(
        code=371, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_Per_Sector[6][1]: IjiLocData(
        code=372, region=RegNames.Sector7_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_Per_Sector[6][2]: IjiLocData(
        code=373, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_Per_Sector[6][3]: IjiLocData(
        code=374, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_Per_Sector[6][4]: IjiLocData(
        code=375, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_Per_Sector[6][5]: IjiLocData(
        code=376, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_Per_Sector[6][6]: IjiLocData(
        code=377, region=RegNames.Sector7_Side[6],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[8],world)
    ),
    LocNames.Weapons_Per_Sector[7][0]: IjiLocData(
        code=381, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_Per_Sector[7][1]: IjiLocData(
        code=382, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_Per_Sector[7][2]: IjiLocData(
        code=383, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_Per_Sector[7][3]: IjiLocData(
        code=384, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_Per_Sector[7][4]: IjiLocData(
        code=385, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_Per_Sector[7][5]: IjiLocData(
        code=386, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_Per_Sector[7][6]: IjiLocData(
        code=387, region=RegNames.Sector8_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[8],world)
    ),
    LocNames.Weapons_Per_Sector[8][0]: IjiLocData(
        code=391, region=RegNames.Sector9_Side[0],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_Per_Sector[8][1]: IjiLocData(
        code=392, region=RegNames.Sector9_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_Per_Sector[8][2]: IjiLocData(
        code=393, region=RegNames.Sector9_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_Per_Sector[8][3]: IjiLocData(
        code=394, region=RegNames.Sector9_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_Per_Sector[8][4]: IjiLocData(
        code=395, region=RegNames.Sector9_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_Per_Sector[8][5]: IjiLocData(
        code=396, region=RegNames.Sector9_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_Per_Sector[8][6]: IjiLocData(
        code=397, region=RegNames.Sector9_Main[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[8],world)
    ),
    LocNames.Weapons_Per_Sector[9][0]: IjiLocData(
        code=301, region=RegNames.SectorX_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_Per_Sector[9][1]: IjiLocData(
        code=302, region=RegNames.SectorX_Core[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_Per_Sector[9][2]: IjiLocData(
        code=303, region=RegNames.SectorX_Core[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_Per_Sector[9][3]: IjiLocData(
        code=304, region=RegNames.SectorX_Core[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_Per_Sector[9][4]: IjiLocData(
        code=305, region=RegNames.SectorX_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_Per_Sector[9][5]: IjiLocData(
        code=306, region=RegNames.SectorX_Main[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_Per_Sector[9][6]: IjiLocData(
        code=307, region=RegNames.SectorX_Core[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 2,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[8],world)
    ),
    LocNames.Weapons_Per_Sector[9][7]: IjiLocData(
        code=308, region=RegNames.SectorX_Final[3],
        valid=lambda world: world.options.basic_weapon_locations.value >= 2)
}

locations_allbasicweapons: Dict[str, IjiLocData] = {
    LocNames.Weapons_All_Instances[0][0][0]: IjiLocData(
        code=3311, region=RegNames.Sector3_Main[0],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[0][0][1]: IjiLocData(
        code=3312, region=RegNames.Sector3_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[0][0][2]: IjiLocData(
        code=3313, region=RegNames.Sector3_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[0][1][0]: IjiLocData(
        code=3321, region=RegNames.Sector3_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[0][1][1]: IjiLocData(
        code=3322, region=RegNames.Sector3_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[1][0][0]: IjiLocData(
        code=3421, region=RegNames.Sector4_Main[0],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[1][0][1]: IjiLocData(
        code=3422, region=RegNames.Sector4_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[2][0][0]: IjiLocData(
        code=3511, region=RegNames.Sector5_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[2][0][1]: IjiLocData(
        code=3512, region=RegNames.Sector5_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[2][1][0]: IjiLocData(
        code=3521, region=RegNames.Sector5_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[2][1][1]: IjiLocData(
        code=3522, region=RegNames.Sector5_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[2][2][0]: IjiLocData(
        code=3551, region=RegNames.Sector5_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[2][2][1]: IjiLocData(
        code=3552, region=RegNames.Sector5_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[2][2][2]: IjiLocData(
        code=3553, region=RegNames.Sector5_Ribbon,
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[3][0][0]: IjiLocData(
        code=3611, region=RegNames.Sector6_Main[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[3][0][1]: IjiLocData(
        code=3612, region=RegNames.Sector6_Main[6],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[3][1][0]: IjiLocData(
        code=3621, region=RegNames.Sector6_Main[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[3][1][1]: IjiLocData(
        code=3622, region=RegNames.Sector6_Main[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[3][1][2]: IjiLocData(
        code=3623, region=RegNames.Sector6_Ribbon,
        valid=lambda world: world.options.basic_weapon_locations.value== 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[3][2][0]: IjiLocData(
        code=3631, region=RegNames.Sector6_Side[10],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_All_Instances[3][2][1]: IjiLocData(
        code=3632, region=RegNames.Sector6_Poster[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state, ItemNames.Weapons[4], world)
    ),
    LocNames.Weapons_All_Instances[3][3][0]: IjiLocData(
        code=3651, region=RegNames.Sector6_Main[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[3][3][1]: IjiLocData(
        code=3652, region=RegNames.Sector6_Ribbon,
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[3][4][0]: IjiLocData(
        code=3661, region=RegNames.Sector6_Side[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[3][4][1]: IjiLocData(
        code=3662, region=RegNames.Sector6_Side[6],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[3][4][2]: IjiLocData(
        code=3663, region=RegNames.Sector6_Ribbon,
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[4][0][0]: IjiLocData(
        code=3721, region=RegNames.Sector7_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[4][0][1]: IjiLocData(
        code=3722, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[4][0][2]: IjiLocData(
        code=3723, region=RegNames.Sector7_Main[10],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[4][1][0]: IjiLocData(
        code=3741, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_All_Instances[4][1][1]: IjiLocData(
        code=3742, region=RegNames.Sector7_Side[10],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_All_Instances[4][2][0]: IjiLocData(
        code=3751, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[4][2][1]: IjiLocData(
        code=3752, region=RegNames.Sector7_Ribbon,
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[4][3][0]: IjiLocData(
        code=3761, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[4][3][1]: IjiLocData(
        code=3762, region=RegNames.Sector7_Side[10],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[4][3][2]: IjiLocData(
        code=3763, region=RegNames.Sector7_Ribbon,
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[5][0][0]: IjiLocData(
        code=3821, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[5][0][1]: IjiLocData(
        code=3822, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[5][0][2]: IjiLocData(
        code=3823, region=RegNames.Sector8_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[5][1][0]: IjiLocData(
        code=3851, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[5][1][1]: IjiLocData(
        code=3852, region=RegNames.Sector8_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[5][2][0]: IjiLocData(
        code=3861, region=RegNames.Sector8_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[5][2][1]: IjiLocData(
        code=3862, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[6][0][0]: IjiLocData(
        code=3911, region=RegNames.Sector9_Side[0],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[6][0][1]: IjiLocData(
        code=3912, region=RegNames.Sector9_Main[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[6][0][2]: IjiLocData(
        code=3913, region=RegNames.Sector9_Main[13],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[6][0][3]: IjiLocData(
        code=3914, region=RegNames.Sector9_Poster[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[6][1][0]: IjiLocData(
        code=3921, region=RegNames.Sector9_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)),
    LocNames.Weapons_All_Instances[6][1][1]: IjiLocData(
        code=3922, region=RegNames.Sector9_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[6][1][2]: IjiLocData(
        code=3923, region=RegNames.Sector9_Main[6],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[6][1][3]: IjiLocData(
        code=3924, region=RegNames.Sector9_Main[13],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[6][1][4]: IjiLocData(
        code=3925, region=RegNames.Sector9_Poster[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[6][2][0]: IjiLocData(
        code=3931, region=RegNames.Sector9_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_All_Instances[6][2][1]: IjiLocData(
        code=3932, region=RegNames.Sector9_Main[6],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_All_Instances[6][2][2]: IjiLocData(
        code=3933, region=RegNames.Sector9_Main[13],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_All_Instances[6][2][3]: IjiLocData(
        code=3934, region=RegNames.Sector9_Poster[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_All_Instances[6][3][0]: IjiLocData(
        code=3941, region=RegNames.Sector9_Main[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_All_Instances[6][3][1]: IjiLocData(
        code=3942, region=RegNames.Sector9_Side[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_All_Instances[6][3][2]: IjiLocData(
        code=3943, region=RegNames.Sector9_Main[13],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_All_Instances[6][3][3]: IjiLocData(
        code=3944, region=RegNames.Sector9_Poster[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_All_Instances[6][4][0]: IjiLocData(
        code=3951, region=RegNames.Sector9_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[6][4][1]: IjiLocData(
        code=3952, region=RegNames.Sector9_Main[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[6][4][2]: IjiLocData(
        code=3953, region=RegNames.Sector9_Main[13],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[6][4][3]: IjiLocData(
        code=3954, region=RegNames.Sector9_Poster[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[6][5][0]: IjiLocData(
        code=3961, region=RegNames.Sector9_Main[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[6][5][1]: IjiLocData(
        code=3962, region=RegNames.Sector9_Side[14],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[6][5][2]: IjiLocData(
        code=3963, region=RegNames.Sector9_Main[13],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[6][5][3]: IjiLocData(
        code=3964, region=RegNames.Sector9_Poster[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[6][6][0]: IjiLocData(
        code=3971, region=RegNames.Sector9_Main[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[8],world)
    ),
    LocNames.Weapons_All_Instances[6][6][1]: IjiLocData(
        code=3972, region=RegNames.Sector9_Main[13],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[8],world)
    ),
    LocNames.Weapons_All_Instances[6][6][2]: IjiLocData(
        code=3973, region=RegNames.Sector9_Poster[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[8],world)
    ),
    LocNames.Weapons_All_Instances[7][0][0]: IjiLocData(
        code=3011, region=RegNames.SectorX_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[7][0][1]: IjiLocData(
        code=3012, region=RegNames.SectorX_Core[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[7][0][2]: IjiLocData(
        code=3013, region=RegNames.SectorX_Final[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[2],world)
    ),
    LocNames.Weapons_All_Instances[7][1][0]: IjiLocData(
        code=3021, region=RegNames.SectorX_Core[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[7][1][1]: IjiLocData(
        code=3022, region=RegNames.SectorX_Main[11],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[7][1][2]: IjiLocData(
        code=3023, region=RegNames.SectorX_Final[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[3],world)
    ),
    LocNames.Weapons_All_Instances[7][1][3]: IjiLocData(
        code=3024, region=RegNames.SectorX_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
        ),
    LocNames.Weapons_All_Instances[7][2][0]: IjiLocData(
        code=3031, region=RegNames.SectorX_Core[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_All_Instances[7][2][1]: IjiLocData(
        code=3032, region=RegNames.SectorX_Main[11],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_All_Instances[7][2][2]: IjiLocData(
        code=3033, region=RegNames.SectorX_Final[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[4],world)
    ),
    LocNames.Weapons_All_Instances[7][2][3]: IjiLocData(
        code=3034, region=RegNames.SectorX_Side[0],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state, ItemNames.Weapons[4], world)
    ),
    LocNames.Weapons_All_Instances[7][3][0]: IjiLocData(
        code=3041, region=RegNames.SectorX_Core[1],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_All_Instances[7][3][1]: IjiLocData(
        code=3042, region=RegNames.SectorX_Core[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[5],world)
    ),
    LocNames.Weapons_All_Instances[7][4][0]: IjiLocData(
        code=3051, region=RegNames.SectorX_Main[2],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[7][4][1]: IjiLocData(
        code=3052, region=RegNames.SectorX_Core[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[7][4][2]: IjiLocData(
        code=3053, region=RegNames.SectorX_Main[11],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[7][4][3]: IjiLocData(
        code=3054, region=RegNames.SectorX_Final[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[6],world)
    ),
    LocNames.Weapons_All_Instances[7][5][0]: IjiLocData(
        code=3061, region=RegNames.SectorX_Main[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[7][5][1]: IjiLocData(
        code=3062, region=RegNames.SectorX_Main[11],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[7][5][2]: IjiLocData(
        code=3063, region=RegNames.SectorX_Final[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[7],world)
    ),
    LocNames.Weapons_All_Instances[7][6][0]: IjiLocData(
        code=3071, region=RegNames.SectorX_Core[4],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[8],world)
    ),
    LocNames.Weapons_All_Instances[7][6][1]: IjiLocData(
        code=3072, region=RegNames.SectorX_Main[6],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[8],world)
    ),
    LocNames.Weapons_All_Instances[7][6][2]: IjiLocData(
        code=3073, region=RegNames.SectorX_Main[11],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[8],world)
    ),
    LocNames.Weapons_All_Instances[7][6][3]: IjiLocData(
        code=3074, region=RegNames.SectorX_Final[3],
        valid=lambda world: world.options.basic_weapon_locations.value == 3,
        logic=lambda world, state: has_weapon_stats(state,ItemNames.Weapons[8],world)
    )
}

locations_logbooks: Dict[str, IjiLocData] = {
    LocNames.Logbooks[1][0]:  IjiLocData(
        code=1101, region=RegNames.Sector1_Main[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][1]:  IjiLocData(
        code=1102, region=RegNames.Sector1_Main[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][2]:  IjiLocData(
        code=1103, region=RegNames.Sector1_Main[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][3]:  IjiLocData(
        code=1104, region=RegNames.Sector1_Main[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][4]:  IjiLocData(
        code=1105, region=RegNames.Sector1_Main[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][5]:  IjiLocData(
        code=1106, region=RegNames.Sector1_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][6]:  IjiLocData(
        code=1107, region=RegNames.Sector1_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][7]:  IjiLocData(
        code=1108, region=RegNames.Sector1_Side[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][8]:  IjiLocData(
        code=1109, region=RegNames.Sector1_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][9]:  IjiLocData(
        code=1110, region=RegNames.Sector1_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][10]: IjiLocData(
        code=1111, region=RegNames.Sector1_Poster,
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][11]: IjiLocData(
        code=1112, region=RegNames.Sector1_Poster,
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][12]: IjiLocData(
        code=1113, region=RegNames.Sector1_Poster,
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][13]: IjiLocData(
        code=1114, region=RegNames.Sector1_Poster,
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[1][14]: IjiLocData(
        code=1115, region=RegNames.Sector1_Super,
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][0]: IjiLocData(
        code=1201, region=RegNames.Sector2_Main[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][1]: IjiLocData(
        code=1202, region=RegNames.Sector2_Main[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][2]: IjiLocData(
        code=1203, region=RegNames.Sector2_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][3]: IjiLocData(
        code=1204, region=RegNames.Sector2_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][4]: IjiLocData(
        code=1205, region=RegNames.Sector2_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][5]: IjiLocData(
        code=1206, region=RegNames.Sector2_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][6]: IjiLocData(
        code=1207, region=RegNames.Sector2_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][7]: IjiLocData(
        code=1208, region=RegNames.Sector2_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][8]: IjiLocData(
        code=1209, region=RegNames.Sector2_Main[7],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][9]: IjiLocData(
        code=1210, region=RegNames.Sector2_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][10]: IjiLocData(
        code=1211, region=RegNames.Sector2_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][11]: IjiLocData(
        code=1212, region=RegNames.Sector2_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][12]: IjiLocData(
        code=1213, region=RegNames.Sector2_Main[5],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][13]: IjiLocData(
        code=1214, region=RegNames.Sector2_Main[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][14]: IjiLocData(
        code=1215, region=RegNames.Sector2_Poster,
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[2][15]: IjiLocData(
        code=1216, region=RegNames.Sector2_Poster,
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][0]:  IjiLocData(
        code=1301, region=RegNames.Sector3_Main[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][1]:  IjiLocData(
        code=1302, region=RegNames.Sector3_Side[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][2]:  IjiLocData(
        code=1303, region=RegNames.Sector3_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][3]:  IjiLocData(
        code=1304, region=RegNames.Sector3_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][4]:  IjiLocData(
        code=1305, region=RegNames.Sector3_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][5]:  IjiLocData(
        code=1306, region=RegNames.Sector3_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][6]:  IjiLocData(
        code=1307, region=RegNames.Sector3_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][7]:  IjiLocData(
        code=1308, region=RegNames.Sector3_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][8]:  IjiLocData(
        code=1309, region=RegNames.Sector3_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][9]: IjiLocData(
        code=1310, region=RegNames.Sector3_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][10]: IjiLocData(
        code=1311, region=RegNames.Sector3_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][11]: IjiLocData(
        code=1312, region=RegNames.Sector3_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][12]: IjiLocData(
        code=1313, region=RegNames.Sector3_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][13]: IjiLocData(
        code=1314, region=RegNames.Sector3_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][14]: IjiLocData(
        code=1315, region=RegNames.Sector3_Side[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][15]: IjiLocData(
        code=1316, region=RegNames.Sector3_Side[8],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][16]: IjiLocData(
        code=1317, region=RegNames.Sector3_Side[8],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[3][17]: IjiLocData(
        code=1318, region=RegNames.Sector3_Poster[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[4][0]: IjiLocData(
        code=1401, region=RegNames.Sector4_Main[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[4][1]: IjiLocData(
        code=1402, region=RegNames.Sector4_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[4][2]: IjiLocData(
        code=1403, region=RegNames.Sector4_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[4][3]: IjiLocData(
        code=1404, region=RegNames.Sector4_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[4][4]: IjiLocData(
        code=1405, region=RegNames.Sector4_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[4][5]: IjiLocData(
        code=1406, region=RegNames.Sector4_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[4][6]: IjiLocData(
        code=1407, region=RegNames.Sector4_Main[5],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[4][7]: IjiLocData(
        code=1408, region=RegNames.Sector4_Main[5],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[4][8]: IjiLocData(
        code=1409, region=RegNames.Sector4_Main[5],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[4][9]: IjiLocData(
        code=1410, region=RegNames.Sector4_Side[0],
        valid=lambda world: world.options.logbook_locations
        ),
    LocNames.Logbooks[4][10]: IjiLocData(
        code=1411, region=RegNames.Sector4_Side[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[4][11]: IjiLocData(
        code=1412, region=RegNames.Sector4_Side[4],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[4][12]: IjiLocData(
        code=1413, region=RegNames.Sector4_Poster[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[5][0]: IjiLocData(
        code=1501, region=RegNames.Sector5_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[5][1]: IjiLocData(
        code=1502, region=RegNames.Sector5_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[5][2]: IjiLocData(
        code=1503, region=RegNames.Sector5_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[5][3]: IjiLocData(
        code=1504, region=RegNames.Sector5_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[5][4]: IjiLocData(
        code=1505, region=RegNames.Sector5_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[5][5]: IjiLocData(
        code=1506, region=RegNames.Sector5_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[5][6]: IjiLocData(
        code=1507, region=RegNames.Sector5_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[5][7]: IjiLocData(
        code=1508, region=RegNames.Sector5_Side[7],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[5][8]: IjiLocData(
        code=1509, region=RegNames.Sector5_Poster[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[5][9]: IjiLocData(
        code=1510, region=RegNames.Sector5_Main[7],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[6][0]:  IjiLocData(
        code=1601, region=RegNames.Sector6_Side[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[6][1]:  IjiLocData(
        code=1602, region=RegNames.Sector6_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[6][2]:  IjiLocData(
        code=1603, region=RegNames.Sector6_Main[4],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[6][3]:  IjiLocData(
        code=1604, region=RegNames.Sector6_Main[5],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[6][4]:  IjiLocData(
        code=1605, region=RegNames.Sector6_Main[5],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[6][5]:  IjiLocData(
        code=1606, region=RegNames.Sector6_Main[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[6][6]:  IjiLocData(
        code=1607, region=RegNames.Sector6_Main[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[6][7]:  IjiLocData(
        code=1608, region=RegNames.Sector6_Main[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[6][8]:  IjiLocData(
        code=1609, region=RegNames.Sector6_Main[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[6][9]: IjiLocData(
        code=1610, region=RegNames.Sector6_Side[12],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[6][10]: IjiLocData(
        code=1611, region=RegNames.Sector6_Poster[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][0]:  IjiLocData(
        code=1701, region=RegNames.Sector7_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][1]:  IjiLocData(
        code=1702, region=RegNames.Sector7_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][2]:  IjiLocData(
        code=1703, region=RegNames.Sector7_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][3]:  IjiLocData(
        code=1704, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][4]:  IjiLocData(
        code=1705, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][5]:  IjiLocData(
        code=1706, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][6]:  IjiLocData(
        code=1707, region=RegNames.Sector7_Main[4],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][7]:  IjiLocData(
        code=1708, region=RegNames.Sector7_Main[4],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][8]:  IjiLocData(
        code=1709, region=RegNames.Sector7_Main[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][9]: IjiLocData(
        code=1710, region=RegNames.Sector7_Main[7],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][10]: IjiLocData(
        code=1711, region=RegNames.Sector7_Main[9],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][11]: IjiLocData(
        code=1712, region=RegNames.Sector7_Main[10],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][12]: IjiLocData(
        code=1713, region=RegNames.Sector7_Side[13],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][13]: IjiLocData(
        code=1714, region=RegNames.Sector7_Side[13],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][14]: IjiLocData(
        code=1715, region=RegNames.Sector7_Side[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][15]: IjiLocData(
        code=1716, region=RegNames.Sector7_Side[8],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][16]: IjiLocData(
        code=1717, region=RegNames.Sector7_Side[8],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][17]: IjiLocData(
        code=1718, region=RegNames.Sector7_Poster,
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][18]: IjiLocData(
        code=1719, region=RegNames.Sector7_Poster,
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][19]: IjiLocData(
        code=1720, region=RegNames.Sector7_Side[14],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][20]: IjiLocData(
        code=1721, region=RegNames.Sector7_Side[14],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][21]: IjiLocData(
        code=1722, region=RegNames.Sector7_Side[14],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[7][22]: IjiLocData(
        code=1723, region=RegNames.Sector7_Side[11],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][0]:  IjiLocData(
        code=1801, region=RegNames.Sector8_Main[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][1]:  IjiLocData(
        code=1802, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][2]:  IjiLocData(
        code=1803, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][3]:  IjiLocData(
        code=1804, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][4]:  IjiLocData(
        code=1805, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][5]:  IjiLocData(
        code=1806, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][6]:  IjiLocData(
        code=1807, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][7]:  IjiLocData(
        code=1808, region=RegNames.Sector8_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][8]:  IjiLocData(
        code=1809, region=RegNames.Sector8_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][9]: IjiLocData(
        code=1810, region=RegNames.Sector8_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][10]: IjiLocData(
        code=1811, region=RegNames.Sector8_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][11]: IjiLocData(
        code=1812, region=RegNames.Sector8_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][12]: IjiLocData(
        code=1813, region=RegNames.Sector8_Side[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][13]: IjiLocData(
        code=1814, region=RegNames.Sector8_Poster,
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[8][14]: IjiLocData(
        code=1815, region=RegNames.Sector8_Side[5],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][0]: IjiLocData(
        code=1901, region=RegNames.Sector9_Main[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][1]: IjiLocData(
        code=1902, region=RegNames.Sector9_Side[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][2]: IjiLocData(
        code=1903, region=RegNames.Sector9_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][3]: IjiLocData(
        code=1904, region=RegNames.Sector9_Main[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][4]: IjiLocData(
        code=1905, region=RegNames.Sector9_Poster[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][5]: IjiLocData(
        code=1906, region=RegNames.Sector9_Side[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][6]: IjiLocData(
        code=1907, region=RegNames.Sector9_Main[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][7]: IjiLocData(
        code=1908, region=RegNames.Sector9_Side[9],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][8]: IjiLocData(
        code=1909, region=RegNames.Sector9_Main[13],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][9]: IjiLocData(
        code=1910, region=RegNames.Sector9_Main[13],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][10]: IjiLocData(
        code=1911, region=RegNames.Sector9_Main[13],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][11]: IjiLocData(
        code=1912, region=RegNames.Sector9_Main[13],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][12]: IjiLocData(
        code=1913, region=RegNames.Sector9_Main[13],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][13]: IjiLocData(
        code=1914, region=RegNames.Sector9_Poster[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][14]: IjiLocData(
        code=1915, region=RegNames.Sector9_Side[11],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][15]: IjiLocData(
        code=1916, region=RegNames.Sector9_Main[13],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][16]: IjiLocData(
        code=1917, region=RegNames.Sector9_Deep[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][17]: IjiLocData(
        code=1918, region=RegNames.Sector9_Deep[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[9][18]: IjiLocData(
        code=1919, region=RegNames.Sector9_Deep[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][0]:  IjiLocData(
        code=1001, region=RegNames.SectorX_Main[1],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][1]: IjiLocData(
        code=1002, region=RegNames.SectorX_Main[4],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][2]: IjiLocData(
        code=1003, region=RegNames.SectorX_Main[4],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][3]: IjiLocData(
        code=1004, region=RegNames.SectorX_Core[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][4]: IjiLocData(
        code=1005, region=RegNames.SectorX_Core[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][5]: IjiLocData(
        code=1006, region=RegNames.SectorX_Core[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][6]: IjiLocData(
        code=1007, region=RegNames.SectorX_Core[4],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][7]: IjiLocData(
        code=1008, region=RegNames.SectorX_Core[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][8]: IjiLocData(
        code=1009, region=RegNames.SectorX_Main[5],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][9]: IjiLocData(
        code=1010, region=RegNames.SectorX_Main[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][10]: IjiLocData(
        code=1011, region=RegNames.SectorX_Main[7],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][11]: IjiLocData(
        code=1012, region=RegNames.SectorX_Main[7],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][12]: IjiLocData(
        code=1013, region=RegNames.SectorX_Main[11],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][13]: IjiLocData(
        code=1014, region=RegNames.SectorX_Final[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][14]: IjiLocData(
        code=1015, region=RegNames.SectorX_Final[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][15]: IjiLocData(
        code=1016, region=RegNames.SectorX_Final[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][16]: IjiLocData(
        code=1017, region=RegNames.SectorX_Final[3],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][17]: IjiLocData(
        code=1018, region=RegNames.SectorX_Final[4],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][18]: IjiLocData(
        code=1019, region=RegNames.SectorX_Final[4],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][19]: IjiLocData(
        code=1020, region=RegNames.SectorX_Final[5],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][20]: IjiLocData(
        code=1021, region=RegNames.SectorX_Final[5],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][21]: IjiLocData(
        code=1022, region=RegNames.SectorX_Poster[0],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][22]: IjiLocData(
        code=1023, region=RegNames.SectorX_Side[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][23]: IjiLocData(
        code=1024, region=RegNames.SectorX_Side[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[10][24]: IjiLocData(
        code=1025, region=RegNames.SectorX_Side[6],
        valid=lambda world: world.options.logbook_locations
    ),
    LocNames.Logbooks[0][0]:  IjiLocData(
        code=1116, region=RegNames.SectorZ,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations() if (
            world.options.allow_sector_z.is_post_game(world)) else None
    ),
    LocNames.Logbooks[0][1]:  IjiLocData(
        code=1117, region=RegNames.SectorZ,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations() if (
            world.options.allow_sector_z.is_post_game(world)) else None
    ),
    LocNames.Logbooks[11][0]:  IjiLocData(
        code=1118, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][1]: IjiLocData(
        code=1119, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][2]: IjiLocData(
        code=1120, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][3]: IjiLocData(
        code=1121, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][4]: IjiLocData(
        code=1122, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][5]: IjiLocData(
        code=1123, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][6]: IjiLocData(
        code=1124, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][7]: IjiLocData(
        code=1125, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][8]: IjiLocData(
        code=1126, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][9]: IjiLocData(
        code=1127, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][10]: IjiLocData(
        code=1128, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][11]: IjiLocData(
        code=1129, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][12]: IjiLocData(
        code=1130, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][13]: IjiLocData(
        code=1131, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    ),
    LocNames.Logbooks[11][14]: IjiLocData(
        code=1132, region=RegNames.SectorY,
        valid=lambda world: world.options.logbook_locations,
        on_added=lambda world: world.increment_post_goal_locations()
    )
}

locations_crackboxes: Dict[str, IjiLocData] = {
    LocNames.CrackBoxes[0][0]: IjiLocData(
        code=721, region=RegNames.Sector2_Main[1],
        valid=lambda world: world.options.security_box_locations
    ),
    LocNames.CrackBoxes[0][1]: IjiLocData(
        code=722, region=RegNames.Sector2_Main[1],
        valid=lambda world: world.options.security_box_locations
    ),
    LocNames.CrackBoxes[0][2]: IjiLocData(
        code=723, region=RegNames.Sector2_Side[1],
        valid=lambda world: world.options.security_box_locations
    ),
    LocNames.CrackBoxes[0][3]: IjiLocData(
        code=724, region=RegNames.Sector2_Main[5],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 1)
    ),
    LocNames.CrackBoxes[0][4]: IjiLocData(
        code=725, region=RegNames.Sector2_Side[4],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 2)
    ),
    LocNames.CrackBoxes[0][5]: IjiLocData(
        code=726, region=RegNames.Sector2_Side[5],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 1)
    ),
    LocNames.CrackBoxes[0][6]: IjiLocData(
        code=727, region=RegNames.Sector2_Main[6],
        valid=lambda world: world.options.security_box_locations
    ),
    LocNames.CrackBoxes[1][0]: IjiLocData(
        code=731, region=RegNames.Sector3_Side[1],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 1)
    ),
    LocNames.CrackBoxes[1][1]: IjiLocData(
        code=732, region=RegNames.Sector3_Side[1],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 2)
    ),
    LocNames.CrackBoxes[1][2]: IjiLocData(
        code=733, region=RegNames.Sector3_Main[0],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 2)
    ),
    LocNames.CrackBoxes[1][3]: IjiLocData(
        code=734, region=RegNames.Sector3_Main[3],
        valid=lambda world: world.options.security_box_locations
    ),
    LocNames.CrackBoxes[1][4]: IjiLocData(
        code=735, region=RegNames.Sector3_Main[3],
        valid=lambda world: world.options.security_box_locations
    ),
    LocNames.CrackBoxes[2][0]: IjiLocData(
        code=741, region=RegNames.Sector4_Main[3],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 2)
    ),
    LocNames.CrackBoxes[3][0]: IjiLocData(
        code=751, region=RegNames.Sector5_Side[0],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 1)
    ),
    LocNames.CrackBoxes[3][1]: IjiLocData(
        code=752, region=RegNames.Sector5_Side[0],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 3)
    ),
    LocNames.CrackBoxes[3][2]: IjiLocData(
        code=753, region=RegNames.Sector5_Side[1],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 4)
    ),
    LocNames.CrackBoxes[3][3]: IjiLocData(
        code=754, region=RegNames.Sector5_Side[2],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 1)
    ),
    LocNames.CrackBoxes[3][4]: IjiLocData(
        code=755, region=RegNames.Sector5_Side[8],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 3)
    ),
    LocNames.CrackBoxes[3][5]: IjiLocData(
        code=756, region=RegNames.Sector5_Side[8],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 7)
    ),
    LocNames.CrackBoxes[4][0]: IjiLocData(
        code=761, region=RegNames.Sector6_Side[7],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 3)
    ),
    LocNames.CrackBoxes[4][1]: IjiLocData(
        code=762, region=RegNames.Sector6_Main[5],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 2)
    ),
    LocNames.CrackBoxes[5][0]: IjiLocData(
        code=771, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 5)
    ),
    LocNames.CrackBoxes[5][1]: IjiLocData(
        code=772, region=RegNames.Sector7_Main[3],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 2)
    ),
    LocNames.CrackBoxes[5][2]: IjiLocData(
        code=773, region=RegNames.Sector7_Ribbon,
        valid=lambda world: world.options.security_box_locations
    ),
    LocNames.CrackBoxes[6][0]: IjiLocData(
        code=781, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 7)
    ),
    LocNames.CrackBoxes[6][1]: IjiLocData(
        code=782, region=RegNames.Sector8_Main[2],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 4)
    ),
    LocNames.CrackBoxes[7][0]: IjiLocData(
        code=791, region=RegNames.Sector9_Side[12],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 4)
    ),
    LocNames.CrackBoxes[7][1]: IjiLocData(
        code=792, region=RegNames.Sector9_Side[12],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 1)
    ),
    LocNames.CrackBoxes[7][2]: IjiLocData(
        code=793, region=RegNames.Sector9_Main[3],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 3)
    ),
    LocNames.CrackBoxes[7][3]: IjiLocData(
        code=794, region=RegNames.Sector9_Side[2],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 4)
    ),
    LocNames.CrackBoxes[7][4]: IjiLocData(
        code=795, region=RegNames.Sector9_Side[4],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 3)
    ),
    LocNames.CrackBoxes[8][0]: IjiLocData(
        code=701, region=RegNames.SectorX_Main[1],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 2)
    ),
    LocNames.CrackBoxes[8][1]: IjiLocData(
        code=702, region=RegNames.SectorX_Main[7],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 6)
    ),
    LocNames.CrackBoxes[8][2]: IjiLocData(
        code=703, region=RegNames.SectorX_Side[5],
        valid=lambda world: world.options.security_box_locations,
        logic=lambda world, state: has_stats(world, ItemNames.Stat_Crack, 9)
    )
}

locations_overloads: Dict[str, IjiLocData] = {
    LocNames.Overloads[0][0]: IjiLocData(
        code=821, region=RegNames.Sector2_Main[2],
        valid=lambda world: world.options.nano_overload_locations
    ),
    LocNames.Overloads[0][1]: IjiLocData(
        code=822, region=RegNames.Sector2_Side[3],
        valid=lambda world: world.options.nano_overload_locations
    ),
    LocNames.Overloads[1][0]: IjiLocData(
        code=831, region=RegNames.Sector3_Side[4],
        valid=lambda world: world.options.nano_overload_locations
    ),
    LocNames.Overloads[2][0]: IjiLocData(
        code=841, region=RegNames.Sector4_Side[3],
        valid=lambda world: world.options.nano_overload_locations
    ),
    LocNames.Overloads[3][0]: IjiLocData(
        code=851, region=RegNames.Sector5_Side[3],
        valid=lambda world: world.options.nano_overload_locations
    ),
    LocNames.Overloads[3][1]: IjiLocData(
        code=852, region=RegNames.Sector5_Main[3],
        valid=lambda world: world.options.nano_overload_locations
    ),
    LocNames.Overloads[4][0]: IjiLocData(
        code=861, region=RegNames.Sector6_Main[4],
        valid=lambda world: world.options.nano_overload_locations
    ),
    LocNames.Overloads[5][0]: IjiLocData(
        code=871, region=RegNames.Sector7_Side[3],
        valid=lambda world: world.options.nano_overload_locations
    ),
    LocNames.Overloads[5][1]: IjiLocData(
        code=872, region=RegNames.Sector7_Main[8],
        valid=lambda world: world.options.nano_overload_locations
    ),
    LocNames.Overloads[6][0]: IjiLocData(
        code=881, region=RegNames.Sector8_Side[6],
        valid=lambda world: world.options.nano_overload_locations
    ),
    LocNames.Overloads[7][0]: IjiLocData(
        code=891, region=RegNames.Sector9_Main[9],
        valid=lambda world: world.options.nano_overload_locations
    ),
    LocNames.Overloads[7][1]: IjiLocData(
        code=892, region=RegNames.Sector9_Main[1],
        valid=lambda world: world.options.nano_overload_locations
    ),
    LocNames.Overloads[8][0]: IjiLocData(
        code=801, region=RegNames.SectorX_Final[0],
        valid=lambda world: world.options.nano_overload_locations
    ),
    LocNames.Overloads[8][1]: IjiLocData(
        code=802, region=RegNames.SectorX_Side[7],
        valid=lambda world: world.options.nano_overload_locations
    )
}

locations_tutorialpages: Dict[str, IjiLocData] = {
    LocNames.Tutorial_Pages[0]: IjiLocData(
        code=25, region=RegNames.Sector1_Main[0]
    ),
    LocNames.Tutorial_Pages[1]: IjiLocData(
        code=26, region=RegNames.Sector1_Main[0]
    ),
    LocNames.Tutorial_Pages[2]: IjiLocData(
        code=27, region=RegNames.Sector1_Main[0]
    ),
    LocNames.Tutorial_Pages[2]: IjiLocData(
        code=28, region=RegNames.Sector1_Main[0]
    ),
    LocNames.Tutorial_Pages[2]: IjiLocData(
        code=29, region=RegNames.Sector1_Main[0]
    ),
    LocNames.Tutorial_Pages[2]: IjiLocData(
        code=30, region=RegNames.Sector1_Main[1]
    )
}

locations_enemy_scout: Dict[str, IjiLocData] = {
    data[1]: IjiLocData(
        code = 2000+data[0], region = data[2],
        valid = lambda world, difficulty = data[3]: enemy_is_valid(world, "Tasen Scout", difficulty)
    ) for data in LocNames.Kills_Scouts
}

locations_enemy_soldier: Dict[str, IjiLocData] = {
    data[1]: IjiLocData(
        code = 2000+data[0], region = data[2],
        valid = lambda world, difficulty = data[3]: enemy_is_valid(world, "Tasen Soldier", difficulty)
    ) for data in LocNames.Kills_Soldiers
}

locations_enemy_commander: Dict[str, IjiLocData] = {
    data[1]: IjiLocData(
        code = 2000+data[0], region = data[2],
        valid = lambda world, difficulty = data[3]: enemy_is_valid(world, "Tasen Commander", difficulty)
    ) for data in LocNames.Kills_Commanders
}

locations_enemy_elite: Dict[str, IjiLocData] = {
    data[1]: IjiLocData(
        code = 2000+data[0], region = data[2],
        valid = lambda world, difficulty = data[3]: enemy_is_valid(world, "Tasen Elite", difficulty)
    ) for data in LocNames.Kills_Elites
}

locations_enemy_trooper: Dict[str, IjiLocData] = {
    data[1]: IjiLocData(
        code = 2000+data[0], region = data[2],
        valid = lambda world, difficulty = data[3]: enemy_is_valid(world, "Komato Trooper", difficulty)
    ) for data in LocNames.Kills_Troopers
}

locations_enemy_berserker: Dict[str, IjiLocData] = {
    data[1]: IjiLocData(
        code = 2000+data[0], region = data[2],
        valid = lambda world, difficulty = data[3]: enemy_is_valid(world, "Komato Berserker", difficulty)
    ) for data in LocNames.Kills_Berserkers
}

locations_enemy_beast: Dict[str, IjiLocData] = {
    data[1]: IjiLocData(
        code = 2000+data[0], region = data[2],
        valid = lambda world, difficulty = data[3]: enemy_is_valid(world, "Komato Beast", difficulty),
    ) for data in LocNames.Kills_Beasts
}

locations_enemy_assassin: Dict[str, IjiLocData] = {
    data[1]: IjiLocData(
        code = 2000+data[0], region = data[2],
        valid = lambda world: enemy_is_valid(world, "Komato Assassin", 0)
    ) for data in LocNames.Kills_Assassins
}

locations_enemy_annihilator: Dict[str, IjiLocData] = {
    data[1]: IjiLocData(
        code = 2000+data[0], region = data[2],
        valid = lambda world: enemy_is_valid(world, "Komato Annihilator", 0),
        logic = lambda world, state: can_kill_annihilators(state, world)
    ) for data in LocNames.Kills_Annihilators
}

locations_enemy_bosses: Dict[str, IjiLocData] = {
    LocNames.Kills_Bosses[0]: IjiLocData( # Krotera
        code=2095, region = RegNames.Sector_Ends[2],
        valid = lambda world: enemy_is_valid(world, "Bosses", 0),
        on_added = lambda world: world.increment_post_goal_locations() if world.options.end_goal.value == 3 else None
    ),
    LocNames.Kills_Bosses[1]: IjiLocData( # Iosa
        code=2720, region = RegNames.Sector_Ends[8],
        valid = lambda world: enemy_is_valid(world, "Bosses", 0),
        on_added = lambda world: world.increment_post_goal_locations() if world.options.end_goal.value == 9 else None
    ),
    LocNames.Kills_Bosses[2]: IjiLocData( # Asha
        code=2755, region = RegNames.SectorX_Core[7],
        valid = lambda world: enemy_is_valid(world, "Bosses", 0),
    ),
    LocNames.Kills_Bosses[3]: IjiLocData( # Tor
        code=2798, region = RegNames.Sector_Ends[9],
        valid = lambda world: enemy_is_valid(world, "Bosses", 0),
        logic = lambda world, state: state.has("Iosa's Fate", world.player), # Tor cannot be killed while Iosa is alive
        on_added = lambda world: world.increment_post_goal_locations() if world.options.end_goal.value == 10 else None
    ),
    LocNames.Kills_Bosses[4]: IjiLocData( # Sentinel Proxima
        code=2915, region = RegNames.Sector_Ends[6],
        valid = lambda world: enemy_is_valid(world, "Bosses", 0),
        on_added = lambda world: world.increment_post_goal_locations() if world.options.end_goal.value == 7 else None
    ),
    LocNames.Kills_Bosses[5]: IjiLocData( # Yukabacera (Not actually a boss)
        code=2276, region = RegNames.Sector6_Poster[3],
        valid = lambda world: enemy_is_valid(world, "Tasen Soldier", 0),
        logic = lambda world, state: can_kill_yukabacera(state, world)
    )
}

locations_enemy_z: Dict[str, IjiLocData] = {
    LocNames.Kills_Sector_Z[i]: IjiLocData(
        code = 2801 + i,
        region = RegNames.SectorZ,
        valid = lambda world: enemy_is_valid(world, "Sector Z", 0),
        on_added = lambda world: world.increment_post_goal_locations if (
            world.options.allow_sector_z.is_post_game(world)
        ) else None
    ) for i in range(len(LocNames.Kills_Sector_Z))
}

enemy_locations = {
    **locations_enemy_bosses,
    **locations_enemy_scout,
    **locations_enemy_soldier,
    **locations_enemy_commander,
    **locations_enemy_elite,
    **locations_enemy_trooper,
    **locations_enemy_berserker,
    **locations_enemy_beast,
    **locations_enemy_assassin,
    **locations_enemy_annihilator,
    **locations_enemy_z
}

location_table = {
    **locations_sector_complete,
    **locations_level_up,
    **locations_stat_levels,
    **locations_ribbon,
    **locations_poster,
    **locations_supercharge,
    **locations_upgrades,
    **locations_unique_basic_weapons,
    **locations_sector_weapons,
    **locations_allbasicweapons,
    **locations_combinedweapons,
    **locations_uniquespecialweapons,
    **locations_logbooks,
    **locations_checkpoints,
    **locations_crackboxes,
    **locations_overloads,
    **locations_enemy_bosses,
    **locations_enemy_scout,
    **locations_enemy_soldier,
    **locations_enemy_commander,
    **locations_enemy_elite,
    **locations_enemy_trooper,
    **locations_enemy_berserker,
    **locations_enemy_beast,
    **locations_enemy_assassin,
    **locations_enemy_annihilator,
    **locations_enemy_z
}