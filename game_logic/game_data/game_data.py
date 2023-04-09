from game_logic.game_data.steps_clock import StepsClock
from game_logic.game_data.id_generator import IdGenerator
from core.mech.base.pools import DetailsPool, SkillsPool
from game_logic.game_data.game_settings import GameSettings


class GameData:
    settings: GameSettings

    def __init__(self, id_generator: IdGenerator = None, details_pool: DetailsPool = None):
        self.steps_clock = StepsClock(self.settings.actions_count)
        self.id_generator: IdGenerator = id_generator if id_generator else IdGenerator(self.settings.seed)
        self.details_pool: DetailsPool = details_pool if details_pool else DetailsPool(self.id_generator)
        self.skills_pool: SkillsPool = self.details_pool.skills_pool

    @property
    def real_players_num(self) -> int:
        return self.settings.real_players_num

    @property
    def players_num(self) -> int:
        return self.settings.players_num
