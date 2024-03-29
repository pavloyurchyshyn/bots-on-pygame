from visual.UI.base.button import Button
from visual.styles import get_green_btn_style
from visual.UI.constants.attrs import ButtonAttrs, TextAttrs
from game_client.stages.maps_editor.settings.uids import UIDs
from game_client.stages.maps_editor.settings.menu_abs import MenuAbs
from visual.UI.yes_no_popup import YesNoPopUp
from global_obj.main import Global


def save(b: Button, forced=False):
    try:
        menu: MenuAbs = b.parent
        menu.current_save.set_name(menu.name_inp.str_text)
        menu.current_save.set_world_to_json_data(menu.w)
        menu.current_save.set_spawns(menu.spawns)
        menu.current_save.save(forced)
        menu.fill_saves_container()
        menu.unsaved_edit = False
    except FileExistsError:
        b.parent.add_popup(YesNoPopUp(f'{menu.current_save.name}_pop',
                                      text=f'Rewrite {menu.current_save.name}?',
                                      no_on_click_action=lambda n_b: n_b.parent.close(n_b),
                                      yes_on_click_action=lambda y_b: (save(b, True),
                                                                       y_b.parent.close(y_b)
                                                                       ),
                                      )
                           )


def exit_to_main_menu(b):
    if b.parent.unsaved_edit:
        b.parent.add_popup(YesNoPopUp(f'exit_to_main_pop',
                                      text=f'Exit to main menu?',
                                      no_on_click_action=lambda n_b: n_b.parent.close(n_b),
                                      yes_on_click_action=lambda y_b: (y_b.parent.close(y_b),
                                                                       Global.stages.main_menu(),
                                                                       ),
                                      )
                           )

    else:
        Global.stages.main_menu()


def minus_h_size_l(b: Button):
    b.parent.minus_save_h_size_l()


def add_save_h_size_l(b: Button):
    b.parent.add_save_h_size_l()


def add_h_size_r(b: Button):
    b.parent.add_save_h_size_r()


def minus_h_size_r(b: Button):
    b.parent.minus_save_h_size_r()


def add_save_v_size_b(b: Button):
    b.parent.add_save_v_size_b()


def minus_save_v_size_b(b: Button):
    b.parent.minus_save_v_size_b()


BUTTONS_DATA = {
    'save': {
        'kwargs': {
            ButtonAttrs.UID: UIDs.SaveMap,
            ButtonAttrs.Text: 'Save',
            ButtonAttrs.XK: 0.918,
            ButtonAttrs.YK: 0.05,
            ButtonAttrs.HSizeK: 0.08,
            ButtonAttrs.VSizeK: 0.05,
            ButtonAttrs.Style: get_green_btn_style(),
            ButtonAttrs.OnClickAction: save,
            ButtonAttrs.TextKwargs: {
                TextAttrs.FontSize: 30,
            }
        }
    },
    'add_v_b': {
        'kwargs': {
            ButtonAttrs.UID: UIDs.AddMapV,
            ButtonAttrs.Text: '+ b',
            ButtonAttrs.XK: 0.880,
            ButtonAttrs.YK: 0.14,
            ButtonAttrs.HSizeK: 0.03,
            ButtonAttrs.VSizeK: 0.03,
            ButtonAttrs.OnClickAction: add_save_v_size_b,
        }
    },
    'minus_v': {
        'kwargs': {
            ButtonAttrs.UID: UIDs.MinusMapV,
            ButtonAttrs.Text: '-',
            ButtonAttrs.XK: 0.910,
            ButtonAttrs.YK: 0.14,
            ButtonAttrs.HSizeK: 0.025,
            ButtonAttrs.VSizeK: 0.03,
            ButtonAttrs.OnClickAction: minus_save_v_size_b,
        }
    },

    # 'add_h_l': {
    #     'kwargs': {
    #         ButtonAttrs.UID: f"{UIDs.AddMapH}_l",
    #         ButtonAttrs.Text: '<- +',
    #         ButtonAttrs.XK: 0.870,
    #         ButtonAttrs.YK: 0.175,
    #         ButtonAttrs.HSizeK: 0.025,
    #         ButtonAttrs.VSizeK: 0.03,
    #         ButtonAttrs.OnClickAction: add_save_h_size_l,
    #     }
    # },

    'add_h_r': {
        'kwargs': {
            ButtonAttrs.UID: f"{UIDs.AddMapH}_r",
            ButtonAttrs.Text: '+ ->',
            ButtonAttrs.XK: 0.901,
            ButtonAttrs.YK: 0.175,
            ButtonAttrs.HSizeK: 0.025,
            ButtonAttrs.VSizeK: 0.03,
            ButtonAttrs.OnClickAction: add_h_size_r,
        }
    },

    # 'minus_h_l': {
    #     'kwargs': {
    #         ButtonAttrs.UID: f"{UIDs.MinusMapH}_l",
    #         ButtonAttrs.Text: '<- -',
    #         ButtonAttrs.XK: 0.9302,
    #         ButtonAttrs.YK: 0.175,
    #         ButtonAttrs.HSizeK: 0.025,
    #         ButtonAttrs.VSizeK: 0.03,
    #         ButtonAttrs.OnClickAction: minus_h_size_l,
    #     }
    # },

    'minus_h_r': {
        'kwargs': {
            ButtonAttrs.UID: f"{UIDs.MinusMapH}_r",
            ButtonAttrs.Text: '- ->',
            ButtonAttrs.XK: 0.9603,
            ButtonAttrs.YK: 0.175,
            ButtonAttrs.HSizeK: 0.025,
            ButtonAttrs.VSizeK: 0.03,
            ButtonAttrs.OnClickAction: minus_h_size_r,
        }
    },

    'exit': {
        'kwargs': {
            ButtonAttrs.UID: UIDs.Exit,
            ButtonAttrs.Text: 'X',
            ButtonAttrs.XK: 0.970,
            ButtonAttrs.YK: 0.005,
            ButtonAttrs.HSizeK: 0.02,
            ButtonAttrs.VSizeK: 0.03,
            ButtonAttrs.OnClickAction: exit_to_main_menu,
        }
    },

}
