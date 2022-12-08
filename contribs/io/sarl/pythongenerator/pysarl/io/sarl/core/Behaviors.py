from __future__ import annotations
import abc
from typing import List, Callable, Iterable, TYPE_CHECKING
from collections.abc import Iterable as Iter

from multipledispatch import dispatch

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Address import Address
    from pysarl.io.sarl.lang.core.EventListener import EventListener

from pysarl.io.sarl.lang.core.Behavior import Behavior
from pysarl.io.sarl.lang.core.Capacity import Capacity
from pysarl.io.sarl.lang.core.Event import Event
from pysarl.io.sarl.lang.core.Scope import Scope


class Behaviors(Capacity, abc.ABC):

    @abc.abstractmethod
    def asEventListener(self) -> EventListener:
        pass

    @abc.abstractmethod
    def getRegisteredBehaviors(self) -> List[Behavior]:
        pass

    @abc.abstractmethod
    def hasRegisteredBehavior(self) -> bool:
        pass

    """
        @param : attitude
        @param : filterRegister
        @param : initializationParameters
    """
    @abc.abstractmethod
    def registerBehavior(self, attitude: Behavior, filterRegister: Callable[[Event], bool] = None, *initializationParameters: object) -> Behavior:
        pass

    """
        @param : attribute
    """
    @abc.abstractmethod
    def unregisterBehavior(self, attribute: Behavior) -> Behavior:
        pass

    """
        @param : behavior
        @param : event
    """
    @dispatch(Behavior, Event)
    @abc.abstractmethod
    def wake(self, behavior: Behavior, event: Event) -> None:
        pass

    """
        @param : event
    """
    @dispatch(Event)
    @abc.abstractmethod
    def wake(self, event: Event) -> None:
        pass

    """
        @param : event
        @param : scope
    """
    @dispatch(Event, Scope)
    @abc.abstractmethod
    def wake(self, event: Event, scope: Scope[Address]) -> None:
        pass

    """
        @param : behaviors
        @param : event
    """
    @dispatch(Iter, Event)
    @abc.abstractmethod
    def wake(self, behaviors: Iterable[Behavior], event: Event) -> None:
        pass
