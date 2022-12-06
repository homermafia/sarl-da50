from contribs.io.sarl.pythongenerator.api.event.space import Space


class Context():
    def __init__(self):
        self.defaultSpace = Space()
        self.spaces = []

    def getDefaultSpace(self):
        return self.defaultSpace

    def createSpace(self,uuid):
        self.spaces.append(Space())

