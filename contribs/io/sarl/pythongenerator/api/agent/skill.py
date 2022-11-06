from contribs.io.sarl.pythongenerator.api.agent.agentTrait import AgentTrait
from contribs.io.sarl.pythongenerator.api.agent.agent import Agent


class Skill(AgentTrait):

    def __init__(self, agent: Agent = None):
        super().__init__(agent)