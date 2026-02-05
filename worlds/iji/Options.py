from typing import List, TYPE_CHECKING, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Range, Toggle, DeathLink, Choice, DefaultOnToggle, OptionGroup, OptionSet, OptionDict
#from .Rules import WeaponData
from .Names.ItemNames import Weapons as WeaponNames
#from Names import EventNames
import logging

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
            value_list.append(interpret_randomizable_option(world,
                                                            world.options.health_balancing.value[hb_sector_indices[i]],
                                                            f"{hb_sector_indices[i]} Health Balancing"))
        else:
            value_list.append(i + 1)
        world.options.health_balancing.value[hb_sector_indices[i]] = value_list[i]

    return value_list

def interpret_randomizable_option(world: "IjiWorld",
                                  value: Any,
                                  option_name: str,
                                  lower_bound: int = 0,
                                  upper_bound: int = 9) -> int:
    if type(value) == int:
        if value < lower_bound or value > upper_bound:
            raise ValueError(f"{option_name} must be between {lower_bound} and {upper_bound}")
        return value
    elif type(value) == str:
        return choose_random_option_from_string(world, value, option_name, lower_bound, upper_bound)
    else:
        raise ValueError(f"{option_name} must be either an integer or a string representing a range between two integers")

weapon_error_names: List[str] = [
    "Tasen",
    "Komato",
    "Crack"
]

#def interpret_weapon_requirements(world: "IjiWorld"):
#    for key, data in world.weapon_stats_needed.items():
#        for i in range(3):
#            weapon_value: int = 0
#            stat_dict: Dict[str, Any]
#            if i == 0: stat_dict = world.options.tasen_weapon_requirements.value
#            elif i == 1: stat_dict = world.options.komato_weapon_requirements.value
#            else: stat_dict = world.options.crack_weapon_requirements.value
#
#            if key in stat_dict.keys():
#                if type(stat_dict[key]) == int:
#                    weapon_value = stat_dict[key]
#                    if weapon_value < 0 or weapon_value > 9:
#                        raise ValueError(f"{weapon_error_names[i]} stat requirement for {key} must be between 0 and 9")
#
#                elif type(stat_dict[key]) == str:
#                    weapon_value = choose_random_option_from_string(
#                        world,
#                        stat_dict[key],
#                        weapon_error_names[i]+" stat requirement for "+key,
#                        0, 9)
#
#                if i == 0: data.tasen = weapon_value
#                elif i == 1: data.komato = weapon_value
#                else: data.crack = weapon_value

def weapon_requirements_to_slot_data(world: "IjiWorld") -> Dict[str, str]:
    ret: Dict[str, str] = {}
    for key, data in world.weapon_stats_needed.items():
        ret[key] = str(data.tasen)+str(data.komato)+str(data.crack)
    return ret

def get_weapon_requirements_from_slot_data(world: "IjiWorld", data: Dict[str, str]):
    for key, value in world.weapon_stats_needed.items():
        if key in data.keys():
            value.tasen = int(data[key][0])
            value.komato = int(data[key][1])
            value.crack = int(data[key][2])

combined_weapons_indices: Dict[str, List[str]] = {
        WeaponNames[9]: [WeaponNames[1], WeaponNames[2]],
        WeaponNames[10]: [WeaponNames[2], WeaponNames[7]],
        WeaponNames[11]: [WeaponNames[1], WeaponNames[3]],
        WeaponNames[12]: [WeaponNames[3], WeaponNames[4]],
        WeaponNames[13]: [WeaponNames[1], WeaponNames[5]],
        WeaponNames[14]: [WeaponNames[5], WeaponNames[6]],
        WeaponNames[15]: [WeaponNames[6], WeaponNames[7]],
        WeaponNames[16]: [WeaponNames[4], WeaponNames[8]]
    }

