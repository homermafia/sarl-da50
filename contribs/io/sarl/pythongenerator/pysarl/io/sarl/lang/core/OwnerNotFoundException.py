from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.AgentTrait import AgentTrait


class OwnerNotFoundException(Exception):
    __trait: AgentTrait

    def __init__(self, trait: AgentTrait):
        self.__trait = trait

    """ Return the agent trait """
    def getAgentTrait(self) -> AgentTrait:
        return self.__trait
