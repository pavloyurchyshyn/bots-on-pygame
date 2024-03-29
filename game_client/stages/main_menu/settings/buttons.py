from visual.UI.manager import UIManager
from visual.UI.base.button import Button
from visual.UI.constants.attrs import ButtonAttrs, TextAttrs

from settings.localization.menus.UI import UILocal

from game_client.stages.main_menu.settings.uids import UIDs
from global_obj.main import Global
from visual.styles import get_btn_style, DEFAULT_V_SIZE, DEFAULT_H_SIZE


MENU_UIDS = (
    # UIDs.NewGame,
    # UIDs.LoadGame,
    UIDs.HostGame,
    UIDs.JoinGame,
    UIDs.MapEditor,
    # UIDs.Settings,
    UIDs.Exit,
)


def test_draw_btn(b: Button):
    Global.test_draw = not Global.test_draw
    if Global.test_draw:
        b.surface = b.active_surface
    else:
        b.surface = b.inactive_surface


def test_func(b):
    b.parent.UI_manager.get_by_uid(UIDs.NewGame).switch_active()


def exit_btn_func(b):
    ui_manager: UIManager = b.parent.UI_manager
    for uid in MENU_UIDS:
        ui_manager.get_by_uid(uid).deactivate()

    b.parent.add_yes_no_popup(msg='Close game?',
                              yes_action=yes_btn_func, no_action=no_btn_func,
                              yes_uid=UIDs.ExitYes, no_uid=UIDs.ExitNo,
                              parent=b.parent)


def join_menu(b):
    Global.stages.join_menu()


def yes_btn_func(b):
    Global.logger.debug(f'Clicked Yes to exit in main menu.')
    Global.stages.exit_game()


def no_btn_func(b):
    b.parent.close(button)

    ui_manager: UIManager = b.parent.parent.UI_manager
    for uid in MENU_UIDS:
        ui_manager.get_by_uid(uid).activate()


def set_host_game(b: Button):
    Global.stages.host_game()


BUTTONS_DATA = {
    'solo_game': {
        'kwargs': {
            ButtonAttrs.YK: 0.2,
            TextAttrs.Text: UILocal.MainMenu.NewGame,
            ButtonAttrs.UID: UIDs.NewGame,
            ButtonAttrs.Active: False,
            # TextAttrs.RawText: False,
            ButtonAttrs.OnClickAction: lambda b: Global.stages.solo_game_menu(),
        }
    },

    'load_solo_game': {
        'kwargs': {
            ButtonAttrs.YK: 0.3,
            TextAttrs.Text: 'Load Game',
            ButtonAttrs.UID: UIDs.LoadGame,
            ButtonAttrs.Active: False,
            ButtonAttrs.OnClickAction: lambda b: Global.stages.solo_game_menu(),
        }
    },

    'host_game': {
        'kwargs': {
            ButtonAttrs.YK: 0.4,
            TextAttrs.Text: UILocal.MainMenu.HostGame,
            ButtonAttrs.UID: UIDs.HostGame,
            ButtonAttrs.OnClickAction: set_host_game,
        }
    },

    'join_game': {
        'kwargs': {
            ButtonAttrs.YK: 0.5,
            TextAttrs.Text: UILocal.MainMenu.Multiplayer,
            ButtonAttrs.UID: UIDs.JoinGame,
            ButtonAttrs.OnClickAction: join_menu,
        }
    },
    'map_editor': {
        'kwargs': {
            ButtonAttrs.YK: 0.6,
            TextAttrs.Text: UILocal.MainMenu.MapEditor,
            ButtonAttrs.UID: UIDs.MapEditor,
            ButtonAttrs.OnClickAction: lambda b: Global.stages.map_editor(),
        }
    },
    'settings': {
        'kwargs': {
            ButtonAttrs.YK: 0.7,
            TextAttrs.Text: UILocal.MainMenu.Settings,
            ButtonAttrs.UID: UIDs.Settings,
            ButtonAttrs.Active: False,
        }
    },

    'about': {
        'kwargs': {
            ButtonAttrs.YK: 0.8,
            ButtonAttrs.Text: 'About',
            ButtonAttrs.UID: 'about_btn',
            ButtonAttrs.Active: False,
            ButtonAttrs.OnClickAction: lambda b: 1,
        }
    },

    'exit': {
        'kwargs': {
            ButtonAttrs.YK: 0.9,
            TextAttrs.Text: UILocal.MainMenu.Exit,
            ButtonAttrs.UID: UIDs.Exit,
            ButtonAttrs.OnClickAction: exit_btn_func,
        }
    },
}

start_pos = 0.5
default_style = get_btn_style()

for button in BUTTONS_DATA.values():
    button['kwargs'][ButtonAttrs.HSizeK] = DEFAULT_H_SIZE
    button['kwargs'][ButtonAttrs.VSizeK] = DEFAULT_V_SIZE
    button['kwargs'][ButtonAttrs.YK] = start_pos
    button['kwargs'][ButtonAttrs.Style] = default_style
    start_pos += button['kwargs'][ButtonAttrs.VSizeK] + button['kwargs'][ButtonAttrs.VSizeK] * 0.15


BUTTONS_DATA['test_draw'] = {
    "kwargs": {
        TextAttrs.Text: '+',
        ButtonAttrs.Layer: 2,
        ButtonAttrs.UID: 'test_draw',
        ButtonAttrs.XK: 0.975,
        ButtonAttrs.YK: 0.01,
        ButtonAttrs.HSizeK: 0.02,
        ButtonAttrs.RectSize: 1,
        ButtonAttrs.Active: Global.test_draw,
        # ButtonAttrs.Visible: Global.test_draw,
        ButtonAttrs.OnClickAction: test_draw_btn,
    }
}
