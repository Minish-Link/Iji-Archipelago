from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING
from ..Rules import can_destroy_sentinel_proxima, can_kill_annihilators, has_stats, has_xp
from ..Names import LocNames, RegNames, ItemNames, EventNames
from .LocData import IjiLocData, location_table
from .ItemData import IjiItemData
from BaseClasses import ItemClassification

events_levels: Dict[str, IjiLocData] = {
    EventNames.Levels[1]: IjiLocData(
        region=RegNames.Sector1_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 1, 1)
    ),
    EventNames.Levels[2]: IjiLocData(
        region=RegNames.Sector1_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 1, 2)
    ),
    EventNames.Levels[3]: IjiLocData(
        region=RegNames.Sector1_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 1, 3)
    ),
    EventNames.Levels[4]: IjiLocData(
        region=RegNames.Sector1_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 1, 4)
    ),
    EventNames.Levels[5]: IjiLocData(
        region=RegNames.Sector1_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 1, 5)
    ),
    EventNames.Levels[6]: IjiLocData(
        region=RegNames.Sector2_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 2, 1)
    ),
    EventNames.Levels[7]: IjiLocData(
        region=RegNames.Sector2_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 2, 2)
    ),
    EventNames.Levels[8]:   IjiLocData(
        region=RegNames.Sector2_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 2, 3)
    ),
    EventNames.Levels[9]:   IjiLocData(
        region=RegNames.Sector2_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 2, 4)
    ),
    EventNames.Levels[10]:  IjiLocData(
        region=RegNames.Sector2_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 2, 5)
    ),
    EventNames.Levels[11]:  IjiLocData(
        region=RegNames.Sector3_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 3, 1)
    ),
    EventNames.Levels[12]:  IjiLocData(
        region=RegNames.Sector3_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 3, 2)
    ),
    EventNames.Levels[13]:  IjiLocData(
        region=RegNames.Sector3_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 3, 3)
    ),
    EventNames.Levels[14]:  IjiLocData(
        region=RegNames.Sector3_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 3, 4)
    ),
    EventNames.Levels[15]:  IjiLocData(
        region=RegNames.Sector3_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 3, 5)
    ),
    EventNames.Levels[16]:  IjiLocData(
        region=RegNames.Sector4_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 4, 1)
    ),
    EventNames.Levels[17]:  IjiLocData(
        region=RegNames.Sector4_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 4, 2)
    ),
    EventNames.Levels[18]:  IjiLocData(
        region=RegNames.Sector4_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 4, 3)
    ),
    EventNames.Levels[19]:  IjiLocData(
        region=RegNames.Sector4_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 4, 4)
    ),
    EventNames.Levels[20]:  IjiLocData(
        region=RegNames.Sector4_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 4, 5)
    ),
    EventNames.Levels[21]:  IjiLocData(
        region=RegNames.Sector5_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 5, 1)
    ),
    EventNames.Levels[22]:  IjiLocData(
        region=RegNames.Sector5_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 5, 2)
    ),
    EventNames.Levels[23]:  IjiLocData(
        region=RegNames.Sector5_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 5, 3)
    ),
    EventNames.Levels[24]:  IjiLocData(
        region=RegNames.Sector5_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 5, 4)
    ),
    EventNames.Levels[25]:  IjiLocData(
        region=RegNames.Sector5_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 5, 5)
    ),
    EventNames.Levels[26]:  IjiLocData(
        region=RegNames.Sector6_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 6, 1)
    ),
    EventNames.Levels[27]:  IjiLocData(
        region=RegNames.Sector6_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 6, 2)
    ),
    EventNames.Levels[28]:  IjiLocData(
        region=RegNames.Sector6_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 6, 3)
    ),
    EventNames.Levels[29]:  IjiLocData(
        region=RegNames.Sector6_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 6, 4)
    ),
    EventNames.Levels[30]:  IjiLocData(
        region=RegNames.Sector6_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 6, 5)
    ),
    EventNames.Levels[31]:  IjiLocData(
        region=RegNames.Sector7_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 7, 1)
    ),
    EventNames.Levels[32]:  IjiLocData(
        region=RegNames.Sector7_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 7, 2)
    ),
    EventNames.Levels[33]:  IjiLocData(
        region=RegNames.Sector7_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 7, 3)
    ),
    EventNames.Levels[34]:  IjiLocData(
        region=RegNames.Sector7_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 7, 4)
    ),
    EventNames.Levels[35]:  IjiLocData(
        region=RegNames.Sector7_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 7, 5)
    ),
    EventNames.Levels[36]:  IjiLocData(
        region=RegNames.Sector8_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 8, 1)
    ),
    EventNames.Levels[37]:  IjiLocData(
        region=RegNames.Sector8_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 8, 2)
    ),
    EventNames.Levels[38]:  IjiLocData(
        region=RegNames.Sector8_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 8, 3)
    ),
    EventNames.Levels[39]:  IjiLocData(
        region=RegNames.Sector8_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 8, 4)
    ),
    EventNames.Levels[40]:  IjiLocData(
        region=RegNames.Sector8_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 8, 5)
    ),
    EventNames.Levels[41]:  IjiLocData(
        region=RegNames.Sector9_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 9, 1)
    ),
    EventNames.Levels[42]:  IjiLocData(
        region=RegNames.Sector9_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 9, 2)
    ),
    EventNames.Levels[43]:  IjiLocData(
        region=RegNames.Sector9_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 9, 3)
    ),
    EventNames.Levels[44]:  IjiLocData(
        region=RegNames.Sector9_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 9, 4)
    ),
    EventNames.Levels[45]:  IjiLocData(
        region=RegNames.Sector9_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 9, 5)
    ),
    EventNames.Levels[46]:  IjiLocData(
        region=RegNames.SectorX_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 10, 1)
    ),
    EventNames.Levels[47]:  IjiLocData(
        region=RegNames.SectorX_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 10, 2)
    ),
    EventNames.Levels[48]:  IjiLocData(
        region=RegNames.SectorX_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 10, 3)
    ),
    EventNames.Levels[49]:  IjiLocData(
        region=RegNames.SectorX_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 10, 4)
    ),
    EventNames.Levels[50]:  IjiLocData(
        region=RegNames.SectorX_Main[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.levelsanity.value == 0,
        logic=lambda world, state: has_xp(state, world, 10, 5)
    ),
}

