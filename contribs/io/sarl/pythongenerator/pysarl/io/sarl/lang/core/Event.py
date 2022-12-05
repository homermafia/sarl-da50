import abc

from multipledispatch import dispatch

from pysarl.io.sarl.lang.core.Address import Address
from uuid import UUID


class Event(abc.ABC):
    __source: Address

    def __init__(self, source: Address = None):
        self.__source = source

    def equals(self, obj: object) -> bool:
        if self == obj:
            return True
        if obj is not None and self.__class__ == obj.__class__:
            return (self.__source is None and obj.__source is None) or (self.__source is not None and self.__source.equals(obj.__source))
        return False

    """
        Return the source of the event
    """
    def getSource(self) -> Address:
        return self.__source

    """
        @param source : the address of the source
    """
    def setSource(self, source: Address) -> None:
        self.__source = source

    def __str__(self) -> str:
        return "Event{" + str(self.__source) + "}"

    """
        @param address : the address of the emitter
        Return true if the event was emitted by an entity with the address given in parameter
    """
    @dispatch(Address)
    def isFrom(self, address: Address) -> bool:
        return address is not None and address.equals(self.getSource())

    """
        @param entityId : the id of the emitter 
        return true if the event was emitted by an entity with the id given in parameter
    """
    @dispatch(UUID)
    def isFrom(self, entityId: UUID) -> bool:
        iSource: Address = self.getSource()
        return (entityId is not None) and (iSource is not None) and entityId == iSource.getID()
