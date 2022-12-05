import abc
from typing import TypeVar, Type

from pysarl.io.sarl.lang.core.Agent import Agent
from pysarl.io.sarl.lang.core.AgentTrait import AgentTrait
from pysarl.io.sarl.lang.core.AtomicSkillReference import AtomicSkillReference
from pysarl.io.sarl.lang.core.Capacities import Capacities
from pysarl.io.sarl.lang.core.Capacity import Capacity
from pysarl.io.sarl.lang.core.IBehaviorGuardEvaluatorReceiver import IBehaviorGuardEvaluatorReceiver
from pysarl.io.sarl.lang.core.Skill import Skill
from pysarl.io.sarl.lang.core.UnimplementedCapacityException import UnimplementedCapacityException

C = TypeVar('C', bound=Type[Capacity])
S = TypeVar('S', bound=Capacity)


class Behavior(abc.ABC, AgentTrait, IBehaviorGuardEvaluatorReceiver):

    def __init__(self, agent: Agent):
        super().__init__(agent)

    def _castSkill(self, capacity: C, skillReference: AtomicSkillReference) -> S:
        original: Skill = skillReference.get()
        if original is None:
            raise UnimplementedCapacityException(capacity, self.getOwner().getID())
        return Capacities.createSkillDelegatorIfPossible(original, capacity, self)

    def install(self) -> None:
        pass

    def uninstall(self) -> None:
        pass
