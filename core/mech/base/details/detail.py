from typing import Union
from core.mech.base.details.constants import *
from core.mech.base.exceptions import *
from global_obj.main import Global

__all__ = ['BaseDetail', ]


class BaseDetail:
    logger = Global.logger

    name: str = None
    original_name: str = None
    verbal_name: str = None

    is_limb = False
    is_weapon = False
    material = MaterialTypes.METAL_TYPE
    detail_type = None

    arm_types = (DetailsTypes.ARM_TYPE, DetailsTypes.ARM_AND_LEG_TYPE)
    leg_types = (DetailsTypes.LEG_TYPE, DetailsTypes.ARM_AND_LEG_TYPE)
    mod_types = (DetailsTypes.MOD_TYPE, DetailsTypes.BODY_MOD_TYPE)
    body_types = (DetailsTypes.BODY,)
    body_mod_types = (DetailsTypes.BODY_MOD_TYPE,)

    def __init__(self, unique_id=None, **kwargs):
        """
        :param unique_id:
        :param kwargs:
        """
        self.__unique_id = unique_id
        if self.name is None:
            raise NoDetailNameError(self)

        if self.original_name is None:
            raise NoOriginalNameError(self)

        if self.__unique_id is None:
            raise NotUniqueIdError(self)

        if self.detail_type is None:
            raise NoDetailTypeError

        self._damage = kwargs.get(DetailsAttrs.Damage, 0)
        self._armor = kwargs.get(DetailsAttrs.Armor, 0)
        self._add_hp = kwargs.get(DetailsAttrs.AddHP, 0)
        self._hp_regen = kwargs.get(DetailsAttrs.HPRegen, 0)
        self._add_energy = kwargs.get(DetailsAttrs.AddEnergy, 0)
        self._energy_regen = kwargs.get(DetailsAttrs.EnergyRegen, 0)

        self._skills = []
        self.add_skills(kwargs.get(DetailsAttrs.Skills, []))

    def add_skills(self, skills) -> None:
        for skill in skills:
            self.add_skill(skill)

    def add_skill(self, skill) -> None:
        """
        :param skill: skill class
        :return:
        """
        self._skills.append(skill(len(self._skills), self.__unique_id))

    @property
    def damage(self) -> Union[float, int]:  # name according to DetailAttrs constants
        return self._damage

    @property
    def armor(self) -> Union[float, int]:  # name according to DetailAttrs constants
        return self._armor

    @property
    def add_hp(self) -> Union[float, int]:  # name according to DetailAttrs constants
        return self._add_hp

    @property
    def hp_regen(self) -> Union[float, int]:  # name according to DetailAttrs constants
        return self._hp_regen

    @property
    def add_energy(self) -> Union[float, int]:  # name according to DetailAttrs constants
        return self._add_energy

    @property
    def energy_regen(self) -> Union[float, int]:  # name according to DetailAttrs constants
        return self._energy_regen

    @property
    def unique_id(self) -> Union[float, int]:
        return self.__unique_id

    @property
    def is_arm(self) -> bool:
        return self.detail_type in self.arm_types

    @property
    def is_leg(self) -> bool:
        return self.detail_type in self.leg_types

    @property
    def is_mod(self) -> bool:
        return self.detail_type in self.mod_types

    @property
    def is_body(self) -> bool:
        return self.detail_type in self.body_types

    @property
    def is_body_mod(self) -> bool:
        return self.detail_type in self.body_mod_types

    @property
    def skills(self) -> list:
        return self._skills
