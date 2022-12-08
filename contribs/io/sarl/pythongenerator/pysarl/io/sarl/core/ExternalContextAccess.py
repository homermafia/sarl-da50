from __future__ import annotations
import abc
from typing import List, TYPE_CHECKING
from uuid import UUID

from multipledispatch import dispatch

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Address import Address
    from pysarl.io.sarl.lang.core.EventSpace import EventSpace
    from pysarl.io.sarl.lang.core.AgentContext import AgentContext
    from pysarl.io.sarl.lang.core.Scope import Scope

from pysarl.io.sarl.lang.core.Capacity import Capacity
from pysarl.io.sarl.lang.core.Event import Event
from pysarl.io.sarl.lang.core.Space import Space
from pysarl.io.sarl.lang.core.SpaceID import SpaceID


class ExternalContextAccess(Capacity, abc.ABC):

    """
    Emits an event with the provided scope in a space
    @param : space
    @param : event
    @param : scope
    """
    @abc.abstractmethod
    def emit(self, space: EventSpace, event: Event, scope: Scope[Address] = None) -> None:
        pass

    @abc.abstractmethod
    def getAllContexts(self) -> List[AgentContext]:
        pass

    """
    Return the AgentContext for the contextID.
    @param : contextID 
    """
    @abc.abstractmethod
    def getContext(self, contextID: UUID) -> AgentContext:
        pass

    """
    Return the AgentContext that is the root of all the contexts
    """
    @abc.abstractmethod
    def getUniverseContext(self) -> AgentContext:
        pass

    """
    Return true if the event was emitted in the space
    @param : event
    @param : space
    """
    @dispatch(Event, Space)
    @abc.abstractmethod
    def isInSpace(self, event: Event, space: Space) -> bool:
        pass

    """
    Return true if the event was emitted in the space with the given identifier..
    @param : event
    @param : spaceID
    """
    @dispatch(Event, SpaceID)
    @abc.abstractmethod
    def isInSpace(self, event: Event, spaceID: SpaceID) -> bool:
        pass

    """
    Replies if the given event was emitted in the space with the given identifier..
    @param : event
    @param : spaceID
    """
    @dispatch(Event, UUID)
    @abc.abstractmethod
    def isInSpace(self, event: Event, spaceID: UUID) -> bool:
        pass

    """
    Join a new parent context
    @param : contextID
    @param : expectedDefaultSpaceID
    """
    @abc.abstractmethod
    def join(self, contextID: UUID, expectedDefaultSpaceID: UUID) -> AgentContext:
        pass

    """"
    Leave the parent's context
    @param : contextID
    """
    @abc.abstractmethod
    def leave(self, contextID: UUID) -> bool:
        pass
