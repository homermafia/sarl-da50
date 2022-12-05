import abc

from pysarl.io.sarl.lang.core.Agent import Agent
from pysarl.io.sarl.lang.core.AgentTrait import AgentTrait
from pysarl.io.sarl.lang.core.Capacities import Capacities
from pysarl.io.sarl.lang.core.IBehaviorGuardEvaluatorReceiver import IBehaviorGuardEvaluatorReceiver


class Skill(abc.ABC, AgentTrait, IBehaviorGuardEvaluatorReceiver):
    __referencesFromCapacityMap: int

    def __init__(self, agent: Agent = None):
        AgentTrait.__init__(self, agent)
        self.__referencesFromCapacityMap = 0

    def setOwner(self, agent: Agent) -> None:
        AgentTrait.setOwner(self, agent)
        self.__referencesFromCapacityMap = 0

    def getCaller(self) -> AgentTrait:
        return Capacities.getCaller(self)

    def install(self) -> None:
        pass

    def prepareUninstallation(self) -> None:
        pass

    def uninstall(self) -> None:
        pass

    def increaseReference(self) -> None:
        oldValue: int = self.__referencesFromCapacityMap
        self.__referencesFromCapacityMap = self.__referencesFromCapacityMap + 1
        if oldValue <= 0:
            self.install()

    def decreaseReference(self) -> None:
        newValue: int = self.__referencesFromCapacityMap - 1
        self.__referencesFromCapacityMap = newValue
        if newValue <= 0:
            self.prepareUninstallation()
            self.uninstall()

    def getReferenceCount(self) -> int:
        return self.__referencesFromCapacityMap
