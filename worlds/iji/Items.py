import logging
from math import ceil, floor
from BaseClasses import Item, ItemClassification
from .Locations import get_remaining_locations
from typing import List, Dict, TYPE_CHECKING, NamedTuple
from .Data.ItemData import item_table, items_filler, items_sectors, items_stats, items_traits, items_traps, items_other
from .Data.EventData import event_item_table
from .Options import interpret_randomizable_option

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

def create_item_pool(world: "IjiWorld") -> List[Item]:
    item_pool: List[Item] = []

    item_pool += create_compacted_stat_items(world)

    sector_count: int = min(10, world.options.end_goal.value)

    #if world.options.levelsanity:
    #    item_pool += create_multiple_items(world, ItemNames.Supercharge, world.options.game_difficulty * sector_count)

    if world.options.out_of_order_sectors:
        for i in range(2, sector_count + 1):
            item_pool.append(create_item(world, ItemNames.Sector_Access[i]))
    else:
        item_pool += create_multiple_items(world, ItemNames.Sector_Access[0], sector_count - 1)

    if world.options.special_trait_items:
        for name in ItemNames.Special_Traits:
            item_pool.append(create_item(world, name))

    if world.options.debug_item:
        item_pool.append(create_item(world, ItemNames.Debug))

    if world.options.jump_upgrades.value == 1:
        if sector_count >= 5:
            item_pool += create_multiple_items(world, ItemNames.Upgrade_Jump, 2)
        else:
            item_pool.append(create_item(world, ItemNames.Upgrade_Jump))

    if world.options.armor_upgrades.value & 1 == 1:
        if sector_count >= 10:
            item_pool += create_multiple_items(world, ItemNames.Upgrade_Armor, 5)
        elif sector_count == 9:
            item_pool += create_multiple_items(world, ItemNames.Upgrade_Armor, 4)
        elif sector_count == 8:
            item_pool += create_multiple_items(world, ItemNames.Upgrade_Armor, 3)
        elif sector_count == 7:
            item_pool += create_multiple_items(world, ItemNames.Upgrade_Armor, 2)
        else:
            item_pool.append(create_item(world, ItemNames.Upgrade_Armor))

    #if world.options.supercharge_locations.value == 2:
    #    item_pool += create_multiple_items(world, ItemNames.Supercharge, sector_count)

    unfilled_locations = get_remaining_locations(world)

    if world.options.goal_ribbons.value > 0:
        item_pool += create_ribbon_items(world, unfilled_locations - len(item_pool))

    item_pool += create_duplicate_items(world, unfilled_locations - len(item_pool))

    item_pool += create_filler_items(world, unfilled_locations - len(item_pool))

    return item_pool

def create_item(world: "IjiWorld", name: str, progtype: ItemClassification = None) -> Item:
    data = items_and_events[name]
    if progtype is None:
        return IjiItem(name, data.progtype, data.code, world.player)
    else:
        return IjiItem(name, progtype, data.code, world.player)

def create_compacted_stat_items(world: "IjiWorld") -> List[Item]:
    ret: List[Item] = []
    for name, value in world.max_stats.items():
        stats_needed = ceil((value - world.current_stat_items[name]) / world.compact_stats[name])
        ret += create_multiple_items(world, name, stats_needed)
        logging.warning(f"Adding {stats_needed} {name}s to Item Pool")
        logging.warning(world.max_stats[name])
        logging.warning(world.compact_stats[name])
        logging.warning(world.current_stat_items[name])
    return ret

def create_multiple_items(world: "IjiWorld", name: str, count: int, progtype: ItemClassification = None) -> List[Item]:
    itemlist: List[Item] = []
    data = item_table[name]

    for i in range(count):
        if progtype is not None:
            itemlist += [IjiItem(name, progtype, data.code, world.player)]
        else:
            itemlist += [IjiItem(name, data.progtype, data.code, world.player)]

    return itemlist

def create_ribbon_items(world: "IjiWorld", maximum: int) -> List[Item]:
    itemlist: List[Item] = []

    allowed_ribbons = max(0, maximum - world.post_goal_locations)

    if world.options.ribbon_items.value > allowed_ribbons:
        world.options.ribbon_items.value = allowed_ribbons
        logging.warning(f"{world.player_name} selected more ribbons than available locations")
        logging.warning(f"Their ribbon count has been reduced to {world.options.ribbon_items.value}")

    prog_ribbons: int = ceil(world.options.ribbon_items.value * (world.options.goal_ribbons.value / 100))
    useful_ribbons = world.options.ribbon_items.value - prog_ribbons
    itemlist += create_multiple_items(world, ItemNames.Ribbon, prog_ribbons, ItemClassification.progression_skip_balancing)
    itemlist += create_multiple_items(world, ItemNames.Ribbon, useful_ribbons, ItemClassification.useful)

    return itemlist

