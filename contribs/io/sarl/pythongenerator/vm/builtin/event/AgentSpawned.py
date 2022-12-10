from pysarl.io.sarl.lang.core.Event import Event


class AgentSpawned(Event):

    def __init__(self, sourceAddress, agentId, agentType: str):
        super().__init__(sourceAddress)
        self.__agentId = agentId
        self.__agentType = agentType

    def getAgentId(self):
        return self.__agentId

    def getAgentType(self):
        return self.__agentType
