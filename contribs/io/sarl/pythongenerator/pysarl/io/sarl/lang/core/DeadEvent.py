from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Event import Event


class DeadEvent(Event):
    __event: object

    def __init__(self, event: Event):
        assert event is not None
        super().__init__(event.getSource())
        self.__event = event

    def getEvent(self) -> object:
        return self.__event
