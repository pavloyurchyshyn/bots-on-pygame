from core.mech.skills.constants import INFINITE_VALUE
from core.mech.skills.skill import BaseSkill
from core.validators.skill import SkillsValidations
from core.entities.entity import BaseEntity
from core.vanilla_effects.double_damage import DoubleDamageEffect


class DoubleDamageAttrs:
    spell_cost = 3
    cooldown = 10


class DoubleDamage(BaseSkill):
    name = 'double_damage'
    verbal_name = 'Double Damage'
    targets = BaseSkill.TargetsConst.AnyMech,

    def __init__(self, num, unique_id):
        super(DoubleDamage, self).__init__(unique_id=unique_id, num=num,
                                           energy_cost=DoubleDamageAttrs.spell_cost,
                                           cooldown=DoubleDamageAttrs.cooldown,
                                           target_validation_func=SkillsValidations.validate_target_is_mech,
                                           cast_range=INFINITE_VALUE,
                                           )

    def use(self, player, game_obj, mech: BaseEntity, skill_cast_uid: str, **__) -> None:
        mech.events_manager.do_pre_skill_use_event(skill=self)
        mech.spend_energy(self.energy_cost)
        effect = DoubleDamageEffect(dealer=player.mech, target=mech, uid=skill_cast_uid, parent_skill=self)
        mech.add_effect(effect)
        self.set_on_cooldown()
        mech.events_manager.do_post_skill_use_event(skill=self)

    def get_dict(self) -> dict:
        return self.get_base_dict()

    def update_attrs(self, attrs: dict) -> None:
        self.update_base_attrs(attrs=attrs)
