from abc import abstractmethod
from visual.UI.base.menu import Menu


class Processor:
    UI: Menu

    def __init__(self, admin: bool):
        self.admin = admin

    @abstractmethod
    def connect(self, response: dict):
        raise NotImplementedError

    @abstractmethod
    def process_req(self, r: dict):
        raise NotImplementedError

    @abstractmethod
    def update(self):
        raise NotImplementedError