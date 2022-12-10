from __future__ import annotations
import abc
from typing import TYPE_CHECKING

from pysarl.io.sarl.lang.core.Identifiable import Identifiable

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Event import Event


class EventListener(Identifiable, abc.ABC):

    @abc.abstractmethod
    def receiveEvent(self, event: Event) -> None:
        pass