events_xp: Dict[str, IjiLocData] = {
    # Sector 1
    EventNames.XP_Sector[0][0]: IjiLocData(
        region=RegNames.Sector1_Main[0],
        locked_item=lambda world: EventNames.XP[0][1]
    ),
    EventNames.XP_Sector[0][1]: IjiLocData(
        region=RegNames.Sector1_Main[1],
        locked_item=lambda world: EventNames.XP[0][3]
    ),
    EventNames.XP_Sector[0][2]: IjiLocData(
        region=RegNames.Sector1_Main[1],
        locked_item=lambda world: EventNames.XP[0][1]
    ),
    EventNames.XP_Sector[0][3]: IjiLocData(
        region=RegNames.Sector1_Side[1],
        locked_item=lambda world: EventNames.XP[0][1]
    ),
    EventNames.XP_Sector[0][4]: IjiLocData(
        region=RegNames.Sector1_Main[2],
        locked_item=lambda world: EventNames.XP[0][1]
    ),
    EventNames.XP_Sector[0][5]: IjiLocData(
        region=RegNames.Sector1_Main[3],
        locked_item=lambda world: EventNames.XP[0][2]
    ),

    # Sector 2
    EventNames.XP_Sector[1][0]: IjiLocData(
        region=RegNames.Sector2_Side[0],
        locked_item=lambda world: EventNames.XP[1][2]
    ),
    EventNames.XP_Sector[1][1]: IjiLocData(
        region=RegNames.Sector2_Main[1],
        locked_item=lambda world: EventNames.XP[1][2]
    ),
    EventNames.XP_Sector[1][2]: IjiLocData(
        region=RegNames.Sector2_Main[2],
        locked_item=lambda world: EventNames.XP[1][3]
    ),
    EventNames.XP_Sector[1][3]: IjiLocData(
        region=RegNames.Sector2_Main[2],
        locked_item=lambda world: EventNames.XP[1][2]
    ),
    EventNames.XP_Sector[1][4]: IjiLocData(
        region=RegNames.Sector2_Main[3],
        locked_item=lambda world: EventNames.XP[1][2]
    ),
    EventNames.XP_Sector[1][5]: IjiLocData(
        region=RegNames.Sector2_Main[4],
        locked_item=lambda world: EventNames.XP[1][1]
    ),
    EventNames.XP_Sector[1][6]: IjiLocData(
        region=RegNames.Sector2_Side[1],
        locked_item=lambda world: EventNames.XP[1][3]
    ),
    EventNames.XP_Sector[1][7]: IjiLocData(
        region=RegNames.Sector2_Side[1],
        locked_item=lambda world: EventNames.XP[1][2]
    ),
    EventNames.XP_Sector[1][8]: IjiLocData(
        region=RegNames.Sector2_Main[5],
        locked_item=lambda world: EventNames.XP[1][3]
    ),
    EventNames.XP_Sector[1][9]: IjiLocData(
        region=RegNames.Sector2_Main[5],
        locked_item=lambda world: EventNames.XP[1][2],
        logic=lambda world, state: (
            has_stats(state, world, ItemNames.Stat_Crack, 1)
        )
    ),
    EventNames.XP_Sector[1][10]: IjiLocData(
        region=RegNames.Sector2_Side[3],
        locked_item=lambda world: EventNames.XP[1][2]
    ),
    EventNames.XP_Sector[1][11]: IjiLocData(
        region=RegNames.Sector2_Side[4],
        locked_item=lambda world: EventNames.XP[1][2]
    ),
    EventNames.XP_Sector[1][12]: IjiLocData(
        region=RegNames.Sector2_Main[6],
        locked_item=lambda world: EventNames.XP[1][3]
    ),
    EventNames.XP_Sector[1][13]: IjiLocData(
        region=RegNames.Sector2_Side[5],
        locked_item=lambda world: EventNames.XP[1][0]
    ),

    # Sector 3
    EventNames.XP_Sector[2][0]: IjiLocData(
        region=RegNames.Sector3_Side[0],
        locked_item=lambda world: EventNames.XP[2][1]
    ),
    EventNames.XP_Sector[2][1]: IjiLocData(
        region=RegNames.Sector3_Side[1],
        locked_item=lambda world: EventNames.XP[2][1],
        logic=lambda world, state: (
            has_stats(state, world, ItemNames.Stat_Crack, 2)
        )
    ),
    EventNames.XP_Sector[2][2]: IjiLocData(
        region=RegNames.Sector3_Side[2],
        locked_item=lambda world: EventNames.XP[2][1]
    ),
    EventNames.XP_Sector[2][3]: IjiLocData(
        region=RegNames.Sector3_Side[3],
        locked_item=lambda world: EventNames.XP[2][1]
    ),
    EventNames.XP_Sector[2][4]: IjiLocData(
        region=RegNames.Sector3_Main[0],
        locked_item=lambda world: EventNames.XP[2][2]
    ),
    EventNames.XP_Sector[2][5]: IjiLocData(
        region=RegNames.Sector3_Main[0],
        locked_item=lambda world: EventNames.XP[2][2],
        logic=lambda world, state: (
            has_stats(state, world, ItemNames.Stat_Crack, 2)
        )
    ),
    EventNames.XP_Sector[2][6]: IjiLocData(
        region=RegNames.Sector3_Main[1],
        locked_item=lambda world: EventNames.XP[2][5],
    ),
    EventNames.XP_Sector[2][7]: IjiLocData(
        region=RegNames.Sector3_Main[1],
        locked_item=lambda world: EventNames.XP[2][4]
    ),
    EventNames.XP_Sector[2][8]: IjiLocData(
        region=RegNames.Sector3_Main[2],
        locked_item=lambda world: EventNames.XP[2][4]
    ),
    EventNames.XP_Sector[2][9]: IjiLocData(
        region=RegNames.Sector3_Side[10],
        locked_item=lambda world: EventNames.XP[2][2]
    ),
    EventNames.XP_Sector[2][10]: IjiLocData(
        region=RegNames.Sector3_Main[3],
        locked_item=lambda world: EventNames.XP[2][0]
    ),
    EventNames.XP_Sector[2][11]: IjiLocData(
        region=RegNames.Sector3_Side[9],
        locked_item=lambda world: EventNames.XP[2][2]
    ),
    EventNames.XP_Sector[2][12]: IjiLocData(
        region=RegNames.Sector3_Side[6],
        locked_item=lambda world: EventNames.XP[2][2]
    ),

    # Sector 4
    EventNames.XP_Sector[3][0]: IjiLocData(
        region=RegNames.Sector4_Side[0],
        locked_item=lambda world: EventNames.XP[3][3]
    ),
    EventNames.XP_Sector[3][1]: IjiLocData(
        region=RegNames.Sector4_Main[0],
        locked_item=lambda world: EventNames.XP[3][3]
    ),
    EventNames.XP_Sector[3][2]: IjiLocData(
        region=RegNames.Sector4_Main[0],
        locked_item=lambda world: EventNames.XP[3][2]
    ),
    EventNames.XP_Sector[3][3]: IjiLocData(
        region=RegNames.Sector4_Main[0],
        locked_item=lambda world: EventNames.XP[3][1],
        logic=lambda world, state: (
            state.has(ItemNames.Upgrade_Jump, world.player, 1) or
            (state.has_any([EventNames.Weapons[3],EventNames.Weapons[7]], world.player) and
             world.options.logic_difficulty.value >= 2)
        )
    ),
    EventNames.XP_Sector[3][4]: IjiLocData(
        region=RegNames.Sector4_Super[0],
        locked_item=lambda world: EventNames.XP[3][3]
    ),
    EventNames.XP_Sector[3][5]: IjiLocData(
        region=RegNames.Sector4_Super[1],
        locked_item=lambda world: EventNames.XP[3][3]
    ),
    EventNames.XP_Sector[3][6]: IjiLocData(
        region=RegNames.Sector4_Main[1],
        locked_item=lambda world: EventNames.XP[3][3]
    ),
    EventNames.XP_Sector[3][7]: IjiLocData(
        region=RegNames.Sector4_Main[1],
        locked_item=lambda world: EventNames.XP[3][2]
    ),
    EventNames.XP_Sector[3][8]: IjiLocData(
        region=RegNames.Sector4_Side[3],
        locked_item=lambda world: EventNames.XP[3][1]
    ),
    EventNames.XP_Sector[3][9]: IjiLocData(
        region=RegNames.Sector4_Main[2],
        locked_item=lambda world: EventNames.XP[3][5]
    ),
    EventNames.XP_Sector[3][10]: IjiLocData(
        region=RegNames.Sector4_Main[3],
        locked_item=lambda world: EventNames.XP[3][3]
    ),
    EventNames.XP_Sector[3][11]: IjiLocData(
        region=RegNames.Sector4_Main[3],
        locked_item=lambda world: EventNames.XP[3][3],
        logic=lambda world, state: (
            has_stats(state, world, ItemNames.Stat_Crack, 2)
        )
    ),
    EventNames.XP_Sector[3][12]: IjiLocData(
        region=RegNames.Sector4_Main[4],
        locked_item=lambda world: EventNames.XP[3][2]
    ),
    EventNames.XP_Sector[3][13]: IjiLocData(
        region=RegNames.Sector4_Main[6],
        locked_item=lambda world: EventNames.XP[3][3]
    ),
    EventNames.XP_Sector[3][14]: IjiLocData(
        region=RegNames.Sector4_Poster[0],
        locked_item=lambda world: EventNames.XP[3][0]
    ),

    # Sector 5
    EventNames.XP_Sector[4][0]: IjiLocData(
        region=RegNames.Sector5_Main[0],
        locked_item=lambda world: EventNames.XP[4][3]
    ),
    EventNames.XP_Sector[4][1]: IjiLocData(
        region=RegNames.Sector5_Main[1],
        locked_item=lambda world: EventNames.XP[4][4],
        logic=lambda world, state: (
            state.has(ItemNames.Upgrade_Jump, world.player, 1)
        )
    ),
    EventNames.XP_Sector[4][2]: IjiLocData(
        region=RegNames.Sector5_Side[2],
        locked_item=lambda world: EventNames.XP[4][1],
        logic=lambda world, state: (
            has_stats(state, world, ItemNames.Stat_Crack, 1)
        )
    ),
    EventNames.XP_Sector[4][3]: IjiLocData(
        region=RegNames.Sector5_Main[2],
        locked_item=lambda world: EventNames.XP[4][5],
    ),
    EventNames.XP_Sector[4][4]: IjiLocData(
        region=RegNames.Sector5_Main[2],
        locked_item=lambda world: EventNames.XP[4][5]
    ),
    EventNames.XP_Sector[4][5]: IjiLocData(
        region=RegNames.Sector5_Poster[1],
        locked_item=lambda world: EventNames.XP[4][1]
    ),
    EventNames.XP_Sector[4][6]: IjiLocData(
        region=RegNames.Sector5_Poster[2],
        locked_item=lambda world: EventNames.XP[4][4]
    ),
    EventNames.XP_Sector[4][7]: IjiLocData(
        region=RegNames.Sector5_Main[3],
        locked_item=lambda world: EventNames.XP[4][4]
    ),
    EventNames.XP_Sector[4][8]: IjiLocData(
        region=RegNames.Sector5_Main[3],
        locked_item=lambda world: EventNames.XP[4][3]
    ),
    EventNames.XP_Sector[4][9]: IjiLocData(
        region=RegNames.Sector5_Main[4],
        locked_item=lambda world: EventNames.XP[4][4]
    ),
    EventNames.XP_Sector[4][10]: IjiLocData(
        region=RegNames.Sector5_Main[5],
        locked_item=lambda world: EventNames.XP[4][4]
    ),
    EventNames.XP_Sector[4][11]: IjiLocData(
        region=RegNames.Sector5_Side[7],
        locked_item=lambda world: EventNames.XP[4][3]
    ),

    # Sector 6
    EventNames.XP_Sector[5][0]: IjiLocData(
        region=RegNames.Sector6_Main[0],
        locked_item=lambda world: EventNames.XP[5][1]
    ),
    EventNames.XP_Sector[5][1]: IjiLocData(
        region=RegNames.Sector6_Side[1],
        locked_item=lambda world: EventNames.XP[5][3]
    ),
    EventNames.XP_Sector[5][2]: IjiLocData(
        region=RegNames.Sector6_Side[2],
        locked_item=lambda world: EventNames.XP[5][2]
    ),
    EventNames.XP_Sector[5][3]: IjiLocData(
        region=RegNames.Sector6_Side[5],
        locked_item=lambda world: EventNames.XP[5][4]
    ),
    EventNames.XP_Sector[5][4]: IjiLocData(
        region=RegNames.Sector6_Main[1],
        locked_item=lambda world: EventNames.XP[5][4]
    ),
    EventNames.XP_Sector[5][5]: IjiLocData(
        region=RegNames.Sector6_Side[4],
        locked_item=lambda world: EventNames.XP[5][2]
    ),
    EventNames.XP_Sector[5][6]: IjiLocData(
        region=RegNames.Sector6_Main[3],
        locked_item=lambda world: EventNames.XP[5][3]
    ),
    EventNames.XP_Sector[5][7]: IjiLocData(
        region=RegNames.Sector6_Side[7],
        locked_item=lambda world: EventNames.XP[5][2],
        logic=lambda world, state: has_stats(state, world, ItemNames.Stat_Crack, 3)
    ),
    EventNames.XP_Sector[5][8]: IjiLocData(
        region=RegNames.Sector6_Main[4],
        locked_item=lambda world: EventNames.XP[5][5]
    ),
    EventNames.XP_Sector[5][9]: IjiLocData(
        region=RegNames.Sector6_Main[4],
        locked_item=lambda world: EventNames.XP[5][4]
    ),
    EventNames.XP_Sector[5][10]: IjiLocData(
        region=RegNames.Sector6_Main[4],
        locked_item=lambda world: EventNames.XP[5][3]
    ),
    EventNames.XP_Sector[5][11]: IjiLocData(
        region=RegNames.Sector6_Side[15],
        locked_item=lambda world: EventNames.XP[5][1]
    ),
    EventNames.XP_Sector[5][12]: IjiLocData(
        region=RegNames.Sector6_Poster[0],
        locked_item=lambda world: EventNames.XP[5][2]
    ),
    EventNames.XP_Sector[5][13]: IjiLocData(
        region=RegNames.Sector6_Poster[1],
        locked_item=lambda world: EventNames.XP[5][2]
    ),
    EventNames.XP_Sector[5][14]: IjiLocData(
        region=RegNames.Sector6_Poster[2],
        locked_item=lambda world: EventNames.XP[5][2]
    ),
    EventNames.XP_Sector[5][15]: IjiLocData(
        region=RegNames.Sector6_Side[8],
        locked_item=lambda world: EventNames.XP[5][3]
    ),
    EventNames.XP_Sector[5][16]: IjiLocData(
        region=RegNames.Sector6_Main[5],
        locked_item=lambda world: EventNames.XP[5][2]
    ),
    EventNames.XP_Sector[5][17]: IjiLocData(
        region=RegNames.Sector6_Main[6],
        locked_item=lambda world: EventNames.XP[5][2]
    ),
    EventNames.XP_Sector[5][18]: IjiLocData(
        region=RegNames.Sector6_Main[7],
        locked_item=lambda world: EventNames.XP[5][3],
        logic=lambda world, state: state.has(ItemNames.Upgrade_Jump, world.player, 2)
    ),
    EventNames.XP_Sector[5][19]: IjiLocData(
        region=RegNames.Sector6_Side[11],
        locked_item=lambda world: EventNames.XP[5][4],
        logic=lambda world, state: state.has(ItemNames.Upgrade_Jump, world.player, 2)
    ),
    EventNames.XP_Sector[5][20]: IjiLocData(
        region=RegNames.Sector6_Main[12],
        locked_item=lambda world: EventNames.XP[5][3]
    ),
    EventNames.XP_Sector[5][21]: IjiLocData(
        region=RegNames.Sector6_Side[12],
        locked_item=lambda world: EventNames.XP[5][2]
    ),
    EventNames.XP_Sector[5][22]: IjiLocData(
        region=RegNames.Sector6_Side[13],
        locked_item=lambda world: EventNames.XP[5][4]
    ),

    # Sector 7
    EventNames.XP_Sector[6][0]: IjiLocData(
        region=RegNames.Sector7_Main[1],
        locked_item=lambda world: EventNames.XP[6][3]
    ),
    EventNames.XP_Sector[6][1]: IjiLocData(
        region=RegNames.Sector7_Main[1],
        locked_item=lambda world: EventNames.XP[6][4]
    ),
    EventNames.XP_Sector[6][2]: IjiLocData(
        region=RegNames.Sector7_Main[2],
        locked_item=lambda world: EventNames.XP[6][3]
    ),
    EventNames.XP_Sector[6][3]: IjiLocData(
        region=RegNames.Sector7_Main[2],
        locked_item=lambda world: EventNames.XP[6][2]
    ),
    EventNames.XP_Sector[6][4]: IjiLocData(
        region=RegNames.Sector7_Main[3],
        locked_item=lambda world: EventNames.XP[6][5]
    ),
    EventNames.XP_Sector[6][5]: IjiLocData(
        region=RegNames.Sector7_Main[3],
        locked_item=lambda world: EventNames.XP[6][4]
    ),
    EventNames.XP_Sector[6][6]: IjiLocData(
        region=RegNames.Sector7_Side[4],
        locked_item=lambda world: EventNames.XP[6][2]
    ),
    EventNames.XP_Sector[6][7]: IjiLocData(
        region=RegNames.Sector7_Side[6],
        locked_item=lambda world: EventNames.XP[6][1]
    ),
    EventNames.XP_Sector[6][8]: IjiLocData(
        region=RegNames.Sector7_Main[4],
        locked_item=lambda world: EventNames.XP[6][4]
    ),
    EventNames.XP_Sector[6][9]: IjiLocData(
        region=RegNames.Sector7_Main[5],
        locked_item=lambda world: EventNames.XP[6][4]
    ),
    EventNames.XP_Sector[6][10]: IjiLocData(
        region=RegNames.Sector7_Side[8],
        locked_item=lambda world: EventNames.XP[6][2]
    ),
    EventNames.XP_Sector[6][11]: IjiLocData(
        region=RegNames.Sector7_Side[9],
        locked_item=lambda world: EventNames.XP[6][2]
    ),
    EventNames.XP_Sector[6][12]: IjiLocData(
        region=RegNames.Sector7_Main[7],
        locked_item=lambda world: EventNames.XP[6][3]
    ),
    EventNames.XP_Sector[6][13]: IjiLocData(
        region=RegNames.Sector7_Main[8],
        locked_item=lambda world: EventNames.XP[6][4]
    ),
    EventNames.XP_Sector[6][14]: IjiLocData(
        region=RegNames.Sector7_Main[9],
        locked_item=lambda world: EventNames.XP[6][4]
    ),
    EventNames.XP_Sector[6][15]: IjiLocData(
        region=RegNames.Sector7_Main[10],
        locked_item=lambda world: EventNames.XP[6][5]
    ),
    EventNames.XP_Sector[6][16]: IjiLocData(
        region=RegNames.Sector7_Side[12],
        locked_item=lambda world: EventNames.XP[6][1]
    ),
    EventNames.XP_Sector[6][17]: IjiLocData(
        region=RegNames.Sector7_Ribbon,
        locked_item=lambda world: EventNames.XP[6][5]
    ),

    # Sector 8
    EventNames.XP_Sector[7][0]: IjiLocData(
        region=RegNames.Sector8_Main[1],
        locked_item=lambda world: EventNames.XP[7][5]
    ),
    EventNames.XP_Sector[7][1]: IjiLocData(
        region=RegNames.Sector8_Side[0],
        locked_item=lambda world: EventNames.XP[7][3]
    ),
    EventNames.XP_Sector[7][2]: IjiLocData(
        region=RegNames.Sector8_Side[1],
        locked_item=lambda world: EventNames.XP[7][3]
    ),
    EventNames.XP_Sector[7][3]: IjiLocData(
        region=RegNames.Sector8_Side[2],
        locked_item=lambda world: EventNames.XP[7][4]
    ),
    EventNames.XP_Sector[7][4]: IjiLocData(
        region=RegNames.Sector8_Main[2],
        locked_item=lambda world: EventNames.XP[7][5]
    ),
    EventNames.XP_Sector[7][5]: IjiLocData(
        region=RegNames.Sector8_Main[2],
        locked_item=lambda world: EventNames.XP[7][5]
    ),
    EventNames.XP_Sector[7][6]: IjiLocData(
        region=RegNames.Sector8_Main[2],
        locked_item=lambda world: EventNames.XP[7][5],
        logic=lambda world, state: can_kill_annihilators(state, world)
    ),
    EventNames.XP_Sector[7][7]: IjiLocData(
        region=RegNames.Sector8_Side[3],
        locked_item=lambda world: EventNames.XP[7][2]
    ),
    EventNames.XP_Sector[7][8]: IjiLocData(
        region=RegNames.Sector8_Main[2],
        locked_item=lambda world: EventNames.XP[7][4],
        logic=lambda world, state: has_stats(state, world, ItemNames.Stat_Crack, 4)
    ),
    EventNames.XP_Sector[7][9]: IjiLocData(
        region=RegNames.Sector8_Main[3],
        locked_item=lambda world: EventNames.XP[7][5]
    ),
    EventNames.XP_Sector[7][10]: IjiLocData(
        region=RegNames.Sector8_Main[3],
        locked_item=lambda world: EventNames.XP[7][5]
    ),
    EventNames.XP_Sector[7][11]: IjiLocData(
        region=RegNames.Sector8_Main[3],
        locked_item=lambda world: EventNames.XP[7][5]
    ),
    EventNames.XP_Sector[7][12]: IjiLocData(
        region=RegNames.Sector8_Main[3],
        locked_item=lambda world: EventNames.XP[7][4],
        logic=lambda world, state: can_kill_annihilators(state, world)
    ),
    EventNames.XP_Sector[7][13]: IjiLocData(
        region=RegNames.Sector8_Side[4],
        locked_item=lambda world: EventNames.XP[7][2]
    ),
    EventNames.XP_Sector[7][14]: IjiLocData(
        region=RegNames.Sector8_Side[5],
        locked_item=lambda world: EventNames.XP[7][2]
    ),

    # Sector 9
    EventNames.XP_Sector[8][0]: IjiLocData(
        region=RegNames.Sector9_Main[0],
        locked_item=lambda world: EventNames.XP[8][3]
    ),
    EventNames.XP_Sector[8][1]: IjiLocData(
        region=RegNames.Sector9_Side[12],
        locked_item=lambda world: EventNames.XP[8][1],
        logic=lambda world, state: has_stats(state, world, ItemNames.Stat_Crack, 1)
    ),
    EventNames.XP_Sector[8][2]: IjiLocData(
        region=RegNames.Sector9_Side[1],
        locked_item=lambda world: EventNames.XP[8][3]
    ),
    EventNames.XP_Sector[8][3]: IjiLocData(
        region=RegNames.Sector9_Main[1],
        locked_item=lambda world: EventNames.XP[8][3]
    ),
    EventNames.XP_Sector[8][4]: IjiLocData(
        region=RegNames.Sector9_Main[1],
        locked_item=lambda world: EventNames.XP[8][4],
        logic=lambda world, state: state.has(ItemNames.Upgrade_Jump, world.player, 2)
    ),
    EventNames.XP_Sector[8][5]: IjiLocData(
        region=RegNames.Sector9_Main[2],
        locked_item=lambda world: EventNames.XP[8][4]
    ),
    EventNames.XP_Sector[8][6]: IjiLocData(
        region=RegNames.Sector9_Main[3],
        locked_item=lambda world: EventNames.XP[8][5]
    ),
    EventNames.XP_Sector[8][7]: IjiLocData(
        region=RegNames.Sector9_Main[3],
        locked_item=lambda world: EventNames.XP[8][5]
    ),
    EventNames.XP_Sector[8][8]: IjiLocData(
        region=RegNames.Sector9_Main[3],
        locked_item=lambda world: EventNames.XP[8][4],
        logic=lambda world, state: can_kill_annihilators(state, world)
    ),
    EventNames.XP_Sector[8][9]: IjiLocData(
        region=RegNames.Sector9_Side[13],
        locked_item=lambda world: EventNames.XP[8][3]
    ),
    EventNames.XP_Sector[8][10]: IjiLocData(
        region=RegNames.Sector9_Bulkhead[1],
        locked_item=lambda world: EventNames.XP[8][2]
    ),
    EventNames.XP_Sector[8][11]: IjiLocData(
        region=RegNames.Sector9_Bulkhead[2],
        locked_item=lambda world: EventNames.XP[8][2]
    ),
    EventNames.XP_Sector[8][12]: IjiLocData(
        region=RegNames.Sector9_Bulkhead[3],
        locked_item=lambda world: EventNames.XP[8][3]
    ),
    EventNames.XP_Sector[8][13]: IjiLocData(
        region=RegNames.Sector9_Main[4],
        locked_item=lambda world: EventNames.XP[8][4]
    ),
    EventNames.XP_Sector[8][14]: IjiLocData(
        region=RegNames.Sector9_Poster[0],
        locked_item=lambda world: EventNames.XP[8][3]
    ),
    EventNames.XP_Sector[8][15]: IjiLocData(
        region=RegNames.Sector9_Main[5],
        locked_item=lambda world: EventNames.XP[8][1]
    ),
    EventNames.XP_Sector[8][16]: IjiLocData(
        region=RegNames.Sector9_Side[14],
        locked_item=lambda world: EventNames.XP[8][3]
    ),
    EventNames.XP_Sector[8][17]: IjiLocData(
        region=RegNames.Sector9_Main[6],
        locked_item=lambda world: EventNames.XP[8][5]
    ),
    EventNames.XP_Sector[8][18]: IjiLocData(
        region=RegNames.Sector9_Main[9],
        locked_item=lambda world: EventNames.XP[8][3]
    ),
    EventNames.XP_Sector[8][19]: IjiLocData(
        region=RegNames.Sector9_Main[9],
        locked_item=lambda world: EventNames.XP[8][4],
        logic=lambda world, state: can_kill_annihilators(state, world)
    ),
    EventNames.XP_Sector[8][20]: IjiLocData(
        region=RegNames.Sector9_Main[10],
        locked_item=lambda world: EventNames.XP[8][2]
    ),
    EventNames.XP_Sector[8][21]: IjiLocData(
        region=RegNames.Sector9_Side[9],
        locked_item=lambda world: EventNames.XP[8][5]
    ),
    EventNames.XP_Sector[8][22]: IjiLocData(
        region=RegNames.Sector9_Main[13],
        locked_item=lambda world: EventNames.XP[8][3]
    ),
    EventNames.XP_Sector[8][23]: IjiLocData(
        region=RegNames.Sector9_Deep[9],
        locked_item=lambda world: EventNames.XP[8][3]
    ),
    EventNames.XP_Sector[8][24]: IjiLocData(
        region=RegNames.Sector9_Deep[8],
        locked_item=lambda world: EventNames.XP[8][4]
    ),

    # Sector X
    EventNames.XP_Sector[9][0]: IjiLocData(
        region=RegNames.SectorX_Main[1],
        locked_item=lambda world: EventNames.XP[9][4]
    ),
    EventNames.XP_Sector[9][1]: IjiLocData(
        region=RegNames.SectorX_Main[1],
        locked_item=lambda world: EventNames.XP[9][4],
        logic=lambda world, state: can_kill_annihilators(state, world)
    ),
    EventNames.XP_Sector[9][2]: IjiLocData(
        region=RegNames.SectorX_Main[2],
        locked_item=lambda world: EventNames.XP[9][3]
    ),
    EventNames.XP_Sector[9][3]: IjiLocData(
        region=RegNames.SectorX_Poster[0],
        locked_item=lambda world: EventNames.XP[9][3]
    ),
    EventNames.XP_Sector[9][4]: IjiLocData(
        region=RegNames.SectorX_Poster[1],
        locked_item=lambda world: EventNames.XP[9][2]
    ),
    EventNames.XP_Sector[9][5]: IjiLocData(
        region=RegNames.SectorX_Main[5],
        locked_item=lambda world: EventNames.XP[9][4]
    ),
    EventNames.XP_Sector[9][6]: IjiLocData(
        region=RegNames.SectorX_Core[1],
        locked_item=lambda world: EventNames.XP[9][5],
        logic=lambda world, state: state.has(EventNames.SectorX_Terminal_Megacore[0], world.player)
    ),
    EventNames.XP_Sector[9][7]: IjiLocData(
        region=RegNames.SectorX_Core[1],
        locked_item=lambda world: EventNames.XP[9][4],
        logic=lambda world, state: (
            state.has(EventNames.SectorX_Terminal_Megacore[0], world.player) and
            can_kill_annihilators(state, world)
        )
    ),
    EventNames.XP_Sector[9][8]: IjiLocData(
        region=RegNames.SectorX_Core[4],
        locked_item=lambda world: EventNames.XP[9][4]
    ),
    EventNames.XP_Sector[9][9]: IjiLocData(
        region=RegNames.SectorX_Core[5],
        locked_item=lambda world: EventNames.XP[9][2]
    ),
    EventNames.XP_Sector[9][10]: IjiLocData(
        region=RegNames.SectorX_Main[7],
        locked_item=lambda world: EventNames.XP[9][2],
        logic=lambda world, state: has_stats(state, world, ItemNames.Stat_Crack, 6)
    ),
    EventNames.XP_Sector[9][11]: IjiLocData(
        region=RegNames.SectorX_Main[8],
        locked_item=lambda world: EventNames.XP[9][3]
    ),
    EventNames.XP_Sector[9][12]: IjiLocData(
        region=RegNames.SectorX_Main[12],
        locked_item=lambda world: EventNames.XP[9][2]
    ),
    EventNames.XP_Sector[9][13]: IjiLocData(
        region=RegNames.SectorX_Main[9],
        locked_item=lambda world: EventNames.XP[9][3]
    ),
    EventNames.XP_Sector[9][14]: IjiLocData(
        region=RegNames.SectorX_Main[10],
        locked_item=lambda world: EventNames.XP[9][3]
    ),
    EventNames.XP_Sector[9][15]: IjiLocData(
        region=RegNames.SectorX_Side[1],
        locked_item=lambda world: EventNames.XP[9][2]
    ),
    EventNames.XP_Sector[9][16]: IjiLocData(
        region=RegNames.SectorX_Main[11],
        locked_item=lambda world: EventNames.XP[9][3]
    ),
    EventNames.XP_Sector[9][17]: IjiLocData(
        region=RegNames.SectorX_Final[0],
        locked_item=lambda world: EventNames.XP[9][4]
    ),
    EventNames.XP_Sector[9][18]: IjiLocData(
        region=RegNames.SectorX_Final[0],
        locked_item=lambda world: EventNames.XP[9][4],
        logic=lambda world, state: can_kill_annihilators(state, world)
    ),
    EventNames.XP_Sector[9][19]: IjiLocData(
        region=RegNames.SectorX_Side[3],
        locked_item=lambda world: EventNames.XP[9][2]
    ),
    EventNames.XP_Sector[9][20]: IjiLocData(
        region=RegNames.SectorX_Final[1],
        locked_item=lambda world: EventNames.XP[9][3]
    ),
    EventNames.XP_Sector[9][21]: IjiLocData(
        region=RegNames.SectorX_Final[2],
        locked_item=lambda world: EventNames.XP[9][3]
    ),
    EventNames.XP_Sector[9][22]: IjiLocData(
        region=RegNames.SectorX_Side[5],
        locked_item=lambda world: EventNames.XP[9][5]
    ),
    EventNames.XP_Sector[9][23]: IjiLocData(
        region=RegNames.SectorX_Final[3],
        locked_item=lambda world: EventNames.XP[9][5]
    ),
    EventNames.XP_Sector[9][24]: IjiLocData(
        region=RegNames.SectorX_Final[3],
        locked_item=lambda world: EventNames.XP[9][5]
    ),
    EventNames.XP_Sector[9][25]: IjiLocData(
        region=RegNames.SectorX_Final[3],
        locked_item=lambda world: EventNames.XP[9][4],
        logic=lambda world, state: can_kill_annihilators(state, world)
    )
}

