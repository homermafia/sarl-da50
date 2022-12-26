from __future__ import annotations
import abc
from typing import Callable, TYPE_CHECKING
from uuid import UUID

from multipledispatch import dispatch

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.SpaceID import SpaceID


class Space(abc.ABC):

    @abc.abstractmethod
    def getSpaceID(self) -> SpaceID:
        # Replies the Identification of this Interaction Space
        pass

    @dispatch()
    def isPseudoEmpty(self) -> bool:
        # Replies if the space could be considered as empty
        return self.getNumberOfStrongParticipants() == 0

    @dispatch(UUID)
    @abc.abstractmethod
    def isPseudoEmpty(self, identifier: UUID) -> bool:
        # Replies if the space is empty or the given identifier is associated to the only one participant to the space
        pass

    @abc.abstractmethod
    def emit(self):
        pass

    # @abc.abstractmethod
    # def getNumberOfStrongParticipants(self) -> int:
    #     # Replies the number of strong participants to the space
    #     pass
    #
    # @abc.abstractmethod
    # def getNumberOfWeakParticipants(self) -> int:
    #     # Replies the number of weak participants to the space
    #     pass
    #
    # @abc.abstractmethod
    # def forEachStrongParticipant(self, callback: Callable[[UUID], None]):
    #     pass
    #
    # @abc.abstractmethod
    # def forEachWeakParticipant(self, callback: Callable[[UUID], None]) -> None:
    #     pass