#def finalize_weapon_stats(world: "IjiWorld"):
#    ret: Dict[str, WeaponData] = {}
#    for i in range(2, 9): # iterate through basic weapons
#        temp_tasen = world.weapon_stats_needed[WeaponNames[i]].tasen
#        temp_komato = world.weapon_stats_needed[WeaponNames[i]].komato
#        world.weapon_stats_needed[WeaponNames[i]].points_needed  = temp_tasen + temp_komato
#
#    for key, value in combined_weapons_indices.items():
#        temp_tasen = max(world.weapon_stats_needed[value[0]].tasen,
#                         world.weapon_stats_needed[value[1]].tasen)
#        temp_komato = max(world.weapon_stats_needed[value[0]].komato,
#                          world.weapon_stats_needed[value[1]].komato)
#        world.weapon_stats_needed[key].tasen = temp_tasen
#        world.weapon_stats_needed[key].komato = temp_komato
#        world.weapon_stats_needed[key].calculate_points_needed()
#
#    world.weapon_stats_needed[WeaponNames[0]] = WeaponData() # Null Driver
#    world.weapon_stats_needed[WeaponNames[18]] = WeaponData() # Massacre
#
#def revert_invalid_weapon_stats(world: "IjiWorld", new_table: Dict[str, WeaponData]):
#    vanilla_table = world.weapon_stats_needed
#    max_points = world.max_stats[EventNames.Levels[0]]
#    for i in range(2,9): # Iterate through basic weapons
#        if new_table[WeaponNames[i]].points_needed <= vanilla_table[WeaponNames[i]].points_needed:
#            continue
#        if revert_basic_weapon(vanilla_table[WeaponNames[i]],new_table[WeaponNames[i]], max_points):
#            logging.warning(f"Stat requirement for {WeaponNames[i]} was too high for {world.player_name}'s world. "
#                            f"Some or all of its stats have been automatically reduced to their vanilla requirements.")
#    for i in range(9,17): # Iterate through combined weapons
#        if new_table[WeaponNames[i]].points_needed <= vanilla_table[WeaponNames[i]].points_needed:
#            continue
#        component: int = 2
#        reduced: bool = False
#        while component >= 0 and new_table[WeaponNames[i]].points_needed > max_points:
#            component -= 1
#
#def revert_basic_weapon(vanilla_weapon: WeaponData, modified_weapon: WeaponData, max_points: int) -> bool:
#    stat: int = 0
#    reduced: bool = False
#    while stat <= 1 and modified_weapon.points_needed > max_points:
#        if stat == 0:
#            reduced = reduced or modified_weapon.clamp_tasen(vanilla_weapon.tasen)
#        elif stat == 1:
#            reduced = reduced or modified_weapon.clamp_komato(vanilla_weapon.komato)
#        stat += 1
#    return reduced

def choose_random_option_from_string(world: "IjiWorld",
                                     option_range: str,
                                     option_name: str,
                                     lower_bound: int = 0,
                                     upper_bound: int = 9) -> int:
    options = option_range.split('-')
    values: List[int] = [0,0]
    if len(options) == 1:
        try:
            values[0] = int(options[0])
            values[1] = values[0]
        except ValueError:
            raise ValueError(option_name+" is either not an integer, or is not a valid range of integers")
    elif len(options) == 2:
        try:
            values[0] = int(options[0])
            values[1] = int(options[1])
        except ValueError:
            raise ValueError(option_name+" is either not an integer, or is not a valid range of integers")
        if values[0] < lower_bound or values[1] > upper_bound:
            raise ValueError(f"{option_name} must be between {lower_bound} and {upper_bound}")
        if values[0] > values[1]:
            temp = values[0]
            values[0] = values[1]
            values[1] = temp
        if values[0] < lower_bound or values[1] > upper_bound:
            raise ValueError(f"range chosen for {option_name} is invalid. Minimum value is {lower_bound} and maximum value is {upper_bound}")
    elif len(options) >= 3:
        raise ValueError(option_name+" is either not an integer, or is not a valid range of integers")

    return world.random.randrange(values[0],values[1]+1)

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

    def get_normal_sector_count(self) -> int:
        return min(10,self.value)

