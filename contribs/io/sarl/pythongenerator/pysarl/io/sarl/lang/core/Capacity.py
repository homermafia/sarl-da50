from __future__ import annotations
import abc
from typing import TypeVar, TYPE_CHECKING

from pysarl.io.sarl.lang.core.Capacities import Capacities

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.AgentTrait import AgentTrait

    S = TypeVar('S', bound="Capacity")


class Capacity(abc.ABC):

    class ContextAwareCapacityWrapper():
        capacity: S
        __caller: AgentTrait

        def __init__(self, capacity: S, caller: AgentTrait):
            assert capacity is not None
            self.capacity = capacity
            self.__caller = caller

        def ensureCallerInLocalThread(self) -> None:
            Capacities.CALLER.agent = self.__caller

        def resetCallerInLocalThread(self) -> None:
            Capacities.CALLER.agent = None

        def getDelegate(self) -> S:
            return self.capacity
