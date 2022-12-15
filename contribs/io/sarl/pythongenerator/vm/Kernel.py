from vm.builtin.service.LifecycleService import LifecycleService
from vm.builtin.skill.SreDynamicSkillProvider import SreDynamicSkillProvider


class Kernel:

    def __init__(self):
        self.__lifecycleService = LifecycleService(SreDynamicSkillProvider())

    def start(self, bootAgentClass):
        self.__lifecycleService.createAgent(bootAgentClass)
        self.__lifecycleService.killAgentsLeft()
