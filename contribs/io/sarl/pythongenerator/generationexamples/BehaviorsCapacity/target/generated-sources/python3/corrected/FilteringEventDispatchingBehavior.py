#!/usr/bin/env python3
# Generated by the SARL compiler the Sat Oct 22 13:20:32 CEST 2022. Do not change this file.

from io.sarl.core import Behaviors
from io.sarl.lang.core import Behavior
from io.sarl.lang.core import Event
from io.sarl.lang.core import EventListener
from io.sarl.lang.core import Scope
from io.sarl.lang.util import ConcurrentCollection

from multipledispatch import dispatch
from typing import Type, Callable

from FilteringEventListener import FilteringEventListener


class FilteringEventDispatchingBehavior(Behaviors, object):
    def asEventListener(self) -> EventListener:
        return FilteringEventListener(self)

    def getRegisteredBehaviors(self) -> ConcurrentCollection[Behavior]:
        return self.behaviorDelegate.getRegisteredBehaviors()

    def hasRegisteredBehavior(self) -> bool:
        return self.behaviorDelegate.hasRegisteredBehavior()

    def registerBehavior(self, attitude: Behavior, _filter: Callable, *initializationParameters: object) -> Behavior:
        return self.behaviorDelegate.registerBehavior(attitude, _filter, initializationParameters)

    def unregisterBehavior(self, attitude: Behavior) -> Behavior:
        return self.behaviorDelegate.unregisterBehavior(attitude)

    @dispatch(Event, Scope)
    def wake(self, event: Event, scope: Scope):
        self.behaviorDelegate.wake(event, scope)

    @dispatch(Event)
    def wake(self, event: Event):
        return self.wake(event, None)

    @dispatch(Behavior, Event)
    def wake(self, beh: Behavior, event: Event):
        self.behaviorDelegate.wake(beh, event)

    @dispatch(Behavior, Event)
    def wake(self, behs: list, event: Event):
        self.behaviorDelegate.wake(behs, event)

    def __init__(self, acceptedType: Type[Event], behaviorDelegate: Behaviors):
        self.acceptedType = acceptedType
        self.behaviorDelegate = behaviorDelegate
