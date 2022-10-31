from contribs.io.sarl.pythongenerator.api.capacity.capacity import Capacity


class Logging(Capacity, object):

    def debug(self, message):
        raise Exception("Unimplemented function")

    def info(self, message):
        raise Exception("Unimplemented function")

    def warning(self, message):
        raise Exception("Unimplemented function")

    def error(self, message):
        raise Exception("Unimplemented function")

    def __init__(self, C):
        super().__init__(C)
