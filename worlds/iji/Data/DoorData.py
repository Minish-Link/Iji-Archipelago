from typing import NamedTuple, List, Dict

class DoorData(NamedTuple):
    terminal: bool = False
    strength: int = 0
    crack: int = 0

# Sector 1
Sector1_Progression_Strength: List[int] = [1,2]
Sector1_Doors_Strength: List[Dict[int, DoorData]] = [
    {
        501: DoorData(strength = 1),
        503: DoorData(strength = 1),
        504: DoorData(strength = 1),
        505: DoorData(strength = 1),
        506: DoorData(strength = 1),
        507: DoorData(strength = 1)
    },
    {
        502: DoorData(strength = 2)
    }
]

# Sector 2
Sector2_Progression_Strength: List[int] = [1,2]
Sector2_Doors_Strength: List[Dict[int, DoorData]] = [
    {
        510: DoorData(strength = 1),
        515: DoorData(strength = 1)
    },
    {
        509: DoorData(strength = 2)
    }
]

Sector2_Progression_Crack: List[int] = [1,3]
Sector2_Doors_Crack: List[Dict[int, DoorData]] = [
    {
        508: DoorData(crack = 1),
        514: DoorData(crack = 1)
    },
    {
        513: DoorData(crack = 3)
    }
]

Sector2_Doors_Terminal: Dict[int, DoorData] = {
    511: DoorData(terminal = True),
    512: DoorData(terminal = True)
}

# Sector 3
Sector3_Progression_Strength: List[int] = [1,2,4,10]
Sector3_Doors_Strength: List[Dict[int, DoorData]] = [
    {
        516: DoorData(strength = 1),
        517: DoorData(strength = 1),
        522: DoorData(strength = 1),
        527: DoorData(strength = 1),
        528: DoorData(strength = 1),
        529: DoorData(strength = 1),
        532: DoorData(strength = 1),
        534: DoorData(strength = 1),
        535: DoorData(strength = 1),
        536: DoorData(strength = 1)
    },
    {
        518: DoorData(strength = 2),
        519: DoorData(strength = 2),
        521: DoorData(strength = 2),
        523: DoorData(strength = 2)
    },
    {
        530: DoorData(strength = 4),
        531: DoorData(strength = 4)
    },
    {
        525: DoorData(strength = 10)
    }
]

Sector3_Progression_Crack: List[int] = [1,2,3,10]
Sector3_Doors_Crack: List[Dict[int, DoorData]] = [
    {
        537: DoorData(crack = 1)
    },
    {
        524: DoorData(crack = 2),
        533: DoorData(crack = 2)
    },
    {
        520: DoorData(crack = 3)
    },
    {
        526: DoorData(crack = 10)
    }
]

# Sector 4
Sector4_Progression_Strength: List[int] = [1,4,6,11]
Sector4_Doors_Strength: List[Dict[int,DoorData]] = [
    {
        546: DoorData(strength = 1)
    },
    {
        540: DoorData(strength = 4)
    },
    {
        545: DoorData(strength = 6)
    },
    {
        541: DoorData(strength = 11)
    }
]

Sector4_Progression_Crack: List[int] = [1,3]
Sector4_Doors_Crack: List[Dict[int,DoorData]] = [
    {
        538: DoorData(crack = 1)
    },
    {
        542: DoorData(crack = 3)
    }
]

Sector4_Doors_Terminal: Dict[int, DoorData] = {
    539: DoorData(terminal = True),
    543: DoorData(terminal = True),
    544: DoorData(terminal = True),
    547: DoorData(terminal = True),
    548: DoorData(terminal = True)
}

# Sector 5
Sector5_Progression_Strength: List[int] = [1,3,4,5,7,8]
Sector5_Doors_Strength: List[Dict[int, DoorData]] = [
    {
        549: DoorData(strength = 1),
        560: DoorData(strength = 1),
        561: DoorData(strength = 1)
    },
    {
        553: DoorData(strength = 3),
        559: DoorData(strength = 3)
    },
    {
        563: DoorData(strength = 4)
    },
    {
        552: DoorData(strength = 5)
    },
    {
        551: DoorData(strength = 7)
    },
    {
        554: DoorData(strength = 8)
    }
]

