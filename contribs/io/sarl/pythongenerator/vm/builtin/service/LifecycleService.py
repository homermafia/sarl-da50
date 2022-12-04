import uuid

from vm.builtin.EventDispatcher import EventDispatcher
from vm.builtin.event.Destroy import Destroy
from vm.builtin.event.Initialize import Initialize

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

    def killAgent(self, agent, forceKillable, terminationCause):
        self.__agents.index(agent)
        self.__eventDispatcher.dispatch(agent, Destroy())
        self.__eventDispatcher.unregister(agent)


