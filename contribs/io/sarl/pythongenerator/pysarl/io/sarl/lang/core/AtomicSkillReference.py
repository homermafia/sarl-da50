import copy
from typing import Any

from pysarl.io.sarl.lang.core.Skill import Skill


class AtomicSkillReference():
    __reference: Skill

    def __init__(self, obj: Skill):
        assert obj is not None
        self.__reference = obj
        obj.increaseReference()

    def clone(self) -> "AtomicSkillReference":
        # shallow copy
        try:
            return copy.copy(self)
        except copy.Error as e:
            raise Exception(e)

    def get(self) -> Skill:
        return self.__reference

    def clear(self) -> Skill:
        ref: Skill = self.__reference
        self.__reference = None
        if ref is not None:
            ref.decreaseReference()
        return ref

    def __str__(self) -> str:
        ref: Skill = self.__reference
        if ref is not None:
            return str(ref)
        return "null"

    def equals(self, obj: Any) -> bool:
        if self == obj:
            return True
        if obj is None:
            return False
        if type(obj) != AtomicSkillReference:
            return False
        ref: Skill = self.__reference
        aref: AtomicSkillReference = obj
        oref = aref.__reference
        if ref is None:
            return oref is None
        if oref is None:
            return ref is None
        return ref == oref
