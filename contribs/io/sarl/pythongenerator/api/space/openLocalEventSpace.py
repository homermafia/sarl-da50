#Source: https://github.com/sarl/sarl/blob/master/sre/io.janusproject/io.janusproject.plugin/src/main/sarl/io/sarl/sre/spaces/OpenLocalEventSpace.sarl
from contribs.io.sarl.pythongenerator.api.event.address import Address
from contribs.io.sarl.pythongenerator.api.space.abstractEventSpace import AbstractEventSpace


class OpenLocalEventSpace(AbstractEventSpace):
    def register(self, entity: AbstractEventSpace, weakParticipant: bool) -> Address:
        entity.registerToSpace(weakParticipant)

    def registerStrongParticipant(self, entity: AbstractEventSpace) -> Address:
        entity.registerToSpace(False)

    def registerWeakParticipant(self, entity: AbstractEventSpace) -> Address:
        entity.registerToSpace(True)

    def unregister(self, entity) -> Address:
        entity.unregisterFromSpace()
