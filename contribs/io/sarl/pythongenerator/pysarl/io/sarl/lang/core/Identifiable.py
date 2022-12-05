import abc
from uuid import UUID


class Identifiable(abc.ABC):

    @abc.abstractmethod
    def getID(self) -> UUID:
        pass
