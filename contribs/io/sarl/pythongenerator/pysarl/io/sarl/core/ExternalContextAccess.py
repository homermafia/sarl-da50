from pysarl.io.sarl.lang.core.EventSpace import EventSpace
from pysarl.io.sarl.lang.core.Capacity import Capacity
from pysarl.io.sarl.lang.core.Event import Event
from pysarl.io.sarl.lang.core.AgentContext import AgentContext
from pysarl.io.sarl.lang.core.Space import Space
from pysarl.io.sarl.lang.core.SpaceID import SpaceID
from uuid import UUID

class ExternalContextAccess(Capacity):
    """
    @param : space
    @param : event
    @param : scope
    Emits an event with the provided scope in a space
    """

    def emit(space: EventSpace, event: Event, scope):
        pass

    def getAllContexts(self):
        pass

    """
    @param : contextID 
    Return the AgentContext for the contextID.
    """

    def getContext(self, contextID: UUID) -> AgentContext:
        pass

    """
    Return the AgentContext that is the root of all the contexts
    """

    def getUniverseContext(self) -> AgentContext:
        pass

    """
    Return true if the event was emitted in the space
    @param : event
    @param : space
    """

    def isInSpace(self, event: Event, space: Space) -> bool:
        pass

    """
    Return true if the event was emitted in the space with the given identifier..
    @param : event
    @param : spaceID
    """

    def isInSpaceID(self, event: Event, spaceID: SpaceID) -> bool:
        pass

    def isInSpaceUUID(self, event: Event, spaceID: UUID) -> bool:
        pass

    """
    Join a new parent context
    @param : contextID
    @param : expectedDefaultSpaceID
    """

    def join(self, contextID: UUID, expectedDefaultSpaceID: UUID) -> AgentContext:
        pass

    """"
    Leave the parent's context
    @param : contextID
    """

    def leave(self, contextID: UUID) -> bool:
        pass
