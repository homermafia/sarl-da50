from contribs.io.sarl.pythongenerator.api.event.event import Event


class Initialize(Event):

    def __init__(self, spawner, *params):
        super().__init__()
        self.__spawner = spawner
        self.__params = params


