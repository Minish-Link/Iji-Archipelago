import logging
from typing import Callable, Dict, List, TYPE_CHECKING, NamedTuple
from BaseClasses import MultiWorld, Region, Entrance, CollectionState
from worlds.generic.Rules import CollectionRule

from .Locations import IjiLocation, events_and_locations
from .Data.RegData import region_exit_table
from .Data.LocData import IjiLocData

if TYPE_CHECKING:
    from . import IjiWorld

def create_regions(world: "IjiWorld"):
    
    existing_regions: List[str] = []
    create_region(world, "Menu", existing_regions)


def create_region(world: "IjiWorld", name: str, existing_regions: List[str]) -> Region:

    temp_region = Region(name, world.player, world.multiworld)
    temp_region.add_locations(
        {
            location_name: location_data.code for location_name, location_data in events_and_locations.items()
            if location_data.region == temp_region.name and location_data.valid(world)
        }, IjiLocation
    )

    world.multiworld.regions.append(temp_region)
    existing_regions.append(name)

    for key, exit_data in region_exit_table[name].items():
        if exit_data.valid(world):
            #logging.warning(f"Connected {name} to {key}")
            if key not in existing_regions:
                exit_region = create_region(world, key, existing_regions)
            else:
                exit_region = world.get_region(key)

            temp_region.connect(exit_region, None, lambda state, tempdata=exit_data: (tempdata.logic(world, state)))
            
    return temp_region