events_poster: Dict[str, IjiLocData] = {
    EventNames.Posters[1]: IjiLocData(
        region=RegNames.Sector1_Poster,
        locked_item=lambda world: EventNames.Posters[0]
    ),
    EventNames.Posters[2]: IjiLocData(
        region=RegNames.Sector2_Poster,
        locked_item=lambda world: EventNames.Posters[0]
    ),
    EventNames.Posters[3]: IjiLocData(
        region=RegNames.Sector3_Poster[1],
        locked_item=lambda world: EventNames.Posters[0]
    ),
    EventNames.Posters[4]: IjiLocData(
        region=RegNames.Sector4_Poster[1],
        locked_item=lambda world: EventNames.Posters[0]
    ),
    EventNames.Posters[5]: IjiLocData(
        region=RegNames.Sector5_Poster[2],
        locked_item=lambda world: EventNames.Posters[0]
    ),
    EventNames.Posters[6]: IjiLocData(
        region=RegNames.Sector6_Poster[3],
        locked_item=lambda world: EventNames.Posters[0]
    ),
    EventNames.Posters[7]: IjiLocData(
        region=RegNames.Sector7_Poster,
        locked_item=lambda world: EventNames.Posters[0]
    ),
    EventNames.Posters[8]: IjiLocData(
        region=RegNames.Sector8_Poster,
        locked_item=lambda world: EventNames.Posters[0]
    ),
    EventNames.Posters[9]: IjiLocData(
        region=RegNames.Sector9_Poster[2],
        locked_item=lambda world: EventNames.Posters[0]
    ),
    EventNames.Posters[10]:IjiLocData(
        region=RegNames.SectorX_Poster[3],
        locked_item=lambda world: EventNames.Posters[0]
    ),
}

