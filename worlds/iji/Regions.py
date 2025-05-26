import logging
from typing import Callable, Dict, List, TYPE_CHECKING, NamedTuple
from BaseClasses import MultiWorld, Region, Entrance, CollectionState
from worlds.generic.Rules import CollectionRule

from .Locations import IjiLocation, events_and_locations
from .Data.RegData import region_exit_table

if TYPE_CHECKING:
    from . import IjiWorld

def create_regions(world: "IjiWorld"):
    
    existing_regions: List[str] = []
    create_region(world, "Menu", existing_regions)



def create_region(world: "IjiWorld", name: str, existing_regions: List[str]) -> Region:

    tempregion = Region(name, world.player, world.multiworld)
    tempregion.add_locations(
        {
            location_name: location_data.code for location_name, location_data in events_and_locations.items()
            if location_data.region == tempregion.name and location_data.valid(world)
        }, IjiLocation
    )

    exitregion: Region = None
    world.multiworld.regions.append(tempregion)
    existing_regions.append(name)

    for key, exitdata in region_exit_table[name].items():
        if (exitdata.valid(world)):
            #logging.warning(f"Connected {name} to {key}")
            if key not in existing_regions:
                exitregion = create_region(world, key, existing_regions)
            else:
                exitregion = world.get_region(key)

            tempregion.connect(exitregion, None, lambda state, tempdata=exitdata: (tempdata.logic(world, state)))
            
    return tempregion