Sector5_Progression_Crack: List[int] = [2,4]
Sector5_Doors_Crack: List[Dict[int, DoorData]] = [
    {
        550: DoorData(crack = 2)
    },
    {
        562: DoorData(crack = 4)
    }
]

Sector5_Doors_Terminal: Dict[int, DoorData] = {
    555: DoorData(terminal = True),
    556: DoorData(terminal = True),
    557: DoorData(terminal = True),
    558: DoorData(terminal = True)
}

# Sector 6
Sector6_Progression_Strength: List[int] = [1,2,11]
Sector6_Doors_Strength: List[Dict[int, DoorData]] = [
    {
        565: DoorData(strength = 1),
        566: DoorData(strength = 1),
        571: DoorData(strength = 1),
        572: DoorData(strength = 1),
        574: DoorData(strength = 1),
        575: DoorData(strength = 1),
        576: DoorData(strength = 1),
        579: DoorData(strength = 1),
        581: DoorData(strength = 1),
        582: DoorData(strength = 1),
        583: DoorData(strength = 1),
        584: DoorData(strength = 1),
        585: DoorData(strength = 1),
        587: DoorData(strength = 1)
    },
    {
        578: DoorData(strength = 2)
    },
    {
        567: DoorData(strength = 11)
    }
]

Sector6_Progression_Crack: List[int] = [3,4,10]
Sector6_Doors_Crack: List[Dict[int, DoorData]] = [
    {
        564: DoorData(crack = 3)
    },
    {
        573: DoorData(crack = 4)
    },
    {
        570: DoorData(crack = 10)
    }
]

Sector6_Doors_Terminal: Dict[int, DoorData] = {
    568: DoorData(terminal = True),
    569: DoorData(terminal = True),
    577: DoorData(terminal = True),
    580: DoorData(terminal = True),
    586: DoorData(terminal = True)
}

# Sector 7
Sector7_Progression_Strength: List[int] = [1,3,4,6,8]
Sector7_Doors_Strength: List[Dict[int, DoorData]] = [
    {
        588: DoorData(strength = 1),
        592: DoorData(strength = 1),
        597: DoorData(strength = 1),
        600: DoorData(strength = 1),
        601: DoorData(strength = 1),
        607: DoorData(strength = 1),
        608: DoorData(strength = 1)
    },
    {
        591: DoorData(strength = 3)
    },
    {
        606: DoorData(strength = 4)
    },
    {
        590: DoorData(strength = 6)
    },
    {
        589: DoorData(strength = 8)
    }
]

Sector7_Progression_Crack: List[int] = [1,3,8]
Sector7_Doors_Crack: List[Dict[int, DoorData]] = [
    {
        603: DoorData(crack = 1)
    },
    {
        593: DoorData(crack = 3),
        599: DoorData(crack = 3)
    },
    {
        596: DoorData(crack = 8)
    }
]

Sector7_Doors_Terminal: Dict[int, DoorData] = {
    594: DoorData(terminal = True),
    595: DoorData(terminal = True),
    598: DoorData(terminal = True),
    602: DoorData(terminal = True),
    604: DoorData(terminal = True),
    605: DoorData(terminal = True)
}

# Sector 8
Sector8_Progression_Strength: List[int] = [1,3,4,5,9,10]
Sector8_Doors_Strength: List[Dict[int, DoorData]] = [
    {
        609: DoorData(strength = 1),
        610: DoorData(strength = 1),
        613: DoorData(strength = 1),
        616: DoorData(strength = 1)
    },
    {
        617: DoorData(strength = 3)
    },
    {
        612: DoorData(strength = 4)
    },
    {
        619: DoorData(strength = 5)
    },
    {
        611: DoorData(strength = 9)
    },
    {
        620: DoorData(strength = 10)
    }
]

Sector8_Progression_Crack: List[int] = [5,8]
Sector8_Doors_Crack: List[Dict[int, DoorData]] = [
    {
        614: DoorData(crack = 5)
    },
    {
        618: DoorData(crack = 8)
    }
]

Sector8_Doors_Terminal: Dict[int, DoorData] = {
    615: DoorData(terminal = True)
}

