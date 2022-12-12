from __future__ import annotations
from uuid import UUID
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Address import Address

from pysarl.io.sarl.lang.core.Event import Event


class MemberJoined(Event):
    agentID: UUID
    agentType: str

    def __init__(self, source: Address, agentID: UUID, agentType: str):
        super().__init__(source)
        self.agentID = agentID
        self.agentType = agentType
