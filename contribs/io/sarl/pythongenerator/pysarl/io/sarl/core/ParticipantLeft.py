from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.Address import Address
    from pysarl.io.sarl.lang.core.SpaceID import SpaceID

from pysarl.io.sarl.lang.core.Event import Event


class ParticipantLeft(Event):
    spaceID: SpaceID

    def __init__(self, source: Address, spaceID: SpaceID):
        super().__init__(source)
        self.spaceID = spaceID
