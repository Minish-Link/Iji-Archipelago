from math import ceil
from typing import List, TYPE_CHECKING, Dict
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Range, Toggle, DeathLink, Choice, OptionDict, DefaultOnToggle, OptionGroup

if TYPE_CHECKING:
    from . import IjiWorld

def get_compacted_stat_items(world: "IjiWorld") -> Dict[str, int]:
    compacted_items = {
        "Health Stat":       ceil(world.options.HealthItems.value    / world.options.CompactStatItems),  # Health Stat
        "Attack Stat":       ceil(world.options.AttackItems.value    / world.options.CompactStatItems),  # Attack Stat
        "Assimilate Stat":   ceil(world.options.AssimilateItems.value/ world.options.CompactStatItems),  # Assimilate Stat
        "Strength Stat":     ceil(world.options.StrengthItems.value  / world.options.CompactStatItems),  # Strength Stat
        "Crack Stat":        ceil(world.options.CrackItems.value     / world.options.CompactStatItems),  # Crack Stat
        "Tasen Stat":        ceil(world.options.TasenItems.value     / world.options.CompactStatItems),  # Tasen Stat
        "Komato Stat":       ceil(world.options.KomatoItems.value    / world.options.CompactStatItems)   # Komato Stat
    }

    return compacted_items



class EndGoal(Choice):
    """
    Sector X: Reach the end of Sector X and defeat General Tor.
    
    Sector Z: Enter and complete Sector Z.
    The requirements to enter Sector Z can be adjusted via the settings below.
    
    Sector Y: Obtain the Null Driver from Sector Z, defeat General Tor with it, then reach the end of Sector Y.
    The requirements to enter Sector Z, and to obtain the Null Driver, can be adjusted via the settings below.
    """
    display_name = "End Goal"
    default = 1
    option_sector_x = 1
    option_sector_z = 2
    option_sector_y = 3

class SectorZPosterLocationsRequired(Range):
    """
    If Sector Z locations are not included in your world, this option does nothing, and Sector Z will also be inaccessible.
    How many Poster locations you need to reach to enter the Sector Z portal.
    """
    display_name = "Sector Z Posters Required"
    default = 10
    range_start = 0
    range_end = 10

class SectorZRibbonItemsRequired(Range):
    """
    If Sector Z locations are not included in your world, this option does nothing, and Ribbon items will not be shuffled into the item pool.
    How many Ribbon items are required to enter the Sector Z portal.
    """
    display_name = "Sector Z Ribbons Required"
    default = 0
    range_start = 0
    range_end = 10

class NullDriverPosterLocationsRequired(Range):
    """
    If Sector Z locations are not included in your world, this option does nothing.
    How many Poster locations you need to reach to enter the portal leading to the Null Driver.

    """
    display_name = "Null Driver Posters Required"
    default = 10
    range_start = 0
    range_end = 10

class NullDriverRibbonItemsRequired(Range):
    """
    If Sector Z locations are not included in your world, this options does nothing.
    How many Ribbon locations you need to enter the portal leading to the Null Driver.
    """
    display_name = "Null Driver Ribbons Required"
    default = 10
    range_start = 0
    range_end = 10

class RibbonItemCount(Range):
    """
    If Sector Z locations are not included in your world, this option does nothing.
    How many total Ribbon items to shuffle into the item pool. If the number of Ribbons added is fewer than the number required
    to access Sector Z or the Null Driver, extra Ribbons will be added to meet the minimum.
    If Sector Z or the Null Driver require no ribbons to enter, no Ribbon items will be added to the pool.
    """
    display_name = "Total Ribbon Items"
    default = 10
    range_start = 0
    range_end = 20

class PostGameLocations(Choice):
    """
    Whether to include Sector Z and/or Sector Y locations to the pool.
    (Contains Posters, Logbooks, and the Null Driver)
    Intended for worlds that do not release on completion,
    or if Sector Z can be accessed earlier than Sector X
    
    None: Do not add post game locations to the pool.
    
    Sector Z: Adds Sector Z locations to the pool. 
    If your goal is to complete Sector Z or Sector Y, this option does nothing.
    
    Sector Y: Adds Sector Y locations to the pool.
    If your goal is to complete Sector Y, this option does nothing.
    """
    display_name = "Post Game Locations"
    option_none = 0
    option_sector_z = 1
    option_sector_y = 2
    default = 0

