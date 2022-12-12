from __future__ import annotations
from uuid import UUID
from typing import TYPE_CHECKING, TypeVar, Type

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Address import Address
    from pysarl.io.sarl.lang.core.Agent import Agent

    A = TypeVar('A', bound=Type[Agent])

from pysarl.io.sarl.core.Failure import Failure


class AgentSpawnFailure(Failure):
    agentType: A
    contextId: UUID

    def __init__(self, source: Address = None, contextId: UUID = None, agentType: A = None, cause: object = None):
        super().__init__(source, cause)
        self.agentType = agentType
        self.contextId = contextId
