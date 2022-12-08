from __future__ import annotations
from typing import Callable, TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Agent import Agent

from pysarl.io.sarl.lang.core.SRESpecificDataContainer import SRESpecificDataContainer


class AgentTask(SRESpecificDataContainer):
    TRUE_GUARD: Callable[[Agent], bool] = lambda a: True
    FALSE_GUARD: Callable[[Agent], bool] = lambda a: False
    __name: str
    __guard: Callable[[Agent], bool]
    __procedure: Callable[[Agent], None]
    __initiator: object

    """
        return the guard of the task
    """
    def __init__(self, name: str, initiator: object = None):
        assert name is not None
        self.__name = name
        self.__initiator = initiator

    """
        return the procedure of the task
    """
    def getProcedure(self) -> Callable[[Agent], None]:
        return self.__procedure

    """
        used to set the procedure of the task
        @param : procedure
    """
    def setProcedure(self, procedure: Callable[[Agent], None]) -> None:
        self.__procedure = procedure

    def getGuard(self) -> Callable[[Agent], bool]:
        return self.__guard

    """
        used to set the guard of the task
        @param : guard
    """
    def setGuard(self, guard: Callable[[Agent], bool]) -> None:
        self.__guard = guard

    """
        return the task name
    """
    def getName(self) -> str:
        return self.__name

    """
        used to set the name of the task
        @param : name
    """
    def setTaskName(self, name: str) -> None:
        assert name is not None
        self.__name = name

    """
        Change the guard of this that with the negation of the given predicate.
    """
    def unless(self, predicate: Callable[[Agent], bool]) -> "AgentTask":
        if predicate is None:
            self.__guard = AgentTask.FALSE_GUARD
        else:
            self.__guard: Callable[[Agent], bool] = lambda a: not predicate(a)
        return self

    """
        Change the guard to the given predicate.
    """
    def ifTrue(self, predicate: Callable[[Agent], bool]) -> "AgentTask":
        if predicate is None:
            self.__guard = None
        else:
            self.__guard = predicate
        return self

    """
        used to print of the task's information
    """
    def __str__(self) -> str:
        return "AgentTask: " + self.__name

    """
        return the initiator of the task
    """
    def getInitiator(self) -> object:
        return self.__initiator