class RibbonLocations(DefaultOnToggle):
    """
    If enabled, Finding ribbons sends checks.
    """

class PosterLocations(DefaultOnToggle):
    """
    If enabled, Finding posters sends checks.
    """

class SuperchargeLocations(Toggle):
    """
    If enabled, Finding supercharges sends checks.
    """

class BasicWeaponLocations(Choice):
    """
    Determines if collecting Basic Nanoweapons send checks.
    Off: Basic Nanoweapons are not locations.

    First Time: Assimilating a basic Nanoweapon sends a check, one per type of weapon.

    First Per Sector: Assimilating a basic Nanoweapon sends a check, one per type of weapon per Sector.

    All Instances: All instances of basic Nanoweapons in the game send checks
    """
    display_name = "Basic Weapon Locations"
    option_off = 0
    option_first_time = 1
    option_first_per_sector = 2
    option_all_instances = 3
    default = 1

class CombinedWeaponLocations(DefaultOnToggle):
    """
    If enabled, combining two Nanoweapons together sends a check, one per combination.
    """
    display_name = "Combined Weapon Locations"

class UniqueWeaponLocations(Toggle):
    """
    If enabled, obtaining special Nanoweapons sends checks.
    Includes Banana Gun, Massacre, and Null Driver.
    Null Driver will not be a location if Sector Z locations are not included in the world.
    """

class UpgradeLocations(DefaultOnToggle):
    """
    If enabled, obtaining Jump and Armor Upgrades sends checks
    """

class LogbookLocations(Toggle):
    """
    If enabled, each logbook in the game is a check
    """
    display_name = "Logbook Locations"

class PacifistLocations(Toggle):
    """
    If disabled, locations that require the player to be pacifist to some extent will not be added.
    This includes the Deep Sector Logbooks and Supercharge in Sector 9, and the Massacre in Sector X.
    """
    display_name = "Pacifist Locations"

class SectorAccessItems(Range):
    """
    How many Sector Access items to add to the item pool.
    9 of them are required to beat the game, and obtaining any more than that has no effect
    """
    display_name = "Sector Access Items"
    default = 9
    range_start = 9
    range_end = 15

class HealthItems(Range):
    """
    How many Health Stat items to add to the item pool.
    Obtaining more than 9 has no effect.
    """
    display_name = "Health Stat items"
    default = 9
    range_start = 9
    range_end = 15

class AttackItems(Range):
    """
    How many Attack Stat items to add to the item pool.
    Obtaining more than 9 has no effect.
    """
    display_name = "Attack Stat Items"
    default = 9
    range_start = 9
    range_end = 15

class AssimilateItems(Range):
    """
    How many Assimilate Stat items to add to the item pool.
    Obtaining more than 9 has no effect.
    """
    display_name = "Assimilate Stat Items"
    default = 9
    range_start = 9
    range_end = 15

class StrengthItems(Range):
    """
    How many Strength Stat items to add to the item pool.
    Obtaining more than 9 has no effect.
    """
    display_name = "Strength Stat Items"
    default = 9
    range_start = 9
    range_end = 15

class CrackItems(Range):
    """
    How many Crack Stat items to add to the item pool.
    Obtaining more than 9 has no effect.
    """
    display_name = "Crack Stat Items"
    default = 9
    range_start = 9
    range_end = 15

class TasenItems(Range):
    """
    How many Tasen Stat items to add to the item pool.
    Obtaining more than 9 has no effect.
    """
    display_name = "Tasen Stat Items"
    default = 9
    range_start = 9
    range_end = 15

class KomatoItems(Range):
    """
    How many Komato Stat items to add to the item pool.
    Obtaining more than 9 has no effect.
    """
    display_name = "Komato Stat Items"
    default = 9
    range_start = 9
    range_end = 15

class SpecialTraitItems(Toggle):
    """
    If enabled, the Special Trait items will be shuffled into the item pool.
    """
    display_name = "Special Traits"

class SuperchargePointHandling(Choice):
    """
    Off: Supercharges behave normally, only granting 1 Stat point for the current Sector when collected.

    Progressive: Supercharges grant 1 Stat point when collected,
    and also grant 1 Stat point at the start of each Sector that comes after the Sector it was collected in.
    
    Shuffled: Supercharges no longer grant Stat points when collected.
    Instead, 10 Supercharge items are shuffled into the item pool that each grant 1 Stat point at the start of each Sector.
    """
    display_name = "Supercharge Points"
    option_off = 0
    option_progressive = 1
    option_shuffled = 2
    default = 1

