import uuid

from pysarl.io.sarl.core.AgentKilled import AgentKilled
from pysarl.io.sarl.core.AgentSpawned import AgentSpawned
from pysarl.io.sarl.core.Destroy import Destroy
from pysarl.io.sarl.core.Initialize import Initialize
from vm.builtin.EventDispatcher import EventDispatcher
from vm.utils.singleton import singleton


@singleton
class LifecycleService:
    __agents = []
    __defaultDynamicSkillProvider = None
    __eventDispatcher = None

    def __init__(self, defaultDynamicSkillProvider):
        self.__defaultDynamicSkillProvider = defaultDynamicSkillProvider
        self.__eventDispatcher = EventDispatcher()

    def createAgent(self, agentClass, parentId = None, dynamicSkillProvider = None):
        if dynamicSkillProvider is None:
            dynamicSkillProvider = self.__defaultDynamicSkillProvider
        newAgent = agentClass(parentId, uuid.uuid4(), dynamicSkillProvider)
        self.__agents.append(newAgent)
        self.__eventDispatcher.register(newAgent)
        errors = self.__eventDispatcher.dispatch(newAgent, Initialize(parentId))
        if len(errors) > 0:
            self.__agents.remove(newAgent)
            self.__eventDispatcher.unregister(newAgent)
        # We check that the agent hasn't been killed during the Initialize process
        # and we check that no exceptions were thrown during the Initialize process
        if newAgent in self.__agents:
            self.__eventDispatcher.dispatch(newAgent,
                                            AgentSpawned(None, newAgent.getID(), agentClass.__name__))

    def killAgent(self, agent, forceKillable, terminationCause):
        self.__agents.remove(agent)
        self.__eventDispatcher.dispatch(agent, Destroy())
        self.__eventDispatcher.dispatch(agent, AgentKilled(None, type(agent).__name__, terminationCause))
        self.__eventDispatcher.unregister(agent)

    def killAgentsLeft(self):
        for a in self.__agents:
            self.killAgent(a, False, "End of the program")
