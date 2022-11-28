from pysarl.io.sarl.lang.core.Space import Space
from pysarl.io.sarl.lang.core.Event import Event
from pysarl.io.sarl.lang.core.Address import Address
import uuid
import abc


class EventSpace(Space, abc.ABC):

    @abc.abstractmethod
    def emit(self, eventSource: uuid, event: Event):
        # Emits the event inside this space
        self.emitWithScope(eventSource, event, None)

    @abc.abstractmethod
    def emitWithScope(self, eventSource: uuid, event: Event, scope):
        # Emits the event inside this space with the given scope
        pass

    @abc.abstractmethod
    def getAddress(self, identifier: uuid) -> Address:
        # Returns the address of the agent identified by id
        pass