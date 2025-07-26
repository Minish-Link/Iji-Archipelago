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
        for i in range(2, sector_count + 1):
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

    allowed_ribbons = maximum - get_post_goal_location_count(world)

    if world.options.ribbon_items.value > allowed_ribbons:
        world.options.ribbon_items.value = allowed_ribbons
        logging.warning(f"{world.player_name} selected more ribbons than available locations")
        logging.warning(f"Their ribbon count has been reduced to {world.options.ribbon_items.value}")

    itemlist += create_multiple_items(world, ItemNames.Ribbon, world.options.ribbon_items.value)

    return itemlist

def get_post_goal_location_count(world: "IjiWorld") -> int:
    count: int = 0

    if world.options.end_goal.value == 12:
        count += 2 # Null Driver location and Sector Z complete

    if world.options.supercharge_locations.value > 0:
        if (world.options.end_goal.value == 5 or world.options.end_goal.value == 7):
            count += 1 # Asha/Proxima supercharge

    if world.options.logbook_locations.value > 0:
        if world.options.end_goal.value >= 11:
            count += 2 # Sector Z logbooks
        if world.options.end_goal.value == 12:
            count += 15 # Sector Y logbooks

    if world.options.poster_locations.value > 0:
        if world.options.end_goal.value >= 11:
            count += 1 # Epic Poster
        if world.options.end_goal.value == 12:
            count += 1 # Poster of Doom
    
    return count

def create_duplicate_items(world: "IjiWorld", maximum: int) -> List[Item]:
    itemlist: List[Item] = []

    sector_count: int = min(10, world.options.end_goal.value)

    dupe_amounts: List[int] = []

    dupe_array: List[str] = [
    "Sector Access",
    ItemNames.Upgrade_Jump,
    ItemNames.Supercharge,
    ItemNames.Stat_Health,
    ItemNames.Stat_Crack,
    ItemNames.Stat_Strength,
    ItemNames.Stat_Tasen,
    ItemNames.Stat_Komato,
    ItemNames.Stat_Attack,
    ItemNames.Stat_Assimilate,
    ItemNames.Upgrade_Armor,
    ItemNames.Special_Health,
    ItemNames.Special_Attack,
    ItemNames.Special_Assimilate,
    ItemNames.Special_Strength,
    ItemNames.Special_Crack,
    ItemNames.Special_Tasen,
    ItemNames.Special_Komato
]

    for item_name in dupe_array:
        if item_name in world.options.extra_items.value.keys():
            if world.options.extra_items.value[item_name] < 0:
                dupe_amounts.append(world.random.randint(0, abs(world.options.extra_items.value[item_name])))
            else:
                dupe_amounts.append(world.options.extra_items.value[item_name])
        else:
            dupe_amounts.append(0)

    dupe_count: int = 0
    for i in range(len(dupe_amounts)):
        dupe_count += dupe_amounts[i]

    dupe_count = min(dupe_count, maximum)

    while dupe_count > 0:
        for i in range(len(dupe_amounts)):
            if dupe_amounts[i] > 0 and dupe_count > 0:
                if i == 0:
                    if world.options.out_of_order_sectors:
                        sector: int = (dupe_amounts[0] % (sector_count - 1)) + 2
                        itemlist.append(create_item(world, ItemNames.Sector_Access[sector]))
                    else:
                        itemlist.append(create_item(world, ItemNames.Sector_Access[0]))
                elif (i < 11 or world.options.special_trait_items):
                    itemlist.append(create_item(world, dupe_array[i]))
                dupe_amounts[i] -= 1
                dupe_count -= 1

    return itemlist


def create_filler_items(world: "IjiWorld", count: int) -> List[Item]:
    fillerlist: List[Item] = []

    trapitemcount: int = 0
    
    for trap_name in ItemNames.Traps:
        if (trap_name in world.options.trap_weights.value.keys() and world.options.trap_weights.value[trap_name] > 0):
            trapitemcount = floor((world.options.trap_percentage.value / 100.0) * count)
            break
    
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
    trap_list: List[Item] = []

    trap_weights: Dict[str, int] = {}
    
    for trap_name in ItemNames.Traps:
        if trap_name in world.options.trap_weights.value.keys():
            trap_weights[trap_name] = max(0, world.options.trap_weights.value[trap_name])
        else:
            trap_weights[trap_name] = 0
    
    for i in range(count):
        trap_list += [create_item(world,
            world.random.choices(list(trap_weights.keys()), weights=list(trap_weights.values()), k=1)[0])]

    return trap_list


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
