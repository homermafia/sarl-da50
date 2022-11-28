from pysarl.io.sarl.lang.core.AtomicSkillReference import AtomicSkillReference
from pysarl.io.sarl.lang.core.SRESpecificDataContainer import SRESpecificDataContainer
from pysarl.io.sarl.lang.core.AbstractSkillContainer import AbstractSkillContainer
from pysarl.io.sarl.lang.core.DynamicSkillProvider import DynamicSkillProvider
from pysarl.io.sarl.lang.core.IBehaviorGuardEvaluatorReceiver import IBehaviorGuardEvaluatorReceiver
from pysarl.io.sarl.lang.core.Skill import Skill
from pysarl.io.sarl.lang.core.Agent import Agent
from pysarl.io.sarl.lang.core.Behavior import Behavior


class SREutils():
    """
        @param
    """
    def getSreSpecificData(self, container : SRESpecificDataContainer): #, Class<S> type) {
        pass

    """
        @param
    """
    def setSreSpecificDataObject(self, container : SRESpecificDataContainer, data : object) -> None :
        pass

    """
        @param
    """
    def setSreSpecificData(self, container: SRESpecificDataContainer): #, S data, Class<S> type)
        pass

    """
	    @param
    """
    def getInternalSkillReference(self, container: AbstractSkillContainer) -> AtomicSkillReference : #, Class<? extends Capacity> type
        pass

    """
	    @param
    """
    def castInternalSkillReference(self, container : AbstractSkillContainer, reference: AtomicSkillReference): # Class<S> type) {
        pass

    """	
        @param
    """
    def setInternalSkill(self, container : AbstractSkillContainer, skill : Skill)-> AtomicSkillReference : #, Class<? extends Capacity>[] capacities) {
        pass

    """	
        @param
    """
    def setInternalSkillIfAbsent(self, container : AbstractSkillContainer, skill: Skill) -> AtomicSkillReference : #, Class<? extends Capacity>[] capacities) {
        pass
	"""
	    @param
	"""
    def getInternalSkill(self, container: AbstractSkillContainer): #, Class<S> type)
        pass

    """
	    @param
	"""
    def getSkillRepository(self, container : AbstractSkillContainer ) :
        pass

	"""
	    @param container the container.
	    @param provider the provider.
	"""
    def setDynamicSkillProvider(self, container : AbstractSkillContainer, provider :DynamicSkillProvider) -> None :
        container.setDynamicSkillProvider(provider)

	"""
	    @param skill to be installed.
	"""
    def doSkillInstallation(self, skill : Skill ) -> None :
		skill.install()

    """
        @param skill to be uninstalled.
    """
    def doSkillUninstallationPreparation(self, skill : Skill) -> None:
		skill.prepareUninstallation()

    """	
         @param skill to be uninstalled.
    """
    def doSkillUninstallation(self, skill : Skill ) -> None :
		skill.uninstall()
    """
	    @param receiver : the object that will receive the event
	    @param event:
	    @param behaviorsMethodsToExecute: 
	"""
    def doEvaluateBehaviorGuards(self, receiver: IBehaviorGuardEvaluatorReceiver, event: object ) -> None : #, Collection<Runnable> behaviorsMethodsToExecute) {
		pass

    """	 
        @param receiver: the object that receives the events
	    @param events: 
	"""
    def doGetSupportedEvents(receiver : IBehaviorGuardEvaluatorReceiver) -> None : #, Set<Class<? extends Event>> events) {
        pass

    """	
	    @param receiver : the object which receive the event
	    @param event to test
    """
    def doIsSupportedEvent(self, receiver : IBehaviorGuardEvaluatorReceiver) -> bool : #, Class<? extends Event> event)
        pass

	""" 
	    @param behavior to be installed
	"""
    def doBehaviorInstallation(self, behavior: Behavior ) -> None :
        behavior.install()

	""" 
	    @param behavior to be uninstalled.
	"""
    def doBehaviorUninstallation (self, behavior: Behavior)-> None:
        behavior.uninstall()

	""" Provide an agent with a callback function for the skill installation"""
    def setSkillInstallationCallback(self, agent: Agent) : #(Agent agent, Procedure2<Agent, Skill> callback)
        pass