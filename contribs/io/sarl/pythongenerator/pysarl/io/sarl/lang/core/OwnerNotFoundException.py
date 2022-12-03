from pysarl.io.sarl.lang.core.AgentTrait import AgentTrait

class OwnerNotFoundException(Exception):

    def __init__(self, trait: AgentTrait):
        self.__trait = trait

	""" Return the agent trait """
	def getAgentTrait(self) -> AgentTrait:
		return self.__trait