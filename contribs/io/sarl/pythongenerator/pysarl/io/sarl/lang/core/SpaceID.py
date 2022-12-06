from __future__ import annotations
import copy

from uuid import UUID
from typing import TypeVar, Type, TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.SpaceSpecification import SpaceSpecification

    T = TypeVar('T', bound=Type[SpaceSpecification])

from pysarl.io.sarl.lang.core.SRESpecificDataContainer import SRESpecificDataContainer


class SpaceID(SRESpecificDataContainer):
    __id: UUID
    contextID: UUID
    spaceSpec: T

    def __init__(self, contextID: UUID, identifier: UUID, spaceSpec: T):
        assert contextID is not None
        assert identifier is not None
        self.__id = identifier
        self.__contextID = contextID
        self.__spaceSpec = spaceSpec

    def clone(self) -> "SpaceID":
        # shallow copy
        try:
            return copy.copy(self)
        except copy.Error as e:
            raise Exception(e)

    """
        Return the identifier for the Space
    """
    def getID(self) -> UUID:
        return self.__id

    """
        Return the identifier of the context where the space was created
    """
    def getContextID(self) -> UUID:
        return self.__contextID

    """
        Return the SpaceSpecification of the Space
    """
    def getSpaceSpecification(self) -> T:
        return self.__spaceSpec

    """
        @:param : the identifier of the space
        Return :
                - if the spaceID is none : false
                - ... : false
                - true if the spaceID is equal to ...  
    """
    def equals(self, obj: object) -> bool:
        if self == obj:
            return True
        if obj is None:
            return False
        if type(obj) != SpaceID:
            return False
        if not self.equalsContext(obj):
            return False
        return self.equalsID(obj)

    """
        @:param : the identifier of the space
        Return true if the contextID correspond to the contextID of the spaceId
    """
    def equalsContext(self, other: "SpaceID"):
        if self.__contextID is None:
            return other.getContextID() is None
        return self.__contextID == other.getContextID()

    """
        @:param : the identifier of the space
        Return : ...
    """
    def equalsID(self, other: "SpaceID"):
        if self.__id is None:
            return other.getID() is None
        return self.__id == other.getID()

    def __str__(self) -> str:
        return "SpaceID{ContextID : " + str(self.__contextID) + ", ID : " + str(self.__id) + "}"

    """
        @param : SpaceID
        Return : a integer
    """
    def compareTo(self, otherID: "SpaceID") -> int:
        # TODO: the int value returned is correct sign-wise, but not value-wise
        if self.__contextID == otherID.__contextID:
            if self.__id == otherID.__id:
                return 0
            elif self.__id > otherID.__id:
                return 1
            else:
                return -1
        else:
            if self.__contextID > otherID.__contextID:
                return 1
            else:
                return -1
