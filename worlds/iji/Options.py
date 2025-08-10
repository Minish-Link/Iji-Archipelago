from math import ceil
from typing import List, TYPE_CHECKING, Dict
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Range, Toggle, DeathLink, Choice, DefaultOnToggle, OptionGroup, OptionList, OptionDict

if TYPE_CHECKING:
    from . import IjiWorld


hb_sector_indices: List[str] = [
    "Sector 2",
    "Sector 3",
    "Sector 4",
    "Sector 5",
    "Sector 6",
    "Sector 7",
    "Sector 8",
    "Sector 9",
    "Sector X"
]

def define_health_balancing(world: "IjiWorld") -> List[int]:
    value_list: List[int] = []

    for i in range(9):
        if hb_sector_indices[i] in world.options.health_balancing.value:
            cur_val: int = world.options.health_balancing.value[hb_sector_indices[i]]
            if cur_val < 0:
                value_list.append(get_random_health_balance_value(world, cur_val))
            else:
                value_list.append(min(9, cur_val))
        else:
            value_list.append(i + 1)

        world.options.health_balancing.value[hb_sector_indices[i]] = value_list[i]
    
    return value_list

def get_random_health_balance_value(world: "IjiWorld", value: int) -> int:
    return min(9, world.random.randint(0, abs(value)))

def get_shuffled_music(world: "IjiWorld") -> Dict[str, str]:
    music_list: List[str] = [
        "secintro.mp3",
        "sec1.mp3",
        "sec2.mp3",
        "sec3.mp3",
        "sec4.mp3",
        "sec5.mp3",
        "boss.mp3",
        "tor.mp3",
        "ending.mp3",
        "mainmenu.mp3",
        "clear.mp3",
        "calm.mp3",
        "dark.mp3",
        "sad.mp3",
        "asha.mp3",
        "hero3d.mp3"
    ]
    music_dict: Dict[str, str] = {}
    for name in music_list:
        music_dict[name] = name
    

    if world.options.music_shuffle == 3:
        temp_track = music_list[world.random.randrange(0,len(music_list))]
        for name in music_list:
            music_dict[name] = temp_track
    else:
        song_shuffle_count = 0
        if world.options.music_shuffle == 1:
            song_shuffle_count = 6
        elif world.options.music_shuffle == 2:
            song_shuffle_count = 15

        temp_music_list = music_list[:song_shuffle_count]
        for i in range(song_shuffle_count):
            music_dict[music_list[i]] = temp_music_list.pop(world.random.randrange(0, len(temp_music_list)))

    return music_dict


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
    range_end = 100

class AllowSectorZ(Choice):
    """
    Whether or not your world will be able to enter Sector Z, and whether or not you'll be able to reach the Null Driver
    If your goal is Sector Z, this option won't do anything unless you choose to also enable the Null Driver
    If your goal is Sector Y, this option won't do anything at all.
    You can also additionally lock Sector Z behind the same ribbon/poster requirement as your goal
    If your chosen goal allows you to reach Sector X, and you choose to allow getting the null driver here, Sector Y locations will also be added.
    """
    display_name = "Allow Sector Z Locations"
    default = 0
    option_off = 0
    option_sector_z = 0b001
    option_sector_z_and_nulldriver = 0b011
    option_sector_z_with_goal_requirement = 0b101
    option_sector_z_and_null_driver_with_goal_requirement = 0b111

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

class ExtraItemCount(OptionDict):
    """
    How many duplicates of each major item to add to the pool.
    Negative numbers will choose a random number between 0 and the absolute value of that number.
    e.g. -7 will choose a random value between 0 and 7.

    If you choose to have extra sector accesses with out of order sectors enabled,
    an even split of the sector accesses will be added.

    Duplicates of Special Trait items (The ones in capital letters) will only be added
    if Special Trait Items are enabled

    Duplicate Jump and Armor upgrades can appear anywhere in the multiworld,
    even if vanilla locations are chosen for the respective original items.

    Duplicates of Fire Anytime will only be added if debug_item is set to shuffle

    Note: If there aren't enough locations to fit all the duplicates, it will instead add
    as much as it can, leaving no room for filler or traps.
    Also, Duplicates are created after Ribbons, so if your chosen Ribbon count fills up all
    remaining locations in your world, no duplicate items will be created at all.
    """
    display_name = "Extra Items"
    default = {
        "Sector Access": 0,
        "Supercharge": 0,
        "Health Stat": 0,
        "Attack Stat": 0,
        "Assimilate Stat": 0,
        "Strength Stat": 0,
        "Crack Stat": 0,
        "Tasen Stat": 0,
        "Komato Stat": 0,
        "Jump Upgrade": 0,
        "Armor Upgrade": 0,
        "Fire Anytime": 0,
        "SUPPRESSION": 0,
        "IMPROVED AUTOLOADING": 0,
        "ADVANCED RECOVERY": 0,
        "CYBERNETIC ENDURANCE": 0,
        "ELECTRONIC MASTERY": 0,
        "VENGEANCE": 0,
        "GLORY": 0
    }

