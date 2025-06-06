from typing import List

Weapons: List[str] = [
    "Has Null Driver",
    "Has Shotgun",
    "Has Machine Gun",
    "Has Rocket Launcher",
    "Has MPFB Devastator",
    "Has Resonance Detonator",
    "Has Pulse Cannon",
    "Has Shocksplinter",
    "Has Cyclic Fusion Ignition System",
    "Has Buster Gun",
    "Has Splintergun",
    "Has Spread Rockets",
    "Has Nuke",
    "Has Resonance Reflector",
    "Has Hyper Pulse",
    "Has Plasma Cannon",
    "Has Velocithor V2-10",
    "Has Banana Gun",
    "Has Massacre"
]

Weapon_Locations: List[List[List[str]]] = [
[["Sector 1 - Got Machine Gun"]],

[["Sector 2 - Got Machine Gun"],
 ["Sector 2 - Got Rocket Launcher"],
 ["Sector 2 - Got Resonance Detonator"]],

[["Sector 3 - Got Machine Gun 1/3","Sector 3 - Got Machine Gun 2/3","Sector 3 - Got Machine Gun 3/3"],
 ["Sector 3 - Got Rocket Launcher 1/2","Sector 3 - Got Rocket Launcher 2/2"],
 ["Sector 3 - Got Resonance Detonator"],
 ["Sector 3 - Got Pulse Cannon"]],

[["Sector 4 - Got Machine Gun"],
 ["Sector 4 - Got Rocket Launcher 1/2","Sector 4 - Got Rocket Launcher 2/2"],
 ["Sector 4 - Got MPFB Devastator"],
 ["Sector 4 - Got Resonance Detonator"],
 ["Sector 4 - Got Pulse Cannon"]],

[["Sector 5 - Got Machine Gun 1/2","Sector 5 - Got Machine Gun 2/2"],
 ["Sector 5 - Got Rocket Launcher 1/2","Sector 5 - Got Rocket Launcher 2/2"],
 ["Sector 5 - Got MPFB Devastator"],
 ["Sector 5 - Got Resonance Detonator"],
 ["Sector 5 - Got Pulse Cannon 1/3","Sector 5 - Got Pulse Cannon 2/3","Sector 5 - Got Pulse Cannon 3/3"],
 ["Sector 5 - Got Shocksplinter"]],

[["Sector 6 - Got Machine Gun 1/2","Sector 6 - Got Machine Gun 2/2"],
 ["Sector 6 - Got Rocket Launcher 1/3","Sector 6 - Got Rocket Launcher 2/3","Sector 6 - Got Rocket Launcher 3/3"],
 ["Sector 6 - Got MPFB Devastator 1/2","Sector 6 - Got MPFB Devastator 2/2"],
 ["Sector 6 - Got Resonance Detonator"],
 ["Sector 6 - Got Pulse Cannon 1/2","Sector 6 - Got Pulse Cannon 2/2"],
 ["Sector 6 - Got Shocksplinter 1/3","Sector 6 - Got Shocksplinter 2/3","Sector 6 - Got Shocksplinter 3/3"],
 ["Sector 6 - Got Cyclic Fusion Ignition System"]],

[["Sector 7 - Got Machine Gun"],
 ["Sector 7 - Got Rocket Launcher 1/3","Sector 7 - Got Rocket Launcher 2/3","Sector 7 - Got Rocket Launcher 3/3"],
 ["Sector 7 - Got MPFB Devastator"],
 ["Sector 7 - Got Resonance Detonator 1/2","Sector 7 - Got Resonance Detonator 2/2"],
 ["Sector 7 - Got Pulse Cannon 1/2","Sector 7 - Got Pulse Cannon 2/2"],
 ["Sector 7 - Got Shocksplinter 1/3","Sector 7 - Got Shocksplinter 2/3","Sector 7 - Got Shocksplinter 3/3"],
 ["Sector 7 - Got Cyclic Fusion Ignition System"]],

[["Sector 8 - Got Machine Gun"],
 ["Sector 8 - Got Rocket Launcher 1/3","Sector 8 - Got Rocket Launcher 2/3","Sector 8 - Got Rocket Launcher 3/3"],
 ["Sector 8 - Got MPFB Devastator"],
 ["Sector 8 - Got Resonance Detonator"],
 ["Sector 8 - Got Pulse Cannon 1/2","Sector 8 - Got Pulse Cannon 2/2"],
 ["Sector 8 - Got Shocksplinter 1/2","Sector 8 - Got Shocksplinter 2/2"],
 ["Sector 8 - Got Cyclic Fusion Ignition System"]],

[["Sector 9 - Got Machine Gun 1/4","Sector 9 - Got Machine Gun 2/4","Sector 9 - Got Machine Gun 3/4","Sector 9 - Got Machine Gun 4/4"],
 ["Sector 9 - Got Rocket Launcher 1/5","Sector 9 - Got Rocket Launcher 2/5","Sector 9 - Got Rocket Launcher 3/5","Sector 9 - Got Rocket Launcher 4/5","Sector 9 - Got Rocket Launcher 5/5"],
 ["Sector 9 - Got MPFB Devastator 1/4","Sector 9 - Got MPFB Devastator 2/4","Sector 9 - Got MPFB Devastator 3/4","Sector 9 - Got MPFB Devastator 4/4"],
 ["Sector 9 - Got Resonance Detonator 1/4","Sector 9 - Got Resonance Detonator 2/4","Sector 9 - Got Resonance Detonator 3/4","Sector 9 - Got Resonance Detonator 4/4"],
 ["Sector 9 - Got Pulse Cannon 1/4","Sector 9 - Got Pulse Cannon 2/4","Sector 9 - Got Pulse Cannon 3/4","Sector 9 - Got Pulse Cannon 4/4"],
 ["Sector 9 - Got Shocksplinter 1/4","Sector 9 - Got Shocksplinter 2/4","Sector 9 - Got Shocksplinter 3/4","Sector 9 - Got Shocksplinter 4/4"],
 ["Sector 9 - Got Cyclic Fusion Ignition System 1/3","Sector 9 - Got Cyclic Fusion Ignition System 2/3","Sector 9 - Got Cyclic Fusion Ignition System 3/3"]],

[["Sector X - Got Machine Gun 1/3","Sector X - Got Machine Gun 2/3","Sector X - Got Machine Gun 3/3"],
 ["Sector X - Got Rocket Launcher 1/3","Sector X - Got Rocket Launcher 2/3","Sector X - Got Rocket Launcher 3/3"],
 ["Sector X - Got MPFB Devastator 1/4","Sector X - Got MPFB Devastator 2/4","Sector X - Got MPFB Devastator 3/4","Sector X - Got MPFB Devastator 4/4"],
 ["Sector X - Got Resonance Detonator 1/2","Sector X - Got Resonance Detonator 2/2"],
 ["Sector X - Got Pulse Cannon 1/4","Sector X - Got Pulse Cannon 2/4","Sector X - Got Pulse Cannon 3/4","Sector X - Got Pulse Cannon 4/4"],
 ["Sector X - Got Shocksplinter 1/3","Sector X - Got Shocksplinter 2/3","Sector X - Got Shocksplinter 3/3"],
 ["Sector X - Got Cyclic Fusion Ignition System 1/4","Sector X - Got Cyclic Fusion Ignition System 2/4","Sector X - Got Cyclic Fusion Ignition System 3/4","Sector X - Got Cyclic Fusion Ignition System 4/4"],
 ["Sector X - Got Resonance Reflector"]]
]

