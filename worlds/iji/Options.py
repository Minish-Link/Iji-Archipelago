from math import ceil
from typing import List, TYPE_CHECKING, Dict
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Range, Toggle, DeathLink, Choice, DefaultOnToggle, OptionGroup, OptionList

if TYPE_CHECKING:
    from . import IjiWorld

def define_health_balancing(world: "IjiWorld") -> List[int]:
    value_list = world.options.health_balancing.value
    while (len(value_list) < 9):
        value_list.append(0)

    for i in range(9):
        if value_list[i] < 0:
            value_list[i] = get_random_health_balance_value(world, value_list[i])
        if value_list[i] > 9:
            value_list[i] = 9
    
    return value_list[:8]


def get_random_health_balance_value(world: "IjiWorld", value: int) -> int:
    return world.random.randint(0, abs(value))

class EndGoal(Choice):
    """
    Sector 3: Reach the end of Sector 3 and defeat Elite Krotera. Sectors 4-X will be excluded.

    Sector 5: Reach the end of Sector 5 and defeat Assassin Asha. Sectors 6-X will be excluded.

    Sector 7: Reach the end of Sector 7 and defeat Sentinel Proxima. Sectors 8-X will be excluded.

    Sector 9: Reach the end of Sector 9 and defeat Annihilator Iosa. Sector X will be excluded.

    Sector X: Reach the end of Sector X and defeat General Tor. The vanilla ending of the game.
    
    Sector Z: Enter and reach the end of Sector Z. Sectors 1-X are included.
    
    Sector Y: Obtain the Null Driver from Sector Z, defeat General Tor with it, then reach the end of Sector Y.
    """
    display_name = "End Goal"
    default = 10
    option_sector_3 = 3
    option_sector_5 = 5
    option_sector_7 = 7
    option_sector_9 = 9
    option_sector_x = 10
    option_sector_z = 11
    option_sector_y = 12

class GoalPosterLocations(Range):
    """
    How many Poster locations you are required to find before being able to complete your goal.
    If you chose Sector X as your goal, the elevator at the end of the sector will be deactivated until you find them.
    If you chose Sector Y or Sector Z as your goal, you won't be able to enter Sector Z until you find them.
    """
    display_name = "Poster Locations Required for Goal"
    default = 0
    range_start = 0
    range_end = 10

class GoalRibbonItems(Range):
    """
    What percentage of your Ribbon items you need to obtain to complete your goal.
    If you chose Sector 3, 5, 7, or 9 as your goal, the boss arena in that Sector will be blocked by a door until you get enough.
    If you chose Sector X as your goal, the elevator at the end of the sector will be deactivated until you get enough.
    If you chose Sector Y or Sector Z as your goal, you won't be able to enter Sector Z until you get enough.
    """
    display_name = "Ribbon Percentage Required for Goal"
    default = 0
    range_start = 0
    range_end = 100

class RibbonItemCount(Range):
    """
    How many Ribbon items to add to the item pool.
    If there are fewer available locations than this number,
    a number of ribbons equal to the number of remaining locations will be added instead.
    If your goal requires zero ribbons, no ribbons will be added.
    """
    display_name = "Maximum Ribbon Items"
    default = 10
    range_start = 0
    range_end = 500

class PosterLocations(DefaultOnToggle):
    """
    If enabled, Finding posters sends checks.
    """
    display_name = "Poster Locations"

class SuperchargeLocations(Choice):
    """
    Whether or not collecting Supercharges are checks.
    Off: Supercharges are not locations.
    Locations Only: Supercharges are locations and award a stat point as normal
    Locations and Items: Supercharges are locations, and do NOT award stat points. Instead, 10 Supercharge items will be added.
    """
    display_name = "Supercharge Locations"
    option_off = 0
    option_locations_only = 1
    option_locations_and_items = 2

class BasicWeaponLocations(Choice):
    """
    How obtaining new weapons will send checks.

    First Time: Assimilating a basic Nanoweapon sends a check, one per type of weapon.

    First Per Sector: Assimilating a basic Nanoweapon sends a check, one per type of weapon per Sector.

    All Instances: All instances of basic Nanoweapons in the game send checks
    """
    display_name = "Basic Weapon Locations"
    option_first_time = 1
    option_first_per_sector = 2
    option_all_instances = 3
    default = 1

class LogbookLocations(Toggle):
    """
    If enabled, each logbook in the game is a check
    """
    display_name = "Logbook Locations"

class SectorAccessItems(Range):
    """
    How many extra Sector Access items to add to the item pool.
    """
    display_name = "Extra Sector Access Items"
    default = 0
    range_start = 0
    range_end = 20

class HealthItems(Range):
    """
    How many extra Health Stat items to add to the item pool.
    """
    display_name = "Extra Health Stat items"
    default = 0
    range_start = 0
    range_end = 20

class AttackItems(Range):
    """
    How many extra Attack Stat items to add to the item pool.
    """
    display_name = "Extra Attack Stat Items"
    default = 0
    range_start = 0
    range_end = 20

class AssimilateItems(Range):
    """
    How many extra Assimilate Stat items to add to the item pool.
    """
    display_name = "Extra Assimilate Stat Items"
    default = 0
    range_start = 0
    range_end = 20

