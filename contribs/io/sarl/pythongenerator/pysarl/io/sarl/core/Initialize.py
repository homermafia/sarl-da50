from typing import Tuple
from uuid import UUID

from multipledispatch import dispatch

from pysarl.io.sarl.lang.core.Address import Address
from pysarl.io.sarl.lang.core.Event import Event


class Initialize(Event):
    parameters: Tuple[object]
    spawner: UUID

    @dispatch(Address, UUID, [object])
    def __init__(self, source: Address, spawner: UUID, *params: object):
        super().__init__(source)
        self.parameters = params
        self.spawner = spawner

    @dispatch(object, [object])  # Dispatching object in first argument instead of UUID because spawner can be None
    def __init__(self, spawner: UUID, *params: object):
        super().__init__()
        self.parameters = params
        self.spawner = spawner
