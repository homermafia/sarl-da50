from pysarl.io.sarl.lang.core.Scope import Scope
from pysarl.io.sarl.lang.core.Space import Space
from pysarl.io.sarl.lang.core.Event import Event
from pysarl.io.sarl.lang.core.Address import Address
from uuid import UUID
import abc


class EventSpace(abc.ABC, Space):

    @abc.abstractmethod
    def getAddress(self, identifier: UUID) -> Address:
        # Returns the address of the agent identified by id
        pass

    @abc.abstractmethod
    def emit(self, eventSource: UUID, event: Event, scope: Scope = None) -> None:
        # Emits the event inside this space with the given scope
        pass
