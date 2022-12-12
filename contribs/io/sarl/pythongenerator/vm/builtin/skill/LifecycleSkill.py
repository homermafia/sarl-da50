from typing import TypeVar, Type
from uuid import UUID

from multipledispatch import dispatch

from pysarl.io.sarl.core.Lifecycle import Lifecycle
from pysarl.io.sarl.lang.core.Agent import Agent
from pysarl.io.sarl.lang.core.AgentContext import AgentContext
from pysarl.io.sarl.lang.core.Skill import Skill
from vm.builtin.service.LifecycleService import LifecycleService
from vm.builtin.exceptions.KillMeException import KillMeException

A = TypeVar('A', bound=Type[Agent])


class LifecycleSkill(Skill, Lifecycle):
    __lifecycle: LifecycleService

    def __init__(self, dynamicSkillProvider):
        super().__init__()
        self.__lifecycle = LifecycleService(dynamicSkillProvider)

    def killMe(self, terminationCause: object = None) -> None:
        self.__lifecycle.killAgent(self.getOwner(), False, terminationCause)
        raise KillMeException()

    @dispatch(Agent.__class__, [object])
    def spawn(self, agentType: A, *params: object) -> None:
        self.__lifecycle.createAgent(agentType, self.getOwner().getID())

    @dispatch(int, Agent.__class__, [object])
    def spawn(self, nbAgents: int, agentType: A, *params: object) -> None:
        # TODO: Write this method
        pass

    @dispatch(Agent.__class__, AgentContext, [object])
    def spawnInContext(self, agentClass: A, context: AgentContext, *params: object) -> None:
        # TODO: Write this method
        pass

    @dispatch(int, Agent.__class__, AgentContext, [object])
    def spawnInContext(self, nbAgents: int, agentClass: A, context: AgentContext, *params: object) -> None:
        # TODO: Write this method
        pass

    def spawnInContextWithID(self, agentClass: A, agentID: UUID, context: AgentContext, *params: object) -> None:
        # TODO: Write this method
        pass

    def spawnWithID(self, agentClass: A, agentID: UUID, *params: object) -> None:
        # TODO: Write this method
        pass