Supercharges: List[str] = [
    "Has Sector 1 Supercharge",
    "Has Sector 2 Supercharge",
    "Has Sector 3 Supercharge",
    "Has Sector 4 Supercharge",
    "Has Sector 5 Supercharge",
    "Has Sector 6 Supercharge",
    "Has Sector 7 Supercharge",
    "Has Sector 8 Supercharge",
    "Has Sector 9 Supercharge",
    "Has Sector X Supercharge"
]

Posters: List[str] = [
    "Found Poster",
    "Found Sector 1 Poster",
    "Found Sector 2 Poster",
    "Found Sector 3 Poster",
    "Found Sector 4 Poster",
    "Found Sector 5 Poster",
    "Found Sector 6 Poster",
    "Found Sector 7 Poster",
    "Found Sector 8 Poster",
    "Found Sector 9 Poster",
    "Found Sector X Poster"
]

XP: List[List[str]] = [
    ["1-4 XP",
     "1-8 XP",
     "1-16 XP",
     "1-32 XP",
     "1-64 XP",
     "1-128 XP"],
    ["2-4 XP",
     "2-8 XP",
     "2-16 XP",
     "2-32 XP",
     "2-64 XP",
     "2-128 XP"],
    ["3-4 XP",
     "3-8 XP",
     "3-16 XP",
     "3-32 XP",
     "3-64 XP",
     "3-128 XP"],
    ["4-4 XP",
     "4-8 XP",
     "4-16 XP",
     "4-32 XP",
     "4-64 XP",
     "4-128 XP"],
    ["5-4 XP",
     "5-8 XP",
     "5-16 XP",
     "5-32 XP",
     "5-64 XP",
     "5-128 XP"],
    ["6-4 XP",
     "6-8 XP",
     "6-16 XP",
     "6-32 XP",
     "6-64 XP",
     "6-128 XP"],
    ["7-4 XP",
     "7-8 XP",
     "7-16 XP",
     "7-32 XP",
     "7-64 XP",
     "7-128 XP"],
    ["8-4 XP",
     "8-8 XP",
     "8-16 XP",
     "8-32 XP",
     "8-64 XP",
     "8-128 XP"],
    ["9-4 XP",
     "9-8 XP",
     "9-16 XP",
     "9-32 XP",
     "9-64 XP",
     "9-128 XP"],
    ["X-4 XP",
     "X-8 XP",
     "X-16 XP",
     "X-32 XP",
     "X-64 XP",
     "X-128 XP"],
]

