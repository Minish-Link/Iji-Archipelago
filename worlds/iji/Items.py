import logging
from math import floor
from BaseClasses import Item, ItemClassification
from .Locations import get_remaining_locations
from typing import List, Dict, TYPE_CHECKING, NamedTuple
from .Data.ItemData import item_table, items_filler
from .Data.EventData import event_item_table

from .Names import ItemNames

if TYPE_CHECKING:
    from . import IjiWorld

class IjiItem(Item):
    game = "Iji"

class IjiItemData(NamedTuple):
    code: int
    progtype: ItemClassification
    weight: int = 1

items_and_events = {
    **item_table,
    **event_item_table
}

def create_itempool(world: "IjiWorld") -> List[Item]:
    itempool: List[Item] = []

    itempool += create_multiple_items(world, ItemNames.Stat_Health, 9)
    itempool += create_multiple_items(world, ItemNames.Stat_Attack, 9)
    itempool += create_multiple_items(world, ItemNames.Stat_Assimilate, 9)
    itempool += create_multiple_items(world, ItemNames.Stat_Strength, 9)
    itempool += create_multiple_items(world, ItemNames.Stat_Crack, 9)
    itempool += create_multiple_items(world, ItemNames.Stat_Tasen, 9)
    itempool += create_multiple_items(world, ItemNames.Stat_Komato, 9)

    sector_count: int = min(10, world.options.end_goal.value)

    if world.options.levelsanity:
        itempool += create_multiple_items(world, ItemNames.Supercharge, 5 * sector_count)

    if world.options.out_of_order_sectors:
        for i in range(1, sector_count + 1):
            itempool.append(create_item(world, ItemNames.Sector_Access[i]))
    else:
        itempool += create_multiple_items(world, ItemNames.Sector_Access[0], sector_count - 1)

    if world.options.special_trait_items:
        itempool.append(create_item(world, ItemNames.Special_Health))
        itempool.append(create_item(world, ItemNames.Special_Attack))
        itempool.append(create_item(world, ItemNames.Special_Assimilate))
        itempool.append(create_item(world, ItemNames.Special_Strength))
        itempool.append(create_item(world, ItemNames.Special_Crack))
        itempool.append(create_item(world, ItemNames.Special_Tasen))
        itempool.append(create_item(world, ItemNames.Special_Komato))

    if world.options.debug_item:
        itempool.append(create_item(world, ItemNames.Debug))

    if world.options.jump_upgrades.value == 1:
        if sector_count >= 5:
            itempool += create_multiple_items(world, ItemNames.Upgrade_Jump, 2)
        else:
            itempool.append(create_item(world, ItemNames.Upgrade_Jump))

    if world.options.armor_upgrades.value & 1 == 1:
        if sector_count >= 10:
            itempool += create_multiple_items(world, ItemNames.Upgrade_Armor, 5)
        elif sector_count == 9:
            itempool += create_multiple_items(world, ItemNames.Upgrade_Armor, 4)
        elif sector_count == 8:
            itempool += create_multiple_items(world, ItemNames.Upgrade_Armor, 3)
        elif sector_count == 7:
            itempool += create_multiple_items(world, ItemNames.Upgrade_Armor, 2)
        else:
            itempool.append(create_item(world, ItemNames.Upgrade_Armor))

    if world.options.supercharge_locations.value == 2:
        itempool += create_multiple_items(world, ItemNames.Supercharge, sector_count)

    unfilled_locations = get_remaining_locations(world)

    if world.options.goal_ribbons.value > 0:
        itempool += create_ribbon_items(world, unfilled_locations - len(itempool))

    itempool += create_duplicate_items(world, unfilled_locations - len(itempool))

    itempool += create_filler_items(world, unfilled_locations - len(itempool))

    return itempool

def create_item(world: "IjiWorld", name: str) -> Item:
    data = items_and_events[name]
    return IjiItem(name, data.progtype, data.code, world.player)

def create_multiple_items(world: "IjiWorld", name: str, count: int) -> List[Item]:
    itemlist: List[Item] = []
    data = item_table[name]

    for i in range(count):
        itemlist += [IjiItem(name, data.progtype, data.code, world.player)]

    return itemlist

def create_ribbon_items(world: "IjiWorld", maximum: int) -> List[Item]:
    itemlist: List[Item] = []

    if world.options.goal_ribbons.value > maximum:
        world.options.goal_ribbons.value = maximum
        logging.warning(f"{world.player_name} did not have enough locations for their ribbon requirement")
        logging.warning(f"Their ribbon requirement has been reduced to {world.options.goal_ribbons.value}")

    itemlist += create_multiple_items(world, ItemNames.Ribbon, world.options.goal_ribbons.value)

    return itemlist

