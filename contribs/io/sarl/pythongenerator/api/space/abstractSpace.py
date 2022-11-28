#Source: https://github.com/sarl/sarl/blob/master/sre/io.janusproject/io.janusproject.plugin/src/main/sarl/io/sarl/sre/spaces/AbstractSpace.sarl

class AbstractSpace():
    def __init__(self, id: SpaceID):
        self.id = id

    def fireDestroyableSpace(self) -> None:
        pass

    def getSpaceID(self) -> SpaceID:
        pass

    def setSpaceListenerIfNone(self, listener: SpaceListener):
        pass

    def toString(self) -> str:
        pass