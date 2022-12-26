from abc import ABC
from uuid import UUID

from pysarl.io.sarl.core.DefaultContextInteractions import DefaultContextInteractions
from pysarl.io.sarl.lang.core import Agent
from pysarl.io.sarl.lang.core.Address import Address
from pysarl.io.sarl.lang.core.Event import Event
from pysarl.io.sarl.lang.core.Scope import Scope
from pysarl.io.sarl.lang.core.Skill import Skill
from vm.builtin.service.Context import Context


class DefaultContextInteractionsSkill(Skill, DefaultContextInteractions, ABC):
    def __init__(self):
        super().__init__()

    def emit(self, event):
        dc = self.getDefaultContext()
        ds = dc.getDefaultSpace()
        ds.emit(event)

    def getDefaultContext(self):
        return self.getOwner().getDefaultContext()

    def getDefaultSpace(self):
        return self.getOwner().getDefaultContext().getDefaultSpace()

    def emitToParent(self, event: Event) -> None:
        return

    def getDefaultAddress(self) -> Address:
        return None

    def getDefaultParentID(self) -> UUID:
        return self.getParentID()

    def getDefaultParentScope(self) -> Scope[Address]:
        return None

    def isInDefaultSpace(self, event: Event) -> bool:
        return False
