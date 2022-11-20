from constants.stages import StagesConstants


class Stages:
    def __init__(self, logger):
        self.logger = logger
        self.__prev_stage = None
        self.current_stage = StagesConstants.MainMenu

    def main_menu(self):
        self.change_current_stage(StagesConstants.MainMenu)

    def solo_game_menu(self):
        self.change_current_stage(StagesConstants.SoloGameMenu)

    def close_game(self):
        self.change_current_stage(StagesConstants.CloseGame)

    def set_prev_stage(self):
        self.change_current_stage(self.prev_stage)

    def change_current_stage(self, stage: str):
        self.logger.info(f'Stage {self.current_stage} changed to {stage}')
        self.__prev_stage = self.current_stage
        self.current_stage = stage

    @property
    def prev_stage(self) -> str:
        return self.__prev_stage if self.__prev_stage else self.current_stage