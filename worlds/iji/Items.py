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
    progtype: ItemClassification = ItemClassification.filler,
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

    if world.options.SpecialTraitItems.value == world.options.SpecialTraitItems.option_items_only or \
       world.options.SpecialTraitItems.value == world.options.SpecialTraitItems.option_locations_and_items:
        for name in items_traits.keys():
            itempool += create_multiple_items(world, name, 1)

    itempool += create_poster_items(world)
    itempool += create_ribbon_items(world)

    itempool += create_filler_items(world, get_total_locations(world) - len(itempool))

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

def create_poster_items(world: "IjiWorld") -> List[Item]:
    itemlist: List[Item] = []
    
    if world.options.EndGoal.value >= world.options.EndGoal.option_sector_z or \
        world.options.PostGameLocations.value >= world.options.PostGameLocations.option_sector_z:

        if (world.options.SectorZRequirementType == world.options.SectorZRequirementType.option_poster_items and \
            world.options.SectorZRequirements.value > 0) or \
            (world.options.NullDriverPosterRequirementType.value == \
            world.options.NullDriverPosterRequirementType.option_poster_items and \
            world.options.NullDriverPosterRequirement > 0):

            itemlist += create_multiple_items(world, "Poster", 10)

    return itemlist

def create_ribbon_items(world: "IjiWorld") -> List[Item]:
    itemlist: List[Item] = []

    if world.options.EndGoal.value >= world.options.EndGoal.option_sector_z or \
        world.options.PostGameLocations.value >= world.options.PostGameLocations.option_sector_z:

        if world.options.NullDriverRibbonRequirementType.value == \
            world.options.NullDriverRibbonRequirementType.option_ribbon_items and \
            world.options.NullDriverRibbonRequirement.value > 0:

            itemlist += create_multiple_items(world, "Ribbon", 10)

    return itemlist

def create_filler_items(world: "IjiWorld", count: int) -> List[Item]:
    fillerlist: List[Item] = []

    #trapitemcount: int = 0
    #if world.options.RocketTrapWeight.value > 0 or world.options.BlitsTrapWeight.value > 0 or \
    #    world.options.NullDriveTrapWeight.value > 0 or world.options.TurboTrapWeight.value > 0 or \
    #    world.options.NapTrapWeight.value > 0 or world.options.ClownShoesWeight.value > 0:
    #
    #    trapitemcount = floor((world.options.TrapPercentage.value / 100.0) * count)
    #
    #filleritemcount: int = count - trapitemcount
    #
    #fillerweights: Dict[str, int] = {}
    #
    #for name, filler in items_filler.items():
    #    fillerweights[name] = filler.weight
    #
    #for i in range(filleritemcount):
    #    fillerlist += [create_item(world,
    #        world.random.choices(list(fillerweights.keys()), weights=list(fillerweights.values()), k=1)[0])]
    #
    #fillerlist += create_trap_items(world, trapitemcount)

    return fillerlist

def create_trap_items(world: "IjiWorld", count: int) -> List[Item]:
    traplist: List[Item] = []

    #trapweights: Dict[str, int] = {}
    #
    #trapweights["Rocket to the Face Trap"] = world.options.RocketTrapWeight.value
    #trapweights["Blits Trap"] = world.options.BlitsTrapWeight.value
    #trapweights["Null Drive Trap"] = world.options.NullDriveTrapWeight.value
    #trapweights["Turbo Trap"] = world.options.TurboTrapWeight.value
    #trapweights["Nap Trap"] = world.options.NapTrapWeight.value
    #trapweights["Clown Shoes Trap"] = world.options.ClownShoesWeight.value
    #
    #for i in range(count):
    #    traplist += [create_item(world,
    #        world.random.choices(list(trapweights.keys()), weights=list(trapweights.values()), k=1)[0])]

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
    "Poster":       IjiItemData(code=10, progtype = ItemClassification.progression),
    "Ribbon":       IjiItemData(code=11, progtype = ItemClassification.progression)
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
    "Health Pickup":    IjiItemData(code=201, weight=16),
    "Armor Pickup":     IjiItemData(code=202, weight=4),
    "Nano Pickup":      IjiItemData(code=203, weight=6),
    "Machine Ammo":     IjiItemData(code=204, weight=8),
    "Rocket Ammo":      IjiItemData(code=205, weight=4),
    "MPFB Ammo":        IjiItemData(code=206, weight=2),
    "Pulse Ammo":       IjiItemData(code=207, weight=6),
    "Shock Ammo":       IjiItemData(code=208, weight=3),
    "CFIS Ammo":        IjiItemData(code=209, weight=1),
    "Nano Overload":    IjiItemData(code=210, weight=10),
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

item_table = {
    **items_primary,
    **items_other,
    **items_traits,
    **items_filler,
    **items_traps
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

# items_doors: IjiItemData = {}

### End of unimplemented section.

item_groups_table = {
    "Stats": items_primary.keys(),
    "Traits": items_traits.keys(),
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
