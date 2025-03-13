from math import floor
from BaseClasses import Item, ItemClassification
from .Locations import get_total_locations
from .Options import get_compacted_stat_items
from typing import List, Dict, TYPE_CHECKING, NamedTuple


if TYPE_CHECKING:
    from . import IjiWorld

class IjiItem(Item):
    game = "Iji"

class IjiItemData(NamedTuple):
    code: int
    progtype: ItemClassification
    weight: int = 1

def create_itempool(world: "IjiWorld") -> List[Item]:
    itempool: List[Item] = []

    statitems = get_compacted_stat_items(world)
    for name, count in statitems.items():
        itempool += create_multiple_items(world, name, count)

    itempool += create_multiple_items(world, "Sector Access", world.options.SectorAccessItems.value)

    superchargecount = world.options.ExtraSupercharges.value
    if world.options.SuperchargePointHandling.value == world.options.SuperchargePointHandling.option_shuffled:
        superchargecount += 10

    itempool += create_multiple_items(world, "Supercharge", superchargecount)

    if world.options.SpecialTraitItems.value:# == world.options.SpecialTraitItems.option_items_only or \
       #world.options.SpecialTraitItems.value == world.options.SpecialTraitItems.option_locations_and_items:
        for name in items_traits.keys():
            itempool += create_multiple_items(world, name, 1)

    itempool += create_ribbon_items(world)

    itempool += create_filler_items(world, get_total_locations(world) - len(itempool))

    #if (world.options.LogbookLocations.value == False):
    #    world.multiworld.get_location("Sector 1 - Sector Complete", world.player).place_locked_item(create_item(world, "Sector Access"))

    return itempool

def create_item(world: "IjiWorld", name: str) -> Item:
    data = item_table[name]
    return IjiItem(name, data.progtype, data.code, world.player)

def create_multiple_items(world: "IjiWorld", name: str, count: int) -> List[Item]:
    itemlist: List[Item] = []
    data = item_table[name]

    for i in range(count):
        itemlist += [IjiItem(name, data.progtype, data.code, world.player)]

    return itemlist

def create_ribbon_items(world: "IjiWorld") -> List[Item]:
    itemlist: List[Item] = []

    if world.options.EndGoal.value >= world.options.EndGoal.option_sector_z or \
        world.options.PostGameLocations.value >= world.options.PostGameLocations.option_sector_z:
        ribbonsneeded = max(world.options.SectorZRibbonItemsRequired.value,
                            world.options.NullDriverRibbonItemsRequired.value)
        if ribbonsneeded == 0:
            return itemlist
        else:
            itemlist += create_multiple_items(world, "Ribbon", max(ribbonsneeded,world.options.RibbonItemCount.value))

    return itemlist

def create_filler_items(world: "IjiWorld", count: int) -> List[Item]:
    fillerlist: List[Item] = []

    trapitemcount: int = 0
    if world.options.RocketTrapWeight.value > 0 or world.options.BlitsTrapWeight.value > 0 or \
        world.options.NullDriveTrapWeight.value > 0 or world.options.TurboTrapWeight.value > 0 or \
        world.options.NapTrapWeight.value > 0 or world.options.ClownShoesWeight.value > 0:
    
        trapitemcount = floor((world.options.TrapPercentage.value / 100.0) * count)
    
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
    
    trapweights["Rocket to the Face Trap"] = world.options.RocketTrapWeight.value
    trapweights["Blits Trap"] = world.options.BlitsTrapWeight.value
    trapweights["Null Drive Trap"] = world.options.NullDriveTrapWeight.value
    trapweights["Turbo Trap"] = world.options.TurboTrapWeight.value
    trapweights["Nap Trap"] = world.options.NapTrapWeight.value
    trapweights["Clown Shoes Trap"] = world.options.ClownShoesWeight.value
    
    for i in range(count):
        traplist += [create_item(world,
            world.random.choices(list(trapweights.keys()), weights=list(trapweights.values()), k=1)[0])]

    return traplist

