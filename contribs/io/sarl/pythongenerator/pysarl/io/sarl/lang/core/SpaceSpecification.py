from pysarl.io.sarl.lang.core.Space import Space
import abc
from typing import TypeVar, Generic

from pysarl.io.sarl.lang.core.SpaceID import SpaceID

T = TypeVar('T', bound=Space)


class SpaceSpecification(abc.ABC, Generic[T]):

    @abc.abstractmethod
    def create(self, identifier: SpaceID, *params: object) -> T:
        # Creates a Space that respects this specification
        pass
