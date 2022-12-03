import abc
from typing import TypeVar, Type

from pysarl.io.sarl.lang.core.Skill import Skill

S = TypeVar('S', bound=Type[Skill])


class DefaultSkill(abc.ABC):

    @abc.abstractmethod
    def value(self) -> S:
        pass