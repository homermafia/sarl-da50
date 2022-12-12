from __future__ import annotations
import abc

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Address import Address
    from pysarl.io.sarl.lang.core.EventListener import EventListener

from pysarl.io.sarl.lang.core.EventSpace import EventSpace


class OpenEventSpace(EventSpace, abc.ABC):

    """
    @param : participant
    @param : weakParticipant
    """
    def register(self, participant: EventListener, weakParticipant: bool = False) -> Address:
        if weakParticipant:
            return self.registerWeakParticipant(participant)
        else:
            return self.registerStrongParticipant(participant)

    """
        Register the strong participant in the space.
        @param : participant
    """
    @abc.abstractmethod
    def registerStrongParticipant(self, participant: EventListener) -> Address:
        pass

    """
        Register the weak participant in the space.
        @param : participant
    """
    @abc.abstractmethod
    def registerWeakParticipant(self, participant: EventListener) -> Address:
        pass

    """
        Unregister the entity inside the space
        @param : participant
    """
    @abc.abstractmethod
    def unregister(self, participant: EventListener) -> Address:
        pass
