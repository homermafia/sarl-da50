from pysarl.io.sarl.lang.core.Space import Space
import abc
from typing import TypeVar, Generic

T = TypeVar('T', bound=Space)


class SpaceSpecification(abc.ABC, Generic[T]):

    @abc.abstractmethod
    def create(self, identifier, *params) -> T:
        # Creates a Space that respects this specification
        pass


