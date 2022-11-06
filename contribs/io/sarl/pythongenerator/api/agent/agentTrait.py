from contribs.io.sarl.pythongenerator.api.agent.agent import Agent


class AgentTrait(object):

    def __init__(self, agent: Agent = None):
        self.__agentRef = agent

    def setOwner(self, agent):
        self.__agentRef = agent

    def getOwner(self):
        return self.__agentRef

    def getSkill(self, capacity):
        assert self.__agentRef is not None
        return self.__agentRef.getSkill(capacity)

    def setSkill(self, skill, *capacities):
        if self.__agentRef is None:
            return skill
        self.__agentRef.setSkill(skill, capacities)

