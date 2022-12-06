from pysarl.io.sarl.lang.core.Capacity import Capacity
from pysarl.io.sarl.lang.core.Space import Space
from pysarl.io.sarl.lang.core.SpaceID import SpaceID
from pysarl.io.sarl.lang.core.Event import Event
from pysarl.io.sarl.lang.core.AgentContext import AgentContext
from pysarl.io.sarl.lang.core.EventSpace import EventSpace
from uuid import UUID


class InnerContextAccess(Capacity):
    """
    Return the inner context.
    """

    def getInnerContext(self) -> AgentContext:
        pass

    def getInnerDefaultSpace(self) -> EventSpace:
        pass

    """
    Return the number of agent that are agent of the inner context
    """

    def getMemberAgentCount(self) -> int:
        pass

    """
    Return all agent in the inner context
    """

    def getMemberAgents(self):
        pass

    """
    Return true if it has a member agent
    """

    def hasMemberAgent(self) -> bool:
        pass

    """
    Return true if the given event was emitted in the default space of the inner context
    @param : event
    """

    def isInnerDefaultSpace(self, event: Event) -> bool:
        pass

    """
    Return true if the given space is the default space of the inner context
    @param : space
    """

    def isInnerDefaultSpace(self, space: Space) -> bool:
        pass

    """
    Replies if the given identifier is the identifier of the default space of the inner context.
    @param : spaceID
    """

    def isInnerDefaultSpace(spaceID: SpaceID) -> bool:
        pass

    """
    Replies if the given identifier is the identifier of the default space of the inner context
    @param : spaceID
    """

    def isInnerDefaultSpace(spaceID: UUID) -> bool:
        pass
