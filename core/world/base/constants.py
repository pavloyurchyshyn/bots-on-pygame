IMPASSABLE_VALUE = float('inf')


class TileDataAbs:
    name: str
    verbose_name: str
    hp: int = 0.
    move_energy_coeff: float = 0.
    eternal: bool = False
    destroyed_type = None
    direction: int = 0
    height: int

    def __init__(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def parameters_dict(self):
        des_type = None
        if self.destroyed_type:
            des_type = self.destroyed_type if type(self.destroyed_type) is str else self.destroyed_type.name
        return {
            'name': self.name,
            'hp': self.hp,
            'move_energy_coeff': self.move_energy_coeff,
            'eternal': self.eternal,
            'destroyed_type': des_type,
        }


class EmptyCell(TileDataAbs):
    name = 'empty'
    verbose_name = 'empty'
    hp = 0
    move_energy_coeff: float = 0.
    eternal: bool = False
    destroyed_type = None
    direction: int = 0
    height: int = 0


class TileData(TileDataAbs):
    destroyed_type: TileDataAbs = None


class EternalTileData(TileDataAbs):
    eternal = True
    destroyed_type: TileDataAbs = None


class TilesNames:
    Ruins = 'ruins'
    Field = 'filed'
    Hole = 'hole'
    PrivateHouse = 'privath'
    Forest = 'forest'
    Road = 'road'
    HighRise = 'highh'
    Water = 'water'
    DeepWater = 'deepwater'
    Bridge = 'bridge'
    HighBridge = 'hbridge'
    Wall = 'wall'


class TileTypes:
    class Hole(EternalTileData):
        verbose_name = 'Hole'
        name = TilesNames.Hole
        move_energy_coeff = 0.2
        color = (50, 100, 50)

    class Field(TileData):
        verbose_name = 'Field'
        name = TilesNames.Field
        hp = 50
        destroyed_type = TilesNames.Hole
        color = (20, 235, 20)

    class Ruins(EternalTileData):
        verbose_name = 'Ruins'
        name = TilesNames.Ruins
        move_energy_coeff = 0.2
        color = (50, 50, 50)

    class PrivateHouse(TileData):
        name = TilesNames.PrivateHouse
        hp = 50
        move_energy_coeff = 0.5
        destroyed_type = TilesNames.Ruins
        color = (150, 150, 50)

    class Forest(TileData):
        name = TilesNames.Forest
        hp = 10
        color = (0, 150, 50)

    class Road(TileData):
        name = TilesNames.Road
        hp = 0
        move_energy_coeff = -0.1
        color = (10, 10, 10)

    class HighRise(TileData):
        name = TilesNames.HighRise
        hp = 200
        move_energy_coeff = IMPASSABLE_VALUE
        color = (150, 150, 150)

    class DeepRiver(EternalTileData):
        name = TilesNames.DeepWater
        hp = 0
        eternal = True
        move_energy_coeff = 1.
        color = (50, 50, 150)

    class Water(TileData):
        name = TilesNames.Water
        hp = 0
        eternal = True
        move_energy_coeff = 0.5
        destroyed_type = TilesNames.DeepWater
        color = (50, 50, 250)

    class Bridge(TileData):
        name = TilesNames.Bridge
        hp = 100
        move_energy_coeff = -0.1
        destroyed_type = TilesNames.Water
        color = (50, 50, 150)

    class HighBridge(TileData):
        name = TilesNames.HighBridge
        hp = 200
        move_energy_coeff = -0.3
        destroyed_type = TilesNames.Water
        color = (50, 50, 150)

    class Wall(TileData):
        name = TilesNames.Wall
        hp = 50
        move_energy_coeff = IMPASSABLE_VALUE
        destroyed_type = TilesNames.Ruins
        color = (50, 50, 150)

    types_dict = {
        Ruins.name: Ruins,
        PrivateHouse.name: PrivateHouse,
        Forest.name: Forest,
        Road.name: Road,
        HighRise.name: HighRise,
        Water.name: Water,
        DeepRiver.name: DeepRiver,
        Bridge.name: Bridge,
        HighBridge.name: HighBridge,
        Wall.name: Wall,
        Field.name: Field,
        Hole.name: Hole,
    }


if __name__ == '__main__':
    pass
