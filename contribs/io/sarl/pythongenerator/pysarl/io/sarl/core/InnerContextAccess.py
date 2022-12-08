from __future__ import annotations
import abc
from typing import Set, TYPE_CHECKING
from uuid import UUID

from multipledispatch import dispatch

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Event import Event
    from pysarl.io.sarl.lang.core.AgentContext import AgentContext
    from pysarl.io.sarl.lang.core.EventSpace import EventSpace

from pysarl.io.sarl.lang.core.Capacity import Capacity
from pysarl.io.sarl.lang.core.Space import Space
from pysarl.io.sarl.lang.core.SpaceID import SpaceID


class InnerContextAccess(Capacity, abc.ABC):

    """
    Return the inner context.
    """
    @abc.abstractmethod
    def getInnerContext(self) -> AgentContext:
        pass

    @abc.abstractmethod
    def getInnerDefaultSpace(self) -> EventSpace:
        pass

    """
    Return the number of agent that are agent of the inner context
    """
    @abc.abstractmethod
    def getMemberAgentCount(self) -> int:
        pass

    """
    Return all agent in the inner context
    """
    @abc.abstractmethod
    def getMemberAgents(self) -> Set[UUID]:
        pass

    """
    Return true if it has a member agent
    """
    @abc.abstractmethod
    def hasMemberAgent(self) -> bool:
        pass

    """
    Return true if the given event was emitted in the default space of the inner context
    @param : event
    """
    @abc.abstractmethod
    def isInInnerDefaultSpace(self, event: Event) -> bool:
        pass

    """
    Return true if the given space is the default space of the inner context
    @param : space
    """
    @dispatch(Space)
    @abc.abstractmethod
    def isInnerDefaultSpace(self, space: Space) -> bool:
        pass

    """
    Replies if the given identifier is the identifier of the default space of the inner context.
    @param : spaceID
    """
    @dispatch(SpaceID)
    @abc.abstractmethod
    def isInnerDefaultSpace(self, spaceID: SpaceID) -> bool:
        pass

    """
    Replies if the given identifier is the identifier of the default space of the inner context
    @param : spaceID
    """
    @dispatch(UUID)
    @abc.abstractmethod
    def isInnerDefaultSpace(self, spaceID: UUID) -> bool:
        pass
