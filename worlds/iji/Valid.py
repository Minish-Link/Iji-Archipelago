from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from . import IjiWorld

def could_destroy_sentinel_proxima(world: "IjiWorld") -> bool:
    #TODO
    return True

def could_have_stats(world: "IjiWorld", stat_name: str, stat_count: int) -> bool:
    #TODO
    return True

def enemy_is_valid(world: "IjiWorld", enemy_type: str, enemy_difficulty: int) -> bool:
    return (world.options.enemy_location_types.type_allowed(world, enemy_type) and
            (world.options.game_difficulty.value >= enemy_difficulty or world.options.more_enemies))