from __future__ import annotations
import abc
import weakref
from typing import TypeVar, Type, TYPE_CHECKING
from uuid import UUID

from multipledispatch import dispatch

from pysarl.io.sarl.lang.core.Address import Address
from pysarl.io.sarl.lang.core.AgentProtectedAPIObject import AgentProtectedAPIObject
from pysarl.io.sarl.lang.core.OwnerNotFoundException import OwnerNotFoundException
from pysarl.io.sarl.lang.core.UnimplementedCapacityException import UnimplementedCapacityException

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Agent import Agent
    from pysarl.io.sarl.lang.core.AtomicSkillReference import AtomicSkillReference
    from pysarl.io.sarl.lang.core.Capacity import Capacity
    from pysarl.io.sarl.lang.core.Event import Event
    from pysarl.io.sarl.lang.core.Skill import Skill

    C = TypeVar('C', bound=Type[Capacity])
    S = TypeVar('S', bound=Capacity)
    Sk = TypeVar('Sk', bound=Skill)


class AgentTrait(AgentProtectedAPIObject, abc.ABC):
    __agentRef: weakref.ref

    def __init__(self, agent: Agent = None):
        # WARNING: Cannot create a weak reference to an object of type None, so we create a callback that returns None
        if agent is None:
            self.__agentRef = lambda: None
        else:
            self.__agentRef = weakref.ref(agent)

    def __str__(self) -> str:
        return "AgentTrait{Owner : " + str(self.getOwner()) + "}"

    def setOwner(self, agent: Agent) -> None:
        if agent is None:
            self.__agentRef = lambda: None
        else:
            self.__agentRef = weakref.ref(agent)

    def getOwner(self) -> Agent:
        return self.__agentRef()

    def getOwnerClassName(self) -> str:
        return self.getOwner().__class__.__name__

    def getID(self) -> UUID:
        return self.getOwner().getID()

    def getSkill(self, capacity: C) -> S:
        assert capacity is not None
        skill: AtomicSkillReference = self._getSkill(capacity)
        assert skill is not None
        return self._castSkill(capacity, skill)

    def _castSkill(self, capacity: C, skillReference: AtomicSkillReference) -> S:
        if skillReference is not None:
            return skillReference.get()
        raise UnimplementedCapacityException(capacity, self.getOwner().getID())

    def _getSkill(self, capacity: C) -> AtomicSkillReference:
        owner: Agent = self.getOwner()
        if owner is None:
            raise OwnerNotFoundException(self)
        return owner._getSkill(capacity)

    def operator_mappedTo(self, capacity: C, skill: Sk) -> None:
        self.setSkill(skill, capacity)

    def setSkill(self, skill: Skill, *capacities: C) -> Sk:
        owner: Agent = self.getOwner()
        if owner is None:
            return skill
        return owner.setSkill(skill, *capacities)

    def setSkillIfAbsent(self, skill: Skill, *capacities: C) -> None:
        owner: Agent = self.getOwner()
        if owner is not None:
            owner.setSkillIfAbsent(skill, *capacities)

    def clearSkill(self, capacity: C) -> S:
        owner: Agent = self.getOwner()
        if owner is None:
            return None
        return owner.clearSkill(capacity)

    def hasSkill(self, capacity: C) -> bool:
        owner: Agent = self.getOwner()
        if owner is None:
            return False
        return owner.hasSkill(capacity)

    @dispatch(Address)
    def isMe(self, address: Address) -> bool:
        owner: Agent = self.getOwner()
        if owner is None:
            return False
        return owner.isMe(address)

    @dispatch(UUID)
    def isMe(self, uID: UUID) -> bool:
        owner: Agent = self.getOwner()
        if owner is None:
            return False
        return owner.isMe(uID)

    def isFromMe(self, event: Event) -> bool:
        owner: Agent = self.getOwner()
        if owner is None:
            return False
        return owner.isFromMe(event)
