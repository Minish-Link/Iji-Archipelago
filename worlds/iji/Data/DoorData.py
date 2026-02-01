from typing import NamedTuple, List, Dict, TYPE_CHECKING
from enum import Enum

from BaseClasses import CollectionState
from ..Rules import has_stats

if TYPE_CHECKING:
    from .. import IjiWorld

class DoorType(Enum):
    STRENGTH = 1
    CRACK = 2

class DoorData(NamedTuple):
    type: DoorType = None
    level: int = 1
    minimum: int = 1
    maximum: int = 10
    terminal: int = 0

    def shuffle_data(self):
        pass

    def can_open(self, state: CollectionState, world: "IjiWorld", from_terminal: bool = False) -> bool:
        if not from_terminal:
            if self.type == DoorType.STRENGTH:
                if world.current_stat_items["Strength Stat"]+1 < self.level:
                    return False
                return has_stats(world, "Strength Stat", self.level - 1)
            else:
                if world.current_stat_items["Crack Stat"]+1 < self.level:
                    return False
                return has_stats(world, "Crack Stat", self.level - 1)
        else:
            return has_stats(world, "Crack Stat", self.terminal - 1)

    def is_valid_entrance(self, world: "IjiWorld") -> bool:
        if self.terminal != 0:
            return True
        if self.type == DoorType.STRENGTH:
            return world.max_stats["Has Strength Stat"]+1 < self.level
        else:
            return world.max_stats["Has Crack Stat"]+1 < self.level

def shuffle_doors(world: "IjiWorld"):
    ## TODO
    #levels: bool = (world.options.door_shuffle.value & world.options.door_shuffle.option_shuffle_levels_only) != 0
    #types: bool = (world.options.door_shuffle.value & world.options.door_shuffle.option_shuffle_types_only) != 0
    #terminals: bool = (world.options.door_shuffle.value & world.options.door_shuffle.option_shuffle_terminals_only) != 0
    #deviation: int = world.options.door_shuffle_deviation.value
    #for code, data in Door_Levels.items():
    #    world.door_stats[code] = DoorData(
    #        type = data.type if (not types or data.terminal >= 1) else world.random.randrange(1,3)
    #    )
    pass

def choose_random_level(world: "IjiWorld", old_value: int, deviation: int, min_level: int, max_level: int) -> int:
    if old_value < 1 or old_value > 10:
        return old_value
    return world.random.randrange(max(min_level,old_value-deviation), min(max_level+1,old_value+deviation+1))

