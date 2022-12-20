from abc import ABC

from pysarl.io.sarl.core.DefaultContextInteractions import DefaultContextInteractions
from pysarl.io.sarl.lang.core.Skill import Skill
from vm.builtin.service.Context import Context


class DefaultContextInteractionsSkill(Skill, DefaultContextInteractions, ABC):
    def __init__(self):
        self.defaultContext = Context()

    def emit(self, event, scope):
        return 0

    def getDefaultSpace(self):
        return self.defaultContext.getDefaultSpace()

    def getDefaultContext(self):
        return self.defaultContext