events_supercharges: Dict[str, IjiLocData] = {
    EventNames.Supercharges[0]: IjiLocData(
        region=RegNames.Sector1_Super,
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.supercharge_locations.value <= 1
    ),
    EventNames.Supercharges[1]: IjiLocData(
        region=RegNames.Sector2_Super,
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.supercharge_locations.value <= 1
    ),
    EventNames.Supercharges[2]: IjiLocData(
        region=RegNames.Sector3_Super[1],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.supercharge_locations.value <= 1
    ),
    EventNames.Supercharges[3]: IjiLocData(
        region=RegNames.Sector4_Super[2],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.supercharge_locations.value <= 1
    ),
    EventNames.Supercharges[4]: IjiLocData(
        region=RegNames.Sector5_Main[8],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.supercharge_locations.value <= 1,
        logic=lambda world, state: location_table[LocNames.Supercharges[4]].logic(world, state)
    ),
    EventNames.Supercharges[5]: IjiLocData(
        region=RegNames.Sector6_Super,
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.supercharge_locations.value <= 1
    ),
    EventNames.Supercharges[6]: IjiLocData(
        region=RegNames.Sector7_Main[11],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.supercharge_locations.value <= 1,
        logic=lambda world, state: location_table[LocNames.Supercharges[6]].logic(world, state)
    ),
    EventNames.Supercharges[7]: IjiLocData(
        region=RegNames.Sector8_Side[3],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.supercharge_locations.value <= 1,
        logic=lambda world, state: location_table[LocNames.Supercharges[7]].logic(world, state)
    ),
    EventNames.Supercharges[8]: IjiLocData(
        region=RegNames.Sector9_Deep,
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.supercharge_locations.value <= 1
    ),
    EventNames.Supercharges[9]: IjiLocData(
        region=RegNames.SectorX_Core[0],
        locked_item=lambda world: EventNames.Levels[0],
        valid=lambda world: world.options.supercharge_locations.value <= 1,
        logic=lambda world, state: location_table[LocNames.Supercharges[9]].logic(world, state)
    ),
}

