from pysarl.io.sarl.lang.core.AgentTrait import AgentTrait

class OwnerNotFoundException(): #RuntimeException

    def __init__(self, trait: AgentTrait):
        self.__trait = trait

	""" Return the agent trait"""
	def getAgentTrait(self):
		return self.__trait

  	""" @param trait the source of the exception """
	def OwnerNotFoundException(self, trait: AgentTrait):
		self.__trait = trait
		pass