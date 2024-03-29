from game_logic.game_data.steps_clock import RoundsClock
from game_logic.game_data.id_generator import IdGenerator
from game_logic.game_data.game_settings import GameSettings
from core.pools.details_pool import DetailsPool
from core.pools.skills_pool import SkillsPool
from core.pools.effects_pool import EffectsPool


class GameData:
    settings: GameSettings

    def __init__(self, id_generator: IdGenerator = None,
                 details_pool: DetailsPool = None,
                 effects_pool: EffectsPool = None):
        self.rounds_clock = RoundsClock(self.settings.actions_count)
        self.id_generator: IdGenerator = id_generator if id_generator else IdGenerator(self.settings.seed)
        self.details_pool: DetailsPool = details_pool if details_pool else DetailsPool(self.id_generator)
        self.skills_pool: SkillsPool = self.details_pool.skills_pool
        self.effects_pool: EffectsPool = effects_pool if effects_pool else EffectsPool()

    @property
    def real_players_num(self) -> int:
        return self.settings.real_players_num

    @property
    def players_num(self) -> int:
        return self.settings.players_num
