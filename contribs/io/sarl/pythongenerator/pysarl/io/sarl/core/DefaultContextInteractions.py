from __future__ import annotations
import abc
from typing import TypeVar, Type, TYPE_CHECKING
from uuid import UUID

from multipledispatch import dispatch

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Agent import Agent
    from pysarl.io.sarl.lang.core.Scope import Scope
    from pysarl.io.sarl.lang.core.Event import Event
    from pysarl.io.sarl.lang.core.Address import Address
    from pysarl.io.sarl.lang.core.EventSpace import EventSpace

    A = TypeVar('A', bound=Type[Agent])

from pysarl.io.sarl.lang.core.AgentContext import AgentContext
from pysarl.io.sarl.lang.core.Capacity import Capacity
from pysarl.io.sarl.lang.core.Space import Space
from pysarl.io.sarl.lang.core.SpaceID import SpaceID


class DefaultContextInteractions(Capacity, abc.ABC):

    """
    Emits a given event with the provided scope in the DefaultSpace of the DefaultContext.
    @param : event
    @param : scope
    """
    @abc.abstractmethod
    def emit(self, event: Event, scope: Scope[Address] = None) -> None:
        pass

    """
    Emits or forward the given event to the parent agent into the default context of the calling agent.
    @param : event
    """
    @abc.abstractmethod
    def emitToParent(self, event: Event) -> None:
        pass

    """
    Return the Address of the agent in the Default Space
    """
    @abc.abstractmethod
    def getDefaultAddress(self) -> Address:
        pass

    """
    Return the Default context of the agent
    """
    @abc.abstractmethod
    def getDefaultContext(self) -> AgentContext:
        pass

    """
    Return the identifier of the default parent
    """
    @abc.abstractmethod
    def getDefaultParentID(self) -> UUID:
        pass

    # """
    # Return the event scope
    # """
    # @abc.abstractmethod
    # def getDefaultParentScope(self) -> Scope[Address]:
    #     pass
    #
    # """
    # Return the default space of the default context
    # """
    # @abc.abstractmethod
    # def getDefaultSpace(self) -> EventSpace:
    #     pass
    #
    # """
    # Replies if the given context is the default context.
    # @param : context
    # """
    # @dispatch(AgentContext)
    # @abc.abstractmethod
    # def isDefaultContext(self, context: AgentContext) -> bool:
    #     pass
    #
    # """
    # Replies if the given identifier is the identifier of the default context.
    # @param : contextID
    # """
    # @dispatch(UUID)
    # @abc.abstractmethod
    # def isDefaultContext(self, contextID: UUID) -> bool:
    #     pass
    #
    # """
    # Replies if the given space is the default space of the default context.
    # @param : space
    # """
    # @dispatch(Space)
    # @abc.abstractmethod
    # def isDefaultSpace(self, space: Space) -> bool:
    #     pass
    # """
    # Replies if the given identifier is the identifier of the default space of the default context.
    # @param : spaceID
    # """
    # @dispatch(SpaceID)
    # @abc.abstractmethod
    # def isDefaultSpace(self, space: SpaceID) -> bool:
    #     pass
    #
    # """
    # Replies if the given identifier is the identifier of the default space of the default context.
    # @param : spaceUuid
    # """
    # @dispatch(UUID)
    # @abc.abstractmethod
    # def isDefaultSpace(self, space: UUID) -> bool:
    #     pass
    #
    # """
    # Replies if the given event was emitted in the default space of the default context.
    # @param : event
    # """
    # @abc.abstractmethod
    # def isInDefaultSpace(self, event: Event) -> bool:
    #     pass
    #
    # """
    # Deprecated
    # See the Lifecycle capacity.
    # @param : event
    # """
    # @abc.abstractmethod
    # def spawn(self, agentType: A, *params: object) -> UUID:
    #     pass
    #
    # """
    # Deprecated
    # since 0.11, see DefaultContextInteractions.emit(Event,Scope)
    # @param : receiver
    # @param : event
    # """
    # @abc.abstractmethod
    # def willReceive(self, receiver: UUID, event: Event) -> None:
    #     pass
