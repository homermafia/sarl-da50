from contribs.io.sarl.pythongenerator.api.agent.dynamicSkillProvider import DynamicSkillProvider
from contribs.io.sarl.pythongenerator.api.agent.skill import Skill
from contribs.io.sarl.pythongenerator.vm.builtin.capacity.Lifecycle import Lifecycle
from contribs.io.sarl.pythongenerator.vm.builtin.capacity.Logging import Logging
from contribs.io.sarl.pythongenerator.vm.builtin.skill.LifecycleSkill import LifecycleSkill
from contribs.io.sarl.pythongenerator.vm.builtin.skill.LoggingSkill import LoggingSkill


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
