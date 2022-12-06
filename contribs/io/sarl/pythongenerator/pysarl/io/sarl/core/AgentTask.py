from pysarl.io.sarl.lang.core.SRESpecificDataContainer import SRESpecificDataContainer


class AgentTask(SRESpecificDataContainer):
    """
    return the guard of the task
    """

    def __init__(self, name: str, guard, procedure, initiator):
        self.__guard = guard
        self.__procedure = procedure
        self.__taskName = name
        self.__initiator = initiator

    def getGuard(self):
        return self.__guard

    """
    return the task name
    """
    def getName(self) -> str:
        return self.__taskName

    """
    return the procedure of the task
    """
    def getProcedure(self):
        return self.__procedure

    """
    return the initiator of the task
    """
    def getInitiator(self):
        return self.__initiator

    def ifTrue(self):
        pass

    """
    used to set the guard of the task
    @param : guard
    """
    def setGuard(self, guard):
        self.__guard = guard

    """
        used to set the procedure of the task
        @param : procedure
    """
    def setProcedure(self, procedure):
        self.__procedure = procedure

    """
        used to set the name of the task
        @param : name
    """
    def setTaskName(self, name: str):
        self.__taskName = name

    """
        used to print of the task's information
    """
    def toString(self) -> str:
        pass

    def unless(self, predicate):
        pass
