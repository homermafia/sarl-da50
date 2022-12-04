from vm.builtin.event.Destroy import Destroy
from vm.builtin.event.Initialize import Initialize

class EventDispatcher:

    __listeners = dict()
    __onlyOnSameAgent = [Initialize.__name__, Destroy.__name__]

    def register(self, agent):
        guards = [method for method in dir(agent) if
                  method.startswith("__guard") and method.endswith("__")]
        for guard in guards:
            split = guard.split("_")
            event = split[len(split) - 3]
            self.__listeners[(agent, event)] = guard

    def unregister(self, agent):
        self.__listeners = {(a, e): g for (a, e), g in self.__listeners.items() if a != agent }

    def dispatch(self, agent, event):
        eventClass = type(event).__name__
        # list all parent classes
        bases = type(event).__bases__
        basesNames = []
        for b in bases:
            basesNames.append(b.__name__)
        for (a, e), guard in self.__listeners.items():
            if (e == eventClass or e in basesNames) and (not e in self.__onlyOnSameAgent or a == agent):
                attr = getattr(agent, guard)
                methodsToCall = attr(event)
                for method in methodsToCall:
                    method(event)

