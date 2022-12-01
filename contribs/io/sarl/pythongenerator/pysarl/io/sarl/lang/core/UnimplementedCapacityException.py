import uuid


class UnimplementedCapacityException():#RuntimeException

    def __init__(self, callingAgent: uuid, unimplementedCapacity): #private final Class<? extends Capacity> unimplementedCapacity;
        self.__callingAgent = callingAgent
        self.__unimplementedCapacity = unimplementedCapacity

    """
        @:param
    """
    def getCallingAgent(self) -> uuid:
		return self.callingAgent

    def getUnimplementedCapacity(self) :
		return self.__unimplementedCapacity
