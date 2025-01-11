from typing import Optional
from worlds.AutoWorld import World
from ..Helpers import clamp, get_items_with_value
from BaseClasses import MultiWorld, CollectionState

import re

combat_logic_values = [
[0,0,0,0,0,0,0,0,0],
[1,3,5,7,9,9,9,9,9],
[1,2,3,4,5,6,7,8,9],
[0,1,1,2,2,3,3,4,4],
[0,0,0,1,1,1,1,2,2]]

# Sometimes you have a requirement that is just too messy or repetitive to write out with boolean logic.
# Define a function here, and you can use it in a requires string with {function_name()}.
def overfishedAnywhere(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Has the player collected all fish from any fishing log?"""
    for cat, items in world.item_name_groups:
        if cat.endswith("Fishing Log") and state.has_all(items, player):
            return True
    return False

# You can also pass an argument to your function, like {function_name(15)}
# Note that all arguments are strings, so you'll need to convert them to ints if you want to do math.
def anyClassLevel(world: World, multiworld: MultiWorld, state: CollectionState, player: int, level: str):
    """Has the player reached the given level in any class?"""
    for item in ["Figher Level", "Black Belt Level", "Thief Level", "Red Mage Level", "White Mage Level", "Black Mage Level"]:
        if state.count(item, player) >= int(level):
            return True
    return False

# You can also return a string from your function, and it will be evaluated as a requires string.
def requiresMelee(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    """Returns a requires string that checks if the player has unlocked the tank."""
    return "|Figher Level:15| or |Black Belt Level:15| or |Thief Level:15|"

def hasEnoughHealthForSector(world: World, multiworld: MultiWorld, state: CollectionState, player: int, sector_access: str):

    
    chosen_logic = world.options.combat_logic.value
    max_health = world.options.health_items.value

    if state.count("Health Stat", player) >= min(max_health, combat_logic_values[chosen_logic][int(sector_access) - 1]):
        return True

    return False

def canAccessResonanceDetonator(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"|Sector Access:1|"
    return (state.count("Sector Access", player) >= 1)

def canAccessMachineGun(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"|Tasen Stat:2|"
    return (state.count("Tasen Stat", player) >= 2)

def canAccessPulseCannon(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"|Komato Stat:2| AND ((|Sector Access:2| AND |Crack Stat:1|) OR (|Sector Access:3|))"
    komato = state.count("Komato Stat", player)
    sector = state.count("Sector Access", player)
    crack = state.count("Crack Stat", player)

    if komato >= 2:
        if (crack >= 1 and sector >= 2) or sector >= 3:
            return True

    return False

def canAccessRocketLauncher(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"|Tasen Stat:5| AND ((|Sector Access:1| AND |Health Stat:1|) OR (|Sector Access:2|))"
    tasen = state.count("Tasen Stat", player)
    sector = state.count("Sector Access", player)
    health = state.count("Health Stat", player)

    if tasen >= 5:
        if (sector >= 1 and health >= 1) or sector >= 2:
            return True

    return False

def canAccessShocksplinter(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"|Komato Stat:5| AND |Sector Access:4|"
    return (state.count("Komato Stat", player) >= 5 and state.count("Sector Access", player) >= 4)

def canAccessMPFB(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"|Tasen Stat:9| AND |Sector Access:3|"
    return (state.count("Tasen Stat", player) >= 9 and state.count("Sector Access", player) >= 3)

def canAccessCFIS(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"|Komato Stat:9| AND ((|Sector Access:5| AND |Crack Stat:3|) OR (|Sector Access:6| AND |Strength Stat:2|) OR |Sector Access:7|)"
    komato = state.count("Komato Stat", player)
    crack = state.count("Crack Stat", player)
    strength = state.count("Strength Stat", player)
    sector = state.count("Sector Access", player)

    if komato >= 9:
        if (sector >= 5 and crack >= 3) or (sector >= 6 and strength >= 2) or (sector >= 7):
            return True
    return False

def canAccessBusterGun(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"{canReachLocation(Machine Gun)} AND |Crack Stat:2| AND |Sector Access:1|"
    return (canAccessMachineGun(world, multiworld, state, player) and state.count("Crack Stat", player) >= 2)

def canAccessResonanceReflector(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"({canReachLocation(Resonance Detonator)} AND |Crack Stat:3|) OR |Sector Access:9|"
    sector = state.count("Sector Access", player)
    return ((sector >= 1 and state.count("Crack Stat", player) >= 3) or sector >= 9)

def canAccessSplinterGun(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"{canReachLocation(Machine Gun)} AND {canReachLocation(Shocksplinter)} AND |Crack Stat:6|"
    return canAccessMachineGun(world, multiworld, state, player) and canAccessShocksplinter(world, multiworld, state, player) and state.count("Crack Stat", player) >= 6

def canAccessHyperPulse(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"{canReachLocation(Pulse Cannon)} AND |Crack Stat:5|"
    return (canAccessPulseCannon(world, multiworld, state, player) and state.count("Crack Stat", player) >= 5)

def canAccessSpreadRockets(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"{canReachLocation(Rocket Launcher)} AND |Crack Stat:4|"
    return (canAccessRocketLauncher(world, multiworld, state, player) and state.count("Crack Stat", player) >= 4)

def canAccessPlasmaCannon(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"{canReachLocation(Shocksplinter)} AND |Crack Stat:7|"
    return (canAccessShocksplinter(world, multiworld, state, player) and state.count("Crack Stat", player) >= 7)

def canAccessNuke(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"{canReachLocation(MPFB Devastator)} AND |Crack Stat:8|"
    return (canAccessMPFB(world, multiworld, state, player) and state.count("Crack Stat", player) >= 8)

def canAccessVelocithor(world: World, multiworld: MultiWorld, state: CollectionState, player: int):
    #"{canReachLocation(Cyclic Fusion Ignition System)} AND {canReachLocation(MPFB Devastator)} AND |Crack Stat:9|"
    return (canAccessMPFB(world, multiworld, state, player) and canAccessCFIS(world, multiworld, state, player) and state.count("Crack Stat", player) >= 9)