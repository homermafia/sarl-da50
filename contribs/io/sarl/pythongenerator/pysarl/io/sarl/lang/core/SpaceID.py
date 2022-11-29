from pysarl.io.sarl.lang.core.SpaceSpecification import SpaceSpecification
from pysarl.io.sarl.lang.core.SpaceID import SpaceID
import uuid
from typing import TypeVar

T = TypeVar('T', bound=SpaceSpecification)


class SpaceID(object):

    def __init__(self, contextID: uuid.UUID, identifier: uuid, spaceSpec: T):
        assert (contextID is not None) and (identifier is not None)
        self.__contextID = contextID
        self.__id = identifier
        self.__spaceSpec = spaceSpec

    """
        Return the identifier of the context where the space was created
    """
    def getContextID(self):
        return self.__contextID

    """
        Return the identifier for the Space
    """
    def getID(self):
        return self.__id

    """
        Return the SpaceSpecification of the Space
    """
    def getSpaceSpecification(self):
        return self.__spaceSpec

    def __str__(self) -> str:
        return "SpaceID{ContextID : " + str(self.__contextID) + ", ID : " + str(self.__id) + "}"

    """
        @:param : the identifier of the space
        Return true if the contextID correspond to the contextID of the spaceId
    """
    def equalsContext(self, spaceId):
        if self.__contextID is None:
            return spaceId.getContextID() is None
        return self.__contextID == spaceId.getContextID()

    """
        @:param : the identifier of the space
        Return : ...
    """
    def equalsID(self, spaceId):
        if self.__id is None:
            return spaceId.getID() is None
        return self.__id == spaceId.getID()

    """
        @:param : the identifier of the space
        Return :
                - if the spaceID is none : false
                - ... : false
                - true if the spaceID is equal to ...  
    """
    def equals(self, spaceId):
        if spaceId is None:
            return False
        if not self.equalsContext(spaceId):
            return False
        return self.equalsID(spaceId)

    def clone(self):
        pass

    """
        @param : SpaceID
        Return : a integer
    """
    def compareTo(self, otherID: SpaceID) -> int:
        pass