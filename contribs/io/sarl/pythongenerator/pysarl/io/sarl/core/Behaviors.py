from pysarl.io.sarl.lang.core.Capacity import Capacity
from pysarl.io.sarl.lang.core.Event import Event


class Behaviors(Capacity):

    def __init__(self):
        pass

    def asEventListener(self):
        pass

    def getRegisteredBehaviors(self):
        pass

    """
    @param : attribute
    """
    def unregisterBehavior(self, attribute):
        pass
    """
    @param : behavior
    @param : event
    """
    def wake(self, behavior, event: Event):
        pass