XP_Sector: List[List[str]] = [
    [
        "S1 Tutorial XP",
        "S1 UM XP 1",
        "S1 UM XP 2",
        "S1 GP XP",
        "S1 Armory XP",
        "S1 End XP"
    ],
    [
        "S2 Supplies XP",
        "S2 ST Box XP",
        "S2 DO XP 1",
        "S2 DO XP 2",
        "S2 MB XP",
        "S2 HDO XP",
        "S2 STT XP 1",
        "S2 STT XP 2",
        "S2 MAT XP",
        "S2 MAT Box XP",
        "S2 SS XP",
        "S2 SS Box XP",
        "S2 End XP",
        "S2 SR XP"
    ],
    [
        "S3 SWDL XP",
        "S3 SWDL Box XP",
        "S3 SWDR XP",
        "S3 SWDFR XP",
        "S3 Start XP",
        "S3 Start Box XP",
        "S3 Main XP 1",
        "S3 Main XP 2",
        "S3 Komato XP",
        "S3 Pulse XP",
        "S3 Maeja XP",
        "S3 Rec XP",
        "S3 Storage XP"
    ],
    [
        "S4 SC XP",
        "S4 MSH XP 1",
        "S4 MSH XP 2",
        "S4 MSHC XP",
        "S4 MSHR XP",
        "S4 MSTS XP",
        "S4 MS XP 1",
        "S4 MS XP 2",
        "S4 MSO XP",
        "S4 MST XP",
        "S4 RSA XP",
        "S4 RSA Box XP",
        "S4 Core XP",
        "S4 End XP",
        "S4 End2 XP"
    ],
    [
        "S5 Start XP",
        "S5 Start2 XP",
        "S5 SR Box XP",
        "S5 Main1 XP",
        "S5 Main2 XP",
        "S5 P1 XP",
        "S5 P2 XP",
        "S5 CMC1 XP",
        "S5 CMC2 XP",
        "S5 CMS XP",
        "S5 JU XP",
        "S5 BJU XP"
    ],
    [
        "S6 SC Enemy1 XP",
        "S6 SC Enemy2 XP",
        "S6 SCT XP",
        "S6 SNA XP",
        "S6 VS XP",
        "S6 VSS XP",
        "S6 NWS XP",
        "S6 Ele XP",
        "S6 NWR Bot XP",
        "S6 NWR Top XP 1",
        "S6 NWR Top XP 2",
        "S6 NWR Side XP",
        "S6 GRA XP",
        "S6 GRA Top XP",
        "S6 P XP",
        "S6 CFIS XP",
        "S6 USL XP",
        "S6 USR XP",
        "S6 BOL XP",
        "S6 BOR XP",
        "S6 NWC XP",
        "S6 EL XP",
        "S6 ET XP"
    ],
    [
        "S7 NWS 1 XP",
        "S7 NWS 2 XP",
        "S7 ETA XP",
        "S7 ETA Top XP",
        "S7 ARM 1 XP",
        "S7 ARM 2 XP",
        "S7 ASS XP",
        "S7 CFIS XP",
        "S7 CFIS XP",
        "S7 MGA XP",
        "S7 IS XP",
        "S7 ISTL XP",
        "S7 ISTR XP",
        "S7 DP XP",
        "S7 PHC XP",
        "S7 AH XP",
        "S7 RT XP",
        "S7 RTS XP",
        "S7 R XP"
    ],
    [
        "S8 XQX XP",
        "S8 XQX T XP",
        "S8 XQX TR XP",
        "S8 XQX TS XP",
        "S8 SS XP",
        "S8 SS2 XP",
        "S8 SS Anni XP",
        "S8 SSRT XP",
        "S8 SS Box XP",
        "S8 R1 XP",
        "S8 R2 XP",
        "S8 R3 XP",
        "S8 R Anni XP",
        "S8 RSR1 XP",
        "S8 RSR2 XP"
    ],
    [
        "S9 1 XP",
        "S9 GPL Box XP",
        "S9 GP XP",
        "S9 MA Top XP",
        "S9 MA Bot XP",
        "S9 Q XP",
        "S9 SSU1 XP",
        "S9 SSU2 XP",
        "S9 SSU Anni XP",
        "S9 BHA XP",
        "S9 BHB XP",
        "S9 BHC XP",
        "S9 BHD XP",
        "S9 HGO XP",
        "S9 IGS XP",
        "S9 MSS XP",
        "S9 HGOR XP",
        "S9 BRB XP",
        "S9 MCR XP",
        "S9 MCR Anni XP",
        "S9 MCR TR XP",
        "S9 MCR TL XP",
        "S9 BNK XP",
        "S9 DS1 XP",
        "S9 DS2 XP"
    ],
    [
        "SX DA XP", # 0
        "SX DA Anni XP",
        "SX DLR XP",
        "SX DLAB XP", # 3
        "SX VS XP",
        "SX ET XP",
        "SX IL XP", # 6
        "SX IL Anni XP",
        "SX MCC XP",
        "SX MCCB XP", # 9
        "SX MR Box XP",
        "SX MR TL XP",
        "SX MR ML XP", # 12
        "SX MR B XP",
        "SX MR MR XP",
        "SX MR TR XP", # 15
        "SX ARM XP",
        "SX HL1 XP",
        "SX HL1 Anni XP", # 18
        "SX HL1R XP",
        "SX HL2 XP",
        "SX HL3 XP", # 21
        "SX HL3L XP",
        "SX Final1 XP",
        "SX Final2 XP", # 24
        "SX Final Anni XP"
    ]
]

