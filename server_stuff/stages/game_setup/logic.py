from global_obj.main import Global
from server_stuff.stages.abs import LogicStageAbs
from server_stuff.constants.stages import ServerStages
from game_client.server_interactions.network.socket_connection import ConnectionWrapperAbs
from core.world.maps_manager import MapsManager
from server_stuff.constants.setup_stage import SetupStgConst as SSC

from core.player import Player


class GameSetup(LogicStageAbs):

    def __init__(self, game_server, server):
        self.actions = {
            SSC.Player.Chat: self.chat,
            SSC.Player.ChooseMap: self.choose_map,
        }
        super().__init__(game_server, server)
        self.maps_mngr: MapsManager = game_server.maps_mngr
        self.players_objs = game_server.players_objs
        self.chosen_map: int = 0

    def update(self):
        pass

    def process_request(self, request: dict, connection: ConnectionWrapperAbs, player_obj: Player):
        for action, adata in request.items():
            self.actions.get(action, self.bad_action)(action=action,
                                                      request=request,
                                                      connection=connection,
                                                      player_obj=player_obj)

        # response = {'ok': 'process_request ok',
        #             }
        # Global.logger.info(f'Response to {connection.token}: {response}')
        # connection.send_json(response)

    def bad_action(self, action: str, player_obj: Player, **kwargs):
        Global.logger.warning(f'Bad request from {player_obj.token} with action "{action}"')

    def connect(self, response: dict, connection: ConnectionWrapperAbs):
        response[SSC.Maps] = [save.get_save_dict() for save in self.maps_mngr.maps if save]
        response[SSC.Server.ChosenMap] = self.chosen_map

        response[ServerStages.SERVER_STAGE] = ServerStages.GameSetup

    def choose_map(self, request: dict, player_obj: Player, **kwargs):
        Global.logger.info(f'{player_obj.token} changing map.')
        if player_obj.is_admin:
            map__ = map_ = request.get(SSC.Player.ChooseMap, 0)
            try:
                map_ = int(map_)
            except Exception as e:
                Global.logger.error(f'Wrong map format {map__}. Error {e}')
                return
            if map_ == self.chosen_map:
                Global.logger.info(f'This map already chosen')
                return

            # TODO check for maps count
            Global.logger.info(f'{player_obj.token} changing map to {map_}')

            self.game_server.send_to_all({SSC.Server.ChosenMap: map_})
            self.chosen_map = map_
            Global.logger.debug('All ok')
        else:
            Global.logger.debug(f'Player {player_obj.token} is not admin!')

    def chat(self, request: dict, player_obj: Player, **kwargs):
        msg = request.get(SSC.Player.Chat, '')
        Global.logger.info(f'{player_obj.token} send a message {msg}')
        if msg:
            self.game_server.send_to_all({SSC.Server.Chat: request})
