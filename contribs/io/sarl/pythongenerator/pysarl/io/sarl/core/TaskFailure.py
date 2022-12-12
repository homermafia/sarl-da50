from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Address import Address
    from pysarl.io.sarl.core.AgentTask import AgentTask

from pysarl.io.sarl.core.Failure import Failure


class TaskFailure(Failure):
    task: AgentTask

    def __init__(self, source: Address = None, task: AgentTask = None, cause: object = None):
        super().__init__(source, cause)
        self.task = task
