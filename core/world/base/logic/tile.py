from typing import Union
from core.world.base.logic.tiles_data import TileDataAbs, IMPASSABLE_VALUE, TileTypes
from core.world.base.hex_utils import Cube, XYIdHex, HexMath


class LogicTile(XYIdHex, Cube):

    def __init__(self, xy_id: tuple[int, int],
                 tile_data: Union[str, TileDataAbs],
                 at_edge: bool = False):
        XYIdHex.__init__(self, *xy_id)
        Cube.__init__(self, *HexMath.xy_id_to_qr(*xy_id))

        if type(tile_data) is str:
            tile_data = TileTypes.types_dict[tile_data]

        self.name = tile_data.name
        self.verbose_name = tile_data.verbose_name
        self.hp: float = tile_data.hp
        self.eternal: bool = tile_data.eternal
        self.move_energy_k: float = tile_data.move_energy_k
        self.destroyed_type: Union[str, TileDataAbs, None] = tile_data.destroyed_type
        self.height = tile_data.height

        self.img: int = tile_data.img
        self.spawn: bool = tile_data.spawn

        self.at_edge = at_edge

    def apply_type(self, tile_type: Union[str, TileDataAbs]) -> None:
        tile_type = TileTypes.types_dict[tile_type] if type(tile_type) is str else tile_type
        self.name = tile_type.name
        self.hp: float = tile_type.hp
        self.eternal: bool = tile_type.eternal
        self.move_energy_k: float = tile_type.move_energy_k
        self.destroyed_type: Union[str, TileDataAbs, None] = tile_type.destroyed_type

        self.img = tile_type.img

    def damage(self, dmg: float) -> None:
        if not self.eternal and self.hp > 0:
            self.hp -= dmg
            if self.hp < 0:
                self.hp = 0

            if self.hp <= 0.:
                if self.destroyed_type:
                    self.apply_type(self.destroyed_type)
                else:
                    if self.hp < 0:
                        self.hp = 0
                    self.eternal = True

    @property
    def passable(self) -> bool:
        return self.move_energy_k != IMPASSABLE_VALUE

    @property
    def not_passable(self) -> bool:
        return not self.passable

    def get_data_dict(self) -> dict:
        return TileDataAbs.parameters_to_dict(self)

    @property
    def can_be_destroyed(self) -> bool:
        return not self.eternal and self.hp > 0

if __name__ == '__main__':
    tile = LogicTile((0, 0), TileTypes.Forest)
    print(tile.__dict__)
    tile.damage(tile.hp)
    print(tile.__dict__)
