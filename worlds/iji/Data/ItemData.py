from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING
from BaseClasses import ItemClassification
from ..Names import ItemNames

class IjiItemData(NamedTuple):
    progtype: ItemClassification
    code: Optional[int] = None

items_sectors: Dict[str, IjiItemData] = {
    ItemNames.Sector_Access[0]: IjiItemData(
        code=1, progtype=ItemClassification.progression
    )
} | {
    ItemNames.Sector_Access[i]: IjiItemData(
        code=40+i, progtype=ItemClassification.progression
    ) for i in range(1, 11)
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
    ItemNames.Filler[i]: IjiItemData(
        code=201+i,progtype=ItemClassification.filler
    ) for i in range(len(ItemNames.Filler))
}

items_traps: Dict[str, IjiItemData] = {
    ItemNames.Traps[i]: IjiItemData(
        code=401+i, progtype=ItemClassification.trap
    ) for i in range(len(ItemNames.Traps))
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
    ),
    ItemNames.Glitch: IjiItemData(
        code=19, progtype=ItemClassification.progression
    )
}

items_weapons: Dict[str, IjiItemData] = {
    ItemNames.Weapons[i]: IjiItemData(
        code=100+i, progtype=ItemClassification.progression
    ) for i in range(len(ItemNames.Weapons))
} | {
    ItemNames.Weapons_Passive[i]: IjiItemData(
        code=120+i, progtype=ItemClassification.progression
    ) for i in range(len(ItemNames.Weapons_Passive))
}

item_table = {
    **items_sectors,
    **items_stats,
    **items_traits,
    **items_filler,
    **items_traps,
    **items_weapons,
    **items_other
}