from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Address import Address

from pysarl.io.sarl.lang.core.Event import Event


class AgentKilled(Event):
    agentType: str
    terminationCause: object

    def __init__(self, source: Address, agentType: str, terminationCause: object):
        super().__init__(source)
        self.agentType = agentType
        self.terminationCause = terminationCause
