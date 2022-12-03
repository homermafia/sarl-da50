import uuid

class UnimplementedCapacityException(Exception):

    def __init__(self, callingAgent: uuid, unimplementedCapacity): #private final Class<? extends Capacity> unimplementedCapacity;
        self.__callingAgent = callingAgent
        self.__unimplementedCapacity = unimplementedCapacity

    """
        Return the calling agent
    """
    def getCallingAgent(self) -> uuid:
		return self.__callingAgent

    """
        Return the unimplemented capacity
    """
    def getUnimplementedCapacity(self):
		return self.__unimplementedCapacity
