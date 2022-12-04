from pysarl.io.sarl.lang.core.Capacity import Capacity


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