class GoalPosterLocations(Range):
    """
    How many Poster locations you are required to find before being able to complete your goal.
    If you chose Sector X as your goal, the elevator at the end of the sector will be deactivated until you find them.
    If you chose Sector Y or Sector Z as your goal, you won't be able to enter Sector Z until you find them.
    """
    display_name = "Poster Locations Required for Goal"
    default = 0
    range_start = 0
    range_end = 11

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
    option_sector_z_and_null_driver = 0b011
    option_sector_z_with_goal_requirement = 0b101
    option_sector_z_and_null_driver_with_goal_requirement = 0b111

    def has_requirement(self) -> bool:
        return self.value & 0b100 != 0

    def null_driver_allowed(self) -> bool:
        return self.value & 0b010 != 0

    def allowed(self) -> bool:
        return self.value & 0b001 != 0

    def is_post_game(self, world: "IjiWorld") -> bool:
        return self.has_requirement() or world.options.end_goal.value >= 11

class PosterLocations(DefaultOnToggle):
    """
    If enabled, Finding posters sends checks.
    """
    display_name = "Poster Locations"

    def expected_location_count(self, sector_count) -> bool:
        return self.value * sector_count

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

    def awards_points(self) -> bool:
        return self.value <= 1

    def has_locations(self) -> bool:
        return self.value >= 1

    def expected_location_count(self, sector_count: int) -> int:
        return 0 if self.value == 0 else min(10,sector_count)

    def max_without_weapons(self, sector_count: int) -> int:
        if not self.awards_points():
            return sector_count
        ret = sector_count
        if sector_count >= 10:
            ret -= 1
        if sector_count >= 7:
            ret -= 1
        if sector_count >= 6:
            ret -= 1
        if sector_count >= 5:
            ret -= 1
        if sector_count >= 3:
            ret -= 1
        return ret

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
        "Crack": 10,
        "Tasen": 10,
        "Komato": 10
    }