Door_Levels: Dict[int, DoorData] = {
    # Sector 1
    1: DoorData(type=DoorType.STRENGTH, maximum=1), # The first door cannot be randomized
    2: DoorData(type=DoorType.STRENGTH, level=2),
    3: DoorData(type=DoorType.STRENGTH),
    4: DoorData(type=DoorType.STRENGTH),
    5: DoorData(type=DoorType.STRENGTH),
    6: DoorData(type=DoorType.STRENGTH),
    7: DoorData(type=DoorType.STRENGTH),

    # Sector 2
    8: DoorData(type=DoorType.CRACK,maximum=1), # The first door of sector 2 cannot be randomized
    9: DoorData(type=DoorType.STRENGTH,level=2),
    10: DoorData(type=DoorType.STRENGTH),
    11: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    12: DoorData(type=DoorType.CRACK),
    13: DoorData(type=DoorType.CRACK,level=3,terminal=1),
    14: DoorData(type=DoorType.CRACK),
    15: DoorData(type=DoorType.STRENGTH),

    # Sector 3
    16: DoorData(type=DoorType.STRENGTH),
    17: DoorData(type=DoorType.STRENGTH),
    18: DoorData(type=DoorType.STRENGTH,level=2),
    19: DoorData(type=DoorType.STRENGTH,level=2),
    20: DoorData(type=DoorType.CRACK,level=3),
    21: DoorData(type=DoorType.STRENGTH,level=2),
    22: DoorData(type=DoorType.STRENGTH),
    23: DoorData(type=DoorType.STRENGTH,level=2),
    24: DoorData(type=DoorType.CRACK,level=2),
    25: DoorData(type=DoorType.STRENGTH,level=10),
    26: DoorData(type=DoorType.CRACK,level=10),
    27: DoorData(type=DoorType.STRENGTH),
    28: DoorData(type=DoorType.STRENGTH),
    29: DoorData(type=DoorType.STRENGTH),
    30: DoorData(type=DoorType.STRENGTH,level=4),
    31: DoorData(type=DoorType.STRENGTH,level=4),
    32: DoorData(type=DoorType.STRENGTH),
    33: DoorData(type=DoorType.CRACK,level=2),
    34: DoorData(type=DoorType.STRENGTH),
    35: DoorData(type=DoorType.STRENGTH),
    36: DoorData(type=DoorType.STRENGTH),
    37: DoorData(type=DoorType.CRACK),

    # Sector 4
    38: DoorData(type=DoorType.CRACK),
    39: DoorData(type=DoorType.CRACK,level=6,terminal=1),
    40: DoorData(type=DoorType.STRENGTH,level=4),
    41: DoorData(type=DoorType.STRENGTH,level=15),
    42: DoorData(type=DoorType.CRACK,level=3),
    43: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    44: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    45: DoorData(type=DoorType.STRENGTH,level=6),
    46: DoorData(type=DoorType.STRENGTH),
    47: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    48: DoorData(type=DoorType.CRACK,level=15,terminal=1),

    # Sector 5
    49: DoorData(type=DoorType.STRENGTH),
    50: DoorData(type=DoorType.CRACK,level=2),
    51: DoorData(type=DoorType.STRENGTH,level=7),
    52: DoorData(type=DoorType.STRENGTH,level=5),
    53: DoorData(type=DoorType.STRENGTH,level=3),
    54: DoorData(type=DoorType.STRENGTH,level=8),
    55: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    56: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    57: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    58: DoorData(type=DoorType.CRACK,level=9,terminal=1),
    59: DoorData(type=DoorType.STRENGTH,level=3),
    60: DoorData(type=DoorType.STRENGTH),
    61: DoorData(type=DoorType.CRACK),
    62: DoorData(type=DoorType.CRACK,level=4),
    63: DoorData(type=DoorType.STRENGTH,level=4),

    # Sector 6
    64: DoorData(type=DoorType.CRACK,level=3),
    65: DoorData(type=DoorType.STRENGTH),
    66: DoorData(type=DoorType.STRENGTH),
    67: DoorData(type=DoorType.STRENGTH,level=15),
    68: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    69: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    70: DoorData(type=DoorType.CRACK,level=10),
    71: DoorData(type=DoorType.STRENGTH),
    72: DoorData(type=DoorType.STRENGTH),
    73: DoorData(type=DoorType.CRACK,level=4),
    74: DoorData(type=DoorType.STRENGTH),
    75: DoorData(type=DoorType.STRENGTH),
    76: DoorData(type=DoorType.STRENGTH),
    77: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    78: DoorData(type=DoorType.STRENGTH,level=2),
    79: DoorData(type=DoorType.STRENGTH),
    80: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    81: DoorData(type=DoorType.STRENGTH),
    82: DoorData(type=DoorType.STRENGTH),
    83: DoorData(type=DoorType.STRENGTH),
    84: DoorData(type=DoorType.STRENGTH),
    85: DoorData(type=DoorType.STRENGTH),
    86: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    87: DoorData(type=DoorType.STRENGTH),

    # Sector 7
    88: DoorData(type=DoorType.STRENGTH),
    89: DoorData(type=DoorType.STRENGTH,level=8),
    90: DoorData(type=DoorType.STRENGTH,level=6),
    91: DoorData(type=DoorType.STRENGTH,level=3),
    92: DoorData(type=DoorType.STRENGTH),
    93: DoorData(type=DoorType.CRACK,level=3),
    94: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    95: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    96: DoorData(type=DoorType.CRACK,level=8),
    97: DoorData(type=DoorType.STRENGTH),
    98: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    99: DoorData(type=DoorType.CRACK,level=3),
    100: DoorData(type=DoorType.STRENGTH),
    101: DoorData(type=DoorType.STRENGTH),
    102: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    103: DoorData(type=DoorType.CRACK),
    104: DoorData(type=DoorType.CRACK,level=15,terminal=1,minimum=1,maximum=1), # Phantom Hammer
    105: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    106: DoorData(type=DoorType.STRENGTH,level=4),
    107: DoorData(type=DoorType.STRENGTH),
    108: DoorData(type=DoorType.STRENGTH),

    # Sector 8
    109: DoorData(type=DoorType.STRENGTH),
    110: DoorData(type=DoorType.STRENGTH),
    111: DoorData(type=DoorType.STRENGTH,level=9),
    112: DoorData(type=DoorType.STRENGTH,level=4),
    113: DoorData(type=DoorType.STRENGTH),
    114: DoorData(type=DoorType.CRACK,level=5),
    115: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    116: DoorData(type=DoorType.STRENGTH),
    117: DoorData(type=DoorType.STRENGTH,level=3),
    118: DoorData(type=DoorType.CRACK,level=8),
    119: DoorData(type=DoorType.STRENGTH,level=5),
    120: DoorData(type=DoorType.STRENGTH,level=10),

    # Sector 9
    121: DoorData(type=DoorType.STRENGTH,level=3),
    122: DoorData(type=DoorType.STRENGTH),
    123: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    124: DoorData(type=DoorType.STRENGTH),
    125: DoorData(type=DoorType.STRENGTH),
    126: DoorData(type=DoorType.CRACK,level=6),
    127: DoorData(type=DoorType.STRENGTH),
    128: DoorData(type=DoorType.STRENGTH),
    129: DoorData(type=DoorType.STRENGTH),
    130: DoorData(type=DoorType.STRENGTH),
    131: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    132: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    133: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    134: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    135: DoorData(type=DoorType.CRACK),
    136: DoorData(type=DoorType.CRACK),
    137: DoorData(type=DoorType.STRENGTH),
    138: DoorData(type=DoorType.CRACK),
    139: DoorData(type=DoorType.CRACK),
    140: DoorData(type=DoorType.CRACK),
    141: DoorData(type=DoorType.CRACK),
    142: DoorData(type=DoorType.STRENGTH),
    143: DoorData(type=DoorType.STRENGTH,level=5),
    144: DoorData(type=DoorType.STRENGTH,level=9),
    146: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    145: DoorData(type=DoorType.STRENGTH),
    147: DoorData(type=DoorType.CRACK),
    148: DoorData(type=DoorType.CRACK),
    149: DoorData(type=DoorType.STRENGTH,level=5),
    150: DoorData(type=DoorType.CRACK,level=5),
    151: DoorData(type=DoorType.CRACK),
    152: DoorData(type=DoorType.CRACK),
    153: DoorData(type=DoorType.CRACK),
    154: DoorData(type=DoorType.CRACK),
    155: DoorData(type=DoorType.CRACK),
    156: DoorData(type=DoorType.STRENGTH),
    157: DoorData(type=DoorType.CRACK),
    158: DoorData(type=DoorType.STRENGTH),
    159: DoorData(type=DoorType.CRACK,level=15,terminal=1,minimum=1,maximum=1), # Supercharge,

    # Sector X
    160: DoorData(type=DoorType.STRENGTH),
    161: DoorData(type=DoorType.STRENGTH),
    162: DoorData(type=DoorType.STRENGTH),
    163: DoorData(type=DoorType.STRENGTH),
    164: DoorData(type=DoorType.STRENGTH,level=15),
    165: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    166: DoorData(type=DoorType.CRACK,level=15,terminal=1),
    167: DoorData(type=DoorType.CRACK,level=15,terminal=1,minimum=1,maximum=1), # Megacore
    168: DoorData(type=DoorType.STRENGTH),
    169: DoorData(type=DoorType.STRENGTH),
    170: DoorData(type=DoorType.STRENGTH),
    171: DoorData(type=DoorType.CRACK,level=3),
    172: DoorData(type=DoorType.CRACK,level=3),
    173: DoorData(type=DoorType.STRENGTH,level=7),
    174: DoorData(type=DoorType.CRACK),
    175: DoorData(type=DoorType.STRENGTH),
    176: DoorData(type=DoorType.STRENGTH),
    177: DoorData(type=DoorType.CRACK,level=15,terminal=1,minimum=1,maximum=1), # Asha
    178: DoorData(type=DoorType.STRENGTH,level=6),
    179: DoorData(type=DoorType.STRENGTH,level=15),
    180: DoorData(type=DoorType.STRENGTH,level=10),
    181: DoorData(type=DoorType.CRACK,level=7),
    182: DoorData(type=DoorType.STRENGTH,level=8),
    183: DoorData(type=DoorType.CRACK,level=10),
    184: DoorData(type=DoorType.CRACK,level=9),
    185: DoorData(type=DoorType.CRACK,level=9),
    186: DoorData(type=DoorType.STRENGTH),
    187: DoorData(type=DoorType.STRENGTH),
    188: DoorData(type=DoorType.STRENGTH),
    189: DoorData(type=DoorType.STRENGTH),
    190: DoorData(type=DoorType.CRACK),
    191: DoorData(type=DoorType.CRACK)
}