def create_duplicate_items(world: "IjiWorld", maximum: int) -> List[Item]:
    itemlist: List[Item] = []

    sector_count: int = min(10, world.options.end_goal.value)

    dupe_amounts: List[int] = []

    dupe_amounts.append(world.options.extra_sector_access)  # 0
    dupe_amounts.append(world.options.extra_ribbons)        # 1
    dupe_amounts.append(world.options.extra_supercharges)   # 2
    dupe_amounts.append(world.options.extra_health)         # 3
    dupe_amounts.append(world.options.extra_crack)          # 4
    dupe_amounts.append(world.options.extra_strength)       # 5
    dupe_amounts.append(world.options.extra_tasen)          # 6
    dupe_amounts.append(world.options.extra_komato)         # 7
    dupe_amounts.append(world.options.extra_attack)         # 8
    dupe_amounts.append(world.options.extra_assimilate)     # 9

    dupe_count: int = 0
    for i in range(len(dupe_amounts)):
        dupe_count += dupe_amounts[i]

    dupe_count = min(dupe_count, maximum)

    while dupe_count > 0:
        for i in range(len(dupe_amounts)):
            if dupe_amounts[i] > 0 and dupe_count > 0:
                if i == 0 and world.options.out_of_order_sectors:
                    sector: int = (dupe_amounts[0] % (sector_count - 1)) + 2
                    itemlist.append(create_item(world, ItemNames.Sector_Access[sector]))
                else:
                    itemlist.append(create_item(world, dupe_array[i]))
                dupe_amounts[i] -= 1
                dupe_count -= 1

    return itemlist

def create_filler_items(world: "IjiWorld", count: int) -> List[Item]:
    fillerlist: List[Item] = []

    trapitemcount: int = 0
    if world.options.rocket_trap_weight.value > 0 or world.options.blits_trap_weight.value > 0 or \
        world.options.null_drive_trap_weight.value > 0 or world.options.turbo_trap_weight.value > 0 or \
        world.options.nap_trap_weight.value > 0 or world.options.clown_shoes_weight.value > 0 or \
        world.options.banana_trap_weight.value > 0:
    
        trapitemcount = floor((world.options.trap_percentage.value / 100.0) * count)
    
    filleritemcount: int = count - trapitemcount
    
    fillerweights: Dict[str, int] = {}
    
    for name, filler in items_filler.items():
        fillerweights[name] = filler.weight
    
    for i in range(filleritemcount):
        fillerlist += [create_item(world,
            world.random.choices(list(fillerweights.keys()), weights=list(fillerweights.values()), k=1)[0])]
    
    fillerlist += create_trap_items(world, trapitemcount)

    return fillerlist

def create_trap_items(world: "IjiWorld", count: int) -> List[Item]:
    traplist: List[Item] = []

    trapweights: Dict[str, int] = {}
    
    trapweights[ItemNames.Traps[0]] = world.options.rocket_trap_weight.value
    trapweights[ItemNames.Traps[1]] = world.options.blits_trap_weight.value
    trapweights[ItemNames.Traps[2]] = world.options.null_drive_trap_weight.value
    trapweights[ItemNames.Traps[3]] = world.options.turbo_trap_weight.value
    trapweights[ItemNames.Traps[4]] = world.options.nap_trap_weight.value
    trapweights[ItemNames.Traps[5]] = world.options.clown_shoes_weight.value
    trapweights[ItemNames.Traps[6]] = world.options.banana_trap_weight.value
    
    for i in range(count):
        traplist += [create_item(world,
            world.random.choices(list(trapweights.keys()), weights=list(trapweights.values()), k=1)[0])]

    return traplist

dupe_array: List[str] = [
    ItemNames.Sector_Access[0],
    ItemNames.Ribbon,
    ItemNames.Supercharge,
    ItemNames.Stat_Health,
    ItemNames.Stat_Crack,
    ItemNames.Stat_Strength,
    ItemNames.Stat_Tasen,
    ItemNames.Stat_Komato,
    ItemNames.Stat_Attack,
    ItemNames.Stat_Assimilate
]

#item_groups_table = {
#    "Stats": items_primary.keys(),
#    "Traits": items_traits.keys(),
#    "Weapons": {
#        **items_weapons,
#        **items_specialweapons,
#        **items_progressiveweapons,
#    },
#    "Normal Weapons": {
#        **items_weapons,
#        **items_progressiveweapons,
#    },
#    "Special Weapons": items_specialweapons.keys(),
#    # Not sure this one's useful. I'll leave it here but comment it out for now.
#    # "Collectibles": {
#    #     "Poster",
#    #     "Ribbon"
#    # }
#}
