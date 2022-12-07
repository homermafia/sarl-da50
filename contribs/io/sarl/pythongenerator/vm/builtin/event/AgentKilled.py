from contribs.io.sarl.pythongenerator.api.event.event import Event


class AgentKilled(Event):

    def __init__(self, sourceAddress, agentType: str, terminationCause = None):
        super().__init__(sourceAddress)
        self.__agentType = agentType
        self.__terminationCause = terminationCause

    def getAgentType(self):
        return self.__agentType

    def getTerminationCause(self):
        return self.__terminationCause
