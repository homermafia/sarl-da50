from __future__ import annotations
from typing import List, Type, Dict, Callable, Set, TypeVar, TYPE_CHECKING
from multipledispatch import dispatch

if TYPE_CHECKING:
    from pysarl.io.sarl.lang.core.AbstractSkillContainer import AbstractSkillContainer
    from pysarl.io.sarl.lang.core.Agent import Agent
    from pysarl.io.sarl.lang.core.AtomicSkillReference import AtomicSkillReference
    from pysarl.io.sarl.lang.core.Behavior import Behavior
    from pysarl.io.sarl.lang.core.Capacity import Capacity
    from pysarl.io.sarl.lang.core.DynamicSkillProvider import DynamicSkillProvider
    from pysarl.io.sarl.lang.core.Event import Event
    from pysarl.io.sarl.lang.core.IBehaviorGuardEvaluatorReceiver import IBehaviorGuardEvaluatorReceiver
    from pysarl.io.sarl.lang.core.Skill import Skill

    C = TypeVar('C', bound=Type[object])
    S = TypeVar('S', bound=object)
    Cap = TypeVar('Cap', bound=Type[Capacity])
    CS = TypeVar('CS', bound=Capacity)
    E = TypeVar('E', bound=Type[Event])

from pysarl.io.sarl.lang.core.SRESpecificDataContainer import SRESpecificDataContainer


class SREutils():
    """
        @param
    """
    def getSreSpecificData(self, container: SRESpecificDataContainer, typeClass: C) -> S:
        assert container is not None
        return container._getSreSpecificData(typeClass)

    """
        @param
    """
    @dispatch(SRESpecificDataContainer, object)
    def setSreSpecificData(self, container: SRESpecificDataContainer, data: object) -> None:
        assert container is not None
        container._setSreSpecificData(data)

    """
        @param
    """
    @dispatch(SRESpecificDataContainer, object, object)
    def setSreSpecificData(self, container: SRESpecificDataContainer, data: S, typeClass: C) -> S:
        assert container is not None
        oldData: S = container._getSreSpecificData(typeClass)
        container._setSreSpecificData(data)
        return oldData

    """
        @param
    """
    def getInternalSkillReference(self, container: AbstractSkillContainer, typeClass: C) -> AtomicSkillReference:
        return container._getSkill(typeClass)

    """
        @param
    """
    def castInternalSkillReference(self, container: AbstractSkillContainer, reference: AtomicSkillReference, typeClass: Cap) -> CS:
        return container._castSkill(typeClass, reference)

    """	
        @param
    """
    def setInternalSkill(self, container: AbstractSkillContainer, skill: Skill, capacities: List[Cap]) -> AtomicSkillReference:
        assert capacities is not None
        return container._setSkill(skill, False, *capacities)

    """	
        @param
    """
    def setInternalSkillIfAbsent(self, container: AbstractSkillContainer, skill: Skill, capacities: List[Cap]) -> AtomicSkillReference:
        assert capacities is not None
        return container._setSkill(skill, True, *capacities)

    """
        @param
    """
    def getInternalSkill(self, container: AbstractSkillContainer, typeClass: Cap) -> CS:
        return container.getSkill(typeClass)

    """
        @param
    """
    def getSkillRepository(self, container: AbstractSkillContainer) -> Dict[Cap, AtomicSkillReference]:
        return container._getSkillRepository()

    """
        @param container the container.
        @param provider the provider.
    """
    def setDynamicSkillProvider(self, container: AbstractSkillContainer, provider: DynamicSkillProvider) -> None:
        container.setDynamicSkillProvider(provider)

    """
        @param skill to be installed.
    """
    def doSkillInstallation(self, skill: Skill) -> None:
        skill.install()

    """
        @param skill to be uninstalled.
    """
    def doSkillUninstallationPreparation(self, skill: Skill) -> None:
        skill.prepareUninstallation()

    """	
         @param skill to be uninstalled.
    """
    def doSkillUninstallation(self, skill: Skill) -> None:
        skill.uninstall()

    """
        @param receiver : the object that will receive the event
        @param event:
        @param behaviorsMethodsToExecute: 
    """
    def doEvaluateBehaviorGuards(self, receiver: IBehaviorGuardEvaluatorReceiver, event: object, behaviorsMethodsToExecute: List[Callable]) -> None:
        receiver._evaluateBehaviorGuards(event, behaviorsMethodsToExecute)

    """	 
        @param receiver: the object that receives the events
        @param events: 
    """
    def doGetSupportedEvents(self, receiver: IBehaviorGuardEvaluatorReceiver, events: Set[E]) -> None:
        receiver._getSupportedEvents(events)

    """	
        @param receiver : the object which receive the event
        @param event to test
    """
    def doIsSupportedEvent(self, receiver: IBehaviorGuardEvaluatorReceiver, event: E) -> bool:
        return receiver._isSupportedEvent(event)

    """ 
        @param behavior to be installed
    """
    def doBehaviorInstallation(self, behavior: Behavior) -> None:
        behavior.install()

    """ 
        @param behavior to be uninstalled.
    """
    def doBehaviorUninstallation(self, behavior: Behavior) -> None:
        behavior.uninstall()

    """ Provide an agent with a callback function for the skill installation"""
    def setSkillInstallationCallback(self, agent: Agent, callback: Callable[[Agent, Skill], None]):
        agent.setSkillCallback(callback)
