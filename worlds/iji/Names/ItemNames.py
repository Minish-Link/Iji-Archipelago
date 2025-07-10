from typing import List

Stat_Health = "Health Stat"
Stat_Attack = "Attack Stat"
Stat_Assimilate = "Assimilate Stat"
Stat_Strength = "Strength Stat"
Stat_Crack = "Crack Stat"
Stat_Tasen = "Tasen Stat"
Stat_Komato = "Komato Stat"

Sector_Access: List[str] = [
    "Progressive Sector Access",
    "Sector 1 Access",
    "Sector 2 Access",
    "Sector 3 Access",
    "Sector 4 Access",
    "Sector 5 Access",
    "Sector 6 Access",
    "Sector 7 Access",
    "Sector 8 Access",
    "Sector 9 Access",
    "Sector X Access"
]

Ribbon = "Ribbon"
Supercharge = "Supercharge"

Special_Health = "SUPPRESSION"
Special_Attack = "IMPROVED AUTOLOADING"
Special_Assimilate = "ADVANCED RECOVERY"
Special_Strength = "CYBERNETIC ENDURANCE"
Special_Crack = "ELECTRONIC MASTERY"
Special_Tasen = "VENGEANCE"
Special_Komato = "GLORY"

Filler: List[str] = [
    "Health Pickup",
    "Armor Pickup",
    "Nano Pickup",
    "Machine Ammo",
    "Rocket Ammo",
    "MPFB Ammo",
    "Pulse Ammo",
    "Shock Ammo",
    "CFIS Ammo",
    "Nano Overload",
    "Bundle of Ammo"
]

Traps: List[str] = [
    "Rocket to the Face",
    "Blits Nest",
    "Null Drive",
    "Turbo Mode",
    "Power Nap",
    "Clown Shoes",
    "Banana"
]

Debug = "Fire Anytime"
Upgrade_Jump = "Jump Upgrade"
Upgrade_Armor = "Armor Upgrade"

Weapons: List[str] = [
    "Null Driver",
    "Shotgun",
    "Machine Gun",
    "Rocket Launcher",
    "MPFB Devastator",
    "Resonance Detonator",
    "Pulse Cannon",
    "Shocksplinter",
    "Cyclic Fusion Ignition System",
    "Buster Gun",
    "Splintergun",
    "Spread Rockets",
    "Nuke",
    "Resonance Reflector",
    "Hyper Pulse",
    "Plasma Cannon",
    "Velocithor V2-10",
    "Banana Gun",
    "Massacre"
]

Checkpoints: List[str] = [
    "Sector 2 - Checkpoint",
    "Sector 3 - Checkpoint",
    "Sector 4 - Checkpoint",
    "Sector 5 - Checkpoint",
    "Sector 6 - Checkpoint",
    "Sector 7 - First Checkpoint",
    "Sector 7 - Second Checkpoint",
    "Sector 8 - Checkpoint",
    "Sector 9 - First Checkpoint",
    "Sector 9 - Second Checkpoint",
    "Sector X - First Checkpoint",
    "Sector X - Second Checkpoint"
]