class ExtraSupercharges(Range):
    """
    Adds extra Supercharge items to the pool that each grant 1 Stat point at the start of each Sector.
    (If Supercharge Points are shuffled in the above option, this option stacks on top of it.)
    """
    display_name = "Extra Supercharges"
    default = 0
    range_start = 0
    range_end = 10

class TrapPercentage(Range):
    """
    What percentage of filler items should be replaced by traps
    """
    display_name = "Trap Percentage"
    default = 0
    range_start = 0
    range_end = 100

class RocketTrapWeight(Range):
    """
    How weighted Rocket to the Face traps are to be chosen, if traps are shuffled.
    Spawns a rocket that flies towards Iji's face.
    0 Disables Rocket to the Face traps.
    """
    display_name = "Rocket to the Face Weight"
    default = 20
    range_start = 0
    range_end = 100

class BlitsTrapWeight(Range):
    """
    How weighted Blits traps are to be chosen, if traps are shuffled.
    Spawns a Blits nest under Iji's feet that spawns a few Blits enemies.
    0 Disables Blits traps.
    """
    display_name = "Blits Weight"
    default = 20
    range_start = 0
    range_end = 100

class NullDriveTrapWeight(Range):
    """
    How weighted Null Drive traps are to be chosen, if traps are shuffled.
    Randomly shuffles some of the background/tileset images until the game is closed.
    0 Disables Null Drive traps
    """
    display_name = "Null Drive Weight"
    default = 0
    range_start = 0
    range_end = 100

class NullDriveFactor(Range):
    """
    How severe the effect of Null Drive traps are.
    The higher the value, the more backgrounds/tileset images get reassigned.
    50 is the severity used by the vanilla Null Driver
    """
    display_name = "Null Drive Factor"
    default = 25
    range_start = 1
    range_end = 100

class TurboTrapWeight(Range):
    """
    How weighted Turbo traps are to be chosen, if traps are shuffled.
    Doubles the game speed for 20 seconds.
    0 Disables Turbo traps
    """
    display_name = "Turbo Weight"
    default = 20
    range_start = 0
    range_end = 100

class NapTrapWeight(Range):
    """
    How weighted Nap traps are to be chosen, if traps are shuffled.
    Knocks Iji down, and prevents her from getting up for 5 seconds.
    0 Disables Nap traps
    """
    display_name = "Nap Weight"
    default = 20
    range_start = 0
    range_end = 100

class ClownShoesWeight(Range):
    """
    How weighted Clown Shoe traps are to be chosen, if traps are shuffled.
    Iji's footsteps make squeaky noises for 1 minute.
    0 Disables Clown Shoe traps
    """
    display_name = "Clown Shoes Weight"
    default = 20
    range_start = 0
    range_end = 100

class HealthBalancing(DefaultOnToggle):
    """
    If enabled, Sectors will logically require Health Stat items.
    This should force Health Stat items to be forced into earlier spheres.
    Each Sector beyond Sector 1 requires 1 more Health item than the previous,
    up to Sector X logically requiring 9 Health Stat items
    """
    display_name = "Health Progression Balancing"

class CompactStatItems(Range):
    """
    Determines how many levels each Stat item should raise its respective level cap by.
    Higher values will reduce the number of Stat items shuffled into the pool to keep the total value of stats, rounded up
    i.e. if there would be 15 Health Stat items to start, and they are compacted to give 4 each,
    There will be 4 Health Stat items shuffled into the final pool, for a total of 16 levels
    Useful for worlds that want to have fewer location counts.
    """
    display_name = "Compact Stat Items"
    default = 1
    range_start = 1
    range_end = 9

class IjiDeathLink(DeathLink):
    """
    When you die, everyone dies. The reverse is also true.
    
    If DeathLinkDamage is set below 20, you will instead take damage when sent a death
    """

class DeathLinkDamage(Range):
    """
    How much HP damage you take when receiving a death from another player.
    If set to 20, receiving a death instantly kills you instead.
    """
    default = 20
    range_start = 1
    range_end = 20

