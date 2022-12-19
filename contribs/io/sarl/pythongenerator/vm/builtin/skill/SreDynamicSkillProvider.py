from pysarl.io.sarl.core.Lifecycle import Lifecycle
from pysarl.io.sarl.core.Logging import Logging
from pysarl.io.sarl.lang.core.DynamicSkillProvider import DynamicSkillProvider
from pysarl.io.sarl.lang.core.Skill import Skill
from vm.builtin.skill.LifecycleSkill import LifecycleSkill
from vm.builtin.skill.LoggingSkill import LoggingSkill


class SreDynamicSkillProvider(DynamicSkillProvider):

    def __init__(self):
        super().__init__()

    def createSkill(self, capacity) -> Skill:
        if capacity == Lifecycle:
            return LifecycleSkill(self)
        elif capacity == Logging:
            return LoggingSkill()

    def isSkillProviding(self, capacity) -> bool:
        return capacity == Lifecycle \
               or capacity == Logging