Levels: List[str] = [
    "Stat Point",
    "Reached Level 1",
    "Reached Level 2",
    "Reached Level 3",
    "Reached Level 4",
    "Reached Level 5",
    "Reached Level 6",
    "Reached Level 7",
    "Reached Level 8",
    "Reached Level 9",
    "Reached Level 10",
    "Reached Level 11",
    "Reached Level 12",
    "Reached Level 13",
    "Reached Level 14",
    "Reached Level 15",
    "Reached Level 16",
    "Reached Level 17",
    "Reached Level 18",
    "Reached Level 19",
    "Reached Level 20",
    "Reached Level 21",
    "Reached Level 22",
    "Reached Level 23",
    "Reached Level 24",
    "Reached Level 25",
    "Reached Level 26",
    "Reached Level 27",
    "Reached Level 28",
    "Reached Level 29",
    "Reached Level 30",
    "Reached Level 31",
    "Reached Level 32",
    "Reached Level 33",
    "Reached Level 34",
    "Reached Level 35",
    "Reached Level 36",
    "Reached Level 37",
    "Reached Level 38",
    "Reached Level 39",
    "Reached Level 40",
    "Reached Level 41",
    "Reached Level 42",
    "Reached Level 43",
    "Reached Level 44",
    "Reached Level 45",
    "Reached Level 46",
    "Reached Level 47",
    "Reached Level 48",
    "Reached Level 49",
    "Reached Level 50",
]

Sector4_Terminals = "Sector 4 Shaft Terminals"
Sector6_Shredders = "Sector 6 Top Shredders"
Sector6_Terminal_Poster = "Sector 6 Poster Terminal"
Sector6_Terminal_BlackOps = "Sector 6 Black Ops Terminal"
Sector6_Terminal_Ribbon = "Sector 6 Ribbon Terminal"
Sector7_Terminal_CFIS = "Sector 7 CFIS Terminal"
Sector8_Terminal_AnnihilatorBeta = "Sector 8 Annihilator Beta Terminal"
Sector9_Bulkhead: List[str] = [
    "Sector 9 Bulkhead A",
    "Sector 9 Bulkhead B",
    "Sector 9 Bulkhead C",
    "Sector 9 Bulkhead D"
]
SectorX_Terminal_Megacore: List[str] = [
    "Sector X Megacore Terminal Left",
    "Sector X Megacore Terminal Right",
    "Sector X Icarus Exit"
]
SectorX_Megacore = "Sector X Megacore Destroyed"

Victory = "Victory!"

# Unlocked Doors: List[List[str]] = [[]]