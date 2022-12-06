from pysarl.io.sarl.lang.core.Space import Space
from pysarl.io.sarl.lang.core.SpaceID import SpaceID
from pysarl.io.sarl.lang.core.Capacity import Capacity
from pysarl.io.sarl.lang.core.Event import Event
from pysarl.io.sarl.lang.core.Address import Address
from pysarl.io.sarl.lang.core.AgentContext import AgentContext
from pysarl.io.sarl.lang.core.EventSpace import EventSpace


class DefaultContextInteractions(Capacity):
    """
    @param : event
    @param : scope
    """
    def emit(self, event: Event, scope):
        pass

    """
    @param : event
    """
    def emitToParent(self, event: Event):
        pass

    """
    Return the Address of the agent in the Default Space
    """
    def getDefaultAddress(self) -> Address:
        pass

    """
    Return the Default context fo the agent
    """
    def getDefaultContext(self) -> AgentContext:
        pass

    """
    Return the identifier of the default parent
    """
    def getDefaultParentID(self):
        pass

    """
    Return the event scope 
    """
    def getDefaultParentScope(self):
        pass

    """
    Return the default space of the default context
    """
    def getDefaultSpace(self) -> EventSpace:
        pass

    """
    Return true if the given context is the default context
    @param : context
    """
    def isDefaultContext(self, context: AgentContext) -> bool:
        pass

    """
    Return true if the identifier correspond
    @param : contextID
    """
    def isDefaultContext(self, contextID) -> bool:
        pass

    """
        Return true if the space is the default space of the default context
        @param : space
    """
    def isDefaultSpace(self, space: Space) -> bool:
        pass
    """
    @param : spaceID
    """
    def isDefaultSpace(self, spaceId: SpaceID) -> bool:
        pass

    """
        @param : spaceUuid
    """
    def isDefaultSpace(self, spaceUuid) -> bool:
        pass

    """
        @param : event
    """
    def isInDefaultSpace(self, event: Event) -> bool:
        pass

    """
        @param : receiver
        @param : event
    """
    def willReceive(self, receiver, event: Event):
        pass