# Sector 9
Sector9_Progression_Strength: List[int] = [1,3,5,9]
Sector9_Doors_Strength: List[Dict[int, DoorData]] = [
    {
        622: DoorData(strength = 1),
        624: DoorData(strength = 1),
        625: DoorData(strength = 1),
        627: DoorData(strength = 1),
        628: DoorData(strength = 1),
        629: DoorData(strength = 1),
        630: DoorData(strength = 1),
        637: DoorData(strength = 1),
        642: DoorData(strength = 1),
        645: DoorData(strength = 1),
        656: DoorData(strength = 1),
        658: DoorData(strength = 1)
    },
    {
        621: DoorData(strength = 3)
    },
    {
        643: DoorData(strength = 5),
        649: DoorData(strength = 5)
    },
    {
        644: DoorData(strength = 9)
    }
]

Sector9_Progression_Crack: List[int] = [1,5,6]
Sector9_Doors_Crack: List[Dict[int, DoorData]] = [
    {
        635: DoorData(crack = 1),
        636: DoorData(crack = 1),
        638: DoorData(crack = 1),
        639: DoorData(crack = 1),
        640: DoorData(crack = 1),
        641: DoorData(crack = 1),
        647: DoorData(crack = 1),
        648: DoorData(crack = 1),
        651: DoorData(crack = 1),
        652: DoorData(crack = 1),
        653: DoorData(crack = 1),
        654: DoorData(crack = 1),
        655: DoorData(crack = 1),
        657: DoorData(crack = 1)
    },
    {
        650: DoorData(crack = 5)
    },
    {
        626: DoorData(crack = 6)
    }
]

Sector9_Doors_Terminal: Dict[int, DoorData] = {
    623: DoorData(terminal = True),
    631: DoorData(terminal = True),
    632: DoorData(terminal = True),
    633: DoorData(terminal = True),
    634: DoorData(terminal = True),
    646: DoorData(terminal = True),
    659: DoorData(terminal = True)
}

# Sector X
SectorX_Progression_Strength: List[int] = [1,6,7,8,10,11]
SectorX_Doors_Strength: List[Dict[int, DoorData]] = [
    {
        660: DoorData(strength = 1),
        661: DoorData(strength = 1),
        662: DoorData(strength = 1),
        663: DoorData(strength = 1),
        668: DoorData(strength = 1),
        669: DoorData(strength = 1),
        670: DoorData(strength = 1),
        675: DoorData(strength = 1),
        676: DoorData(strength = 1),
        686: DoorData(strength = 1),
        687: DoorData(strength = 1),
        688: DoorData(strength = 1),
        689: DoorData(strength = 1)
    },
    {
        678: DoorData(strength = 6)
    },
    {
        673: DoorData(strength = 7)
    },
    {
        682: DoorData(strength = 8)
    },
    {
        680: DoorData(strength = 10)
    },
    {
        664: DoorData(strength = 11),
        679: DoorData(strength = 11)
    }
]

SectorX_Progression_Crack: List[int] = [1,3,7,9,10]
SectorX_Doors_Crack: List[Dict[int, DoorData]] = [
    {
        674: DoorData(crack = 1),
        690: DoorData(crack = 1),
        691: DoorData(crack = 1)
    },
    {
        671: DoorData(crack = 3),
        672: DoorData(crack = 3)
    },
    {
        681: DoorData(crack = 7)
    },
    {
        684: DoorData(crack = 9),
        685: DoorData(crack = 9)
    },
    {
        683: DoorData(crack = 10)
    }
]

SectorX_Doors_Terminal: Dict[int, DoorData] = {
    665: DoorData(terminal = True),
    666: DoorData(terminal = True),
    667: DoorData(terminal = True),
    677: DoorData(terminal = True)
}

