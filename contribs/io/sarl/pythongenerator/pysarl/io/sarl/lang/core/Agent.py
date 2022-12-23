from __future__ import annotations
from typing import Callable, TYPE_CHECKING
from uuid import UUID
from multipledispatch import dispatch

from pysarl.io.sarl.lang.core.AbstractSkillContainer import AbstractSkillContainer
from pysarl.io.sarl.lang.core.Address import Address
from pysarl.io.sarl.lang.core.IBehaviorGuardEvaluatorReceiver import IBehaviorGuardEvaluatorReceiver
from vm.builtin.service.Context import Context
from vm.builtin.service.PythonContext import PythonContext

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.DynamicSkillProvider import DynamicSkillProvider
    from pysarl.io.sarl.lang.core.Event import Event
    from pysarl.io.sarl.lang.core.Skill import Skill


class Agent(AbstractSkillContainer, IBehaviorGuardEvaluatorReceiver):
    __id: UUID
    __parentID: UUID
    __skillCallback: Callable[["Agent", Skill], None]

    def __init__(self, parentID: UUID, agentID: UUID, dynamicSkillProvider: DynamicSkillProvider = None):
        super(Agent, self).__init__(dynamicSkillProvider)
        self.__parentID = parentID
        self.__id = agentID if agentID is not None else UUID()
        self.__skillCallback = None
        self.__defaultContext = PythonContext()

    def __str__(self) -> str:
        return "Agent{ID:" + str(self.__id) + ", parentID:" + str(self.__parentID) + "}"

    def _attachOwner(self, skill: Skill) -> None:
        skill.setOwner(self)
        if self.__skillCallback is not None:
            self.__skillCallback(self, skill)

    def setSkillCallback(self, callback: Callable[["Agent", Skill], None]) -> None:
        self.__skillCallback = callback

    # Temporary, we should add a defaultContext attribute to Agent
    def getDefaultContext(self) -> Context:
        return self.__defaultContext

    def getParentID(self) -> UUID:
        return self.__parentID

    def getID(self) -> UUID:
        return self.__id

    @dispatch(Address)
    def isMe(self, address: Address) -> bool:
        return address is not None and self.isMe(address.getID())

    @dispatch(UUID)
    def isMe(self, uID: UUID) -> bool:
        return uID is not None and uID == self.__id

    def isFromMe(self, event: Event) -> bool:
        return event is not None and self.isMe(event.getSource())