StrengthDoorLevels: List[List[str]] = [
    [
    "Progressive Shield Doors",
    "Resistance 1 Doors",
    "Resistance 2 Doors",
    "Resistance 3 Doors",
    "Resistance 4 Doors",
    "Resistance 5 Doors",
    "Resistance 6 Doors",
    "Resistance 7 Doors",
    "Resistance 8 Doors",
    "Resistance 9 Doors",
    "Resistance 10 Doors",
    "Resistance 15+ Doors"
    ],
    [
    "Sector 1 Progressive Shield Doors",
    "Sector 1 Resistance 1 Doors",
    "Sector 1 Resistance 2 Doors",
    "Sector 1 Resistance 3 Doors",
    "Sector 1 Resistance 4 Doors",
    "Sector 1 Resistance 5 Doors",
    "Sector 1 Resistance 6 Doors",
    "Sector 1 Resistance 7 Doors",
    "Sector 1 Resistance 8 Doors",
    "Sector 1 Resistance 9 Doors",
    "Sector 1 Resistance 10 Doors",
    "Sector 1 Resistance 15+ Doors"
    ],
    [
    "Sector 2 Progressive Shield Doors",
    "Sector 2 Resistance 1 Doors",
    "Sector 2 Resistance 2 Doors",
    "Sector 2 Resistance 3 Doors",
    "Sector 2 Resistance 4 Doors",
    "Sector 2 Resistance 5 Doors",
    "Sector 2 Resistance 6 Doors",
    "Sector 2 Resistance 7 Doors",
    "Sector 2 Resistance 8 Doors",
    "Sector 2 Resistance 9 Doors",
    "Sector 2 Resistance 10 Doors",
    "Sector 2 Resistance 15+ Doors"
    ],
    [
    "Sector 3 Progressive Shield Doors",
    "Sector 3 Resistance 1 Doors",
    "Sector 3 Resistance 2 Doors",
    "Sector 3 Resistance 3 Doors",
    "Sector 3 Resistance 4 Doors",
    "Sector 3 Resistance 5 Doors",
    "Sector 3 Resistance 6 Doors",
    "Sector 3 Resistance 7 Doors",
    "Sector 3 Resistance 8 Doors",
    "Sector 3 Resistance 9 Doors",
    "Sector 3 Resistance 10 Doors",
    "Sector 3 Resistance 15+ Doors"
    ],
    [
    "Sector 4 Progressive Shield Doors",
    "Sector 4 Resistance 1 Doors",
    "Sector 4 Resistance 2 Doors",
    "Sector 4 Resistance 3 Doors",
    "Sector 4 Resistance 4 Doors",
    "Sector 4 Resistance 5 Doors",
    "Sector 4 Resistance 6 Doors",
    "Sector 4 Resistance 7 Doors",
    "Sector 4 Resistance 8 Doors",
    "Sector 4 Resistance 9 Doors",
    "Sector 4 Resistance 10 Doors",
    "Sector 4 Resistance 15+ Doors"
    ],
    [
    "Sector 5 Progressive Shield Doors",
    "Sector 5 Resistance 1 Doors",
    "Sector 5 Resistance 2 Doors",
    "Sector 5 Resistance 3 Doors",
    "Sector 5 Resistance 4 Doors",
    "Sector 5 Resistance 5 Doors",
    "Sector 5 Resistance 6 Doors",
    "Sector 5 Resistance 7 Doors",
    "Sector 5 Resistance 8 Doors",
    "Sector 5 Resistance 9 Doors",
    "Sector 5 Resistance 10 Doors",
    "Sector 5 Resistance 15+ Doors"
    ],
    [
    "Sector 6 Progressive Shield Doors",
    "Sector 6 Resistance 1 Doors",
    "Sector 6 Resistance 2 Doors",
    "Sector 6 Resistance 3 Doors",
    "Sector 6 Resistance 4 Doors",
    "Sector 6 Resistance 5 Doors",
    "Sector 6 Resistance 6 Doors",
    "Sector 6 Resistance 7 Doors",
    "Sector 6 Resistance 8 Doors",
    "Sector 6 Resistance 9 Doors",
    "Sector 6 Resistance 10 Doors",
    "Sector 6 Resistance 15+ Doors"
    ],
    [
    "Sector 7 Progressive Shield Doors",
    "Sector 7 Resistance 1 Doors",
    "Sector 7 Resistance 2 Doors",
    "Sector 7 Resistance 3 Doors",
    "Sector 7 Resistance 4 Doors",
    "Sector 7 Resistance 5 Doors",
    "Sector 7 Resistance 6 Doors",
    "Sector 7 Resistance 7 Doors",
    "Sector 7 Resistance 8 Doors",
    "Sector 7 Resistance 9 Doors",
    "Sector 7 Resistance 10 Doors",
    "Sector 7 Resistance 15+ Doors"
    ],
    [
    "Sector 8 Progressive Shield Doors",
    "Sector 8 Resistance 1 Doors",
    "Sector 8 Resistance 2 Doors",
    "Sector 8 Resistance 3 Doors",
    "Sector 8 Resistance 4 Doors",
    "Sector 8 Resistance 5 Doors",
    "Sector 8 Resistance 6 Doors",
    "Sector 8 Resistance 7 Doors",
    "Sector 8 Resistance 8 Doors",
    "Sector 8 Resistance 9 Doors",
    "Sector 8 Resistance 10 Doors",
    "Sector 8 Resistance 15+ Doors"
    ],
    [
    "Sector 9 Progressive Shield Doors",
    "Sector 9 Resistance 1 Doors",
    "Sector 9 Resistance 2 Doors",
    "Sector 9 Resistance 3 Doors",
    "Sector 9 Resistance 4 Doors",
    "Sector 9 Resistance 5 Doors",
    "Sector 9 Resistance 6 Doors",
    "Sector 9 Resistance 7 Doors",
    "Sector 9 Resistance 8 Doors",
    "Sector 9 Resistance 9 Doors",
    "Sector 9 Resistance 10 Doors",
    "Sector 9 Resistance 15+ Doors"
    ],
    [
    "Sector X Progressive Shield Doors",
    "Sector X Resistance 1 Doors",
    "Sector X Resistance 2 Doors",
    "Sector X Resistance 3 Doors",
    "Sector X Resistance 4 Doors",
    "Sector X Resistance 5 Doors",
    "Sector X Resistance 6 Doors",
    "Sector X Resistance 7 Doors",
    "Sector X Resistance 8 Doors",
    "Sector X Resistance 9 Doors",
    "Sector X Resistance 10 Doors",
    "Sector X Resistance 15+ Doors"
    ],
]

