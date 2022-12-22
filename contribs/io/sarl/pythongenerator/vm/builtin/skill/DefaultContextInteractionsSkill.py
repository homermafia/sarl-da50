from abc import ABC

from pysarl.io.sarl.core.DefaultContextInteractions import DefaultContextInteractions
from pysarl.io.sarl.lang.core import Agent
from pysarl.io.sarl.lang.core.Skill import Skill
from vm.builtin.service.Context import Context


class DefaultContextInteractionsSkill(Skill, DefaultContextInteractions, ABC):
    def __init__(self, owner: Agent):
        self.__owner = owner

    def emit(self, event):
        dc = self.getDefaultContext()
        ds = dc.getDefaultSpace()
        ds.emit(self.__owner, event)

    def getDefaultContext(self):
        return self.__owner.getDefaultContext()