class MaximumStatAllowed(OptionDict):
    """
    Placeholder
    """
    display_name = "Maximum Allowed Stats"
    default = {
        "Health": 10,
        "Attack": 10,
        "Assimilate": 10,
        "Strength": 10,
        "CracK": 10,
        "Tasen": 10,
        "Komato": 10
    }

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

class TrapWeights(OptionDict):
    """
    How likely each trap is to be chosen when creating a trap item.
    Choosing 0 disables a trap entirely.
    Rocket to the Face spawns a rocket projectile that flies toward Iji.
    Banana spawns an exploding banana projectile at Iji's position.
    Blits Nest spawns a handful of Blit enemies at Iji's position.
    Turbo Mode doubles the game speed for 20 seconds.
    Clown Shoes makes Iji's footsteps squeaky for 1 minute.
    Power Nap knocks Iji down for 10 seconds (or until damaged)
    Null Drive randomly swaps around background textures, effect persists until the game is closed.
    """
    display_name = "Trap Weights"
    default = {
        "Rocket to the Face": 20,
        "Banana": 20,
        "Blits Nest": 20,
        "Turbo Mode": 10,
        "Clown Shoes": 10,
        "Power Nap": 20,
        "Null Drive": 0
    }

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

class HealthBalancing(OptionDict):
    """
    To help push health stat items into earlier locations in the multiworld,
    and to ensure that you don't have to play late game sectors with low health,
    this option will force Sectors to require having a minimum number of Health Stat items to be in logic.
    It won't physically lock you out of the Sectors, so you can still play Sectors out of logic if you want.

    Values should range from 0 to 9.
    Alternatively, you can also enter negative numbers to choose a random value for that sector.
    The absolute value of a negative number determines the maximum range for that random value.
    e.g. a value of -9 will allow any number between 0 and 9 to be chosen,
    and a value of -3 will choose a number between 0 and 3.

    NOTE: Later sectors can be brutally difficult with low health,
    only mess around with this if you are absolutely confident in your abilities.
    """
    display_name = "Health Balancing Values"
    default = {
        "Sector 2": 1,
        "Sector 3": 2,
        "Sector 4": 3,
        "Sector 5": 4,
        "Sector 6": 5,
        "Sector 7": 6,
        "Sector 8": 7,
        "Sector 9": 8,
        "Sector X": 9
    }

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

    Hard Logic: Expects the player to utilize vanilla methods that would be needed to
    reach posters and supercharges in order to reach all locations.

    Extreme Logic: Same as Hard Logic, but some locations may require more setup and/or longer chains of skips

    Ultimortal Logic: Expects more unorthodox skips from the player
    using techniques that would otherwise never be required.

    reallyjoel's Dad Logic: Anything goes. If it's technically possible, it's in logic.
    """
    display_name = "Logic Difficulty"
    option_normal_logic = 0
    option_hard_logic = 1
    option_extreme_logic = 2
    option_ultimortal_logic = 3
    option_reallyjoelsdad_logic = 4
    default = 0

class GameDifficulty(Choice):
    """
    What difficulty of the game the world will be played on.

    Normal: 5 Levels per Sector, Reduced number of enemies, Health pickups restore 2 health

    Hard: 4 Levels per Sector, Tougher bosses, Health pickups restore 1 health

    Extreme: 3 Levels per Sector, Even tougher bosses. No nano overload pickups, unless Nano Overload locations are enabled.
    """
    display_name = "Game Difficulty"
    option_normal = 5
    option_hard = 4
    option_extreme = 3
    default = 5

class MusicShuffle(Choice):
    """
    Whether or not to randomly reassign music tracks.
    Off: No shuffled music
    Levels Only: Only Level Music gets shuffled amongst each other.
    Full Shuffle: All Looping music tracks get shuffled amongst each other
    Singularity: All looping music tracks get replaced by one single track
    """
    display_name = "Music Shuffle"
    option_off = 0
    option_levels_only = 1
    option_full_shuffle = 2
    option_singularity = 3
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
    default = 0

class Checkpointsanity(Choice):
    """
    This option lets you shuffle the ability to warp to any given checkpoint within a level.
    If you reach a checkpoint normally, you will still be able to warp to that checkpoint,
    regardless of whether or not you received it as an item.

    You can also choose whether or not to allow warping to a checkpoint you receive,
    even if you don't receive a Sector Access item to that sector.
    You still won't be able to warp to the start of that sector until you receive a Sector Access item for it.
    """
    option_off = 0
    option_sector_access_required = 1
    option_sector_access_not_required = 2
    default = 0

class DoorShuffle(Toggle):
    """
    Unused Placeholder option for now
    """
    display_name = "Door Shuffle"

# 0b1000 (8) -> individual
# 0b0100 (4) -> per sector
# 0b0011 (3) -> 1 for progressive, 2 for reverse progressive, 3 for separate levels
class ShieldDoorShuffleType(Choice):
    """
    Unused Placeholder option for now
    """
    display_name = "Shield Door Shuffle Type"
    option_none = 0
    option_individual_doors = 0b1000
    option_progressive_resistance = 0b0001
    option_reverse_progressive_resistance = 0b0010
    option_separate_resistances = 0b0011
    option_progressive_resistance_per_sector = 0b0101
    option_reverse_progressive_resistance_per_sector = 0b0110
    option_separate_resistances_per_sector = 0b0111
    default = 0


class SecurityDoorShuffleType(Choice):
    """
    Unused Placeholder option for now
    """
    display_name = "Secured Door Shuffle Type"
    option_none = 0
    option_individual_doors = 0b1000
    option_progressive_security = 0b0001
    option_reverse_progressive_security = 0b0010
    option_separate_securities = 0b0011
    option_progressive_security_per_sector = 0b0101
    option_reverse_progressive_security_per_sector = 0b0110
    option_separate_securities_per_sector = 0b0111
    default = 0

class TerminalDoorShuffleType(Choice):
    """
    Unused Placeholder option for now
    """
    display_name = "Terminal Door Shuffle Type"
    option_individual_doors = 1
    option_terminal_doors_per_sector = 2

@dataclass
class IjiOptions(PerGameCommonOptions):
    end_goal:                       EndGoal
    goal_posters:                   GoalPosterLocations
    goal_ribbons:                   GoalRibbonItems
    ribbon_items:                   RibbonItemCount
    allow_sector_z:                 AllowSectorZ

    game_difficulty:                GameDifficulty
    logic_difficulty:               LogicDifficulty
    out_of_order_sectors:           OutOfOrderSectors
    health_balancing:               HealthBalancing

    poster_locations:               PosterLocations
    supercharge_locations:          SuperchargeLocations
    basic_weapon_locations:         BasicWeaponLocations
    logbook_locations:              LogbookLocations
    security_box_locations:         CrackBoxLocations
    nano_overload_locations:        OverloadLocations

    special_trait_items:            SpecialTraitItems
    extra_items:                    ExtraItemCount
    jump_upgrades:                  JumpUpgrades
    armor_upgrades:                 ArmorUpgrades
    levelsanity:                    Levelsanity
    debug_item:                     DebugAbilities

    trap_percentage:                TrapPercentage
    trap_weights:                   TrapWeights
    null_drive_factor:              NullDriveFactor

    deathlink:                      IjiDeathLink
    deathlink_damage:               DeathLinkDamage
    door_shuffle:                   DoorShuffle
    strength_doors:                 ShieldDoorShuffleType
    crack_doors:                    SecurityDoorShuffleType
    terminal_doors:                 TerminalDoorShuffleType
    music_shuffle:                  MusicShuffle


iji_option_groups = [
    OptionGroup("Goal Options", [
        EndGoal,
        GoalPosterLocations,
        GoalRibbonItems,
        RibbonItemCount,
        AllowSectorZ,
    ]),
    OptionGroup("Game Options", [
        GameDifficulty,
        LogicDifficulty,
        OutOfOrderSectors,
        HealthBalancing,
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
        ExtraItemCount,
        JumpUpgrades,
        ArmorUpgrades,
        Levelsanity,
        DebugAbilities
    ]),
    OptionGroup("Trap Options", [
        TrapPercentage,
        TrapWeights,
        NullDriveFactor
    ]),
    OptionGroup("Miscellaneous Options", [
        IjiDeathLink,
        DeathLinkDamage,
        DoorShuffle,
        ShieldDoorShuffleType,
        SecurityDoorShuffleType,
        TerminalDoorShuffleType,
        MusicShuffle
    ])
]
