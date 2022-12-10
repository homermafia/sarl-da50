from __future__ import annotations
import threading
from typing import Type, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.AgentTrait import AgentTrait
    from pysarl.io.sarl.lang.core.Capacity import Capacity
    from pysarl.io.sarl.lang.core.Skill import Skill

    C = TypeVar('C', bound=Type[Capacity])
    S = TypeVar('S', bound=Capacity)


class Capacities():
    #CALLER: AgentTrait = (lambda a: setattr(a, "agent", None) or a)(threading.local)

    def __init__(self):
        pass

    def getCaller(self) -> AgentTrait:
        return Capacities.CALLER.agent

    def createSkillDelegator(self, originalSkill: Skill, capacity: C, capacityCaller: AgentTrait) -> S:
        # TODO: The implementation of this is much more complex originally.
        #  See: https://github.com/sarl/sarl/blob/master/main/coreplugins/io.sarl.lang.core/src/io/sarl/lang/core/Capacities.java
        return originalSkill

    def createSkillDelegatorIfPossible(self, originalSkill: Skill, capacity: C, capacityCaller: AgentTrait) -> S:
        try:
            return Capacities.createSkillDelegator(Capacities, originalSkill, capacity, capacityCaller)
        except Exception as e:
            # return capacity.cast(originalSkill)  # There is no convenient way to cast an object in python. The closest thing is to change the __class__ attribute of the object, but it does not copy it
            return originalSkill
