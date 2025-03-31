import logging
from typing import Any, Dict
from BaseClasses import Item, ItemClassification, Location, MultiWorld
from worlds.generic.Rules import add_rule, set_rule
from .Items import item_table, create_itempool, create_item, item_groups_table
from .Locations import location_table, location_groups_table
from .Regions import create_regions, sector_z_available
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
    explicit_indirect_conditions = False
    max_stats: Dict[str, int]

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

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "ModVersion": 3,
            "APWorldVersion": "1.2.0",
            "Goal": self.options.EndGoal.value,
            "Difficulty": self.options.GameDifficulty.value,
            "DeathLink": self.options.IjiDeathLink.value,
            "DeathLinkDamage": self.options.DeathLinkDamage.value,
            "Compactment": self.options.CompactStatItems.value,
            "SpecialTraits": self.options.SpecialTraitItems.value,
            "NullDriveFactor": self.options.NullDriveFactor.value,
            "SuperchargeHandling": self.options.Supercharges.value,
            "GoalPosters": self.options.GoalPosterLocationsRequired.value,
            "GoalRibbons": self.options.GoalRibbonItemsRequired.value,
            "SectorZPosters": self.options.SectorZPosterLocationsRequired.value,
            "SectorZRibbons": self.options.SectorZRibbonItemsRequired.value,
            "NullDriverPosters": self.options.NullDriverPosterLocationsRequired.value,
            "NullDriverRibbons": self.options.NullDriverRibbonItemsRequired.value,
            "SectorZAvailable": sector_z_available(self),
            "MaxHealth": self.max_stats["Health Stat"],
            "MaxAttack": self.max_stats["Attack Stat"],
            "MaxAssimilate": self.max_stats["Assimilate Stat"],
            "MaxStrength": self.max_stats["Strength Stat"],
            "MaxCrack": self.max_stats["Crack Stat"],
            "MaxTasen": self.max_stats["Tasen Stat"],
            "MaxKomato": self.max_stats["Komato Stat"],
            "MaxSectors": self.max_stats["Sector Access"],
            "MustCompleteSectors": self.options.MustCompleteSectors.value
        }

    def sector_z_allowed(self) -> bool:
        return self.options.EndGoal.value == self.options.EndGoal.option_sector_z or\
            self.options.AllowSectorZLocations or\
            self.options.EndGoal.value == self.options.EndGoal.option_sector_y

    def sector_y_allowed(self) -> bool:
        return self.options.EndGoal.value == self.options.EndGoal.option_sector_y

    def set_rules(self):
        
        compactment: int = self.options.CompactStatItems.value
        for loc in self.multiworld.get_locations(self.player):
            set_rule(loc, lambda state, temploc=loc: location_table[temploc.name].logic(self, state))

        if self.options.EndGoal.value == self.options.EndGoal.options_sector_3:
            self.multiworld.completion_condition[self.player] = lambda state: \
                state.can_reach_region("Sector 3", self.player)
        elif self.options.EndGoal.value == self.options.EndGoal.options_sector_5:
            self.multiworld.completion_condition[self.player] = lambda state: \
                state.can_reach_region("Sector 5", self.player)
        elif self.options.EndGoal.value == self.options.EndGoal.options_sector_7:
            self.multiworld.completion_condition[self.player] = lambda state: \
                state.can_reach_region("Sector 7", self.player)
        elif self.options.EndGoal.value == self.options.EndGoal.options_sector_9:
            self.multiworld.completion_condition[self.player] = lambda state: \
                state.can_reach_region("Sector 9", self.player)
        elif self.options.EndGoal.value == self.options.EndGoal.option_sector_x:
            self.multiworld.completion_condition[self.player] = lambda state: \
                state.can_reach_region("Sector X", self.player)
        elif self.options.EndGoal.value == self.options.EndGoal.option_sector_z:
            self.multiworld.completion_condition[self.player] = lambda state: \
                state.can_reach_region("Sector Z", self.player)
        elif self.options.EndGoal.value == self.options.EndGoal.option_sector_y:
            self.multiworld.completion_condition[self.player] = lambda state: \
                state.can_reach_region("Sector Y", self.player)
    
    def generate_early(self):

        if self.options.EndGoal == self.options.EndGoal.option_sector_y:
            self.max_stats["Sector Access"] = 9
        else:
            self.max_stats["Sector Access"] = max(self.options.EndGoal.value, self.options.NumberOfSectorsAllowed.value) - 1

        stat_cap = (6 - self.options.GameDifficulty.value) * self.max_stats["Sector Access"]

        self.max_stats["Health Stat"] = min(self.options.HealthItems.value, 9, stat_cap)
        if self.options.GameDifficulty.value == self.options.GameDifficulty.option_ultimortal:
            self.max_stats["Attack Stat"] = 0
            self.max_stats["Assimilate Stat"] = 0
            self.max_stats["Strength Stat"] = 0
            self.max_stats["Crack Stat"] = 0
            self.max_stats["Tasen Stat"] = 0
            self.max_stats["Komato Stat"] = 0
        else:
            self.max_stats["Attack Stat"] = min(self.options.AttackItems.value, 9, stat_cap)
            self.max_stats["Assimilate Stat"] = min(self.options.AssimilateItems.value, 9, stat_cap)
            self.max_stats["Strength Stat"] = min(self.options.StrengthItems.value, 9, stat_cap)
            self.max_stats["Crack Stat"] = min(self.options.CrackItems.value, 9, stat_cap)
            self.max_stats["Tasen Stat"] = min(self.options.TasenItems.value, 9, stat_cap)
            self.max_stats["Komato Stat"] = min(self.options.KomatoItems.value, 9, stat_cap)


        totalitems: int = get_early_total_items(self)
        totallocations: int = get_early_total_locations(self)

        logcompacted = False
        logremoved = False
        removalfailed = False               

        while (totalitems > totallocations):
            removeditem = False

            if self.options.ExtraSupercharges.value > 0:
                self.options.ExtraSupercharges.value -= 1
                removeditem = True
                logremoved = True
                totalitems -= 1
            if self.options.HealthItems.value > 9:
                self.options.HealthItems.value -= 1
                removeditem = True
                logremoved = True
                totalitems -= 1
            if self.options.AttackItems.value > 9:
                self.options.AttackItems.value -= 1
                removeditem = True
                logremoved = True
                totalitems -= 1
            if self.options.AssimilateItems.value > 9:
                self.options.AssimilateItems.value -= 1
                removeditem = True
                logremoved = True
                totalitems -= 1
            if self.options.StrengthItems.value > 9:
                self.options.StrengthItems.value -= 1
                removeditem = True
                logremoved = True
                totalitems -= 1
            if self.options.CrackItems.value > 9:
                self.options.CrackItems.value -= 1
                removeditem = True
                logremoved = True
                totalitems -= 1
            if self.options.TasenItems.value > 9:
                self.options.TasenItems.value -= 1
                removeditem = True
                logremoved = True
                totalitems -= 1
            if self.options.KomatoItems.value > 9:
                self.options.KomatoItems.value -= 1
                removeditem = True
                logremoved = True
                totalitems -= 1
            if self.options.SectorAccessItems.value > 9:
                self.options.SectorAccessItems.value -= 1
                removeditem = True
                logremoved = True
                totalitems -= 1
            if sector_z_available(self) and self.options.RibbonItemCount.value > \
                                                max(self.options.SectorZRibbonItemsRequired.value,
                                                    self.options.NullDriverRibbonItemsRequired.value):

                    self.options.RibbonItemCount.value -= 1
                    removeditem = True
                    logremoved = True

            if not removeditem:
                removalfailed = True
                logging.error(f"{self.multiworld.player_name[self.player]} had more progression items in their pool than locations, and the issue couldn't be resolved.")
                break

        if logcompacted and not removalfailed:
            logging.warning(f"{self.multiworld.player_name[self.player]} had more progression items than locations, so their Stat items have been compacted to make room.")

        if logremoved and not removalfailed:
            logging.warning(f"{self.multiworld.player_name[self.player]} had more progression items than locations, so some of their excess items have been removed to make room.")

