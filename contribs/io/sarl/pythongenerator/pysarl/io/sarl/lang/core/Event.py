from pysarl.io.sarl.lang.core.Address import Address
import uuid


class Event(object):

    def __init__(self, source: Address = None):
        self.__source = source

    """
        Return the source of the event
    """
    def getSource(self):
        return self.__source

    """
        @param source : the address of the source
    """
    def setSource(self, source: Address):
        self.__source = source

    """
        @param address : the address of the emitter
        Return true if the event was emitted by an entity with the address given in parameter
    """
    def isFromAddress(self, address: Address):
        return (self.__source is not None) and (self.__source.equals(address))

    """
        @param entityId : the id of the emitter 
        return true if the event was emitted by an entity with the id given in parameter
    """
    def isFromEntity(self, entityId: uuid):
        return (entityId is not None) and (self.__source is not None) and (self.__source.getParticipantId() == entityId)

    def __str__(self) -> str:
        return "Event{" + str(self.__source) + "}"