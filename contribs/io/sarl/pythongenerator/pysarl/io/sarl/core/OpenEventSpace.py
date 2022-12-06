from pysarl.io.sarl.lang.core.EventSpace import EventSpace
from pysarl.io.sarl.lang.core.Address import Address
from pysarl.io.sarl.lang.core.EventListener import EventListener


class OpenEventSpace(EventSpace):
    """
    @param : participant
    @param : weakParticipant
    """

    def register(self, participant: EventListener, weakParticipant: bool) -> Address:
        pass

    """
        Register the strong participant in the space.
        @param : participant
    """

    def registerStrongParticipant(self, participant: EventListener) -> Address:
        pass

    """
        Register the weak participant in the space.
        @param : participant
    """

    def registerWeakParticipant(self, participant: EventListener) -> Address:
        pass

    """
        Unregister the entity inside the space
        @param : participant
    """

    def unregister(self, participant: EventListener) -> Address:
        pass
