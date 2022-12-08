from __future__ import annotations
import abc
from uuid import UUID
from typing import TypeVar, Type

from multipledispatch import dispatch

from pysarl.io.sarl.lang.core.Agent import Agent
from pysarl.io.sarl.lang.core.AgentContext import AgentContext
from pysarl.io.sarl.lang.core.Capacity import Capacity

A = TypeVar('A', bound=Type[Agent])


class Lifecycle(Capacity, abc.ABC):

    @abc.abstractmethod
    def killMe(self, terminationCause: object = None) -> None:
        pass

    @dispatch(Agent.__class__, [object])
    @abc.abstractmethod
    def spawn(self, agentType: A, *params: object) -> None:
        pass

    @dispatch(int, Agent.__class__, [object])
    @abc.abstractmethod
    def spawn(self, nbAgents: int, agentType: A, *params: object) -> None:
        pass

    @dispatch(Agent.__class__, AgentContext, [object])
    @abc.abstractmethod
    def spawnInContext(self, agentClass: A, context: AgentContext, *params: object) -> None:
        pass

    @dispatch(int, Agent.__class__, AgentContext, [object])
    @abc.abstractmethod
    def spawnInContext(self, nbAgents: int, agentClass: A, context: AgentContext, *params: object) -> None:
        pass

    @abc.abstractmethod
    def spawnInContextWithID(self, agentClass: A, agentID: UUID, context: AgentContext, *params: object) -> None:
        pass

    @abc.abstractmethod
    def spawnWithID(self, agentClass: A, agentID: UUID, *params: object) -> None:
        pass