def create_duplicate_items(world: "IjiWorld", maximum: int) -> List[Item]:
    itemlist: List[Item] = []
    if maximum <= 0:
        return itemlist

    sector_item_count: int = world.options.end_goal.get_normal_sector_count() - 1

    dupe_amounts: Dict[str, int] = {}

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
    ItemNames.Upgrade_Armor
]
    if world.options.special_trait_items:
        dupe_array += [
            ItemNames.Special_Health,
            ItemNames.Special_Attack,
            ItemNames.Special_Assimilate,
            ItemNames.Special_Strength,
            ItemNames.Special_Crack,
            ItemNames.Special_Tasen,
            ItemNames.Special_Komato
        ]
    if world.options.debug_item:
        dupe_array += [ItemNames.Debug]

    for item_name in dupe_array:
        if item_name in world.options.extra_items.value.keys():
            dupe_amounts[item_name] = (interpret_randomizable_option(world,
                                                              world.options.extra_items.value[item_name],
                                                              f"Duplicate {item_name}", 0, 2147483647))

    dupe_count: int = 0
    for i in dupe_amounts.values():
        dupe_count += i
    if dupe_count <= 0:
        return itemlist

    dupe_count = min(dupe_count, maximum)
    sector_dupe_list: List[str] = []

    while dupe_count > 0:
        added_item: bool = False
        for dupe, amount in dupe_amounts.items():
            if dupe_count <= 0:
                break
            if amount <= 0:
                continue
            dupe_to_add = ""

            if dupe == "Sector Access":
                if not world.options.out_of_order_sectors:
                    dupe_to_add = ItemNames.Sector_Access[0]
                else:
                    if len(sector_dupe_list) == 0:
                        sector_dupe_list = get_dupe_sector_list(sector_item_count)
                    dupe_to_add = world.random.choice(sector_dupe_list)
                    sector_dupe_list.remove(dupe_to_add)



            if dupe_to_add != "":
                itemlist.append(create_item(world, dupe_to_add, ItemClassification.useful))
                dupe_amounts[dupe] -= 1
                added_item = True

        if not added_item:
            break
    #while dupe_count > 0:
    #    for i in range(len(dupe_amounts)):
    #        if dupe_amounts[i] > 0 and dupe_count > 0:
    #
    #            if i == 0:
    #                if world.options.out_of_order_sectors:
    #                    sector: int = (dupe_amounts[0] % (sector_count - 1)) + 2
    #                    data = item_table[ItemNames.Sector_Access[sector]]
    #                    itemlist.append(IjiItem(data.name, ItemClassification.useful, data.code, world.player))
    #                else:
    #                    itemlist.append(create_item(world, ItemNames.Sector_Access[0]))
    #            elif i < 11 or (i < 18 and world.options.special_trait_items) or (i == 18 and world.options.debug_item):
    #                data = item_table[dupe_array[i]]
    #                itemlist.append(IjiItem(data.name, ItemClassification.useful, data.code, world.player))
    #            dupe_amounts[i] -= 1
    #            dupe_count -= 1

    return itemlist

def get_dupe_sector_list(sector_item_count: int) -> List[str]:
    return ItemNames.Sector_Access[2:sector_item_count + 1]

def create_filler_items(world: "IjiWorld", count: int) -> List[Item]:
    filler_list: List[Item] = []
    if count <= 0:
        return filler_list

    trap_item_count: int = 0
    
    for trap_name in ItemNames.Traps:
        # TODO interpret randomizable option
        if trap_name in world.options.trap_weights.value.keys() and world.options.trap_weights.value[trap_name] > 0:
            trap_item_count = floor((world.options.trap_percentage.value / 100.0) * count)
            break
    
    filler_item_count: int = count - trap_item_count
    
    filler_weights: Dict[str, int] = {}

    total_weights: int = 0
    for name, weight in world.options.filler_weights.items():
        if name in items_filler.keys():
            filler_weights[name] = interpret_randomizable_option(world, weight, f"Filler Weight: {name}", 0, 2147483647)
            total_weights += filler_weights[name]
    if total_weights == 0:
        filler_weights["Can of Soda"] = 1
    
    for i in range(filler_item_count):
        filler_list += [create_item(world,
            world.random.choices(list(filler_weights.keys()), weights=list(filler_weights.values()), k=1)[0])]
    
    filler_list += create_trap_items(world, trap_item_count)

    return filler_list

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


item_groups_table = {
    "Stat": set(items_stats.keys()),
    "Weapon Stat": {
        ItemNames.Stat_Tasen,
        ItemNames.Stat_Komato
        },
    "Sector Access": set(items_sectors.keys()),
    "Special Trait": set(items_traits.keys()),
    "Filler": set(items_filler.keys()),
    "Traps": set(items_traps.keys())
}

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
