from typing import Dict, List

from core.player.player import PlayerObj
from core.world.base.logic.world import LogicWorld

from game_logic.bots.bot_player import BotPlayer
from game_logic.game_data.game_data import GameData
from game_logic.game_data.game_settings import GameSettings

from game_logic.game_data.id_generator import IdGenerator
from core.mech.base.pools.details_pool import DetailsPool


class Game(GameData):
    def __init__(self,
                 world: LogicWorld,
                 setting: GameSettings,
                 players: Dict[int, PlayerObj],
                 bots: List[BotPlayer],
                 id_generator: IdGenerator = None,
                 details_pool: DetailsPool = None,
                 ):
        self.settings: GameSettings = setting
        super().__init__(id_generator=id_generator, details_pool=details_pool)
        self.bots: List[BotPlayer] = bots
        self.players: Dict[int, PlayerObj] = players  # player number -> player
        self.world: LogicWorld = world

    @property
    def everybody_ready(self) -> bool:
        return all(map(lambda p: p.ready, self.players.values()))

    @property
    def ready_players_number(self) -> int:
        return len(tuple(filter(lambda p: p.ready or p.under_bot_control, self.players.values())))
