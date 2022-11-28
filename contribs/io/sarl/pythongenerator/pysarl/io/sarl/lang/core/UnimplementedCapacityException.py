import uuid


class UnimplementedCapcityException():

    def __init__(self, callingAgent: uuid): #private final Class<? extends Capacity> unimplementedCapacity;
        self.__callingAgent = callingAgent
        #self.__unimplementedCapacity = unimplementedCapacity

    """
        @:param
    """
    def getCallingAgent(self) -> uuid:
		return self.callingAgent

    def getUnimplementedCapacity(self) :
		#return self.unimplementedCapacity
	    pass
