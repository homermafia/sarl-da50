import uuid

from contribs.io.sarl.pythongenerator.vm.builtin.EventDispatcher import EventDispatcher
from contribs.io.sarl.pythongenerator.vm.builtin.event.Destroy import Destroy
from contribs.io.sarl.pythongenerator.vm.builtin.event.Initialize import Initialize
from contribs.io.sarl.pythongenerator.vm.builtin.event.AgentSpawned import AgentSpawned
from contribs.io.sarl.pythongenerator.vm.builtin.event.AgentKilled import AgentKilled


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
        self.__eventDispatcher.dispatch(newAgent, Initialize(parentId))
        # We check that the agent hasn't been killed during the Initialize process
        if newAgent in self.__agents:
            self.__eventDispatcher.dispatch(newAgent,
                                            AgentSpawned(None, newAgent.getID(), agentClass.__name__))

    def killAgent(self, agent, forceKillable, terminationCause):
        self.__agents.remove(agent)
        self.__eventDispatcher.dispatch(agent, Destroy())
        self.__eventDispatcher.dispatch(agent, AgentKilled(None, type(agent).__name__))
        self.__eventDispatcher.unregister(agent)