class StrengthItems(Range):
    """
    How many extra Strength Stat items to add to the item pool.
    """
    display_name = "Extra Strength Stat Items"
    default = 0
    range_start = 0
    range_end = 20

class CrackItems(Range):
    """
    How many extra Crack Stat items to add to the item pool.
    """
    display_name = "Extra Crack Stat Items"
    default = 0
    range_start = 0
    range_end = 20

class TasenItems(Range):
    """
    How many extra Tasen Stat items to add to the item pool.
    """
    display_name = "Extra Tasen Stat Items"
    default = 0
    range_start = 0
    range_end = 20

class KomatoItems(Range):
    """
    How many extra Komato Stat items to add to the item pool.
    """
    display_name = "Extra Komato Stat Items"
    default = 0
    range_start = 0
    range_end = 20

class SpecialTraitItems(Toggle):
    """
    If enabled, the Special Trait items will be shuffled into the item pool.
    """
    display_name = "Special Traits"

class ExtraSupercharges(Range):
    """
    Adds extra Supercharge items to the pool that each grant 1 Stat point at the start of each Sector.
    """
    display_name = "Extra Supercharges"
    default = 0
    range_start = 0
    range_end = 20

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

class BananaTrapWeight(Range):
    """
    How weighted Banana traps are to be chosen, if traps are shuffled.
    Spawns a banana.
    0 Disables Banana traps
    """
    display_name = "Banana Weight"
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

class HealthBalancing(OptionList):
    """
    To help push health stat items into earlier locations in the multiworld,
    and to ensure that you don't have to play late game sectors with low health,
    this option will force Sectors to require having a minimum number of Health Stat items to be in logic.
    It won't physically lock you out of the Sectors, so you can still play Sectors out of logic if you want.

    Should have nine values, representing Sectors 2 through X (Sector 1 never requires Health)
    Values range from 0 to 9.
    Alternatively, you can also enter negative numbers to choose a random value for that sector.
    The absolute value of a negative number determines the maximum range for that random value.
    e.g. a value of -9 will allow any number between 0 and 9 to be chosen,
    and a value of -3 will choose a number between 0 and 3.
    """
    display_name = "Health Balancing Values"
    default = [1,2,3,4,5,6,7,8,9]

class IjiDeathLink(DeathLink):
    """
    When you die, everyone dies. The reverse is also true.
    
    If DeathLinkDamage is set below 20, you will instead take damage when sent a death
    """
    display_name = "Death Link"

class DeathLinkDamage(Range):
    """
    How much HP damage you take when receiving a death from another player.
    If set to 20, receiving a death instantly kills you instead.
    """
    display_name = "Death Link Damage"
    default = 20
    range_start = 1
    range_end = 20

class LogicDifficulty(Choice):
    """
    Normal Logic: Expects the player to reach locations in the normal, dev-intended ways

    Hard Logic: Expects the player to utilize methods needed to reach posters and supercharges, but in other locations.

    Extreme Logic: 

    Ultimortal Logic: 

    reallyjoel's Dad Logic: Anything goes. If it's technically possible, it's in logic.
    """
    display_name = "Logic Difficulty"
    option_normal_logic = 0
    option_hard_logic = 1
    option_extreme_logic = 2
    option_ultimortal_logic = 3
    option_reallyjoelsdad_logic = 4
    default = 0

class MusicShuffle(Choice):
    """
    Whether or not to randomly reassign music tracks.
    Off: No shuffled music
    Levels Only: Only Level Music gets shuffled amongst each other.
    Full Shuffle: All Looping music tracks get shuffled amongst each other
    """
    display_name = "Music Shuffle"
    option_off = 0
    option_levels_only = 1
    option_full_shuffle = 2
    default = 0

class OutOfOrderSectors(Toggle):
    """
    If enabled, Sector Access Items will give access to a specific sector, and Sectors may be accessed outside their intended order.
    If there are extra Sector Access Items are in the pool, the extras will choose a semi-random Sector to grant access to.

    If disabled, Sector Access Items will instead be progressive, giving access to Sectors in their vanilla order.
    """
    display_name = "Out of Order Sectors"

class Levelsanity(Toggle):
    """
    If enabled, Leveling up will no longer award stat points.
    Instead, 50 Supercharge items will be added to the multiworld.
    """
    display_name = "Levelsanity"

class JumpUpgrades(Choice):
    """
    How Jump upgrade items should be handled.

    Vanilla: Jump Upgrade items can be found in their vanilla locations

    Shuffle: Jump Upgrade items can be found anywhere in the multiworld.
    """
    display_name = "Jump Upgrades"
    option_vanilla = 0
    option_shuffle = 1
    default = 0

class ArmorUpgrades(Choice):
    """
    How armor upgrade items and locations should be handled.

    Vanilla: Armor Upgrade items will be found in their vanilla locations.

    Shuffle: Armor Upgrade items can be found anywhere in the multiworld.

    Cursed: The player starts with only 1/4 of their Armor bar.
        The first three armor upgrades found give an additional 1/4 of the bar,
        and the last two increase the Armor stat as normal.
    """
    display_name = "Armor Upgrades"
    option_vanilla = 0
    option_shuffle = 1
    option_vanilla_cursed = 2
    option_shuffle_cursed = 3
    default = 0

