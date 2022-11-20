from abc import abstractmethod
from typing import List
from visual.UI.manager import UIManager
from visual.UI.base.button import Button
from visual.UI.base.mixins import CreateButtonMixin
from global_obj import Global


class Menu(CreateButtonMixin):
    def __init__(self, buttons_data, surface=None):
        self.x, self.y = 0, 0
        self.surface = surface if surface else Global.display
        self.UI_manager = UIManager()
        self.buttons: List[Button, ] = self.create_button_from_data(buttons_data)
        self.UI_manager.add_elements(self.buttons)

    @abstractmethod
    def update(self):
        raise NotImplementedError

    @staticmethod
    def __sort_value(element):
        """
        For sort.

        :param element: Rectangle or Circle object
        :return:
        """
        return element.y
