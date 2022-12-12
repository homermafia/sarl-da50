from uuid import UUID

from pysarl.io.sarl.lang.core.Event import Event


class ContextJoined(Event):
    defaultSpaceID: UUID
    holonContextID: UUID

    def __init__(self, contextID: UUID, defaultSpaceID: UUID):
        super().__init__()
        self.defaultSpaceID = defaultSpaceID
        self.holonContextID = contextID
