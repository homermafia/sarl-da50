from pysarl.io.sarl.lang.core.DynamicSkillProvider import DynamicSkillProvider
from pysarl.io.sarl.lang.core.Skill import Skill
from vm.builtin.capacity.Lifecycle import Lifecycle
from vm.builtin.capacity.Logging import Logging
from vm.builtin.skill.LifecycleSkill import LifecycleSkill
from vm.builtin.skill.LoggingSkill import LoggingSkill


class SreDynamicSkillProvider(DynamicSkillProvider):

    def __init__(self):
        super().__init__()
        self.__skillsDict = {
            Lifecycle: LifecycleSkill(self),
            Logging: LoggingSkill()
        }

    def createSkill(self, capacity) -> Skill:
        return self.__skillsDict[capacity]

    def isSkillProviding(self, capacity) -> bool:
        return self.__skillsDict.keys().__contains__(capacity)
