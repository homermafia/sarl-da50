import abc
from typing import Callable, Set, TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Agent import Agent
    from pysarl.io.sarl.core.AgentTask import AgentTask

from pysarl.io.sarl.lang.core.Capacity import Capacity


class Schedules(Capacity, abc.ABC):

    """
    Schedule a task to be executed at a time.
    @param : task
    @param : time
    @param : procedure
    """
    @abc.abstractmethod
    def at(self, task: AgentTask, time: int, procedure: Callable[[Agent], None]) -> AgentTask:
        pass

    """
    Schedule a single-execution task
    @param : task
    @param : delay
    @param : procedure
    """
    @abc.abstractmethod
    def atFixedDelay(self, task: AgentTask, delay: int, procedure: Callable[[Agent], None]) -> AgentTask:
        pass

    """
    Cancel a task
    @param : task
    @param : mayInterruptIfRunning
    """
    @abc.abstractmethod
    def cancel(self, task: AgentTask, mayInterruptIfRunning: bool) -> bool:
        pass

    """
    Schedule a periodic execution for a task
    @param : task
    @param : period
    @param : procedure
    """
    @abc.abstractmethod
    def every(self, task: AgentTask, period: int, procedure: Callable[[Agent], None]) -> AgentTask:
        pass

    """
    Execute a task
    @param : task
    @param : procedure
    """
    @abc.abstractmethod
    def execute(self, task: AgentTask, procedure: Callable[[Agent], None]) -> AgentTask:
        pass

    """
    Return the name of the active tasks
    """
    @abc.abstractmethod
    def getActiveTasks(self) -> Set[str]:
        pass

    """
    Schedule a given task to be executed after the specified delay
    @param : task
    @param : delay
    @param : procedure
    """
    @abc.abstractmethod
    def _in(self, task: AgentTask, delay: int, procedure: Callable[[Agent], None]) -> AgentTask:
        pass

    """
    @param : task
    """
    @abc.abstractmethod
    def isCanceled(self, task: AgentTask) -> bool:
        pass

    """
    Set a new name for a task
    @param : name
    @param : task
    """
    @abc.abstractmethod
    def setName(self, task: AgentTask, name: str) -> None:
        pass

    """
    Create a named task that can be retrieved and schedule later.
    @param : name
    """
    @abc.abstractmethod
    def task(self, name: str) -> AgentTask:
        pass
