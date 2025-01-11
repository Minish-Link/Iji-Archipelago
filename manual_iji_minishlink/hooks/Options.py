# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
class TotalCharactersToWinWith(Range):
    """Instead of having to beat the game with all characters, you can limit locations to a subset of character victory locations."""
    display_name = "Number of characters to beat the game with before victory"
    range_start = 10
    range_end = 50
    default = 50

class CombatLogic(Choice):
    """This determines how many health stat items are needed for Sectors to be accessible in logic.
    You can still play them out of logic if you have access to the sector,
    but easier options should try to force health upgrades earlier into logic,
    if you're concerned about survival. Sector 1 will never require any items to be in logic.

    The health requirements per setting, from Sector 1 -> X are:
    Off:        [1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, X:0]
    Easy:       [1:0, 2:1, 3:3, 4:5, 5:7, 6:9, 7:9, 8:9, 9:9, X:9]
    Normal:     [1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8, X:9]
    Hard:       [1:0, 2:0, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 9:4, X:4]
    Extreme:    [1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1, 8:1, 9:2, X:2]
    """
    display_name = "Combat Logic"
    option_off = 0
    option_easy = 1
    option_normal = 2
    option_hard = 3
    option_extreme = 4

class MaximumHealthStat(Range):
    """This determines the minimum number of Health stat items that can be shuffled into the pool.

    Note 1: Any items that logically require more Health items than there are in the pool will be removed.
    The Sector Z goal requires 9 Health items.
    Generation for that goal will fail if you choose a lower value here.

    Note 2: If you have combat logic enabled, any sectors that require more health items than there are
    in the pool will have their requirements reduced to the value chosen here.
    """

    display_name = "Maximum Health Stats"
    range_start = 0
    range_end = 9
    default = 9

class MaximumAttackStat(Range):
    """This determines the minimum number of Attack stat items that can be shuffled into the pool.

    Note: Any items that logically require more Attack items than there are in the pool will be removed.
    The Sector Z goal requires at least 2 Attack items.
    Generation for that goal will fail if you choose a lower value here.
    """

    display_name = "Attack Stat Items"
    range_start = 0
    range_end = 9
    default = 9

class MaximumAssimilateStat(Range):
    """This determines the minimum number of Assimilate stat items that can be shuffled into the pool.

    Note: Any items that logically require more Assimilate items than there are in the pool will be removed.
    """

    display_name = "Assimilate Stat Items"
    range_start = 0
    range_end = 9
    default = 9

class MaximumStrengthStat(Range):
    """This determines the minimum number of Strength stat items that can be shuffled into the pool.

    Note: Any items that logically require more Strength items than there are in the pool will be removed.
    The Sector Z goal requires at least 3 Strength items.
    Generation for that goal will fail if you choose a lower value here.
    """

    display_name = "Strength Stat Items"
    range_start = 0
    range_end = 9
    default = 9

class MaximumTasenStat(Range):
    """This determines the minimum number of Tasen stat items that can be shuffled into the pool.
    Machine Gun requires 2 Tasen stat items, Rocket launcher requires 5, and MPFB Devastator requires 9.

    Note: Any items that logically require more Tasen items than there are in the pool will be removed.
    The Sector Z and Massacre goals each require 9 Tasen items.
    Generation for those goals will fail if you choose a lower value here.
    """

    display_name = "Tasen Stat Items"
    range_start = 0
    range_end = 9
    default = 9

class MaximumKomatoStat(Range):
    """This determines the minimum number of Komato stat items that can be shuffled into the pool.
    Pulse Cannon requires 2 Komato stat items, Shocksplinter requires 5, and Cyclic Fusion Ignition System requires 9.

    Note 2: Any items that logically require more Komato items than there are in the pool will be removed.
    The Sector Z and Massacre goals each require 9 Komato items.
    Generation for those goals will fail if you choose a lower value here.
    """

    display_name = "Komato Stat Items"
    range_start = 0
    range_end = 9
    default = 9

class MaximumCrackStat(Range):
    """This determines the minimum number of Crack stat items that can be shuffled into the pool.

    Note 1: Any items that logically require more Crack items than there are in the pool will be removed.
    The Sector Z and Massacre goals each require 9 Crack items.
    Generation for those goals will fail if you choose a lower value here.
    """

    display_name = "Crack Stat Items"
    range_start = 0
    range_end = 9
    default = 9

class GameDifficultySetting(Choice):
    """Choose what difficulty the game will be played on.
    The level/stat limitations of higher difficulties may remove some locations from the pool

    Note 1: Choosing Extreme will make reaching Poster 6 impossible.
    If you chose Sector Z as your goal, generation won't fail,
    but you won't be able to reach all the Posters.
    
    Note 1.5: Poster 6 on Hard difficulty requires at least 3 Supercharges from among Sectors 1-6
    in order to obtain enough stat points.

    Note 2: Choosing Ultimortal will make any goal other than defeating Tor impossible,
    and will cause generation to fail if Sector Z or Massacre are chosen as goals.
    It will also remove all stat items other than health from the pool.

    Note 3: Single Sector Play uses Normal difficulty. Keep in mind how many stat points you are intended to have access to
    for your chosen difficulty level when backtracking for checks via Single Sector Play
    (including Supercharges you found in previous levels)
    """
    display_name = "Game Difficulty"
    option_normal = 0
    option_hard = 1
    option_extreme = 2
    option_ultimortal = 3

# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:

    options["combat_logic"] = CombatLogic
    options["health_items"] = MaximumHealthStat
    options["attack_items"] = MaximumAttackStat
    options["assimilate_items"] = MaximumAssimilateStat
    options["strength_items"] = MaximumStrengthStat
    options["tasen_items"] = MaximumTasenStat
    options["komato_items"] = MaximumKomatoStat
    options["crack_items"] = MaximumCrackStat
    options["game_difficulty"] = GameDifficultySetting

    return options