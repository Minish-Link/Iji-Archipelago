from typing import Any

map_pages = {
    "World": 0,
    "Sector1": 1,
    "Sector2": 2,
    "Sector3": 3,
    "Sector4": 4,
    "Sector5": 5,
    "Sector6": 6,
    "Sector7": 7,
    "Sector8": 8,
    "Sector9": 9,
    "DeepSector": 10,
    "SectorX": 11,
    "SectorZ": 12,
    "SectorY": 13
}

def map_page_index(data: Any):
    return map_pages[data] if (data in map_pages) else 0