# Sectors and Stats
items_primary: Dict[str,IjiItemData] = {
    "Sector Access":    IjiItemData(code=1, progtype=ItemClassification.progression),
    "Health Stat":      IjiItemData(code=2, progtype=ItemClassification.progression),
    "Attack Stat":      IjiItemData(code=3, progtype=ItemClassification.progression),
    "Assimilate Stat":  IjiItemData(code=4, progtype=ItemClassification.progression),
    "Strength Stat":    IjiItemData(code=5, progtype=ItemClassification.progression),
    "Crack Stat":       IjiItemData(code=6, progtype=ItemClassification.progression),
    "Tasen Stat":       IjiItemData(code=7, progtype=ItemClassification.progression),
    "Komato Stat":      IjiItemData(code=8, progtype=ItemClassification.progression)
}

items_other: Dict[str, IjiItemData] = {
    "Supercharge":  IjiItemData(code=9,  progtype = ItemClassification.useful),
    "Ribbon":       IjiItemData(code=11, progtype = ItemClassification.progression),
}

items_traits: Dict[str, IjiItemData] = {
    "SUPPRESSION":          IjiItemData(code=12, progtype=ItemClassification.progression),
    "IMPROVED AUTOLOADING": IjiItemData(code=13, progtype=ItemClassification.useful),
    "ADVANCED RECOVERY":    IjiItemData(code=14, progtype=ItemClassification.useful),
    "CYBERNETIC ENDURANCE": IjiItemData(code=15, progtype=ItemClassification.useful),
    "ELECTRONIC MASTERY":   IjiItemData(code=16, progtype=ItemClassification.useful),
    "VENGEANCE":            IjiItemData(code=17, progtype=ItemClassification.useful),
    "GLORY":                IjiItemData(code=18, progtype=ItemClassification.useful)
}

# Filler
items_filler: Dict[str, IjiItemData] = {
    "Health Pickup":    IjiItemData(code=201, progtype=ItemClassification.filler, weight=16),
    "Armor Pickup":     IjiItemData(code=202, progtype=ItemClassification.filler, weight=4),
    "Nano Pickup":      IjiItemData(code=203, progtype=ItemClassification.filler, weight=6),
    "Machine Ammo":     IjiItemData(code=204, progtype=ItemClassification.filler, weight=8),
    "Rocket Ammo":      IjiItemData(code=205, progtype=ItemClassification.filler, weight=4),
    "MPFB Ammo":        IjiItemData(code=206, progtype=ItemClassification.filler, weight=2),
    "Pulse Ammo":       IjiItemData(code=207, progtype=ItemClassification.filler, weight=6),
    "Shock Ammo":       IjiItemData(code=208, progtype=ItemClassification.filler, weight=3),
    "CFIS Ammo":        IjiItemData(code=209, progtype=ItemClassification.filler, weight=1),
    "Nano Overload":    IjiItemData(code=210, progtype=ItemClassification.filler, weight=10),
}

# Traps
items_traps: Dict[str,IjiItemData] = {
    "Rocket to the Face Trap":  IjiItemData(code=401, progtype=ItemClassification.trap),
    "Blits Trap":               IjiItemData(code=402, progtype=ItemClassification.trap),
    "Null Drive Trap":          IjiItemData(code=403, progtype=ItemClassification.trap),
    "Turbo Trap":               IjiItemData(code=404, progtype=ItemClassification.trap),
    "Nap Trap":                 IjiItemData(code=405, progtype=ItemClassification.trap),
    "Clown Shoes Trap":         IjiItemData(code=406, progtype=ItemClassification.trap)
}

items_debug: Dict[str, IjiItemData] = {
    "Fire While Ducking":                           IjiItemData(code=39, progtype=ItemClassification.useful),
    "Fire While Midair":                            IjiItemData(code=40, progtype=ItemClassification.progression)
}


items_doors_1: Dict[str, IjiItemData] = {
    "Sector 1 Door - After Tutorial":               IjiItemData(code=501, progtype=ItemClassification.progression),
    "Sector 1 Door - Left of Start":                IjiItemData(code=502, progtype=ItemClassification.progression),
    "Sector 1 Door - Tutorial Sideroom":            IjiItemData(code=503, progtype=ItemClassification.filler),
    ## Yes, I accidentally skipped 4. Point and laugh at me.
    "Sector 1 Door - Guard Post":                   IjiItemData(code=505, progtype=ItemClassification.progression_skip_balancing),
    "Sector 1 Door - Next to Ribbon":               IjiItemData(code=506, progtype=ItemClassification.filler),
    "Sector 1 Door - Emergency Armory":             IjiItemData(code=507, progtype=ItemClassification.progression),
    "Sector 1 Door - Medical Surplus":              IjiItemData(code=508, progtype=ItemClassification.progression)
}

