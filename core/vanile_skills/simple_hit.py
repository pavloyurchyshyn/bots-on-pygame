from core.mech.skills.skill import BaseSkill
from core.mech.skills.exceptions import OnCooldownError
from core.mech.mech import BaseMech


class SimpleStepAttrs:
    name = 'simple_step'
    spell_cost = 1
    cooldown = 0


class SimpleHit(BaseSkill):
    name = 'simple_hit'
    verbal_name = 'Simple Hit'
    targets = BaseSkill.TargetsConst.AnyMech,

    def __init__(self, num, unique_id):
        super(SimpleHit, self).__init__(unique_id=unique_id, num=num,
                                        energy_cost=SimpleStepAttrs.spell_cost,
                                        cooldown=SimpleStepAttrs.cooldown, validators=[])

    def use(self, *args, **kwargs):
        if not self.on_cooldown:
            mech: BaseMech = kwargs.get('mech')
            mech.spend_energy(self.energy_cost)

        else:
            raise OnCooldownError