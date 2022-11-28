from contribs.io.sarl.pythongenerator.api.event.event import Event

import abc


class EventListener(abc.ABC):

    @abc.abstractmethod
    def receiveEvent(self, event: Event) -> None:
        pass