items_doors_2: Dict[str, IjiItemData] = {
    "Sector 2 Door - Tutorial":                     IjiItemData(code=509, progtype=ItemClassification.progression),
    "Sector 2 Door - Supplies A":                   IjiItemData(code=510, progtype=ItemClassification.progression_skip_balancing),
    "Sector 2 Door - Doctors' Offices":             IjiItemData(code=511, progtype=ItemClassification.progression),
    "Sector 2 Door - Medical Bay":                  IjiItemData(code=512, progtype=ItemClassification.progression),
    "Sector 2 Door - Break Room":                   IjiItemData(code=513, progtype=ItemClassification.progression),
    "Sector 2 Door - Security Station":             IjiItemData(code=514, progtype=ItemClassification.progression_skip_balancing),
    "Sector 2 Door - Ventilation":                  IjiItemData(code=515, progtype=ItemClassification.useful),
    "Sector 2 Door - Storeroom":                    IjiItemData(code=516, progtype=ItemClassification.progression_skip_balancing)
}

items_doors_3: Dict[str, IjiItemData] = {
    "Sector 3 Door - Software Development Top Left":\
                                                    IjiItemData(code=517, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Software Development Bottom Left":\
                                                    IjiItemData(code=518, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Software Development Top Right":\
                                                    IjiItemData(code=519, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Software Development Bottom Right":\
                                                    IjiItemData(code=520, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Storeroom Left":               IjiItemData(code=521, progtype=ItemClassification.useful),
    "Sector 3 Door - Storeroom Right":              IjiItemData(code=522, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Storage Elevator":             IjiItemData(code=523, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Storage B 1/2":                IjiItemData(code=524, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Storage B 2/2":                IjiItemData(code=525, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Restricted Area 1/2":          IjiItemData(code=526, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Restricted Area 2/2":          IjiItemData(code=527, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Main Entrance Left":           IjiItemData(code=528, progtype=ItemClassification.useful),
    "Sector 3 Door - Outside Left":                 IjiItemData(code=529, progtype=ItemClassification.filler),
    "Sector 3 Door - Outside Right":                IjiItemData(code=530, progtype=ItemClassification.filler),
    "Sector 3 Door - Reception Bottom":             IjiItemData(code=531, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Reception Top":                IjiItemData(code=532, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Teleporter":                   IjiItemData(code=533, progtype=ItemClassification.progression),
    "Sector 3 Door - Pulse Cannon":                 IjiItemData(code=534, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Supercharge 1/2":              IjiItemData(code=535, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - Supercharge 2/2":              IjiItemData(code=536, progtype=ItemClassification.progression_skip_balancing),
    "Sector 3 Door - To Krotera":                   IjiItemData(code=537, progtype=ItemClassification.progression),
    "Sector 3 Door - Poster":                       IjiItemData(code=538, progtype=ItemClassification.progression)
}

items_doors_4: Dict[str, IjiItemData] = {
    "Sector 4 Door - Surveillance Control":         IjiItemData(code=539, progtype=ItemClassification.filler),
    "Sector 4 Door - Main Storage":                 IjiItemData(code=540, progtype=ItemClassification.progression),
    "Sector 4 Door - Main Storage Hub":             IjiItemData(code=541, progtype=ItemClassification.progression_skip_balancing),
    "Sector 4 Door - Main Storage Top":             IjiItemData(code=542, progtype=ItemClassification.progression_skip_balancing),
    "Sector 4 Door - Main Storage Overload":        IjiItemData(code=543, progtype=ItemClassification.useful),
    "Sector 4 Door - Restricted Storage Access 1/2":IjiItemData(code=544, progtype=ItemClassification.progression),
    "Sector 4 Door - Restricted Storage Access 2/2":IjiItemData(code=545, progtype=ItemClassification.progression),
    "Sector 4 Door - Guard Post":                   IjiItemData(code=546, progtype=ItemClassification.progression_skip_balancing),
    "Sector 4 Door - Reactor Core":                 IjiItemData(code=547, progtype=ItemClassification.progression_skip_balancing),
    "Sector 4 Door - Classified Materials Access":  IjiItemData(code=548, progtype=ItemClassification.progression),
    "Sector 4 Door - Communicator":                 IjiItemData(code=549, progtype=ItemClassification.progression)
}

items_doors_5: Dict[str, IjiItemData] = {
    "Sector 5 Door - Storeroom 1":                  IjiItemData(code=550, progtype=ItemClassification.filler),
    "Sector 5 Door - Storeroom 2":                  IjiItemData(code=551, progtype=ItemClassification.filler),
    "Sector 5 Door - Storage Control":              IjiItemData(code=552, progtype=ItemClassification.progression_skip_balancing),
    "Sector 5 Door - Incoming Goods":               IjiItemData(code=553, progtype=ItemClassification.filler),
    "Sector 5 Door - Shocksplinter":                IjiItemData(code=554, progtype=ItemClassification.progression_skip_balancing),
    "Sector 5 Door - Elevator":                     IjiItemData(code=555, progtype=ItemClassification.filler),
    "Sector 5 Door - Tasen vs Komato":              IjiItemData(code=556, progtype=ItemClassification.useful),
    "Sector 5 Door - Classified Materials 1/2":     IjiItemData(code=557, progtype=ItemClassification.progression),
    "Sector 5 Door - Classified Materials 2/2":     IjiItemData(code=558, progtype=ItemClassification.progression),
    "Sector 5 Door - Classified Materials Storage": IjiItemData(code=559, progtype=ItemClassification.progression),
    "Sector 5 Door - Storeroom 3":                  IjiItemData(code=560, progtype=ItemClassification.filler),
    "Sector 5 Door - Below Jump Upgrade":           IjiItemData(code=561, progtype=ItemClassification.progression_skip_balancing),
    "Sector 5 Door - Jump Upgrade":                 IjiItemData(code=562, progtype=ItemClassification.progression),
    "Sector 5 Door - Classified Materials Storage Crack Boxes":\
                                                    IjiItemData(code=563, progtype=ItemClassification.filler),
    "Sector 5 Door - Classified Materials Storage Sideroom":\
                                                    IjiItemData(code=564, progtype=ItemClassification.filler)
}

items_doors_6: Dict[str, IjiItemData] = {
    "Sector 6 Door - Shipping Bay":                 IjiItemData(code=565, progtype=ItemClassification.filler),
    "Sector 6 Door - Ventilation Shaft":            IjiItemData(code=566, progtype=ItemClassification.progression),
    "Sector 6 Door - Ventilation Shaft Shocksplinter":\
                                                    IjiItemData(code=567, progtype=ItemClassification.progression_skip_balancing),
    "Sector 6 Door - Ventilation Shaft Below Shocksplinter":\
                                                    IjiItemData(code=568, progtype=ItemClassification.useful),
    "Sector 6 Door - Main Elevator Bottom":         IjiItemData(code=569, progtype=ItemClassification.progression),
    "Sector 6 Door - Poster":                       IjiItemData(code=570, progtype=ItemClassification.progression),
    "Sector 6 Door - Main Elevator Top":            IjiItemData(code=571, progtype=ItemClassification.progression_skip_balancing),
    "Sector 6 Door - Storeroom":                    IjiItemData(code=572, progtype=ItemClassification.useful),
    "Sector 6 Door - Elevator Shocksplinter":       IjiItemData(code=573, progtype=ItemClassification.progression_skip_balancing),
    "Sector 6 Door - Genetic Research Access":      IjiItemData(code=574, progtype=ItemClassification.progression),
    "Sector 6 Door - Genetic Research Exit":        IjiItemData(code=575, progtype=ItemClassification.progression_skip_balancing),
    "Sector 6 Door - Left of CFIS":                 IjiItemData(code=576, progtype=ItemClassification.progression),
    "Sector 6 Door - Right of CFIS":                IjiItemData(code=577, progtype=ItemClassification.progression_skip_balancing),
    "Sector 6 Door - Elevator Exit":                IjiItemData(code=578, progtype=ItemClassification.progression),
    "Sector 6 Door - Neoweapons Research Sideroom": IjiItemData(code=579, progtype=ItemClassification.useful),
    "Sector 6 Door - Dark Room":                    IjiItemData(code=580, progtype=ItemClassification.progression),
    "Sector 6 Door - Neoweapons Research MPFB":     IjiItemData(code=581, progtype=ItemClassification.progression_skip_balancing),
    "Sector 6 Door - Black Ops Left":               IjiItemData(code=582, progtype=ItemClassification.progression),
    "Sector 6 Door - Black Ops Right":              IjiItemData(code=583, progtype=ItemClassification.progression_skip_balancing),
    "Sector 6 Door - End Shaft Right":              IjiItemData(code=584, progtype=ItemClassification.progression),
    "Sector 6 Door - End Shaft Left":               IjiItemData(code=585, progtype=ItemClassification.progression_skip_balancing),
    "Sector 6 Door - Shortcut to End":              IjiItemData(code=586, progtype=ItemClassification.progression_skip_balancing),
    "Sector 6 Door - End Shaft Top":                IjiItemData(code=587, progtype=ItemClassification.progression)
}

items_doors_7: Dict[str, IjiItemData] = {
    
}

items_doors_8: Dict[str, IjiItemData] = {
    
}

items_doors_9: Dict[str, IjiItemData] = {
    
}

items_doors_x: Dict[str, IjiItemData] = {
    
}

items_doors = {
    **items_doors_1,
    **items_doors_2,
    **items_doors_3,
    **items_doors_4,
    **items_doors_5,
    **items_doors_6,
    **items_doors_7,
    **items_doors_8,
    **items_doors_9,
    **items_doors_x
}

item_table = {
    **items_primary,
    **items_other,
    **items_traits,
    **items_filler,
    **items_traps,
    **items_debug,
    **items_doors
}

#####
#####
##### ALL ITEMS BELOW THIS COMMENT ARE (CURRENTLY) UNIMPLEMENTED
#####
#####


items_weapons: Dict[str, IjiItemData] = {
    "Shotgun":                          IjiItemData(code=20, progtype=ItemClassification.progression),
    "Machine Gun":                      IjiItemData(code=21, progtype=ItemClassification.progression),
    "Rocket Launcher":                  IjiItemData(code=22, progtype=ItemClassification.progression),
    "MPFB Devastator":                  IjiItemData(code=23, progtype=ItemClassification.progression),
    "Resonance Detonator":              IjiItemData(code=24, progtype=ItemClassification.progression),
    "Pulse Cannon":                     IjiItemData(code=25, progtype=ItemClassification.progression),
    "Shocksplinter":                    IjiItemData(code=26, progtype=ItemClassification.progression),
    "Cyclic Fusion Ignition System":    IjiItemData(code=27, progtype=ItemClassification.progression)
}

items_specialweapons: Dict[str, IjiItemData] = {
    "Banana Gun":   IjiItemData(code=28, progtype=ItemClassification.progression),
    "Massacre":     IjiItemData(code=29, progtype=ItemClassification.progression),
    "Null Driver":  IjiItemData(code=30, progtype=ItemClassification.progression)
}

items_progressiveweapons: Dict[str, IjiItemData] = {
    "Progressive Shotgun":                          IjiItemData(code=31, progtype=ItemClassification.progression),
    "Progressive Machine Gun":                      IjiItemData(code=32, progtype=ItemClassification.progression),
    "Progressive Rocket Launcher":                  IjiItemData(code=33, progtype=ItemClassification.progression),
    "Progressive MPFB Devastator":                  IjiItemData(code=34, progtype=ItemClassification.progression),
    "Progressive Resonance Detonator":              IjiItemData(code=35, progtype=ItemClassification.progression),
    "Progressive Pulse Cannon":                     IjiItemData(code=36, progtype=ItemClassification.progression),
    "Progressive Shocksplinter":                    IjiItemData(code=37, progtype=ItemClassification.progression),
    "Progressive Cyclic Fusion Ignition System":    IjiItemData(code=38, progtype=ItemClassification.progression)
}



### End of unimplemented section.

item_groups_table = {
    "Stats": items_primary.keys(),
    "Traits": items_traits.keys(),
    "Doors": items_doors.key(),
    "Weapons": {
        **items_weapons,
        **items_specialweapons,
        **items_progressiveweapons,
    },
    "Normal Weapons": {
        **items_weapons,
        **items_progressiveweapons,
    },
    "Special Weapons": items_specialweapons.keys(),
    # Not sure this one's useful. I'll leave it here but comment it out for now.
    # "Collectibles": {
    #     "Poster",
    #     "Ribbon"
    # }
}
