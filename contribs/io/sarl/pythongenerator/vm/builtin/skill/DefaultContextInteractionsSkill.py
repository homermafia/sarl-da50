from contribs.io.sarl.pythongenerator.api.agent.skill import Skill
from contribs.io.sarl.pythongenerator.vm.builtin.capacity import DefaultContextInteractions
from contribs.io.sarl.pythongenerator.vm.builtin.service.Context import Context


class DefaultContextInteractionsSkill(Skill, DefaultContextInteractions):
    def __init__(self):
        self.defaultContext = Context()

    def emit(self, event, scope):
        return 0

    def getDefaultSpace(self):
        return self.defaultContext.getDefaultSpace()

    def getDefaultContext(self):
        return self.defaultContext