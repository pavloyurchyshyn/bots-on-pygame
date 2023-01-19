from global_obj.main import Global

from visual.UI.base.menu import Menu
from visual.UI.base.container import Container
from visual.UI.base.pop_up import PopUpsController
from visual.UI.base.mixins import DrawElementBorderMixin
from game_client.game_match.stages.match_menu.settings.buttons import BUTTONS_DATA

from game_client.game_match.stages.match_menu.components.world import WorldC


class GameMatch(Menu, PopUpsController,
                WorldC, DrawElementBorderMixin,
                ):

    def __init__(self, processor):
        super(GameMatch, self).__init__(BUTTONS_DATA)
        PopUpsController.__init__(self)
        WorldC.__init__(self)
        self.processor = processor

    def update(self):
        Global.display.fill((0, 0, 0))
        collided_popup_btn = self.update_popups()

        self.simple_buttons_update(self.draw_border_around_element)
        self.update_and_draw_map()

        self.draw_popups()
        if collided_popup_btn:
            self.draw_border_around_element(collided_popup_btn)

    def update_popups(self):
        collided_popup_btn = None
        if self.popups:
            if self.popups[0].collide_point(Global.mouse.pos):
                for btn in self.popups[0].buttons:
                    if btn.collide_point(Global.mouse.pos):
                        collided_popup_btn = btn
                        if Global.mouse.l_up:
                            btn.do_action()
                            if self.popups[0].on_click_action:
                                self.popups[0].on_click_action(self.popups[0], btn)
                            break
                if self.popups and self.popups[0].inactive:
                    self.popups.remove(self.popups[0])
            Global.mouse.l_up = False
            Global.mouse._pos = -10, -10
        return collided_popup_btn
