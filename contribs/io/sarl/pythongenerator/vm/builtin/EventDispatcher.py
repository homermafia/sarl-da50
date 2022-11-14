from contribs.io.sarl.pythongenerator.vm.builtin.event.Initialize import Initialize


class EventDispatcher:

    __listeners = dict()
    __onlyOnSameAgent = [Initialize]

    def register(self, agent):
        guards = [method for method in dir(agent) if
                  method.startswith("__guard") and method.endswith("__")]
        for guard in guards:
            split = guard.split("_")
            event = split[len(split) - 3]
            self.__listeners[(agent, event)] = guard

    def dispatch(self, agent, event):
        for (a, e), guard in self.__listeners.items():
            if e == event.__name__ and not event in self.__onlyOnSameAgent \
                    or event in self.__onlyOnSameAgent and a == agent:
                attr = getattr(agent, guard)
                methodsToCall = attr(1)
                for method in methodsToCall:
                    method(1)