CrackDoorLevels: List[List[str]] = [
    [
    "Progressive Security Doors",
    "Security 1 Doors",
    "Security 2 Doors",
    "Security 3 Doors",
    "Security 4 Doors",
    "Security 5 Doors",
    "Security 6 Doors",
    "Security 7 Doors",
    "Security 8 Doors",
    "Security 9 Doors",
    "Security 10 Doors",
    "Security 15+ Doors"
    ],
    [
    "Sector 1 Progressive Security Doors",
    "Sector 1 Security 1 Doors",
    "Sector 1 Security 2 Doors",
    "Sector 1 Security 3 Doors",
    "Sector 1 Security 4 Doors",
    "Sector 1 Security 5 Doors",
    "Sector 1 Security 6 Doors",
    "Sector 1 Security 7 Doors",
    "Sector 1 Security 8 Doors",
    "Sector 1 Security 9 Doors",
    "Sector 1 Security 10 Doors",
    "Sector 1 Security 15+ Doors"
    ],
    [
    "Sector 2 Progressive Security Doors",
    "Sector 2 Security 1 Doors",
    "Sector 2 Security 2 Doors",
    "Sector 2 Security 3 Doors",
    "Sector 2 Security 4 Doors",
    "Sector 2 Security 5 Doors",
    "Sector 2 Security 6 Doors",
    "Sector 2 Security 7 Doors",
    "Sector 2 Security 8 Doors",
    "Sector 2 Security 9 Doors",
    "Sector 2 Security 10 Doors",
    "Sector 2 Security 15+ Doors"
    ],
    [
    "Sector 3 Progressive Security Doors",
    "Sector 3 Security 1 Doors",
    "Sector 3 Security 2 Doors",
    "Sector 3 Security 3 Doors",
    "Sector 3 Security 4 Doors",
    "Sector 3 Security 5 Doors",
    "Sector 3 Security 6 Doors",
    "Sector 3 Security 7 Doors",
    "Sector 3 Security 8 Doors",
    "Sector 3 Security 9 Doors",
    "Sector 3 Security 10 Doors",
    "Sector 3 Security 15+ Doors"
    ],
    [
    "Sector 4 Progressive Security Doors",
    "Sector 4 Security 1 Doors",
    "Sector 4 Security 2 Doors",
    "Sector 4 Security 3 Doors",
    "Sector 4 Security 4 Doors",
    "Sector 4 Security 5 Doors",
    "Sector 4 Security 6 Doors",
    "Sector 4 Security 7 Doors",
    "Sector 4 Security 8 Doors",
    "Sector 4 Security 9 Doors",
    "Sector 4 Security 10 Doors",
    "Sector 4 Security 15+ Doors"
    ],
    [
    "Sector 5 Progressive Security Doors",
    "Sector 5 Security 1 Doors",
    "Sector 5 Security 2 Doors",
    "Sector 5 Security 3 Doors",
    "Sector 5 Security 4 Doors",
    "Sector 5 Security 5 Doors",
    "Sector 5 Security 6 Doors",
    "Sector 5 Security 7 Doors",
    "Sector 5 Security 8 Doors",
    "Sector 5 Security 9 Doors",
    "Sector 5 Security 10 Doors",
    "Sector 5 Security 15+ Doors"
    ],
    [
    "Sector 6 Progressive Security Doors",
    "Sector 6 Security 1 Doors",
    "Sector 6 Security 2 Doors",
    "Sector 6 Security 3 Doors",
    "Sector 6 Security 4 Doors",
    "Sector 6 Security 5 Doors",
    "Sector 6 Security 6 Doors",
    "Sector 6 Security 7 Doors",
    "Sector 6 Security 8 Doors",
    "Sector 6 Security 9 Doors",
    "Sector 6 Security 10 Doors",
    "Sector 6 Security 15+ Doors"
    ],
    [
    "Sector 7 Progressive Security Doors",
    "Sector 7 Security 1 Doors",
    "Sector 7 Security 2 Doors",
    "Sector 7 Security 3 Doors",
    "Sector 7 Security 4 Doors",
    "Sector 7 Security 5 Doors",
    "Sector 7 Security 6 Doors",
    "Sector 7 Security 7 Doors",
    "Sector 7 Security 8 Doors",
    "Sector 7 Security 9 Doors",
    "Sector 7 Security 10 Doors",
    "Sector 7 Security 15+ Doors"
    ],
    [
    "Sector 8 Progressive Security Doors",
    "Sector 8 Security 1 Doors",
    "Sector 8 Security 2 Doors",
    "Sector 8 Security 3 Doors",
    "Sector 8 Security 4 Doors",
    "Sector 8 Security 5 Doors",
    "Sector 8 Security 6 Doors",
    "Sector 8 Security 7 Doors",
    "Sector 8 Security 8 Doors",
    "Sector 8 Security 9 Doors",
    "Sector 8 Security 10 Doors",
    "Sector 8 Security 15+ Doors"
    ],
    [
    "Sector 9 Progressive Security Doors",
    "Sector 9 Security 1 Doors",
    "Sector 9 Security 2 Doors",
    "Sector 9 Security 3 Doors",
    "Sector 9 Security 4 Doors",
    "Sector 9 Security 5 Doors",
    "Sector 9 Security 6 Doors",
    "Sector 9 Security 7 Doors",
    "Sector 9 Security 8 Doors",
    "Sector 9 Security 9 Doors",
    "Sector 9 Security 10 Doors",
    "Sector 9 Security 15+ Doors"
    ],
    [
    "Sector X Progressive Security Doors",
    "Sector X Security 1 Doors",
    "Sector X Security 2 Doors",
    "Sector X Security 3 Doors",
    "Sector X Security 4 Doors",
    "Sector X Security 5 Doors",
    "Sector X Security 6 Doors",
    "Sector X Security 7 Doors",
    "Sector X Security 8 Doors",
    "Sector X Security 9 Doors",
    "Sector X Security 10 Doors",
    "Sector X Security 15+ Doors"
    ],
]

TerminalDoorGroups: List[str] = [
    "Terminal Doors",
    "Sector 1 Terminal Doors",
    "Sector 2 Terminal Doors",
    "Sector 3 Terminal Doors",
    "Sector 4 Terminal Doors",
    "Sector 5 Terminal Doors",
    "Sector 6 Terminal Doors",
    "Sector 7 Terminal Doors",
    "Sector 8 Terminal Doors",
    "Sector 9 Terminal Doors",
    "Sector X Terminal Doors"
]