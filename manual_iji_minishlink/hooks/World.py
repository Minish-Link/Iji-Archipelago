# Object classes from AP core, to represent an entire MultiWorld and this individual World that's part of it
from worlds.AutoWorld import World
from BaseClasses import MultiWorld, CollectionState

# Object classes from Manual -- extending AP core -- representing items and locations that are used in generation
from ..Items import ManualItem
from ..Locations import ManualLocation

# Raw JSON data from the Manual apworld, respectively:
#          data/game.json, data/items.json, data/locations.json, data/regions.json
#
from ..Data import game_table, item_table, location_table, region_table

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value

# calling logging.info("message") anywhere below in this file will output the message to both console and log file
import logging

########################################################################################
## Order of method calls when the world generates:
##    1. create_regions - Creates regions and locations
##    2. create_items - Creates the item pool
##    3. set_rules - Creates rules for accessing regions and locations
##    4. generate_basic - Runs any post item pool options, like place item/category
##    5. pre_fill - Creates the victory location
##
## The create_item method is used by plando and start_inventory settings to create an item from an item name.
## The fill_slot_data method will be used to send data to the Manual client for later use, like deathlink.
########################################################################################



# Use this function to change the valid filler items to be created to replace item links or starting items.
# Default value is the `filler_item_name` from game.json
def hook_get_filler_item_name(world: World, multiworld: MultiWorld, player: int) -> str | bool:
    return False

