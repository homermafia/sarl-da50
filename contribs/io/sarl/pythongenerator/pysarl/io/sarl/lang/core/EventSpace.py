from __future__ import annotations

from abc import ABC
from uuid import UUID
from typing import TYPE_CHECKING

from pysarl.io.sarl.lang.core.Space import Space
from pysarl.io.sarl.lang.core.SpaceID import SpaceID

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Address import Address
    from pysarl.io.sarl.lang.core.Event import Event
    from pysarl.io.sarl.lang.core.Scope import Scope


class EventSpace(Space, ABC):

    def __init__(self):
        self.participant = [] # list of agents

    def getAddress(self, identifier: UUID) -> Address:
        # Returns the address of the agent identified by id
        pass

    def emit(self, agent, event):

        pass

    def getSpaceID(self) -> SpaceID:
        pass

    def register(self, agent):
        self.participant.append(agent)

    def getParticipants(self):
        return self.participant


