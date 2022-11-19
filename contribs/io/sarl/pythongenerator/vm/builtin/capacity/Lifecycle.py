from contribs.io.sarl.pythongenerator.api.capacity.capacity import Capacity


class Lifecycle(Capacity, object):
    def spawn(self, agentClass):
        raise Exception("Unimplemented function")

    def killMe(self, terminationCause=None):
        raise Exception("Unimplemented function")

    def __init__(self, C):
        super().__init__(C)
