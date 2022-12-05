from uuid import UUID
from typing import TypeVar, Type

from pysarl.io.sarl.lang.core.Capacity import Capacity

C = TypeVar('C', bound=Type[Capacity])


class UnimplementedCapacityException(Exception):
    __unimplementedCapacity: C
    __callingAgent: UUID

    def __init__(self, unimplementedCapacity: C, agent: UUID, cause: Exception = None):
        self.__unimplementedCapacity = unimplementedCapacity
        self.__callingAgent = agent

    """
        Return the calling agent
    """
    def getCallingAgent(self) -> UUID:
        return self.__callingAgent

    """
        Return the unimplemented capacity
    """
    def getUnimplementedCapacity(self) -> C:
        return self.__unimplementedCapacity
