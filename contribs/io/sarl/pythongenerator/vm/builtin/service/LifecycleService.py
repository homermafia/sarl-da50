import uuid

from pysarl.io.sarl.core.AgentKilled import AgentKilled
from pysarl.io.sarl.core.AgentSpawned import AgentSpawned
from pysarl.io.sarl.core.Destroy import Destroy
from pysarl.io.sarl.core.Initialize import Initialize
from vm.builtin.EventDispatcher import EventDispatcher
from vm.builtin.service.PythonContext import PythonContext
from vm.builtin.skill.DefaultContextInteractionsSkill import DefaultContextInteractionsSkill
from vm.utils.singleton import singleton


@singleton
class LifecycleService:
    __agents = []
    __defaultDynamicSkillProvider = None
    __eventDispatcher = None

    def __init__(self, defaultDynamicSkillProvider):
        self.__defaultDynamicSkillProvider = defaultDynamicSkillProvider
        self.__world = PythonContext()

    def createAgent(self, agentClass, parentId = None, dynamicSkillProvider = None, *parameters):
        if dynamicSkillProvider is None:
            dynamicSkillProvider = self.__defaultDynamicSkillProvider
        newAgent = agentClass(parentId, uuid.uuid4(), self.__world, dynamicSkillProvider)
        self.__agents.append(newAgent)
        newAgent.getDefaultContext().getDefaultSpace().register(newAgent)
        errors = newAgent.getDefaultContext().getDefaultSpace().emit(newAgent, Initialize(parentId, *parameters))
        if len(errors) > 0:
            self.__agents.remove(newAgent)
            newAgent.getDefaultContext().getDefaultSpace().unregister(newAgent)
        # We check that the agent hasn't been killed during the Initialize process
        # and we check that no exceptions were thrown during the Initialize process
        if newAgent in self.__agents:
            newAgent.getDefaultContext().getDefaultSpace().emit(newAgent,
                                            AgentSpawned(None, newAgent.getID(), agentClass.__name__))


    def killAgent(self, agent, forceKillable, terminationCause):
        self.__agents.remove(agent)
        agent.getDefaultContext().getDefaultSpace().emit(agent, Destroy())
        agent.getDefaultContext().getDefaultSpace().emit(agent, AgentKilled(None, type(agent).__name__, terminationCause))
        agent.getDefaultContext().getDefaultSpace().unregister(agent)

    def killAgentsLeft(self):
        for a in self.__agents:
            self.killAgent(a, False, "End of the program")
