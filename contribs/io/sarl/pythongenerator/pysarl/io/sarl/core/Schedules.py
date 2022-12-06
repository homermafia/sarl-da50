from pysarl.io.sarl.lang.core.Capacity import Capacity
from pysarl.io.sarl.core.AgentTask import AgentTask


class Schedules(Capacity):

    def __init__(self, name: str):
        self.__name = name

    """
    Schedule a task to be executed at a time.
    @param : task
    @param : time
    @param : procedure
    """

    def at(self, task: AgentTask, time, procedure) -> AgentTask:
        pass

    """
    Schedule a single-execution task
    @param : task
    @param : delay
    @param : procedure
    """

    def atFixedDelay(self, task: AgentTask, delay, procedure) -> AgentTask:
        pass

    """
    Cancel a task
    @param : task
    @param : mayInterruptIfRunning
    """

    def cancel(self, task: AgentTask, mayInterruptIfRunning: bool) -> bool:
        pass

    """
    Schedule a periodic execution for a task
    @param : task
    @param : period
    @param : procedure
    """

    def every(self, task: AgentTask, period, procedure) -> AgentTask:
        pass

    """
    Execute a task
    @param : task
    @param : procedure
    """

    def execute(self, task: AgentTask, procedure) -> AgentTask:
        pass

    """
    Return the name of the active tasks
    """

    def getActiveTasks(self):
        pass

    """
    Schedule a given task to be executed after the specified delay
    @param : task
    @param : delay
    @param : procedure
    """

    def inTask(self, task: AgentTask, delay, procedure) -> AgentTask:
        pass

    """
    @param : task
    """

    def isCanceled(self, task: AgentTask) -> bool:
        pass

    """
    Set a new name for a task
    @param : name
    @param : task
    """

    def setName(self, name: str, task: AgentTask):
        task.setTaskName(name)

    """
    Create a named task that can be retrieved and schedule later.
    @param : name
    """

    def task(self, name: str) -> AgentTask:
        pass
