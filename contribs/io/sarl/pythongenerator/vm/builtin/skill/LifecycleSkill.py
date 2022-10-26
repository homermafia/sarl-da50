from contribs.io.sarl.pythongenerator.api.agent.skill import Skill
from contribs.io.sarl.pythongenerator.vm.builtin.capacity.Lifecycle import Lifecycle
from contribs.io.sarl.pythongenerator.vm.builtin.service.LifecycleService import LifecycleService


class LifecycleSkill(Skill, Lifecycle, object):

    def __init__(self, dynamicSkillProvider):
        super().__init__()
        self.__lifecycleService = LifecycleService(dynamicSkillProvider)

    def spawn(self, agentClass):
        self.__lifecycleService.createAgent(agentClass, self.getOwner().getID())
