from pysarl.io.sarl.lang.core.Event import Event

import abc

from pysarl.io.sarl.lang.core.Identifiable import Identifiable


class EventListener(abc.ABC, Identifiable):

    @abc.abstractmethod
    def receiveEvent(self, event: Event) -> None:
        pass
