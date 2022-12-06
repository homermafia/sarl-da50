from typing import TypeVar, Generic
import abc

T = TypeVar('T')


class Scope(Generic[T], abc.ABC):

    @abc.abstractmethod
    def matches(self, element: T) -> bool:
        # Checks whether the element is included in this scope
        pass
