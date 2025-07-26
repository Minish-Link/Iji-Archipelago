from typing import Any

map_pages = {
    "Sector1": 0,
    "Sector2": 1,
    "Sector3": 2,
    "Sector4": 3,
    "Sector5": 4,
    "Sector6": 5,
    "Sector7": 6,
    "Sector8": 7,
    "Sector9": 8,
    "DeepSector": 9,
    "SectorX": 10,
    "SectorZ": 11,
    "SectorY": 12
}

def map_page_index(data: Any):
    return map_pages[data] if (data in map_pages) else 0