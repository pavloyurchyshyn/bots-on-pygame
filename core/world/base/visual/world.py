if __name__ == '__main__':
    from launch import GameRunner
from typing import List, Type
from pygame import draw, Surface, transform
from global_obj import Global
from core.world.base.logic.tile import LogicTile
from core.world.base.visual.tile import VisualTile
from core.world.base.logic.world import LogicWorld
from core.world.base.hex_utils import get_hex_math, HexMathAbs
from core.world.base.constants import TileDataAbs, IMPASSABLE_VALUE, TileTypes, EmptyTile
from core.world.base.visual.tiles_textures import TilesTextures
from settings.tile_settings import TileSettings
from visual.UI.utils import get_surface
from visual.UI.base.font import get_custom_font
from pygame.rect import Rect


class VisualWorld(LogicWorld):

    def __init__(self, window_rect, tile_size: int = TileSettings.visual_tile_r, parent_surface=Global.display):
        super(VisualWorld, self).__init__(tile_class=VisualTile)
        self.parent_surface = parent_surface
        self.textures = TilesTextures()

        self.window_rect = Rect(window_rect)
        self.x, self.y, self.win_x_size, self.win_y_size = window_rect

        self.dx, self.dy = 0, 0

        self.big_surface: Surface = None
        self.small_surface: Surface = None
        self.surface: Surface = None

        self.hex_math: HexMathAbs = None
        self.reference_hex: VisualTile = None
        self.tile_size: int = tile_size

        self.scale = 1

    @property
    def scaled_tile_size(self):
        return self.tile_size * self.scale

    def reload_surface(self):
        w, h = self.big_surface.get_size()
        self.surface = transform.smoothscale(self.big_surface, (int(w * self.scale), int(h * self.scale)))

    def build_map(self, flat, odd, data: List[List[TileDataAbs]]):
        self.hex_math = get_hex_math(flat, odd)
        super().build_map(flat, odd, data)
        self.big_surface = get_surface(*self.hex_math.get_map_size(self.x_size, self.y_size, self.tile_size))
        self.reference_hex = VisualTile((None, None), self.hex_math.get_dots_by_xy(0, 0, self.tile_size), '')
        self.render()

    def init_hex_math(self, flat=True, odd=True):
        self.hex_math = get_hex_math(flat, odd)

    def get_normalized_mouse_pos(self) -> tuple[int, int]:
        m_pos = self.hex_math.normalize_coordinates(Global.mouse.x - self.x - self.dx,
                                                    Global.mouse.y - self.y - self.dy,
                                                    self.scaled_tile_size)
        return m_pos[0] + self.x + self.dx, m_pos[1] + self.y + self.dy

    def get_mouse_to_xy(self):
        return self.hex_math.get_indexes_from_coordinates(
            (Global.mouse.x - self.x - self.dx) / self.scale,
            (Global.mouse.y - self.y - self.dy) / self.scale,
            self.tile_size)

    def get_tile_under_mouse(self) -> LogicTile:
        return self.xy_to_tile.get(self.get_mouse_to_xy())

    def render(self):
        self.big_surface.fill((0, 0, 0))
        for tile in self.tiles:
            if tile.name != EmptyTile.name:
                self.render_tile(self.big_surface, tile)
        self.surface = self.big_surface.copy()

    def render_tile_by_xy(self, xy: tuple[int, int]):
        self.render_tile(self.big_surface, self.xy_to_tile[xy])

    def rerender_tile(self, xy: tuple[int, int]):
        self.render_tile(self.big_surface, self.xy_to_tile[xy])
        self.reload_surface()

    def render_tile(self, surface, tile: VisualTile):
        # pos = self.hex_math.get_lt_by_id(tile.id_x, tile.id_y, self.tile_size)
        draw.polygon(surface, tile.tile_data.color, tile.dots)
        draw.lines(surface, (50, 50, 50), True, points=tile.dots)

        font = get_custom_font(int(9 * self.scale))
        text = font.render(f'{tile.id_x, tile.id_y}', True, (255, 255, 255))
        pos = self.hex_math.get_center_by_xy_id(tile.id_x, tile.id_y, self.tile_size)
        surface.blit(text, (pos[0] - text.get_width() // 2, pos[1] - text.get_height() // 2))
        # self.textures.get_texture()

    def get_tile_from_data(self, x, y, tile_data: Type[TileDataAbs], **extra_data) -> VisualTile | LogicTile:
        dots = self.hex_math.get_dots_by_xy(x, y, self.tile_size)

        return super().get_tile_from_data(x=x, y=y, tile_data=tile_data, dots=dots)

    def draw_border_for_xy(self, xy, color=(255, 255, 255)):
        self.draw_tile_border(Global.display, self.get_dots_due_to_map_pos(*xy), color=color)

    def draw_border_under_mouse(self, color=(255, 255, 255)):
        pos = self.get_mouse_to_xy()
        if pos in self.xy_to_tile:
            self.draw_border_for_xy(pos, color)

    @staticmethod
    def draw_tile_border(surface, dots, color=(75, 75, 75), width=1):
        draw.lines(surface, color, True, dots, width)

    def get_dots_due_to_map_pos(self, x, y):
        return self.hex_math.get_dots_by_xy(x, y,
                                            self.scaled_tile_size,
                                            self.x + self.dx,
                                            self.y + self.dy)

    def draw(self):
        if self.surface:
            self.parent_surface.blit(self.surface,
                                     (self.x, self.y),
                                     (0 - self.dx, 0 - self.dy, self.win_x_size, self.win_y_size))


# TODO clear all unneeded
if __name__ == '__main__':
    from launch import GameRunner
    import pprint
    from visual.hex_stuff import get_colored_hex, draw_hex_border, rotate_hex
    import random
    from core.world.base.logic.save_and_load_map import *


    class B:
        def __init__(self):
            self.w = VisualWorld((110, 20, 900, 500))
            self.map_data = [[random.choice(tuple((*TileTypes.types_dict.values(), EmptyTile)))() for x in range(1)] for
                             y in
                             range(2)]
            self.w.build_map(True, True, self.map_data)
            self.tile_dir = 0
            data = []
            for line in self.map_data:
                data.append([l.get_data_dict() if l else EmptyTile() for l in line])
            list_data = world_to_list(self.w)
            pprint.pp(list_data == data)
            print()

        def game_loop(self):
            raise Exception
            Global.display.fill((0, 0, 0))
            self.w.draw()
            if self.w.window_rect.collidepoint(Global.mouse.pos):
                pos = self.w.get_mouse_to_xy()
                if pos in self.w.xy_to_tile:
                    draw.circle(Global.display, (255, 0, 255),
                                self.w.get_normalized_mouse_pos(),
                                5)

                    dots = self.w.get_dots_due_to_map_pos(*pos)
                    self.w.draw_tile_border(Global.display, dots, color=(255, 255, 255))

            if Global.mouse.scroll:
                self.w.scale = self.w.scale + Global.mouse.scroll * Global.clock.d_time * 2
                self.w.reload_surface()
            if Global.mouse.m_hold:
                self.w.dx += Global.mouse.rel_x
                self.w.dy += Global.mouse.rel_y

        def get_hexs(self):
            H = get_colored_hex((100, 255, 100))
            draw_hex_border(H, (255, 255, 255))
            return rotate_hex(H, self.tile_dir)


    GameRunner(B()).run()
