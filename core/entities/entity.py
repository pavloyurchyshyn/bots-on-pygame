from typing import Type, Optional, List, Union, Tuple
from core.entities.events import EventsManager
from core.entities.position import EntityPositionPart
from core.entities.stats_attrs import EntityBaseAttrsPart, Attr
from core.entities.effects.manager import EffectsManager
from core.entities.effects.base import BaseEffect
from core.world.base.hex_utils import EntityPosition


class BaseEntity(EntityBaseAttrsPart, EntityPositionPart):
    def __init__(self, uid: str,  position, current_hp: float = 0,
                 max_hp: float = 0, current_max_hp: float = 0,
                 hp_regen: float = 0, current_hp_regen: float = 0,
                 current_energy: float = 0,
                 max_energy: float = 0, current_max_energy: float = 0,
                 energy_regen: float = 0, current_energy_regen: float = 0,
                 damage: float = 0, current_damage: float = 0,
                 armor: float = 0, current_armor: float = 0,
                 attrs_class: Type[Attr] = Attr,
                 effects: Optional[List[BaseEffect]] = None,
                 ):
        self.uid: str = uid
        super().__init__(current_hp=current_hp,
                         max_hp=max_hp, current_max_hp=current_max_hp,
                         hp_regen=hp_regen, current_hp_regen=current_hp_regen,
                         current_energy=current_energy,
                         max_energy=max_energy, current_max_energy=current_max_energy,
                         energy_regen=energy_regen, current_energy_regen=current_energy_regen,
                         damage=damage, current_damage=current_damage,
                         armor=armor, current_armor=current_armor,
                         attrs_class=attrs_class, )
        EntityPositionPart.__init__(self, position=position)
        self.events_manager: EventsManager = EventsManager(entity=self)
        self.effects_manager: EffectsManager = EffectsManager(entity=self, effects=effects)

    def add_effect(self, effect: BaseEffect):
        self.events_manager.on_effect_apply_event(effect=effect)
        self.effects_manager.add_effect(effect=effect)

    def change_position(self, position: Union[Tuple[int, int], EntityPosition]):
        position: EntityPosition = self.get_position_obj(position=position)
        self.events_manager.do_pre_move_event(entity=self, position=position)
        super().change_position(position=position)
        self.events_manager.do_post_move_event(entity=self, position=position)

    @property
    def effects(self) -> List[BaseEffect]:
        return self.effects_manager.effects
