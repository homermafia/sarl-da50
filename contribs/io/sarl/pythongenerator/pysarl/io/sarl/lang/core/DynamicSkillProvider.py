import abc
from typing import TypeVar, Type

from pysarl.io.sarl.lang.core.Capacity import Capacity
from pysarl.io.sarl.lang.core.Skill import Skill

C = TypeVar('C', bound=Type[Capacity])


class DynamicSkillProvider(abc.ABC):

    @abc.abstractmethod
    def createSkill(self, capacity: C) -> Skill:
        pass

    @abc.abstractmethod
    def isSkillProviding(self, capacity: C) -> bool:
        pass


class EmptyDynamicSkillProvider(DynamicSkillProvider):

    def createSkill(self, capacity: C) -> Skill:
        return None

    def isSkillProviding(self, capacity: C) -> bool:
        return False