# Called before regions and locations are created. Not clear why you'd want this, but it's here. Victory location is included, but Victory event is not placed yet.
def before_create_regions(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after regions and locations are created, in case you want to see or modify that information. Victory location is included.
def after_create_regions(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to remove locations from the world
    locationNamesToRemove = [] # List of location names

    # Add your code here to calculate which locations to remove

    if get_option_value(multiworld, player, "health_items") < 9:
        locationNamesToRemove.append("Scrambler")
        locationNamesToRemove.append("Poster 9")
        locationNamesToRemove.append("Banana Gun")
    if get_option_value(multiworld, player, "health_items") < 4:
        locationNamesToRemove.append("Supercharge 7")
    if get_option_value(multiworld, player, "health_items") < 1:
        locationNamesToRemove.append("Poster 3")
        locationNamesToRemove.append("Poster 8")
        locationNamesToRemove.append("Supercharge 2")
        if get_option_value(multiworld, player, "tasen_items") < 5:
            locationNamesToRemove.append("Poster 4")
            if get_option_value(multiworld, player, "strength_items") < 3:
                locationNamesToRemove.append("Supercharge 4")

    if get_option_value(multiworld, player, "attack_items") < 9:
        locationNamesToRemove.append("Scrambler")
        locationNamesToRemove.append("Supercharge 7")
    if get_option_value(multiworld, player, "attack_items") < 4:
        locationNamesToRemove.append("Supercharge 8")
    if get_option_value(multiworld, player, "attack_items") < 2:
        locationNamesToRemove.append("Poster 7")
    
    if get_option_value(multiworld, player, "assimilate_items") < 3:
        locationNamesToRemove.append("Supercharge 7")
    
    if get_option_value(multiworld, player, "strength_items") < 3:
        locationNamesToRemove.append("Poster 3")
        locationNamesToRemove.append("Supercharge 1")
        if get_option_value(multiworld, player, "tasen_items") < 2:
            locationNamesToRemove.append("Poster 2")
        if get_option_value(multiworld, player, "tasen_items") < 5:
            locationNamesToRemove.append("Poster 4")
    if get_option_value(multiworld, player, "strength_items") < 1:
        locationNamesToRemove.append("Poster 1")

    if get_option_value(multiworld, player, "crack_items") < 9:
        locationNamesToRemove.append("Velocithor V2-10")
        locationNamesToRemove.append("Poster 6")
        locationNamesToRemove.append("Supercharge 10")
        locationNamesToRemove.append("Scrambler")
    if get_option_value(multiworld, player, "crack_items") < 8:
        locationNamesToRemove.append("Nuke")
        locationNamesToRemove.append("Poster 5")
        locationNamesToRemove.append("Supercharge 5")
        locationNamesToRemove.append("Poster 7")
        locationNamesToRemove.append("Poster 10")
    if get_option_value(multiworld, player, "crack_items") < 7:
        locationNamesToRemove.append("Plasma Cannon")
    if get_option_value(multiworld, player, "crack_items") < 6:
        locationNamesToRemove.append("Splinter Gun")
        locationNamesToRemove.append("Supercharge 6")
    if get_option_value(multiworld, player, "crack_items") < 5:
        locationNamesToRemove.append("Hyper Pulse")
        locationNamesToRemove.append("Supercharge 3")
    if get_option_value(multiworld, player, "crack_items") < 4:
        locationNamesToRemove.append("Spread Rockets")
        locationNamesToRemove.append("Supercharge 8")
    if get_option_value(multiworld, player, "crack_items") < 2:
        locationNamesToRemove.append("Buster Gun")

    if get_option_value(multiworld, player, "tasen_items") < 9:
        locationNamesToRemove.append("MPFB Devastator")
        locationNamesToRemove.append("Poster 9")
        locationNamesToRemove.append("Nuke")
        locationNamesToRemove.append("Poster 5")
        locationNamesToRemove.append("Poster 7")
        locationNamesToRemove.append("Supercharge 5")
        locationNamesToRemove.append("Poster 10")
        locationNamesToRemove.append("Velocithor V2-10")
        locationNamesToRemove.append("Poster 6")
        locationNamesToRemove.append("Supercharge 7")
        locationNamesToRemove.append("Supercharge 10")
        locationNamesToRemove.append("Banana Gun")
        locationNamesToRemove.append("Scrambler")
    if get_option_value(multiworld, player, "tasen_items") < 5:
        locationNamesToRemove.append("Rocket Launcher")
        locationNamesToRemove.append("Supercharge 2")
        locationNamesToRemove.append("Spread Rockets")
        if get_option_value(multiworld, player, "komato_items") < 5:
            locationNamesToRemove.append("Supercharge 8")
    if get_option_value(multiworld, player, "tasen_items") < 2:
        locationNamesToRemove.append("Machine Gun")
        locationNamesToRemove.append("Splinter Gun")
        locationNamesToRemove.append("Buster Gun")
    
    if get_option_value(multiworld, player, "komato_items") < 9:
        locationNamesToRemove.append("Cyclic Fusion Ignition System")
        locationNamesToRemove.append("Poster 7")
        locationNamesToRemove.append("Velocithor V2-10")
        locationNamesToRemove.append("Poster 6")
        locationNamesToRemove.append("Supercharge 10")
        locationNamesToRemove.append("Banana Gun")
        locationNamesToRemove.append("Scrambler")
    if get_option_value(multiworld, player, "komato_items") < 5:
        locationNamesToRemove.append("Shocksplinter")
        locationNamesToRemove.append("Splinter Gun")
        locationNamesToRemove.append("Poster 10")
        locationNamesToRemove.append("Plasma Cannon")
        if get_option_value(multiworld, player, "tasen_items") < 9 and get_option_value(multiworld, player, "crack_items") < 8:
            locationNamesToRemove.append("Supercharge 6")
        if get_option_value(multiworld, player, "tasen_items") < 2:
            locationNamesToRemove.append("Supercharge 6")
    if get_option_value(multiworld, player, "komato_items") < 2:
        locationNamesToRemove.append("Pulse Cannon")
        locationNamesToRemove.append("Hyper Pulse")
        locationNamesToRemove.append("Supercharge 3")

    for region in multiworld.regions:
        if region.player == player:
            for location in list(region.locations):
                if location.name in locationNamesToRemove:
                    region.locations.remove(location)
    if hasattr(multiworld, "clear_location_cache"):
        multiworld.clear_location_cache()

# The item pool before starting items are processed, in case you want to see the raw item pool at that stage
def before_create_items_starting(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# The item pool after starting items are processed but before filler is added, in case you want to see the raw item pool at that stage
def before_create_items_filler(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    # Use this hook to remove items from the item pool
    itemNamesToRemove = [] # List of item names

    # Add your code here to calculate which items to remove.
    #
    # Because multiple copies of an item can exist, you need to add an item name
    # to the list multiple times if you want to remove multiple copies of it.

    for i in range(get_option_value(multiworld, player, "health_items"), 9):
        itemNamesToRemove.append("Health Stat")
    for i in range(get_option_value(multiworld, player, "attack_items"), 9):
        itemNamesToRemove.append("Attack Stat")
    for i in range(get_option_value(multiworld, player, "assimilate_items"), 9):
        itemNamesToRemove.append("Assimilate Stat")
    for i in range(get_option_value(multiworld, player, "strength_items"), 9):
        itemNamesToRemove.append("Strength Stat")
    for i in range(get_option_value(multiworld, player, "crack_items"), 9):
        itemNamesToRemove.append("Crack Stat")
    for i in range(get_option_value(multiworld, player, "tasen_items"), 9):
        itemNamesToRemove.append("Tasen Stat")
    for i in range(get_option_value(multiworld, player, "komato_items"), 9):
        itemNamesToRemove.append("Komato Stat")

    for itemName in itemNamesToRemove:
        item = next(i for i in item_pool if i.name == itemName)
        item_pool.remove(item)

    return item_pool

    # Some other useful hook options:

    ## Place an item at a specific location
    # location = next(l for l in multiworld.get_unfilled_locations(player=player) if l.name == "Location Name")
    # item_to_place = next(i for i in item_pool if i.name == "Item Name")
    # location.place_locked_item(item_to_place)
    # item_pool.remove(item_to_place)

# The complete item pool prior to being set for generation is provided here, in case you want to make changes to it
def after_create_items(item_pool: list, world: World, multiworld: MultiWorld, player: int) -> list:
    return item_pool

# Called before rules for accessing regions and locations are created. Not clear why you'd want this, but it's here.
def before_set_rules(world: World, multiworld: MultiWorld, player: int):
    pass

# Called after rules for accessing regions and locations are created, in case you want to see or modify that information.
def after_set_rules(world: World, multiworld: MultiWorld, player: int):
    # Use this hook to modify the access rules for a given location

    def Example_Rule(state: CollectionState) -> bool:
        # Calculated rules take a CollectionState object and return a boolean
        # True if the player can access the location
        # CollectionState is defined in BaseClasses
        return True

    ## Common functions:
    # location = world.get_location(location_name, player)
    # location.access_rule = Example_Rule

    ## Combine rules:
    # old_rule = location.access_rule
    # location.access_rule = lambda state: old_rule(state) and Example_Rule(state)
    # OR
    # location.access_rule = lambda state: old_rule(state) or Example_Rule(state)

# The item name to create is provided before the item is created, in case you want to make changes to it
def before_create_item(item_name: str, world: World, multiworld: MultiWorld, player: int) -> str:
    return item_name

# The item that was created is provided after creation, in case you want to modify the item
def after_create_item(item: ManualItem, world: World, multiworld: MultiWorld, player: int) -> ManualItem:
    return item

# This method is run towards the end of pre-generation, before the place_item options have been handled and before AP generation occurs
def before_generate_basic(world: World, multiworld: MultiWorld, player: int) -> list:
    pass

# This method is run at the very end of pre-generation, once the place_item options have been handled and before AP generation occurs
def after_generate_basic(world: World, multiworld: MultiWorld, player: int):
    pass

# This is called before slot data is set and provides an empty dict ({}), in case you want to modify it before Manual does
def before_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called after slot data is set and provides the slot data at the time, in case you want to check and modify it after Manual is done with it
def after_fill_slot_data(slot_data: dict, world: World, multiworld: MultiWorld, player: int) -> dict:
    return slot_data

# This is called right at the end, in case you want to write stuff to the spoiler log
def before_write_spoiler(world: World, multiworld: MultiWorld, spoiler_handle) -> None:
    pass

# This is called when you want to add information to the hint text
def before_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    
    ### Example way to use this hook: 
    # if player not in hint_data:
    #     hint_data.update({player: {}})
    # for location in multiworld.get_locations(player):
    #     if not location.address:
    #         continue
    #
    #     use this section to calculate the hint string
    #
    #     hint_data[player][location.address] = hint_string
    
    pass

def after_extend_hint_information(hint_data: dict[int, dict[int, str]], world: World, multiworld: MultiWorld, player: int) -> None:
    pass
