from core.mech.base.skills.skill import BaseSkill
from core.mech.base.skills.constants import ReservedSkillsIds


class DisconnectDetailSkill(BaseSkill):
    targets = BaseSkill.Targets.Detail,
    name = 'disconnect_detail'

    def __init__(self):
        super(DisconnectDetailSkill, self).__init__(unique_id=ReservedSkillsIds.DisconnectDetailSkillId,
                                                    energy_cost=5, cooldown=0, num=0)
        self.unique_id = ReservedSkillsIds.DisconnectDetailSkillId

    def use(self, *args, **kwargs):
        # TODO
        pass
