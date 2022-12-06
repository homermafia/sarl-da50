from __future__ import annotations
import abc
from typing import List, Callable, Set, TypeVar, Type, TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Event import Event

    T = TypeVar('T', bound=Type[Event])


class IBehaviorGuardEvaluatorReceiver(abc.ABC):
    """ evaluate the behavior unit's guards.
       @ param event to evaluate
       @ param callbacks : the collection of callback that must be run
    """
    def _evaluateBehaviorGuards(self, event: object, callbacks: List[Callable]) -> None:
        pass

    """ Give the list of the supported events by the receiver.
        @param toBeFilled : the set that must be filled with events
    """
    def _getSupportedEvents(self, toBeFilled: Set[T]) -> None:
        pass

    """ Verify if the event given is supported (return true) or not (return false)
        @param event to test
    """
    def _isSupportedEvent(self, event: T) -> bool:
        return False
