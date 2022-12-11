from uuid import UUID


class UnknownContextException(Exception):
    __unknownContextID: UUID

    def __init__(self, unknownContextID: UUID):
        self.__unknownContextID = unknownContextID

    def getUnknownContextID(self):
        return self.__unknownContextID
