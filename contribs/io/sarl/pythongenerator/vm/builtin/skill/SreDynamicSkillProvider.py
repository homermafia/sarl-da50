from contribs.io.sarl.pythongenerator.api.agent.dynamicSkillProvider import DynamicSkillProvider
from contribs.io.sarl.pythongenerator.api.agent.skill import Skill
from contribs.io.sarl.pythongenerator.vm.builtin.capacity.Lifecycle import Lifecycle
from contribs.io.sarl.pythongenerator.vm.builtin.skill.LifecycleSkill import LifecycleSkill


class SreDynamicSkillProvider(DynamicSkillProvider):

    def __init__(self):
        self.__skillsDict = {
            Lifecycle: LifecycleSkill(self),
        }

    def createSkill(self, capacity) -> Skill:
        return self.__skillsDict[capacity]

    def isSkillProviding(self, capacity) -> bool:
        return self.__skillsDict.keys().__contains__(capacity)