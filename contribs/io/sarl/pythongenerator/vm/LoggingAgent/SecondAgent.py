
from pysarl.io.sarl.lang.core.Agent import Agent
from vm.builtin.skill.LoggingSkill import LoggingSkill
from pysarl.io.sarl.core.Logging import Logging
from vm.builtin.service.Context import Context


class SecondAgent(Agent, object):

    def __on_Initialize__(self, occurrence):
        s = LoggingSkill()
        self.setSkill(s)
        self.getSkill(Logging).info(u"Nouvel agent")

    def __guard_io_sarl_core_Initialize__(self, occurrence):
        it = occurrence
        __event_handles = list()
        __event_handles.append(self.__on_Initialize__)
        return __event_handles

    def __init__(self, parentID, agentID, context: Context, dynamicSkillProvider = None):
        super().__init__(parentID, agentID, context, dynamicSkillProvider)