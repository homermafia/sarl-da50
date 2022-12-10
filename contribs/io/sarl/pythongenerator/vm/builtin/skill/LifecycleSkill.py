from pysarl.io.sarl.lang.core.Skill import Skill
from vm.builtin.capacity.Lifecycle import Lifecycle
from vm.builtin.service.LifecycleService import LifecycleService
from vm.builtin.exceptions.KillMeException import KillMeException


class LifecycleSkill(Skill, Lifecycle, object):

    def __init__(self, dynamicSkillProvider):
        super().__init__()
        self.__lifecycleService = LifecycleService(dynamicSkillProvider)

    def spawn(self, agentClass):
        self.__lifecycleService.createAgent(agentClass, self.getOwner().getID())

    def killMe(self, terminationCause=None):
        self.__lifecycleService.killAgent(self.getOwner(), False, terminationCause)
        raise KillMeException()
