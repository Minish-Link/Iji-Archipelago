from typing import Callable, Dict, Mapping, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import CollectionState, Location
from .Data import LocData, EventData

if TYPE_CHECKING:
    from . import IjiWorld

class IjiLocation(Location):
    game="Iji"

def get_remaining_locations(world: "IjiWorld") -> int:
    total: int = 0
    for loc in world.multiworld.get_unfilled_locations(world.player):
        if events_and_locations[loc.name].code:
            total += 1

    return total

def get_location_names() -> Dict[str, int]:
    names = {name: data.code for name, data in LocData.location_table.items()}

events_and_locations = {
    **LocData.location_table,
    **EventData.event_loc_table
}

location_groups_table = {
    group: locations
    for group in [data.region[:8] for _, data in LocData.locations_sectorcomplete.items()]
    for locations in [[location for location, data in LocData.location_table.items() if data.region[:8] == group]]
}
