from uuid import UUID

from pysarl.io.sarl.lang.core.Event import Event


class ContextLeft(Event):
    holonContextID: UUID

    def __init__(self, contextID: UUID):
        super().__init__()
        self.holonContextID = contextID
