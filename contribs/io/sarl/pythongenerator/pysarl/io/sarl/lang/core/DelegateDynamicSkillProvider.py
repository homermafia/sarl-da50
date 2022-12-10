from __future__ import annotations
from typing import List, TypeVar, Type, TYPE_CHECKING

from pysarl.io.sarl.lang.core.DynamicSkillProvider import DynamicSkillProvider

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Capacity import Capacity
    from pysarl.io.sarl.lang.core.Skill import Skill

    C = TypeVar('C', bound=Type[Capacity])


class DelegateDynamicSkillProvider(DynamicSkillProvider):
    __delegates: List[DynamicSkillProvider]

    def __init__(self, delegates: List[DynamicSkillProvider]):
        assert delegates is not None
        self.__delegates = delegates

    def createSkill(self, capacity: C) -> Skill:
        for provider in self.__delegates:
            skill: Skill = provider.createSkill(capacity)
            if skill is not None:
                return skill
        return None

    def isSkillProviding(self, capacity: C) -> bool:
        for provider in self.__delegates:
            if provider.isSkillProviding(capacity):
                return True
        return False
