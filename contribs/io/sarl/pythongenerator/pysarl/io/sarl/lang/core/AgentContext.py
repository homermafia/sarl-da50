import abc
from typing import TypeVar, List, Type
from uuid import UUID
from multipledispatch import dispatch

from pysarl.io.sarl.lang.core.Space import Space
from pysarl.io.sarl.lang.core.EventSpace import EventSpace
from pysarl.io.sarl.lang.core.SpaceSpecification import SpaceSpecification

T = TypeVar('T', bound=Space)


class AgentContext(abc.ABC):

    @abc.abstractmethod
    def getID(self) -> UUID:
        pass

    @abc.abstractmethod
    def getDefaultSpace(self) -> EventSpace:
        pass

    @abc.abstractmethod
    def getSpaces(self, spec: Type[SpaceSpecification] = None) -> List[T]:
        pass

    @abc.abstractmethod
    def createSpace(self, spec: Type[SpaceSpecification], spaceUUID: UUID, *creationParams: object) -> T:
        pass

    @abc.abstractmethod
    def getOrCreateSpace(self, spec: Type[SpaceSpecification], spaceUUID: UUID, *creationParams: object) -> T:
        return self.getOrCreateSpaceWithSpec(spec, spaceUUID, *creationParams)

    @abc.abstractmethod
    def getOrCreateSpaceWithSpec(self, spec: Type[SpaceSpecification], spaceUUID: UUID, *creationParams: object) -> T:
        pass

    @dispatch(UUID, SpaceSpecification.__class__, [object])
    @abc.abstractmethod
    def getOrCreateSpaceWithID(self, spaceUUID: UUID, spec: Type[SpaceSpecification], *creationParams: object) -> T:
        return self.getOrCreateSpaceWithID(spec, spaceUUID, *creationParams)

    @dispatch(SpaceSpecification.__class__, UUID, [object])
    @abc.abstractmethod
    def getOrCreateSpaceWithID(self, spec: Type[SpaceSpecification], spaceUUID: UUID, *creationParams: object) -> T:
        pass

    @abc.abstractmethod
    def getSpace(self, spaceUUID: UUID) -> T:
        pass

    @abc.abstractmethod
    def isRootContext(self) -> bool:
        pass