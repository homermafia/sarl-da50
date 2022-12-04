
from pysarl.io.sarl.lang.core.Agent import Agent
from vm.LoggingAgent.LoggingSkill import LoggingSkill
from vm.LoggingAgent.Logging import Logging


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

    def __init__(self, parentID, agentID, dynamicSkillProvider = None):
        super().__init__(parentID, agentID, dynamicSkillProvider)