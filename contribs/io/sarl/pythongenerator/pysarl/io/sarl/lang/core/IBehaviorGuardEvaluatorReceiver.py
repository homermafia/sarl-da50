class IBehaviorGuardEvaluatorReceiver():
    """ evaluate the behavior unit's guards.
       @ param event to evaluate
       @ param callbacks : the collection of callback that must be run
    """
    def evaluateBehaviorGuards(self, event, callbacks): #, event: Object, Collection < Runnable > callbacks) :
        pass

    """ Give the list of the supported events by the receiver.
        @param toBeFilled : the set that must be filled with events
    """
    def getSupportedEvents(self, toBeFilled): #Set < Class <? extendsEvent >> toBeFilled):
        pass
    """ Verify if the event given is supported (return true) or not (return false)
        @param event to test
    """
    def isSupportedEvent(self, event) -> bool : #Class <? > event)
        return False