from __future__ import annotations
import abc
from typing import TypeVar, Generic, TYPE_CHECKING

from pysarl.io.sarl.lang.core.Space import Space
T = TypeVar('T', bound=Space)

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.SpaceID import SpaceID


class SpaceSpecification(Generic[T], abc.ABC):

    @abc.abstractmethod
    def create(self, identifier: SpaceID, *params: object) -> T:
        # Creates a Space that respects this specification
        pass