events_weapons: Dict[str, IjiLocData] = {
    EventNames.Weapons[0]:  IjiLocData(
        region=RegNames.SectorZ_Null,
        locked_item=lambda world: EventNames.Weapons[0]
    ),
    EventNames.Weapons[1]: IjiLocData(
        region=RegNames.Global,
        locked_item=lambda world: EventNames.Weapons[1]
    ),
    EventNames.Weapons[9]:  IjiLocData(
        region=RegNames.Global,
        locked_item=lambda world: EventNames.Weapons[9],
        logic=lambda world, state: location_table[LocNames.Weapons_Combined[0]].logic(world, state)
    ),
    EventNames.Weapons[10]: IjiLocData(
        region=RegNames.Global,
        locked_item=lambda world: EventNames.Weapons[10],
        valid=lambda world: location_table[LocNames.Weapons_Combined[1]].valid(world),
        logic=lambda world, state: location_table[LocNames.Weapons_Combined[1]].logic(world, state)
    ),
    EventNames.Weapons[11]: IjiLocData(
        region=RegNames.Global,
        locked_item=lambda world: EventNames.Weapons[11],
        logic=lambda world, state: location_table[LocNames.Weapons_Combined[2]].logic(world, state)
    ),
    EventNames.Weapons[12]: IjiLocData(
        region=RegNames.Global,
        locked_item=lambda world: EventNames.Weapons[12],
        valid=lambda world: location_table[LocNames.Weapons_Combined[3]].valid(world),
        logic=lambda world, state: location_table[LocNames.Weapons_Combined[3]].logic(world, state)
    ),
    EventNames.Weapons[13]: IjiLocData(
        region=RegNames.Global,
        locked_item=lambda world: EventNames.Weapons[13],
        logic=lambda world, state: location_table[LocNames.Weapons_Combined[4]].logic(world, state)
    ),
    EventNames.Weapons[14]: IjiLocData(
        region=RegNames.Global,
        locked_item=lambda world: EventNames.Weapons[14],
        logic=lambda world, state: location_table[LocNames.Weapons_Combined[5]].logic(world, state)
    ),
    EventNames.Weapons[15]: IjiLocData(
        region=RegNames.Global,
        locked_item=lambda world: EventNames.Weapons[15],
        valid=lambda world: location_table[LocNames.Weapons_Combined[6]].valid(world),
        logic=lambda world, state: location_table[LocNames.Weapons_Combined[6]].logic(world, state)
    ),
    EventNames.Weapons[16]: IjiLocData(
        region=RegNames.Global,
        locked_item=lambda world: EventNames.Weapons[16],
        valid=lambda world: location_table[LocNames.Weapons_Combined[7]].valid(world),
        logic=lambda world, state: location_table[LocNames.Weapons_Combined[7]].logic(world, state)
    ),
    EventNames.Weapons[17]: IjiLocData(
        region=RegNames.Sector9_Poster[3],
        locked_item=lambda world: EventNames.Weapons[17],
        logic=lambda world, state: location_table[LocNames.Weapon_Banana].logic(world, state)
    ),

    EventNames.Weapon_Locations[0][0][0]: IjiLocData(
        region=RegNames.Sector1_Main[2],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[0][0]].logic(world, state)
    ),

    EventNames.Weapon_Locations[1][0][0]: IjiLocData(
        region=RegNames.Sector2_Main[2],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[1][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[1][1][0]: IjiLocData(
        region=RegNames.Sector2_Side[1],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[1][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[1][2][0]: IjiLocData(
        region=RegNames.Sector2_Main[1],
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[1][2]].logic(world, state)
    ),

    EventNames.Weapon_Locations[2][0][0]: IjiLocData(
        region=RegNames.Sector3_Main[0],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[0][0][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[2][0][1]: IjiLocData(
        region=RegNames.Sector3_Main[1],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[0][0][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[2][0][2]: IjiLocData(
        region=RegNames.Sector3_Main[3],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[0][0][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[2][1][0]: IjiLocData(
        region=RegNames.Sector3_Main[1],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[0][1][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[2][1][1]: IjiLocData(
        region=RegNames.Sector3_Main[3],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[0][1][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[2][2][0]: IjiLocData(
        region=RegNames.Sector3_Main[2],
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[2][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[2][3][0]: IjiLocData(
        region=RegNames.Sector3_Side[10],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[2][3]].logic(world, state)
    ),

    EventNames.Weapon_Locations[3][0][0]: IjiLocData(
        region=RegNames.Sector4_Main[1],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[3][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[3][1][0]: IjiLocData(
        region=RegNames.Sector4_Main[0],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[1][0][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[3][1][1]: IjiLocData(
        region=RegNames.Sector4_Main[2],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[1][0][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[3][2][0]: IjiLocData(
        region=RegNames.Sector4_Super[2],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[3][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[3][3][0]: IjiLocData(
        region=RegNames.Sector4_Main[0],
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[3][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[3][4][0]: IjiLocData(
        region=RegNames.Sector4_Main[2],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[3][4]].logic(world, state)
    ),

    EventNames.Weapon_Locations[4][0][0]: IjiLocData(
        region=RegNames.Sector5_Main[1],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[2][0][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[4][0][1]: IjiLocData(
        region=RegNames.Sector5_Main[3],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[2][0][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[4][1][0]: IjiLocData(
        region=RegNames.Sector5_Main[1],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[2][1][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[4][1][1]: IjiLocData(
        region=RegNames.Sector5_Main[2],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[2][1][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[4][2][0]: IjiLocData(
        region=RegNames.Sector5_Main[6],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[4][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[4][3][0]: IjiLocData(
        region=RegNames.Sector5_Ribbon,
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[4][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[4][4][0]: IjiLocData(
        region=RegNames.Sector5_Main[2],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[2][2][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[4][4][1]: IjiLocData(
        region=RegNames.Sector5_Main[2],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[2][2][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[4][4][2]: IjiLocData(
        region=RegNames.Sector5_Ribbon,
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[2][2][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[4][5][0]: IjiLocData(
        region=RegNames.Sector5_Side[5],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[4][5]].logic(world, state)
    ),

    EventNames.Weapon_Locations[5][0][0]: IjiLocData(
        region=RegNames.Sector6_Main[4],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[3][0][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[5][0][1]: IjiLocData(
        region=RegNames.Sector6_Main[6],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[3][0][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[5][1][0]: IjiLocData(
        region=RegNames.Sector6_Main[4],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[3][1][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[5][1][1]: IjiLocData(
        region=RegNames.Sector6_Main[4],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[3][1][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[5][1][2]: IjiLocData(
        region=RegNames.Sector6_Ribbon,
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[3][1][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[5][2][0]: IjiLocData(
        region=RegNames.Sector6_Side[10],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[3][2][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[5][2][1]: IjiLocData(
        region=RegNames.Sector6_Poster[2],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[3][2][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[5][3][0]: IjiLocData(
        region=RegNames.Sector6_Main[3],
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[5][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[5][4][0]: IjiLocData(
        region=RegNames.Sector6_Main[4],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[3][3][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[5][4][1]: IjiLocData(
        region=RegNames.Sector6_Ribbon,
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[3][3][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[5][5][0]: IjiLocData(
        region=RegNames.Sector6_Side[3],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[3][4][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[5][5][1]: IjiLocData(
        region=RegNames.Sector6_Side[6],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[3][4][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[5][5][2]: IjiLocData(
        region=RegNames.Sector6_Ribbon,
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[3][4][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[5][6][0]: IjiLocData(
        region=RegNames.Sector6_Side[9],
        locked_item=lambda world: EventNames.Weapons[8],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[5][6]].logic(world, state)
    ),

    EventNames.Weapon_Locations[6][0][0]: IjiLocData(
        region=RegNames.Sector7_Main[3],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[6][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[6][1][0]: IjiLocData(
        region=RegNames.Sector7_Main[1],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[4][0][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[6][1][1]: IjiLocData(
        region=RegNames.Sector7_Main[3],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[4][0][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[6][1][2]: IjiLocData(
        region=RegNames.Sector7_Main[10],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[4][0][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[6][2][0]: IjiLocData(
        region=RegNames.Sector7_Main[3],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[6][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[6][3][0]: IjiLocData(
        region=RegNames.Sector7_Main[3],
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[4][1][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[6][3][1]: IjiLocData(
        region=RegNames.Sector7_Side[10],
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[4][1][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[6][4][0]: IjiLocData(
        region=RegNames.Sector7_Main[3],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[4][2][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[6][4][1]: IjiLocData(
        region=RegNames.Sector7_Ribbon,
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[4][2][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[6][5][0]: IjiLocData(
        region=RegNames.Sector7_Main[3],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[4][3][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[6][5][1]: IjiLocData(
        region=RegNames.Sector7_Side[10],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[4][3][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[6][5][2]: IjiLocData(
        region=RegNames.Sector7_Ribbon,
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[4][3][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[6][6][0]: IjiLocData(
        region=RegNames.Sector7_Side[6],
        locked_item=lambda world: EventNames.Weapons[8],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[6][6]].logic(world, state)
    ),

    EventNames.Weapon_Locations[7][0][0]: IjiLocData(
        region=RegNames.Sector8_Main[2],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[7][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[7][1][0]: IjiLocData(
        region=RegNames.Sector8_Main[2],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[5][0][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[7][1][1]: IjiLocData(
        region=RegNames.Sector8_Main[2],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[5][0][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[7][1][2]: IjiLocData(
        region=RegNames.Sector8_Main[3],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[5][0][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[7][2][0]: IjiLocData(
        region=RegNames.Sector8_Main[2],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[7][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[7][3][0]: IjiLocData(
        region=RegNames.Sector8_Main[2],
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[7][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[7][4][0]: IjiLocData(
        region=RegNames.Sector8_Main[2],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[5][1][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[7][4][1]: IjiLocData(
        region=RegNames.Sector8_Main[3],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[5][1][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[7][5][0]: IjiLocData(
        region=RegNames.Sector8_Main[1],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[5][2][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[7][5][1]: IjiLocData(
        region=RegNames.Sector8_Main[2],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[5][2][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[7][6][0]: IjiLocData(
        region=RegNames.Sector8_Main[3],
        locked_item=lambda world: EventNames.Weapons[8],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[7][6]].logic(world, state)
    ),

    EventNames.Weapon_Locations[8][0][0]: IjiLocData(
        region=RegNames.Sector9_Side[0],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][0][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][0][1]: IjiLocData(
        region=RegNames.Sector9_Main[4],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][0][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][0][2]: IjiLocData(
        region=RegNames.Sector9_Main[13],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][0][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][0][3]: IjiLocData(
        region=RegNames.Sector9_Poster[2],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][0][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][1][0]: IjiLocData(
        region=RegNames.Sector9_Main[2],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][1][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][1][1]: IjiLocData(
        region=RegNames.Sector9_Main[3],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][1][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][1][2]: IjiLocData(
        region=RegNames.Sector9_Main[6],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][1][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][1][3]: IjiLocData(
        region=RegNames.Sector9_Main[13],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][1][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][1][4]: IjiLocData(
        region=RegNames.Sector9_Poster[2],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][1][4]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][2][0]: IjiLocData(
        region=RegNames.Sector9_Main[2],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][2][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][2][1]: IjiLocData(
        region=RegNames.Sector9_Main[6],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][2][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][2][2]: IjiLocData(
        region=RegNames.Sector9_Main[13],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][2][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][2][3]: IjiLocData(
        region=RegNames.Sector9_Poster[2],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][2][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][3][0]: IjiLocData(
        region=RegNames.Sector9_Main[1],
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][3][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][3][1]: IjiLocData(
        region=RegNames.Sector9_Side[4],
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][3][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][3][2]: IjiLocData(
        region=RegNames.Sector9_Main[13],
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][3][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][3][3]: IjiLocData(
        region=RegNames.Sector9_Poster[2],
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][3][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][4][0]: IjiLocData(
        region=RegNames.Sector9_Main[2],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][4][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][4][1]: IjiLocData(
        region=RegNames.Sector9_Main[4],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][4][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][4][2]: IjiLocData(
        region=RegNames.Sector9_Main[13],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][4][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][4][3]: IjiLocData(
        region=RegNames.Sector9_Poster[2],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][4][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][5][0]: IjiLocData(
        region=RegNames.Sector9_Main[3],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][5][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][5][1]: IjiLocData(
        region=RegNames.Sector9_Side[14],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][5][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][5][2]: IjiLocData(
        region=RegNames.Sector9_Main[13],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][5][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][5][3]: IjiLocData(
        region=RegNames.Sector9_Poster[2],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][5][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][6][0]: IjiLocData(
        region=RegNames.Sector9_Main[4],
        locked_item=lambda world: EventNames.Weapons[8],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][6][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][6][1]: IjiLocData(
        region=RegNames.Sector9_Main[13],
        locked_item=lambda world: EventNames.Weapons[8],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][6][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[8][6][2]: IjiLocData(
        region=RegNames.Sector9_Poster[2],
        locked_item=lambda world: EventNames.Weapons[8],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[6][6][2]].logic(world, state)
    ),

    EventNames.Weapon_Locations[9][0][0]: IjiLocData(
        region=RegNames.SectorX_Main[2],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][0][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][0][1]: IjiLocData(
        region=RegNames.SectorX_Core[4],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][0][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][0][2]: IjiLocData(
        region=RegNames.SectorX_Final[3],
        locked_item=lambda world: EventNames.Weapons[2],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][0][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][1][0]: IjiLocData(
        region=RegNames.SectorX_Core[4],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][1][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][1][1]: IjiLocData(
        region=RegNames.SectorX_Main[11],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][1][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][1][2]: IjiLocData(
        region=RegNames.SectorX_Final[3],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][1][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][1][3]: IjiLocData(
        region=RegNames.SectorX_Main[2],
        locked_item=lambda world: EventNames.Weapons[3],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][1][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][2][0]: IjiLocData(
        region=RegNames.SectorX_Core[1],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][2][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][2][1]: IjiLocData(
        region=RegNames.SectorX_Main[11],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][2][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][2][2]: IjiLocData(
        region=RegNames.SectorX_Final[3],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][2][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][2][3]: IjiLocData(
        region=RegNames.SectorX_Side[0],
        locked_item=lambda world: EventNames.Weapons[4],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][2][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][3][0]: IjiLocData(
        region=RegNames.SectorX_Core[1],
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][3][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][3][1]: IjiLocData(
        region=RegNames.SectorX_Core[4],
        locked_item=lambda world: EventNames.Weapons[5],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][3][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][4][0]: IjiLocData(
        region=RegNames.SectorX_Main[2],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][4][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][4][1]: IjiLocData(
        region=RegNames.SectorX_Core[4],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][4][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][4][2]: IjiLocData(
        region=RegNames.SectorX_Main[11],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][4][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][4][3]: IjiLocData(
        region=RegNames.SectorX_Final[3],
        locked_item=lambda world: EventNames.Weapons[6],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][4][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][5][0]: IjiLocData(
        region=RegNames.SectorX_Main[4],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][5][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][5][1]: IjiLocData(
        region=RegNames.SectorX_Main[11],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][5][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][5][2]: IjiLocData(
        region=RegNames.SectorX_Final[3],
        locked_item=lambda world: EventNames.Weapons[7],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][5][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][6][0]: IjiLocData(
        region=RegNames.SectorX_Core[4],
        locked_item=lambda world: EventNames.Weapons[8],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][6][0]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][6][1]: IjiLocData(
        region=RegNames.SectorX_Main[6],
        locked_item=lambda world: EventNames.Weapons[8],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][6][1]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][6][2]: IjiLocData(
        region=RegNames.SectorX_Main[11],
        locked_item=lambda world: EventNames.Weapons[8],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][6][2]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][6][3]: IjiLocData(
        region=RegNames.SectorX_Final[3],
        locked_item=lambda world: EventNames.Weapons[8],
        logic=lambda world, state: location_table[LocNames.Weapons_All_Instances[7][6][3]].logic(world, state)
    ),
    EventNames.Weapon_Locations[9][7][0]: IjiLocData(
        region=RegNames.SectorX_Final[3],
        locked_item=lambda world: EventNames.Weapons[13],
        logic=lambda world, state: location_table[LocNames.Weapons_Per_Sector[9][7]].logic(world, state)
    )
}

events_miscellaneous: Dict[str, IjiLocData] = {
    EventNames.Sector4_Terminals: IjiLocData(
        region=RegNames.Sector4_Main[2],
        locked_item=lambda world: EventNames.Sector4_Terminals
    ),
    EventNames.Sector6_Shredders: IjiLocData(
        region=RegNames.Sector6_Side[2],
        locked_item=lambda world: EventNames.Sector6_Shredders
    ),
    EventNames.Sector6_Terminal_Poster: IjiLocData(
        region=RegNames.Sector6_Side[5],
        locked_item=lambda world: EventNames.Sector6_Terminal_Poster
    ),
    EventNames.Sector6_Terminal_BlackOps: IjiLocData(
        region=RegNames.Sector6_Main[7],
        locked_item=lambda world: EventNames.Sector6_Terminal_BlackOps
    ),
    EventNames.Sector6_Terminal_Ribbon: IjiLocData(
        region=RegNames.Sector6_Main[12],
        locked_item=lambda world: EventNames.Sector6_Terminal_Ribbon
    ),
    EventNames.Sector7_Terminal_CFIS: IjiLocData(
        region=RegNames.Sector7_Main[6],
        locked_item=lambda world: EventNames.Sector7_Terminal_CFIS
    ),
    EventNames.Sector8_Terminal_AnnihilatorBeta: IjiLocData(
        region=RegNames.Sector8_Main[3],
        locked_item=lambda world: EventNames.Sector8_Terminal_AnnihilatorBeta
    ),
    EventNames.Sector9_Bulkhead[0]: IjiLocData(
        region=RegNames.Sector9_Bulkhead[0],
        locked_item=lambda world: EventNames.Sector9_Bulkhead[0]
    ),
    EventNames.Sector9_Bulkhead[1]: IjiLocData(
        region=RegNames.Sector9_Bulkhead[1],
        locked_item=lambda world: EventNames.Sector9_Bulkhead[1]
    ),
    EventNames.Sector9_Bulkhead[2]: IjiLocData(
        region=RegNames.Sector9_Bulkhead[2],
        locked_item=lambda world: EventNames.Sector9_Bulkhead[2]
    ),
    EventNames.Sector9_Bulkhead[3]: IjiLocData(
        region=RegNames.Sector9_Bulkhead[3],
        locked_item=lambda world: EventNames.Sector9_Bulkhead[3]
    ),
    EventNames.SectorX_Terminal_Megacore[0]: IjiLocData(
        region=RegNames.SectorX_Core[8],
        locked_item=lambda world: EventNames.SectorX_Terminal_Megacore[0]
    ),
    EventNames.SectorX_Terminal_Megacore[1]: IjiLocData(
        region=RegNames.SectorX_Core[2],
        locked_item=lambda world: EventNames.SectorX_Terminal_Megacore[1]
    ),
    EventNames.SectorX_Terminal_Megacore[2]: IjiLocData(
        region=RegNames.SectorX_Core[3],
        locked_item=lambda world: EventNames.SectorX_Terminal_Megacore[2]
    ),
    EventNames.SectorX_Megacore: IjiLocData(
        region=RegNames.SectorX_Core[0],
        locked_item=lambda world: EventNames.SectorX_Megacore,
        logic=lambda world, state: (
            state.has(EventNames.Weapons[16], world.player) or
            state.has_all([EventNames.SectorX_Terminal_Megacore[0],
            EventNames.SectorX_Terminal_Megacore[1],
            EventNames.SectorX_Terminal_Megacore[2]], world.player))
    )
}

event_loc_table = {
    **events_levels,
    **events_supercharges,
    **events_miscellaneous,
    **events_poster,
    **events_weapons,
    **events_xp,
}

event_item_table = {
    EventNames.Weapons[0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[1]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[2]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[3]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[4]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[5]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[6]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[7]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[8]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[9]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[10]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[11]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[12]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[13]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[14]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[15]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[16]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[17]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Weapons[18]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Posters[0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[0][0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[0][1]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[0][2]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[0][3]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[0][4]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[0][5]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[1][0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[1][1]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[1][2]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[1][3]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[1][4]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[1][5]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[2][0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[2][1]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[2][2]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[2][3]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[2][4]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[2][5]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[3][0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[3][1]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[3][2]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[3][3]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[3][4]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[3][5]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[4][0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[4][1]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[4][2]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[4][3]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[4][4]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[4][5]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[5][0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[5][1]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[5][2]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[5][3]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[5][4]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[5][5]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[6][0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[6][1]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[6][2]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[6][3]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[6][4]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[6][5]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[7][0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[7][1]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[7][2]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[7][3]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[7][4]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[7][5]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[8][0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[8][1]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[8][2]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[8][3]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[8][4]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[8][5]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[9][0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[9][1]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[9][2]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[9][3]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[9][4]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.XP[9][5]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Levels[0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Sector4_Terminals: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Sector6_Shredders: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Sector6_Terminal_Poster: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Sector6_Terminal_BlackOps: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Sector6_Terminal_Ribbon: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Sector7_Terminal_CFIS: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Sector8_Terminal_AnnihilatorBeta: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Sector9_Bulkhead[0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Sector9_Bulkhead[1]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Sector9_Bulkhead[2]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Sector9_Bulkhead[3]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.SectorX_Terminal_Megacore[0]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.SectorX_Terminal_Megacore[1]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.SectorX_Terminal_Megacore[2]: IjiItemData(progtype = ItemClassification.progression),
    EventNames.SectorX_Megacore: IjiItemData(progtype = ItemClassification.progression),
    EventNames.Victory: IjiItemData(progtype = ItemClassification.progression)
}