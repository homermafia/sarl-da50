from pysarl.io.sarl.lang.core.Event import Event

import abc


class EventListener(abc.ABC):

    @abc.abstractmethod
    def receiveEvent(self, event: Event) -> None:
        pass
