class SRESpecificDataContainer():

    def __init__(self, sreSpecificData: object):
        self.__sreSpecificData = sreSpecificData

    def setSreSpecificData(self, data: object):
        self.__sreSpecificData = data

    def getSreSpecificData(self, typeClass): #(Class<S> type)
        pass