class SpecialTraitItems(Toggle):
    """
    If enabled, the Special Trait items will be shuffled into the item pool.
    An additional location for reaching the final level of a stat will also be added.

    Otherwise, the Special Traits will be in effect when you raise the respective stat to its maximum level
    """
    display_name = "Special Traits"

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
    Guilt Trip forces you to read the logbook texts detailing all the enemies you killed so far, and it cannot be skipped.
    Forced Reboot sets all your stats to 1 (refunding 1 stat point for stat level lost), leaving you vulnerable until you raise your stats again
    Assassin Ambush spawns a Komato Assassin at your current location, which follows and attacks Iji for 30 seconds, or until it's defeated.
    """
    display_name = "Trap Weights"
    default = {
        "Rocket to the Face": 20,
        "Banana": 20,
        "Blits Nest": 20,
        "Turbo Mode": 10,
        "Clown Shoes": 10,
        "Power Nap": 20,
        "Null Drive": 0,
        "Guilt Trip": 0,
        "Forced Reboot": 0,
        "Assassin Ambush": 0
    }

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

class HealthBalancing(OptionDict):
    """
    To help push health stat items into earlier locations in the multiworld,
    and to ensure that you don't have to play late game sectors with low health,
    this option will force Sectors to require having a minimum number of Health Stat items to be in logic.
    It won't physically lock you out of the Sectors, so you can still play Sectors out of logic if you want.

    Values should range from 0 to 9.

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
    """
    display_name = "Logic Difficulty"
    option_normal_logic = 0
    option_hard_logic = 1
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

    def levels_per_sector(self) -> int:
        return max(3,min(5,self.value))

    def get_xp_index(self) -> int:
        return 5 - self.levels_per_sector()

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
    Instead, a respective Supercharge item for each level up will be added to the multiworld.
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
    Also, if you are playing on Extreme difficulty where Overloads can't naturally appear, enabling this option will force them to spawn
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

class ShuffleDoors(Choice):
    """
    This option lets you shuffle the strength/crack requirement to open doors
    Not all doors can be shuffled. Doors with a security or resistance higher than 10 will not be randomized.

    Shuffle Levels: The amount of strength or crack stat required to open a given door is randomized.

    Shuffle Terminals: All terminals that open doors will have a cracking minigame,
    and require a random amount of crack to activate.

    Shuffle Types: Randomizes whether any given door requires strength or crack.

    """
    display_name = "Shuffle Door Levels"
    default = 0
    option_off = 0
    option_shuffle_levels_only = 0b001
    option_shuffle_types_only = 0b010
    option_shuffle_terminals_only = 0b100
    option_shuffle_terminals_and_levels = 0b101
    option_shuffle_terminals_and_types = 0b110
    option_shuffle_types_and_levels = 0b011
    option_shuffle_everything = 0b111

    def shuffle_levels(self) -> bool:
        return self.value & self.option_shuffle_levels_only != 0

    def shuffle_types(self) -> bool:
        return self.value & self.option_shuffle_types_only != 0

    def shuffle_terminals(self) -> bool:
        return self.value & self.option_shuffle_terminals_only != 0

class DoorLevelDeviation(Range):
    """
    If Shuffle Door Levels is enabled, this option determines how far a door's level is allowed to deviate from its original level.
    e.g. if a door normally requires 5 strength to open, and the deviation is 3, that door could require anywhere from 2 to 8 strength.
    If Shuffle Terminals is enabled, their base crack requirement is 1 for the purposes of this option.
    """
    display_name = "Door Level Deviation"
    default = 9
    range_start = 1
    range_end = 9

class EnforceHealthBalancing(Toggle):
    """
    If true, you will be prohibited from entering a Sector if you don't meet the health requirement as
    defined by the health balancing option.

    If false, you will be able to enter any Sector you have access to, but the locations won't be in logic
    if you don't meet the health requirement.
    """
    display_name = "Enforce Health Balancing"

class WeaponTasenRequirements(OptionDict):
    """
    How many Tasen stat items are required in order to pick up and use the game's basic weapons.
    Weapons that are combined from two weapons will in turn require the stats needed for each of those weapons.
    The Banana Gun will in turn require the stats needed for all basic weapons.

    If fewer than 9 Tasen items are required to obtain all basic weapons,
    excess Tasen stat items and locations will be removed.
    The requirement for the VENGEANCE special trait will be whatever the new maximum is.
    """
    default = {
        "Machine Gun": 2,
        "Rocket Launcher": 5,
        "MPFB Devastator": 9,
        "Resonance Detonator": 0,
        "Pulse Cannon": 0,
        "Shocksplinter": 0,
        "Cyclic Fusion Ignition System": 0
    }

class WeaponKomatoRequirements(OptionDict):
    """
    How many Tasen stat items are required in order to pick up and use the game's basic weapons.
    Weapons that are combined from two weapons will in turn require the stats needed for each of those weapons.
    The Banana Gun will in turn require the stats needed for all basic weapons.

    If fewer than 9 Komato items are required to obtain all basic weapons,
    excess Komato stat items and locations will be removed.
    The requirement for the GLORY special trait will be whatever the new maximum is.

    """
    default = {
        "Machine Gun": 0,
        "Rocket Launcher": 0,
        "MPFB Devastator": 0,
        "Resonance Detonator": 0,
        "Pulse Cannon": 2,
        "Shocksplinter": 5,
        "Cyclic Fusion Ignition System": 9
    }

class WeaponCrackRequirements(OptionDict):
    """
    How many Crack stat items are required in order to combine two weapons together.
    """
    default = {
        "Buster Gun": 2,
        "Splintergun": 6,
        "Spread Rockets": 4,
        "Nuke": 8,
        "Resonance Reflector": 3,
        "Hyper Pulse": 5,
        "Plasma Cannon": 7,
        "Velocithor V2-10": 9
    }

class ICanRead(Choice):
    """
    Whether or not you read the README file enclosed with the randomizer.
    This has no effect on generation, but it does contain important information you should know :)
    """
    display_name = "I Read the README"
    default = 0
    option_i_did_not_read_the_readme = 0
    option_i_read_the_readme_and_am_a_cool_person = 1

class CompactStats(OptionDict):
    """
    This option lets you compact your stat items into fewer items that give you more stat levels per item.
    i.e. A stat with a compact value of 2 will add half the number of respective stat items (rounded up)
    but each one will increase the respective stat cap by 2 instead of 1.

    Compacting supercharges only affects Supercharge items you receive,
    either from the levelsanity option, supercharge location option, or duplicate supercharges from the extra_items option
    Stat points awarded from picking up Supercharges in levels will not give additional points.
    """
    display_name = "Compact Stats"
    default = {
        "Health Stat": 1,
        "Attack Stat": 1,
        "Assimilate Stat": 1,
        "Strength Stat": 1,
        "Crack Stat": 1,
        "Tasen Stat": 1,
        "Komato Stat": 1,
        "Supercharge": 1,
    }

    def get_chosen_compact_values(self, world) -> Dict[str, int]:
        ret: Dict[str, int] = {}
        for name in self.default.keys():
            if name in self.value.keys():
                ret[name] = interpret_randomizable_option(world, self.value[name], f"Compact Stat: {name}", 1, 9)
            else:
                ret[name] = 1

        return ret

class Scrambler(Toggle):
    """
    Whether the Scrambler should be turned on. This option can be changed later in-game via the Extras menu
    The scrambler occasionally scrambles text by replacing words with a random selection of words, and jumbling vowels.
    No effect on logic, it's just for fun.
    """
    display_name = "Turn on Scrambler"

class AlternateOutfit(Toggle):
    """
    Iji wears an alternate outfit, from the opening cutscene.
    This option can be changed later in-game via the Extras menu
    """
    display_name = "Alternate Outfit"

class FillerWeights(OptionDict):
    """
    This option lets you override the weight for each of the filler items.
    Set an item to 0 weight or remove it from the list to remove it from the pool entirely.
    Health Pickup: Spawns a red pickup that restores health or grants temporary health if already at max hp.
    Armor Pickup: Spawns a green pickup that restores armor.
    Nano Pickup: Spawns a blue pickup that gives restores armor and gives XP when collected. Helps with leveling up.
    Machine/Rocket/MPFB/Pulse/Shock/CFIS Ammo: Spawns a large pickup that gives ammo for the respective weapon
    Bundle of Ammo: Spawns small ammo pickups for each weapon type
    Nano Overload: Gives Iji a random temporary powerup.
    Can of Soda: Spawns a soda can that does nothing.
    Note: If every filler item has a weight of 0, all filler items will be Can of Soda.
    """
    display_name = "Filler Weights"
    default = {
        "Health Pickup": 50,
        "Armor Pickup": 20,
        "Nano Pickup": 40,
        "Machine Ammo": 30,
        "Rocket Ammo": 20,
        "MPFB Ammo": 10,
        "Pulse Ammo": 30,
        "Shock Ammo": 20,
        "CFIS Ammo": 10,
        "Nano Overload": 10,
        "Bundle of Ammo": 40,
        "Can of Soda": 0,
    }

class StartingStats(OptionDict):
    """
    For each stat, you may set its respective starting level cap.
    Increasing a stat's level cap will cause some of its items to be removed from the item pool.
    This is different from putting stat items in your starting items in a couple ways:
    1. Stat levels within your starting level cap will not contain random items when reaching their level
        (if stat_locations is enabled)
    2. Raising your level caps this way is unaffected by the compact_stats option

    Valid values range from 1 to 10
    """
    display_name = "Starting Stats"
    default = {
        "Health Stat": 1,
        "Attack Stat": 1,
        "Assimilate Stat": 1,
        "Strength Stat": 1,
        "Crack Stat": 1,
        "Tasen Stat": 1,
        "Komato Stat": 1,
    }

    def get_starting_stat_items(self, world: "IjiWorld") -> Dict[str, int]:
        ret: Dict[str, int] = {}
        for stat in self.default.keys():
            if stat in self.value.keys():
                ret[stat] = interpret_randomizable_option(world, self.value[stat], f"Starting Stat: {stat}", 1, 10) - 1
            else:
                ret[stat] = 0
        return ret

class StatLocations(DefaultOnToggle):
    """
    If enabled, leveling up a stat to a specific level will contain a random item
    If you have special_trait_items enabled, reaching the max level of a stat will still contain an item

    NOTE: Stat Levels make up a significant portion of this game's locations.
    disabling this option may cause your world to not have enough locations to fit all of your stat items.
    You can choose whether the multiworld generation compensates for this by increasing your starting_stats options,
    or by increasing your compact_stats options (See these options below for more information about how they work)
    """
    display_name = "Stat Level Locations"

class EnemyLocations(Toggle):
    """
    Whether killing individual enemies can send items.
    Note: It does not matter how an enemy dies, nor who kills said enemy to send an item.
    """
    display_name = "Enemy Locations"

class EnemyLocationTypes(OptionDict):
    """
    If Enemy Locations is enabled, these are the types of enemies that can be locations.
    """
    display_name = "Enemy Location Types"
    default = {
        "Bosses": True,
        "Tasen Scout": True,
        "Tasen Soldier": True,
        "Tasen Commander": True,
        "Tasen Elite": True,
        "Komato Trooper": True,
        "Komato Berserker": True,
        "Komato Beast": True,
        "Komato Assassin": True,
        "Komato Annihilator": False,
        "Sector Z": False,
        "Yukabacera": False
    }

    def type_allowed(self, world: "IjiWorld", enemy_type: str) -> bool:
        return world.options.enemy_locations and enemy_type in self.value.keys() and self.value[enemy_type]
    
    def get_slot_data(self) -> Dict[str, int]:
        ret: Dict[str, int] = {}
        for name in self.default.keys():
            if name in self.value.keys():
                if self.value[name] == True:
                    ret[name] = 1
                else:
                    ret[name] = 0
            else:
                ret[name] = 0

        return ret

    def set_from_slot_data(self, slot_data: Dict[str, int]):
        for name, value in slot_data.items():
            if value > 0:
                self.value[name] = True
            else:
                self.value[name] = False

class MoreEnemies(Toggle):
    """
    If enabled, enemies that would normally not appear on normal difficulty will also spawn.
    This has no effect if you are playing on hard difficulty or higher.
    """
    display_name = "More Enemies"


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
    enforce_health_balancing:       EnforceHealthBalancing

    poster_locations:               PosterLocations
    supercharge_locations:          SuperchargeLocations
    basic_weapon_locations:         BasicWeaponLocations
    logbook_locations:              LogbookLocations
    security_box_locations:         CrackBoxLocations
    nano_overload_locations:        OverloadLocations
    #stat_locations:                 StatLocations
    enemy_locations:                EnemyLocations
    enemy_location_types:           EnemyLocationTypes
    more_enemies:                   MoreEnemies

    special_trait_items:            SpecialTraitItems
    extra_items:                    ExtraItemCount
    jump_upgrades:                  JumpUpgrades
    armor_upgrades:                 ArmorUpgrades
    levelsanity:                    Levelsanity
    debug_item:                     DebugAbilities

    filler_weights:                 FillerWeights
    trap_percentage:                TrapPercentage
    trap_weights:                   TrapWeights
    null_drive_factor:              NullDriveFactor

    compact_stats:                  CompactStats
    starting_stats:                 StartingStats
    #door_shuffle:                   ShuffleDoors
    #door_shuffle_deviation:         DoorLevelDeviation
    #tasen_weapon_requirements:      WeaponTasenRequirements
    #komato_weapon_requirements:     WeaponKomatoRequirements
    #crack_weapon_requirements:      WeaponCrackRequirements

    deathlink:                      IjiDeathLink
    deathlink_damage:               DeathLinkDamage
    music_shuffle:                  MusicShuffle
    i_read_the_readme:              ICanRead
    scrambler:                      Scrambler
    alternate_outfit:               AlternateOutfit


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
        EnforceHealthBalancing,
    ]),
    OptionGroup("Location Options", [
        PosterLocations,
        SuperchargeLocations,
        BasicWeaponLocations,
        LogbookLocations,
        CrackBoxLocations,
        OverloadLocations,
        #StatLocations,
        EnemyLocations,
        EnemyLocationTypes,
        MoreEnemies
    ]),
    OptionGroup("Item Options", [
        SpecialTraitItems,
        ExtraItemCount,
        JumpUpgrades,
        ArmorUpgrades,
        Levelsanity,
        DebugAbilities,
    ]),
    OptionGroup("Filler Options", [
        FillerWeights,
        TrapPercentage,
        TrapWeights,
        NullDriveFactor,
    ]),
    OptionGroup("Stat Options", [
        CompactStats,
        StartingStats,
        #ShuffleDoors,
        #DoorLevelDeviation,
        #WeaponTasenRequirements,
        #WeaponKomatoRequirements,
        #WeaponCrackRequirements,
    ]),
    OptionGroup("Miscellaneous Options", [
        IjiDeathLink,
        DeathLinkDamage,
        MusicShuffle,
        ICanRead,
        Scrambler,
        AlternateOutfit,
    ]),
]