class CrackBoxLocations(Toggle):
    """
    If enabled, opening the locked Security Boxes will be checks.
    """
    display_name = "Security Box Locations"

class OverloadLocations(Toggle):
    """
    If enabled, picking up Nano Overloads will be checks.
    """
    display_name = "Nano Overload Locations"

class DebugAbilities(Choice):
    """
    This option adds the 'Fire Anytime' from the vanilla game's debug options as an item to your world.
    This item allows you to fire your weapon even while ducking or in midair.
    It is an extremely powerful item, and opens up a ton of skips in late-game sectors,
    almost all of which are currently NOT accounted for in logic (But they will be in the future.)
    This option will also add the AREYOUSERIOUS logbook in Sector 7 as a location, which is inaccessible without this item.
    """
    display_name = "Fire Anytime Item"
    option_off = 0
    option_shuffle = 1
    option_starting_item = 2
    default = 0

class DoorShuffle(Toggle):
    """
    Unused Placeholder option for now
    """
    display_name = "Door Shuffle"

class ShieldDoorShuffleType(Choice):
    """
    Unused Placeholder option for now
    """
    display_name = "Shield Door Shuffle Type"
    option_individual_doors = 1
    option_progressive_resistance = 2

class SecuredDoorShuffleType(Choice):
    """
    Unused Placeholder option for now
    """
    display_name = "Secured Door Shuffle Type"
    option_individual_doors = 1
    option_progressive_security = 2

class TerminalDoorShuffleType(Choice):
    """
    Unused Placeholder option for now
    """
    display_name = "Terminal Door Shuffle Type"
    option_individual_doors = 1
    option_sector_doors = 2

@dataclass
class IjiOptions(PerGameCommonOptions):
    end_goal:                       EndGoal
    goal_posters:                   GoalPosterLocations
    goal_ribbons:                   GoalRibbonItems
    ribbon_items:                   RibbonItemCount
    out_of_order_sectors:           OutOfOrderSectors

    poster_locations:               PosterLocations
    supercharge_locations:          SuperchargeLocations
    basic_weapon_locations:         BasicWeaponLocations
    logbook_locations:              LogbookLocations
    security_box_locations:         CrackBoxLocations
    nano_overload_locations:        OverloadLocations

    special_trait_items:            SpecialTraitItems
    extra_sector_access:            SectorAccessItems
    extra_health:                   HealthItems
    extra_attack:                   AttackItems
    extra_assimilate:               AssimilateItems
    extra_strength:                 StrengthItems
    extra_crack:                    CrackItems
    extra_tasen:                    TasenItems
    extra_komato:                   KomatoItems
    jump_upgrades:                  JumpUpgrades
    armor_upgrades:                 ArmorUpgrades
    extra_supercharges:             ExtraSupercharges
    levelsanity:                    Levelsanity

    trap_percentage:                TrapPercentage
    rocket_trap_weight:             RocketTrapWeight
    banana_trap_weight:             BananaTrapWeight
    blits_trap_weight:              BlitsTrapWeight
    null_drive_trap_weight:         NullDriveTrapWeight
    null_drive_factor:              NullDriveFactor
    turbo_trap_weight:              TurboTrapWeight
    nap_trap_weight:                NapTrapWeight
    clown_shoes_weight:             ClownShoesWeight

    health_balancing:               HealthBalancing
    deathlink:                      IjiDeathLink
    deathlink_damage:               DeathLinkDamage
    logic_difficulty:               LogicDifficulty
    music_shuffle:                  MusicShuffle
    debug_item:                     DebugAbilities

iji_option_groups = [
    OptionGroup("Goal Options", [
        EndGoal,
        GoalPosterLocations,
        GoalRibbonItems,
        RibbonItemCount
    ]),
    OptionGroup("Location Options", [
        PosterLocations,
        SuperchargeLocations,
        BasicWeaponLocations,
        LogbookLocations,
        CrackBoxLocations,
        OverloadLocations
    ]),
    OptionGroup("Item Options", [
        SpecialTraitItems,
        SectorAccessItems,
        HealthItems,
        AttackItems,
        AssimilateItems,
        StrengthItems,
        CrackItems,
        TasenItems,
        KomatoItems,
        JumpUpgrades,
        ArmorUpgrades,
        ExtraSupercharges,
        Levelsanity,
        DebugAbilities
    ]),
    OptionGroup("Trap Options", [
        TrapPercentage,
        RocketTrapWeight,
        BananaTrapWeight,
        BlitsTrapWeight,
        NullDriveTrapWeight,
        NullDriveFactor,
        TurboTrapWeight,
        NapTrapWeight,
        ClownShoesWeight
    ]),
    OptionGroup("Miscellaneous Options", [
        HealthBalancing,
        LogicDifficulty,
        OutOfOrderSectors,
        IjiDeathLink,
        DeathLinkDamage,
        MusicShuffle
    ])
]
