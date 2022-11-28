#Source: https://github.com/sarl/sarl/blob/master/sre/io.janusproject/io.janusproject.plugin/src/main/sarl/io/sarl/sre/spaces/AbstractEventSpace.sarl

from contribs.io.sarl.pythongenerator.api.space.spaceID import SpaceID
from contribs.io.sarl.pythongenerator.api.event.address import Address
from contribs.io.sarl.pythongenerator.api.space.abstractSpace import AbstractSpace
from contribs.io.sarl.pythongenerator.vm.builtin.service.LoggingService import LoggingService


import uuid


class AbstractEventSpace(AbstractSpace):
    def __init__(self, spaceId: SpaceID, participantListener: SpaceParticipantListener, loggingService: LoggingService, strongRepository: dict, weakRepository: dict):
        super().__init__(spaceId)
        self.spaceParticipantListener = participantListener
        self.logger = loggingService.getKernelModuleLogger(spaceId.getID())
        if strongRepository is None:
            self.strongRepository = dict()
        else:
            self.strongRepository = strongRepository
        if weakRepository is None:
            self.weakRepository = dict()
        else:
            self.weakRepository = weakRepository

    def emit(self, eventSource: uuid.UUID) -> None:
        pass

    def emitLocally(self, event: Event, scope: Scope) -> None:
        pass

    def ensureEventSource(self, eventSource: uuid.UUID, event: Event) -> None:
        pass

    def forEachStrongParticipant(self, callback) -> None:
        pass

    def forEachWeakParticipant(self, callback) -> None:
        pass

    def getAddress(self, id: uuid.UUID) -> Address:
        pass

    def getEventTransportService(self) -> EventTransportService:
        pass

    def getListenerFromStrongParticipant(target: uuid.UUID) -> EventListener:
        pass

    def getLogger(self) -> Logger:
        pass

    def getNumberOfStrongParticipants(self) -> int:
        pass

    def getNumberOfWeakParticipants(self) -> int:
        pass

    def getScopedParticipants(self, scope: Scope) -> list[Participant]:
        pass

    def getSpaceParticipantListener(self) -> SpaceParticipantListener:
        pass

    def IsPseudoEmpty(self, id: uuid.UUID) -> bool:
        pass

    def registerToSpace(self, entity: EventListener, weakParticipant: bool) -> Address:
        pass

    def setEventTransportService(self, router: EventTransportService) -> None:
        pass

    def unregisterFromSpace(self, entity: EventListener) -> Address:
        pass