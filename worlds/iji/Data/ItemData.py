from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING
from BaseClasses import ItemClassification
from ..Names import ItemNames

class IjiItemData(NamedTuple):
    progtype: ItemClassification
    code: Optional[int] = None
    weight: int = 1

items_sectors: Dict[str, IjiItemData] = {
    ItemNames.Sector_Access[0]: IjiItemData(
        code=1, progtype=ItemClassification.progression
    ),
    ItemNames.Sector_Access[1]: IjiItemData(
        code=41, progtype=ItemClassification.progression
    ),
    ItemNames.Sector_Access[2]: IjiItemData(
        code=42, progtype=ItemClassification.progression
    ),
    ItemNames.Sector_Access[3]: IjiItemData(
        code=43, progtype=ItemClassification.progression
    ),
    ItemNames.Sector_Access[4]: IjiItemData(
        code=44, progtype=ItemClassification.progression
    ),
    ItemNames.Sector_Access[5]: IjiItemData(
        code=45, progtype=ItemClassification.progression
    ),
    ItemNames.Sector_Access[6]: IjiItemData(
        code=46, progtype=ItemClassification.progression
    ),
    ItemNames.Sector_Access[7]: IjiItemData(
        code=47, progtype=ItemClassification.progression
    ),
    ItemNames.Sector_Access[8]: IjiItemData(
        code=48, progtype=ItemClassification.progression
    ),
    ItemNames.Sector_Access[9]: IjiItemData(
        code=49, progtype=ItemClassification.progression
    ),
    ItemNames.Sector_Access[10]: IjiItemData(
        code=50, progtype=ItemClassification.progression
    )
}

items_stats: Dict[str, IjiItemData] = {
    ItemNames.Stat_Health: IjiItemData(
        code=2, progtype=ItemClassification.progression
    ),
    ItemNames.Stat_Attack: IjiItemData(
        code=3, progtype=ItemClassification.progression
    ),
    ItemNames.Stat_Assimilate: IjiItemData(
        code=4, progtype=ItemClassification.progression
    ),
    ItemNames.Stat_Strength: IjiItemData(
        code=5, progtype=ItemClassification.progression
    ),
    ItemNames.Stat_Crack: IjiItemData(
        code=6, progtype=ItemClassification.progression
    ),
    ItemNames.Stat_Tasen: IjiItemData(
        code=7, progtype=ItemClassification.progression
    ),
    ItemNames.Stat_Komato: IjiItemData(
        code=8, progtype=ItemClassification.progression
    )
}

items_traits: Dict[str, IjiItemData] = {
    ItemNames.Special_Health: IjiItemData(
        code=12, progtype=ItemClassification.progression
    ),
    ItemNames.Special_Attack: IjiItemData(
        code=13, progtype=ItemClassification.useful
    ),
    ItemNames.Special_Assimilate: IjiItemData(
        code=14, progtype=ItemClassification.useful
    ),
    ItemNames.Special_Strength: IjiItemData(
        code=15, progtype=ItemClassification.useful
    ),
    ItemNames.Special_Crack: IjiItemData(
        code=16, progtype=ItemClassification.useful
    ),
    ItemNames.Special_Tasen: IjiItemData(
        code=17, progtype=ItemClassification.useful
    ),
    ItemNames.Special_Komato: IjiItemData(
        code=18, progtype=ItemClassification.useful
    )
}

items_filler: Dict[str, IjiItemData] = {
    ItemNames.Filler[0]: IjiItemData(
        code=201, progtype=ItemClassification.filler, weight=10
    ),
    ItemNames.Filler[1]: IjiItemData(
        code=202, progtype=ItemClassification.filler, weight=4
    ),
    ItemNames.Filler[2]: IjiItemData(
        code=203, progtype=ItemClassification.filler, weight=12
    ),
    ItemNames.Filler[3]: IjiItemData(
        code=204, progtype=ItemClassification.filler, weight=5
    ),
    ItemNames.Filler[4]: IjiItemData(
        code=205, progtype=ItemClassification.filler, weight=4
    ),
    ItemNames.Filler[5]: IjiItemData(
        code=206, progtype=ItemClassification.filler, weight=3
    ),
    ItemNames.Filler[6]: IjiItemData(
        code=207, progtype=ItemClassification.filler, weight=4
    ),
    ItemNames.Filler[7]: IjiItemData(
        code=208, progtype=ItemClassification.filler, weight=3
    ),
    ItemNames.Filler[8]: IjiItemData(
        code=209, progtype=ItemClassification.filler, weight=2
    ),
    ItemNames.Filler[9]: IjiItemData(
        code=210, progtype=ItemClassification.filler, weight=8
    ),
    ItemNames.Filler[10]: IjiItemData(
        code=211, progtype=ItemClassification.filler, weight=10
    )
}

items_traps: Dict[str, IjiItemData] = {
    ItemNames.Traps[0]: IjiItemData(
        code=401, progtype=ItemClassification.trap
    ),
    ItemNames.Traps[1]: IjiItemData(
        code=402, progtype=ItemClassification.trap
    ),
    ItemNames.Traps[2]: IjiItemData(
        code=403, progtype=ItemClassification.trap
    ),
    ItemNames.Traps[3]: IjiItemData(
        code=404, progtype=ItemClassification.trap
    ),
    ItemNames.Traps[4]: IjiItemData(
        code=405, progtype=ItemClassification.trap
    ),
    ItemNames.Traps[5]: IjiItemData(
        code=406, progtype=ItemClassification.trap
    ),
    ItemNames.Traps[6]: IjiItemData(
        code=407, progtype=ItemClassification.trap
    )
}

items_other: Dict[str, IjiItemData] = {
    ItemNames.Supercharge: IjiItemData(
        code=9, progtype=ItemClassification.progression_skip_balancing
    ),
    ItemNames.Debug: IjiItemData(
        code=10, progtype=ItemClassification.progression
    ),
    ItemNames.Ribbon: IjiItemData(
        code=11, progtype=ItemClassification.progression_skip_balancing
    ),
    ItemNames.Upgrade_Jump: IjiItemData(
        code=51,progtype=ItemClassification.progression
    ),
    ItemNames.Upgrade_Armor: IjiItemData(
        code=52, progtype=ItemClassification.useful
    )
}

item_table = {
    **items_sectors,
    **items_stats,
    **items_traits,
    **items_filler,
    **items_traps,
    **items_other
}