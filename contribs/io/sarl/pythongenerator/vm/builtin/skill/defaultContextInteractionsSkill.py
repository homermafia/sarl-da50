from contribs.io.sarl.pythongenerator.api.agent.skill import Skill
from contribs.io.sarl.pythongenerator.vm.builtin.capacity.defaultContextInteractions import DefaultContextInteractions


class DefaultContextInteractionsSkill(Skill,DefaultContextInteractions, object):

    def __init__(self, dynamicSkillProvider):
        super().__init__()

    def getDefaultContext(self, agentClass, occurrence = None):
        pass
