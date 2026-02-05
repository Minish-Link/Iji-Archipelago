import logging
from typing import Any, Dict, List
from BaseClasses import Item, ItemClassification, Location, MultiWorld, Tutorial
from worlds.generic.Rules import add_rule, set_rule
from .Data.DoorData import DoorData, shuffle_doors, Door_Levels
from .Items import create_item_pool, create_item, item_groups_table, IjiItem
from .Locations import events_and_locations, location_groups_table
from .Data.LocData import location_table
from .Data.ItemData import item_table
from .Regions import create_regions
from .Names import RegNames, EventNames, ItemNames
from .Options import (IjiOptions, iji_option_groups, define_health_balancing, get_shuffled_music,
                      weapon_requirements_to_slot_data,
                      get_weapon_requirements_from_slot_data)
from worlds.AutoWorld import WebWorld, World, CollectionState
from .Maps.map_page_index import map_page_index
from .Rules import WeaponData
#from Utils import visualize_regions


class IjiWeb(WebWorld):
    theme = "dirt"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Iji randomizer connected to an Archipelago Multiworld",
        "English",
        "setup_en.md",
        "setup/en",
        ["Minish"]
    )]
    option_groups = iji_option_groups

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
    web = IjiWeb()

    health_balancing_values: List[int]
    weapon_stats_needed: Dict[str, WeaponData]
    max_stats: Dict[str, int]
    compact_stats: Dict[str, int]
    current_stat_items: Dict[str, int]
    starting_stats: Dict[str, int]
    door_stats: Dict[int, DoorData]
    total_posters: int = 0
    post_goal_locations: int = 0

    # on_added location functions
    def increment_total_posters(self):
        self.total_posters += 1
    def add_max_stats(self, stat_name: str, count: int):
        self.max_stats[stat_name] += count
    def increment_post_goal_locations(self):
        self.post_goal_locations += 1

    ut_can_gen_without_yaml = True
    glitches_item_name = ItemNames.Glitch

    tracker_world = {
        "map_page_folder": "Maps",
        "map_page_maps": "maps.json",
        "map_page_locations": "locations.json",
        "map_page_index": map_page_index
    }


    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def initialize_stat_dicts(self):
        self.compact_stats = {
        ItemNames.Stat_Health: 1,
        ItemNames.Stat_Attack: 1,
        ItemNames.Stat_Assimilate: 1,
        ItemNames.Stat_Strength: 1,
        ItemNames.Stat_Crack: 1,
        ItemNames.Stat_Tasen: 1,
        ItemNames.Stat_Komato: 1,
        ItemNames.Supercharge: 1
        }
        self.max_stats = {
        ItemNames.Stat_Health: 9,
        ItemNames.Stat_Attack: 9,
        ItemNames.Stat_Assimilate: 9,
        ItemNames.Stat_Strength: 9,
        ItemNames.Stat_Crack: 9,
        ItemNames.Stat_Tasen: 9,
        ItemNames.Stat_Komato: 9,
        ItemNames.Supercharge: 0
        }
        self.current_stat_items = {
        ItemNames.Stat_Health: 0,
        ItemNames.Stat_Attack: 0,
        ItemNames.Stat_Assimilate: 0,
        ItemNames.Stat_Strength: 0,
        ItemNames.Stat_Crack: 0,
        ItemNames.Stat_Tasen: 0,
        ItemNames.Stat_Komato: 0,
        ItemNames.Supercharge: 0
        }
        self.starting_stats = {
        ItemNames.Stat_Health: 0,
        ItemNames.Stat_Attack: 0,
        ItemNames.Stat_Assimilate: 0,
        ItemNames.Stat_Strength: 0,
        ItemNames.Stat_Crack: 0,
        ItemNames.Stat_Tasen: 0,
        ItemNames.Stat_Komato: 0,
        ItemNames.Supercharge: 0
        }
        self.weapon_stats_needed = {
        ItemNames.Weapons[0]: WeaponData(), # Null Driver
        ItemNames.Weapons[1]: WeaponData(), # Shotgun
        ItemNames.Weapons[2]: WeaponData(tasen=2), # Machine Gun
        ItemNames.Weapons[3]: WeaponData(tasen=5), # Rocket Launcher
        ItemNames.Weapons[4]: WeaponData(tasen=9), # MPFB Devastator
        ItemNames.Weapons[5]: WeaponData(), # Resonance Detonator
        ItemNames.Weapons[6]: WeaponData(komato=2), # Pulse Cannon
        ItemNames.Weapons[7]: WeaponData(komato=5), # Shocksplinter
        ItemNames.Weapons[8]: WeaponData(komato=9), # Cyclic Fusion Ignition System
        ItemNames.Weapons[9]: WeaponData(tasen=2,crack=2), # Buster Gun
        ItemNames.Weapons[10]: WeaponData(tasen=2,komato=5,crack=6), # Splintergun
        ItemNames.Weapons[11]: WeaponData(tasen=5,crack=4), # Spread Rockets
        ItemNames.Weapons[12]: WeaponData(tasen=9,crack=8), # Nuke
        ItemNames.Weapons[13]: WeaponData(crack=3), # Resonance Reflector
        ItemNames.Weapons[14]: WeaponData(komato=2,crack=5), # Hyperpulse
        ItemNames.Weapons[15]: WeaponData(komato=5,crack=7), # Plasma Cannon
        ItemNames.Weapons[16]: WeaponData(tasen=9,komato=9,crack=9), # Velocithor V2-10
        ItemNames.Weapons[17]: WeaponData(tasen=9, komato=9) # Banana Gun
        }
        self.door_stats = Door_Levels

    def create_items(self):
        self.multiworld.itempool += create_item_pool(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)

    def create_regions(self):
        create_regions(self)
        for loc in self.multiworld.get_locations(self.player):
            if events_and_locations[loc.name].locked_item(self) is not None:
                loc.place_locked_item(create_item(self, events_and_locations[loc.name].locked_item(self)))
            events_and_locations[loc.name].on_added(self)


    def get_filler_item_name(self) -> str:
        return ItemNames.Filler[0]

    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "ModVersion": 4,
            "ModSemantic": "1.3.0",

            "Goal": self.options.end_goal.value,
            "GoalPosters": self.options.goal_posters.value,
            "GoalRibbons": self.options.goal_ribbons.value,
            "RibbonCount": self.options.ribbon_items.value,
            "SectorZPostGame": self.options.allow_sector_z.value,

            "GameDifficulty": self.options.game_difficulty.value,
            "LogicDifficulty": self.options.logic_difficulty.value,
            "OutOfOrderSectors": self.options.out_of_order_sectors.value,
            "HealthBalancing": self.health_balancing_values,
            "EnforceHealthBalancing": self.options.enforce_health_balancing.value,

            "PosterLocations": self.options.poster_locations.value,
            "SuperchargeLocations": self.options.supercharge_locations.value,
            "BasicWeaponLocations": self.options.basic_weapon_locations.value,
            "LogbookLocations": self.options.logbook_locations.value,
            "CrackBoxLocations": self.options.security_box_locations.value,
            "OverloadLocations": self.options.nano_overload_locations.value,
            "EnemyLocations": self.options.enemy_locations.value,
            "MoreEnemies": self.options.more_enemies.value,
            "EnemyLocationTypes": self.options.enemy_location_types.get_slot_data(),

            "SpecialTraits": self.options.special_trait_items.value,
            "JumpUpgrades": self.options.jump_upgrades.value,
            "ArmorUpgrades": self.options.armor_upgrades.value,
            "Levelsanity": self.options.levelsanity.value,
            "FireAnytime": self.options.debug_item.value,
            "CompactStats": self.compact_stats,
            "StartingStats": self.starting_stats,

            "NullDriveFactor": self.options.null_drive_factor.value,

            # TODO: Convert shuffled door data into something that can be passed into slot data
            #"DoorShuffle": self.options.door_shuffle.value,
            #"WeaponStats": weapon_requirements_to_slot_data(self),


            "DeathLink": self.options.deathlink.value,
            "DeathLinkDamage": self.options.deathlink_damage.value,
            "MusicShuffle": self.options.music_shuffle.value,
            "ShuffledSongs": get_shuffled_music(self),
            "Scrambler": self.options.scrambler.value,
            "AlternateOutfit": self.options.alternate_outfit.value,
        }


    def generate_early(self):
        self.initialize_stat_dicts()

        # If using Universal Tracker
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if "Iji" in self.multiworld.re_gen_passthrough:
                passthrough = self.multiworld.re_gen_passthrough["Iji"]

                self.options.end_goal.value = passthrough["Goal"]
                self.options.goal_posters.value = passthrough["GoalPosters"]
                self.options.goal_ribbons.value = passthrough["GoalRibbons"]
                self.options.ribbon_items.value = passthrough["RibbonCount"]
                self.options.allow_sector_z.value = passthrough["SectorZPostGame"]

                self.options.game_difficulty.value = passthrough["GameDifficulty"]
                self.options.logic_difficulty.value = passthrough["LogicDifficulty"]
                self.options.out_of_order_sectors.value = passthrough["OutOfOrderSectors"]
                self.health_balancing_values = []
                for i in list(passthrough["HealthBalancing"]):
                    self.health_balancing_values.append(int(i))
                while len(self.health_balancing_values) < 9:
                    self.health_balancing_values.append(0)
                self.options.enforce_health_balancing.value = passthrough["EnforceHealthBalancing"]

                self.options.poster_locations.value = passthrough["PosterLocations"]
                self.options.supercharge_locations.value = passthrough["SuperchargeLocations"]
                self.options.basic_weapon_locations.value = passthrough["BasicWeaponLocations"]
                self.options.logbook_locations.value = passthrough["LogbookLocations"]
                self.options.security_box_locations.value = passthrough["CrackBoxLocations"]
                self.options.nano_overload_locations.value = passthrough["OverloadLocations"]
                self.options.enemy_locations.value = passthrough["EnemyLocations"]
                self.options.more_enemies.value = passthrough["MoreEnemies"]
                self.options.enemy_location_types.set_from_slot_data(passthrough["EnemyLocationTypes"])

                self.options.special_trait_items.value = passthrough["SpecialTraits"]
                self.options.jump_upgrades.value = passthrough["JumpUpgrades"]
                self.options.armor_upgrades.value = passthrough["ArmorUpgrades"]
                self.options.levelsanity.value = passthrough["Levelsanity"]
                self.options.debug_item.value = passthrough["FireAnytime"]
                self.compact_stats = {key:value for key,value in passthrough["CompactStats"].items()}
                self.starting_stats = {key:value for key,value in passthrough["StartingStats"].items()}

                # TODO get missing Data from passthrough


        else:
            # If not using Universal Tracker
            self.health_balancing_values = define_health_balancing(self)
            for name, value in self.options.starting_stats.get_starting_stat_items(self).items():
                self.current_stat_items[name] = value
                self.starting_stats[name] = value
            for name, value in self.options.compact_stats.get_chosen_compact_values(self).items():
                self.compact_stats[name] = value

            #shuffle_doors(self)

        # Always do this, UT or not

        #finalize_weapon_stats(self)

    @staticmethod
    def interpret_slot_data(slot_data: Dict[str, Any]) -> Dict[str, Any]:

        return slot_data

    #def post_fill(self):
    #    visualize_regions(self.multiworld.get_region(self.origin_region_name, self.player),
    #    f"ijiregions\\{self.player}_{self.player_name}.puml")

    def collect(self, state: CollectionState, item: IjiItem) -> bool:
        ret = super().collect(state, item)
        item_name = item.name

        if item_name[-2:] == "XP":
            state.add_item(EventNames.XP_Collected_Dict[item_name[0]], self.player, int(item_name[2:5]))
        elif item_name in self.compact_stats.keys():
            self.current_stat_items[item_name] += self.compact_stats[item_name]
        elif item_name == EventNames.Weapons[0]:
            self.current_stat_items[ItemNames.Supercharge] += 99
        elif item_name == EventNames.Levels[0]:
            self.current_stat_items[ItemNames.Supercharge] += 1

        return ret

    def remove(self, state: CollectionState, item: IjiItem) -> bool:
        ret = super().remove(state, item)
        item_name = item.name

        if item_name[-2:] == "XP":
            state.remove_item(EventNames.XP_Collected_Dict[item_name[0]], self.player, int(item_name[2:5]))
        elif item_name in self.compact_stats.keys():
            self.current_stat_items[item_name] -= self.compact_stats[item_name]
        elif item_name == EventNames.Weapons[0]:
            self.current_stat_items[ItemNames.Supercharge] -= 99
        elif item_name == EventNames.Levels[0]:
            self.current_stat_items[ItemNames.Supercharge] -= 1

        return ret

    def set_rules(self):
        for loc in self.multiworld.get_locations(self.player):
            set_rule(loc, lambda state, temploc=loc: events_and_locations[temploc.name].logic(self, state))

        if self.options.goal_posters.value > self.total_posters:
            self.options.goal_posters.value = self.total_posters
            logging.warning(f"{self.player_name} required more posters than available sectors.")
            logging.warning(f"Their poster requirement was reduced to {self.options.goal_posters.value}")

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
