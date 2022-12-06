from __future__ import annotations
import copy
from uuid import UUID
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.SpaceID import SpaceID

from pysarl.io.sarl.lang.core.SRESpecificDataContainer import SRESpecificDataContainer


class Address(SRESpecificDataContainer):
    __participantId: UUID
    __spaceId: SpaceID

    def __init__(self, spaceId: SpaceID, participantId: UUID):
        assert spaceId is not None
        assert participantId is not None

        self.__participantId = participantId
        self.__spaceId = spaceId

    def clone(self) -> "Address":
        # shallow copy
        try:
            return copy.copy(self)
        except copy.Error as e:
            raise Exception(e)

    def __str__(self) -> str:
        return "Address{" + str(self.__spaceId) + ", ParticipantId : " + str(self.__participantId) + "}"

    def getUUID(self) -> UUID:
        return self.getID()

    def getID(self) -> UUID:
        return self.__participantId

    def equals(self, address: "Address") -> bool:
        return (address is not None) and (self.__participantId == address.getID()) and (self.__spaceId.equals(address.getSpaceID()))

    def getSpaceID(self) -> SpaceID:
        return self.__spaceId

    def getSpaceId(self) -> SpaceID:
        return self.getSpaceID()
