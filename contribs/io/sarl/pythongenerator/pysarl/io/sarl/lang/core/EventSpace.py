from __future__ import annotations

from abc import ABC
from uuid import UUID
from typing import TYPE_CHECKING

from pysarl.io.sarl.lang.core.Space import Space
from pysarl.io.sarl.lang.core.SpaceID import SpaceID
from vm.builtin.EventDispatcher import EventDispatcher

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Address import Address
    from pysarl.io.sarl.lang.core.Event import Event
    from pysarl.io.sarl.lang.core.Scope import Scope


class EventSpace(Space, ABC):

    def __init__(self):
        self.participants = [] # list of agents
        self.__eventDispatcher = EventDispatcher()

    def getAddress(self, identifier: UUID) -> Address:
        # Returns the address of the agent identified by id
        pass

    def emit(self, agent, event):
        return self.__eventDispatcher.dispatch(agent, event)

    def getSpaceID(self) -> SpaceID:
        pass

    def register(self, agent):
        self.participants.append(agent)
        self.__eventDispatcher.register(agent)

    def unregister(self, agent):
        self.participants.remove(agent)
        self.__eventDispatcher.unregister(agent)

    def getParticipants(self):
        return self.participants

    def getNumberOfStrongParticipants(self) -> int:
        # Replies the number of strong participants to the space
        pass

    def getNumberOfWeakParticipants(self) -> int:
        # Replies the number of weak participants to the space
        pass

    def forEachStrongParticipant(self, callback):
        pass

    def forEachWeakParticipant(self, callback) -> None:
        pass


