from __future__ import annotations
from uuid import UUID
import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Address import Address
    from pysarl.io.sarl.lang.core.Event import Event
    from pysarl.io.sarl.lang.core.Scope import Scope

from pysarl.io.sarl.lang.core.Space import Space


class EventSpace(Space, abc.ABC):

    @abc.abstractmethod
    def getAddress(self, identifier: UUID) -> Address:
        # Returns the address of the agent identified by id
        pass

    @abc.abstractmethod
    def emit(self, eventSource: UUID, event: Event, scope: Scope = None) -> None:
        # Emits the event inside this space with the given scope
        pass
