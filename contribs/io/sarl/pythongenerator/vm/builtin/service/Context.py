from pysarl.io.sarl.lang.core.Space import Space
from vm.builtin.service.PythonContext import PythonContext


class Context(PythonContext):
    def __init__(self):
        self.defaultSpace = Space()
        self.spaces = []

    def getDefaultSpace(self):
        return self.defaultSpace

    def createSpace(self, uuid):
        self.spaces.append(Space())