class LogicDifficulty(Choice):
    """
    Normal Logic: Expects the player to reach locations in the normal, dev-intended ways

    Obscure Logic: Expects the player to reach locations that are technically possible to reach, albeit in obscure or unintended ways.
    Note: I haven't (yet) documented any of these logic skips, so choose this at your own risk

    Extreme Logic: The cursed option. Includes obscure logic skips plus a few other terrible ones.
    """
    display_name = "Logic Difficulty"
    option_normal_logic = 1
    option_obscure_logic = 2
    option_extreme_logic = 3
    default = 1

class Doorsanity(Toggle):
    """
    If enabled, Attempting to open Doors will be location checks,
    Doors will be shuffled into the item pool, and doors won't open until their corresponding item is received
    """
    display_name = "Door Shuffle"

@dataclass
class IjiOptions(PerGameCommonOptions):
    EndGoal:                            EndGoal
    SectorZPosterLocationsRequired:     SectorZPosterLocationsRequired
    SectorZRibbonItemsRequired:         SectorZRibbonItemsRequired
    NullDriverPosterLocationsRequired:  NullDriverPosterLocationsRequired
    NullDriverRibbonItemsRequired:      NullDriverRibbonItemsRequired
    RibbonItemCount:                    RibbonItemCount
    PostGameLocations:                  PostGameLocations

    RibbonLocations:                    RibbonLocations
    PosterLocations:                    PosterLocations
    SuperchargeLocations:               SuperchargeLocations
    BasicWeaponLocations:               BasicWeaponLocations
    CombinedWeaponLocations:            CombinedWeaponLocations
    UniqueWeaponLocations:              UniqueWeaponLocations
    UpgradeLocations:                   UpgradeLocations
    LogbookLocations:                   LogbookLocations
    PacifistLocations:                  PacifistLocations

    SectorAccessItems:                  SectorAccessItems
    HealthItems:                        HealthItems
    AttackItems:                        AttackItems
    AssimilateItems:                    AssimilateItems
    StrengthItems:                      StrengthItems
    CrackItems:                         CrackItems
    TasenItems:                         TasenItems
    KomatoItems:                        KomatoItems
    CompactStatItems:                   CompactStatItems
    SpecialTraitItems:                  SpecialTraitItems
    ExtraSupercharges:                  ExtraSupercharges

    TrapPercentage:                     TrapPercentage
    RocketTrapWeight:                   RocketTrapWeight
    BlitsTrapWeight:                    BlitsTrapWeight
    NullDriveTrapWeight:                NullDriveTrapWeight
    NullDriveFactor:                    NullDriveFactor
    TurboTrapWeight:                    TurboTrapWeight
    NapTrapWeight:                      NapTrapWeight
    ClownShoesWeight:                   ClownShoesWeight

    HealthBalancing:                    HealthBalancing
    SuperchargePointHandling:           SuperchargePointHandling
    DeathLink:                          IjiDeathLink
    DeathLinkDamage:                    DeathLinkDamage
    LogicDifficulty:                    LogicDifficulty
    Doorsanity:                         Doorsanity

iji_option_groups = [
    OptionGroup("Goal Options", [
        EndGoal,
        SectorZPosterLocationsRequired,
        SectorZRibbonItemsRequired,
        NullDriverPosterLocationsRequired,
        NullDriverRibbonItemsRequired,
        RibbonItemCount,
        PostGameLocations
    ]),
    OptionGroup("Locations", [
        RibbonLocations,
        PosterLocations,
        SuperchargeLocations,
        BasicWeaponLocations,
        CombinedWeaponLocations,
        UniqueWeaponLocations,
        UpgradeLocations,
        LogbookLocations,
        PacifistLocations
    ]),
    OptionGroup("Items", [
        SectorAccessItems, 
        HealthItems,
        AttackItems,
        AssimilateItems,
        StrengthItems,
        CrackItems,
        TasenItems,
        KomatoItems,
        CompactStatItems,
        SpecialTraitItems,
        ExtraSupercharges
    ]),
    OptionGroup("Traps", [
        TrapPercentage,
        RocketTrapWeight,
        BlitsTrapWeight,
        NullDriveTrapWeight,
        NullDriveFactor,
        TurboTrapWeight,
        NapTrapWeight,
        ClownShoesWeight
    ]),
    OptionGroup("Miscellaneous", [
        HealthBalancing,
        SuperchargePointHandling,
        IjiDeathLink,
        DeathLinkDamage,
        LogicDifficulty,
        Doorsanity
    ])
]