def get_early_total_items(world: "IjiWorld") -> int:
    totalitems: int = 0
    totalitems += world.options.HealthItems.value
    totalitems += world.options.AttackItems.value
    totalitems += world.options.AssimilateItems.value
    totalitems += world.options.StrengthItems.value
    totalitems += world.options.CrackItems.value
    totalitems += world.options.TasenItems.value
    totalitems += world.options.KomatoItems.value
    totalitems += world.options.SectorAccessItems.value
    if world.options.SuperchargePointHandling.value == 2:
        totalitems += world.max_stats["Sector Access"]
    totalitems += world.options.ExtraSupercharges.value
    if world.options.SpecialTraitItems.value:
        totalitems += 7
    if sector_z_available(world) and (world.options.SectorZRibbonItemsRequired.value > 0 or world.options.NullDriverRibbonItemsRequired.value > 0):
        totalitems += max(world.options.SectorZRibbonItemsRequired.value, world.options.NullDriverRibbonItemsRequired.value, world.options.RibbonItemCount)
    return totalitems

def get_early_total_locations(world: "IjiWorld") -> int:
    totallocations: int = 0
    for data in location_table.values():
        if (data.valid(world)):
            totallocations+=1

    return totallocations

def get_ribbons_required(world: "IjiWorld") -> int:
    if sector_z_available(world):
        return min(world.options.SectorZRibbonItemsRequired.value,
                   world.options.NullDriverRibbonItemsRequired.value,
                   world.options.GoalRibbonItemsRequired.value)
    else:
        return world.options.GoalRibbonItemsRequired.value