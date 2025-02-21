from BaseClasses import Item, ItemClassification, Location, MultiWorld
from worlds.generic.Rules import add_rule, set_rule
from worlds.iji.Rules import can_kill_annihilators, can_rocket_boost, has_weapon_stats
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
        create_regions(self)

        

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
        return self.sector_y_allowed(self) or (self.sector_z_allowed and \
            (self.options.NullDriverPosterRequirementType.value != \
            self.options.NullDriverPosterRequirementType.option_disabled or \
            self.options.NullDriverRibbonRequirementType.value != \
            self.options.NullDriverRibbonRequirementType.option_disabled))

    def set_rules(self):
        # Special Trait Locations
        try:
            set_rule(self.get_location("Reach Health Level 10"),
                     lambda state: state.has("Health Stat", self.player, 9))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Reach Attack Level 10"),
                     lambda state: state.has("Attack Stat", self.player, 9))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Reach Assimilate Level 10"),
                     lambda state: state.has("Assimilate Stat", self.player, 9))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Reach Strength Level 10"),
                     lambda state: state.has("Strength Stat", self.player, 9))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Reach Crack Level 10"),
                     lambda state: state.has("Crack Stat", self.player, 9))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Reach Tasen Level 10"),
                     lambda state: state.has("Tasen Stat", self.player, 9))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Reach Komato Level 10"),
                     lambda state: state.has("Komato Stat", self.player, 9))
        except KeyError:
            pass

        # Supercharge Locations
        try:
            set_rule(self.get_location("Sector 2 - Supercharge"), # Return trip after jump upgrade
                     lambda state: has_weapon_stats(state, "Rocket Launcher", self.player))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Sector 3 - Supercharge"), # Behind suspended strength door
                     lambda state: has_weapon_stats(state, "Hyper Pulse Cannon", self.player))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Sector 5 - Supercharge"), # Nuka Asha
                     lambda state: has_weapon_stats(state, "Nuke", self.player))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Sector 6 - Supercharge"), # Behind suspended Glass
                     lambda state: has_weapon_stats(state, "Splintergun", self.player) or # Splintergun
                         has_weapon_stats(state, "Nuke", self.player) or # Nuke
                         (state.has_all_counts({"Tasen Stat": 9, "Komato Stat": 9}) and # Retribution (Obscure)
                          can_rocket_boost(state, self.player) and 
                          self.options.LogicDifficulty.value >= self.options.LogicDifficulty.option_obscure) or
                          (has_weapon_stats(state, "Shocksplinter", self.player) and # Splinter projectiles (Extreme)
                           self.options.LogicDifficulty.value == self.options.LogicDifficulty.option_extreme)) 
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Sector 7 - Supercharge"), # Destroy Sentinel Proxima without Electric Pads
                     lambda state: has_weapon_stats(state, "MPFB Devastator", self.player) and
                     state.has_all_counts({"Attack Stat": 9, "Health Stat": 10, "Assimilate Stat": 3}))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Sector 8 - Supercharge"), # Kick turret into Staff Storage
                     lambda state: can_kill_annihilators(state, self.player))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Sector X - Supercharge"), # Destroy Core
                     lambda state: has_weapon_stats(state, "Velocithor", self.player))
        except KeyError:
            pass

        #Logbooks
        try:
            set_rule(self.get_location("Sector 3 - Logbook 15"),
                     lambda state: state.has("Strength Stat", self.player, 1))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Sector 4 - Logbook 12"),
                     lambda state: state.has("Strength Stat", self.player, 5))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Sector 8 - Logbook 15"),
                     lambda state: state.has("Strength Stat", self.player, 4))
        except KeyError:
            pass
        try:
            set_rule(self.get_location("Sector 9 - Logbook 15"),
                     lambda state: has_weapon_stats(state, "Hyper Pulse Cannon", self.player) and
                     state.has("Strength Stat", self.player, 4))
        except KeyError:
            pass

        #Weapons
        for name, data in location_weapons_table.items():
            # Special Cases
            if name == "Sector 3 - Pulse Cannon":
                try:
                    set_rule(self.get_location("Sector 3 - Pulse Cannon"),
                             lambda state: has_weapon_stats(state, "Pulse Cannon", self.player) and
                             state.has("Crack Stat", self.player, 1))
                except KeyError:
                    continue
            elif name == "Sector 6 - MPFB Devastator 2/2":
                try:
                    set_rule(self.get_location("Sector 6 - MPFB Devastator 2/2"),
                             lambda state: has_weapon_stats(state, "MPFB Devastator", self.player) and
                             state.has("Crack Stat", self.player, 3))
                except KeyError:
                    continue
            elif name == "Sector 6 - Cyclic Fusion Ignition System":
                try:
                    set_rule(self.get_location("Sector 6 - Cyclic Fusion Ignition System"),
                             lambda state: has_weapon_stats(state, "CFIS", self.player) and
                             state.has("Crack Stat", self.player, 3))
                except KeyError:
                    continue
            elif name == "Sector X - MPFB Devastator 4/4":
                try: set_rule(self.get_location("Sector X - MPFB Devastator 4/4"),
                              lambda state: has_weapon_stats(state, "CFIS", self.player) and
                              state.has("Strength Stat", self.player, 6))
                except KeyError:
                    continue

            # The rest of the weapons
            else:
                try: set_rule(self.get_location(name),
                              lambda state: has_weapon_stats(state, data.weapon, self.player))
                except KeyError:
                    continue

    