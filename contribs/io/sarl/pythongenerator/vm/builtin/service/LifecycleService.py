import uuid


class LifecycleService:

    def __init__(self, defaultDynamicSkillProvider):
        self.__defaultDynamicSkillProvider = defaultDynamicSkillProvider

    def createAgent(self, agentClass, parentId = None, dynamicSkillProvider = None):
        if dynamicSkillProvider is None:
            dynamicSkillProvider = self.__defaultDynamicSkillProvider
        newAgent = agentClass(parentId, uuid.uuid4(), dynamicSkillProvider)
        myAgentEvents = newAgent.__guard_io_sarl_core_Initialize__(1)
        myAgentEvents[0](1)

