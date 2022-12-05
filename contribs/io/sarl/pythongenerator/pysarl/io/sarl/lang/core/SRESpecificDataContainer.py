import abc
from typing import TypeVar, Type

T = TypeVar('T', bound=Type[object])


class SRESpecificDataContainer(abc.ABC):
    __sreSpecificData: object

    def _getSreSpecificData(self, typeClass: T) -> T:
        return self.__sreSpecificData

    def _setSreSpecificData(self, data: object) -> None:
        self.__sreSpecificData = data
