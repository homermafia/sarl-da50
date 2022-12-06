from __future__ import annotations

import abc
from typing import TypeVar, Type, TYPE_CHECKING
from uuid import UUID

from multipledispatch import dispatch

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.AtomicSkillReference import AtomicSkillReference
    from pysarl.io.sarl.lang.core.Capacity import Capacity
    from pysarl.io.sarl.lang.core.Event import Event
    from pysarl.io.sarl.lang.core.Skill import Skill

    C = TypeVar('C', bound=Type[Capacity])
    S = TypeVar('S', bound=Capacity)
    Sk = TypeVar('Sk', bound=Skill)

from pysarl.io.sarl.lang.core.Address import Address
from pysarl.io.sarl.lang.core.SRESpecificDataContainer import SRESpecificDataContainer


class AgentProtectedAPIObject(SRESpecificDataContainer, abc.ABC):

    @abc.abstractmethod
    def __str__(self) -> str:
        pass

    @abc.abstractmethod
    def getSkill(self, capacity: C) -> S:
        pass

    @abc.abstractmethod
    def _getSkill(self, capacity: C) -> AtomicSkillReference:
        pass

    @abc.abstractmethod
    def operator_mappedTo(self, capacity: C, skill: Sk) -> None:
        pass

    @abc.abstractmethod
    def setSkill(self, skill: Skill, *capacities: C) -> Sk:
        pass

    @abc.abstractmethod
    def setSkillIfAbsent(self, skill: Skill, *capacities: C) -> None:
        pass

    @abc.abstractmethod
    def clearSkill(self, capacity: C) -> S:
        pass

    @abc.abstractmethod
    def hasSkill(self, capacity: C) -> bool:
        pass

    @dispatch(Address)
    @abc.abstractmethod
    def isMe(self, address: Address) -> bool:
        pass

    @dispatch(UUID)
    @abc.abstractmethod
    def isMe(self, uID: UUID) -> bool:
        pass

    @abc.abstractmethod
    def isFromMe(self, event: Event) -> bool:
        pass
