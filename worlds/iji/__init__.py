from BaseClasses import Item, ItemClassification, Location, MultiWorld
from worlds.generic.Rules import add_rule, set_rule
from worlds.iji.Rules import can_kill_annihilators, can_rocket_boost, has_weapon_stats, set_rules
from .Items import item_table, create_itempool, create_item, item_groups_table
from .Locations import location_table, location_weapons_table, location_groups_table
from .Regions import create_regions
from .Options import IjiOptions
from worlds.AutoWorld import World, CollectionState

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
    item_name_groups = item_groups_table
    location_name_groups = location_groups_table
    options_dataclass = IjiOptions
    options: IjiOptions

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)

    def create_regions(self):
        create_regions(self, self.options.HealthBalancing.value, self.options.CompactStatItems.value)

    def get_filler_item_name(self) -> str:
        return "Health Pickup"

    def sector_z_allowed(self) -> bool:
        return self.options.EndGoal.value >= self.options.EndGoal.option_sector_z or \
            self.options.PostGameLocations.value >= self.options.PostGameLocations.option_sector_z

    def sector_y_allowed(self) -> bool:
        return self.options.EndGoal.value == self.options.EndGoal.option_sector_y or \
            self.options.PostGameLocations.value == self.options.PostGameLocations.option_sector_y

    def special_trait_locations(self) -> bool:
        return self.options.SpecialTraitItems.value == self.options.SpecialTraitItems.option_locations_only or \
            self.options.SpecialTraitItems.value == self.options.SpecialTraitItems.option_locations_and_items

    def null_driver_allowed(self) -> bool:
        return self.sector_y_allowed() or (self.sector_z_allowed() and \
            (self.options.NullDriverPosterRequirementType.value != \
            self.options.NullDriverPosterRequirementType.option_disabled or \
            self.options.NullDriverRibbonRequirementType.value != \
            self.options.NullDriverRibbonRequirementType.option_disabled))

    def set_rules(self):
        set_rules(self)
        if self.options.EndGoal.value == self.options.EndGoal.option_sector_x:
            self.multiworld.completion_condition[self.player] = lambda state: \
                state.can_reach_region("Sector X", self.player)
        elif self.options.EndGoal.value == self.options.EndGoal.option_sector_z:
            self.multiworld.completion_condition[self.player] = lambda state: \
                state.can_reach_region("Sector Z", self.player)
        elif self.options.EndGoal.value == self.options.EndGoal.option_sector_y:
            self.multiworld.completion_condition[self.player] = lambda state: \
                state.can_reach_region("Sector Y", self.player)