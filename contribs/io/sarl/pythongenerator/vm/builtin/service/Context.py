from pysarl.io.sarl.lang.core.EventSpace import EventSpace
from vm.builtin.service.PythonContext import PythonContext


class Context(PythonContext):
    def __init__(self):
        self.defaultSpace = EventSpace()
        self.spaces = []

    def getDefaultSpace(self):
        return self.defaultSpace

    def createSpace(self, uuid):
        self.spaces.append(EventSpace())