All_Doors_Strength: List[Dict[int, DoorData]] = [
    {
        **Sector1_Doors_Strength[0],
        **Sector2_Doors_Strength[0],
        **Sector3_Doors_Strength[0],
        **Sector4_Doors_Strength[0],
        **Sector5_Doors_Strength[0],
        **Sector6_Doors_Strength[0],
        **Sector7_Doors_Strength[0],
        **Sector8_Doors_Strength[0],
        **Sector9_Doors_Strength[0],
        **SectorX_Doors_Strength[0]
    },
    {
        **Sector1_Doors_Strength[1],
        **Sector2_Doors_Strength[1],
        **Sector3_Doors_Strength[1],
        **Sector6_Doors_Strength[1]
    },
    {
        **Sector5_Doors_Strength[1],
        **Sector7_Doors_Strength[1],
        **Sector8_Doors_Strength[1],
        **Sector9_Doors_Strength[1]
    },
    {
        **Sector3_Doors_Strength[2],
        **Sector4_Doors_Strength[1],
        **Sector5_Doors_Strength[2],
        **Sector7_Doors_Strength[2],
        **Sector8_Doors_Strength[2]
    },
    {
        **Sector5_Doors_Strength[3],
        **Sector8_Doors_Strength[3],
        **Sector9_Doors_Strength[2]
    },
    {
        **Sector4_Doors_Strength[2],
        **Sector7_Doors_Strength[3],
        **SectorX_Doors_Strength[1]
    },
    {
        **Sector5_Doors_Strength[4],
        **SectorX_Doors_Strength[2]
    },
    {
        **Sector5_Doors_Strength[5],
        **Sector7_Doors_Strength[4],
        **SectorX_Doors_Strength[3]
    },
    {
        **Sector8_Doors_Strength[4],
        **Sector9_Doors_Strength[3]
    },
    {
        **Sector3_Doors_Strength[3],
        **Sector8_Doors_Strength[5],
        **SectorX_Doors_Strength[4]
    },
    {
        **Sector4_Doors_Strength[3],
        **Sector6_Doors_Strength[2],
        **SectorX_Doors_Strength[5]
    }
]

All_Doors_Crack: List[Dict[int, DoorData]] = [
    {
        **Sector2_Doors_Crack[0],
        **Sector3_Doors_Crack[0],
        **Sector4_Doors_Crack[0],
        **Sector7_Doors_Crack[0],
        **Sector9_Doors_Crack[0],
        **SectorX_Doors_Crack[0]
    },
    {
        **Sector3_Doors_Crack[1],
        **Sector5_Doors_Crack[1]
    },
    {
        **Sector2_Doors_Crack[1],
        **Sector3_Doors_Crack[2],
        **Sector4_Doors_Crack[1],
        **Sector6_Doors_Crack[0],
        **Sector7_Doors_Crack[1],
        **SectorX_Doors_Crack[1]
    },
    {
        **Sector5_Doors_Crack[1],
        **Sector6_Doors_Crack[1]
    },
    {
        **Sector8_Doors_Crack[0],
        **Sector9_Doors_Crack[1]
    },
    {
        **Sector9_Doors_Crack[2]
    },
    {
        **SectorX_Doors_Crack[2]
    },
    {
        **Sector7_Doors_Crack[2],
        **Sector8_Doors_Crack[1]
    },
    {
        **SectorX_Doors_Crack[3]
    },
    {
        **Sector3_Doors_Crack[3],
        **Sector6_Doors_Crack[2],
        **SectorX_Doors_Crack[4]
    }
]

All_Doors_Terminal: Dict[int, DoorData] = {
    **Sector2_Doors_Terminal,
    **Sector4_Doors_Terminal,
    **Sector5_Doors_Terminal,
    **Sector6_Doors_Terminal,
    **Sector7_Doors_Terminal,
    **Sector8_Doors_Terminal,
    **Sector9_Doors_Terminal,
    **SectorX_Doors_Terminal
}

All_Doors: Dict[int, DoorData] = {
    **All_Doors_Strength[0],
    **All_Doors_Strength[1],
    **All_Doors_Strength[2],
    **All_Doors_Strength[3],
    **All_Doors_Strength[4],
    **All_Doors_Strength[5],
    **All_Doors_Strength[6],
    **All_Doors_Strength[7],
    **All_Doors_Strength[8],
    **All_Doors_Strength[9],
    **All_Doors_Strength[10],
    **All_Doors_Crack[0],
    **All_Doors_Crack[1],
    **All_Doors_Crack[2],
    **All_Doors_Crack[3],
    **All_Doors_Crack[4],
    **All_Doors_Crack[5],
    **All_Doors_Crack[6],
    **All_Doors_Crack[7],
    **All_Doors_Crack[8],
    **All_Doors_Crack[9],
    **All_Doors_Terminal
}