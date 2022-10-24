from contribs.io.sarl.pythongenerator.api.agent.skill import Skill


class DynamicSkillProvider:

    def __init__(self):
        pass

    def createSkill(self, capacity) -> Skill:
        raise Exception("Unimplemented function")

    def isSkillProviding(self, capacity) -> bool:
        raise Exception("Unimplemented function")


class EmptyDynamicSkillProvider(DynamicSkillProvider):

    def __int__(self):
        pass

    def createSkill(self, capacity) -> Skill:
        return None

    def isSkillProviding(self, capacity) -> bool:
        return False