import logging
from typing import Any, Dict
from BaseClasses import Item, ItemClassification, Location, MultiWorld
from worlds.generic.Rules import add_rule, set_rule
from .Items import create_itempool, create_item #, item_groups_table
from .Locations import location_groups_table, events_and_locations
from .Data.LocData import location_table
from .Data.ItemData import item_table
from .Regions import create_regions
from .Names import RegNames
from .Options import IjiOptions
from worlds.AutoWorld import World, CollectionState
from Utils import visualize_regions

from .Names import ItemNames

class IjiWorld(World):
    """
    Iji is a freeware action platformer developed by Daniel Remar and released in 2008.
    You play as Iji: a young woman empowered with alien technology and suddenly thrown into the midst of deadly 
    intergalactic conflict... with the fate of humanity in her hands. The game features ten regular levels and several
    extra levels, an in-depth stat system that rewards customisation, an arsenal of powerful alien weaponry and a
    wealth of secrets to discover.
    """ # Description by Ladybunne

    game="Iji"
    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}
    #item_name_groups = item_groups_table
    location_name_groups = location_groups_table
    options_dataclass = IjiOptions
    options: IjiOptions
    explicit_indirect_conditions = False

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)

    def create_regions(self):
        create_regions(self)
        for loc in self.multiworld.get_locations(self.player):
            if events_and_locations[loc.name].locked_item(self) != None:
                loc.place_locked_item(create_item(self, events_and_locations[loc.name].locked_item(self)))

    def get_filler_item_name(self) -> str:
        return ItemNames.Filler[0]

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "ModVersion": 3,
            "ModSemantic": "1.2.0",
            "Goal": self.options.end_goal.value,
            "GoalRibbons": self.options.goal_ribbons.value,
            "GoalPosters": self.options.goal_posters.value,
            "DeathLink": self.options.deathlink.value,
            "DeathLinkDamage": self.options.deathlink_damage.value,
            "SpecialTraits": self.options.special_trait_items.value,
            "SuperchargeLocations": self.options.supercharge_locations.value,
            "NullDriveFactor": self.options.null_drive_factor.value,
            "MusicShuffle": self.options.music_shuffle.value,
            # For Poptracker
            "LogicDifficulty": self.options.logic_difficulty.value,
            "HealthBalancing": self.options.health_balancing.value,
            "PosterLocations": self.options.poster_locations.value,
            "BasicWeaponLocations": self.options.basic_weapon_locations.value,
            "LogbookLocations": self.options.logbook_locations.value,
            "CrackboxLocations": self.options.security_box_locations.value,
            "OverloadLocations": self.options.nano_overload_locations.value
        }

    def generate_early(self):
        if (self.options.goal_posters.value > self.options.end_goal.value):
            self.options.goal_posters.value = self.options.end_goal.value
            logging.warning(f"{self.player_name} required more posters than available sectors.")
            logging.warning(f"Their poster requirement was reduced to {self.options.goal_posters.value}")

    def post_fill(self):
        visualize_regions(self.multiworld.get_region(self.origin_region_name, self.player), "ijiregions.puml")

    def set_rules(self):
        for loc in self.multiworld.get_locations(self.player):
            set_rule(loc, lambda state, temploc=loc: events_and_locations[temploc.name].logic(self, state))

        if self.options.end_goal.value == 3:
            self.multiworld.completion_condition[self.player] = lambda state: (
                state.can_reach_region(RegNames.Sector3_Main[4], self.player)
            )
        elif self.options.end_goal.value == 5:
            self.multiworld.completion_condition[self.player] = lambda state: (
                state.can_reach_region(RegNames.Sector5_Main[8], self.player)
            )
        elif self.options.end_goal.value == 7:
            self.multiworld.completion_condition[self.player] = lambda state: (
                state.can_reach_region(RegNames.Sector7_Main[11], self.player)
            )
        elif self.options.end_goal.value == 9:
            self.multiworld.completion_condition[self.player] = lambda state: (
                state.can_reach_region(RegNames.Sector9_Main[14], self.player)
            )
        elif self.options.end_goal.value == 10:
            self.multiworld.completion_condition[self.player] = lambda state: (
                state.can_reach_region(RegNames.SectorX_Final[6], self.player)
            )
        elif self.options.end_goal.value == 11:
            self.multiworld.completion_condition[self.player] = lambda state: (
                state.can_reach_region(RegNames.SectorZ, self.player)
            )
        elif self.options.end_goal.value == 12:
            self.multiworld.completion_condition[self.player] = lambda state: (
                state.can_reach_region(RegNames.SectorY, self.player)
            )