# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:00:29 2022

@author: loic
"""
from typing import TypeVar, Dict
import abc

from pysarl.io.sarl.lang.core.AgentProtectedAPIObject import AgentProtectedAPIObject
from pysarl.io.sarl.lang.core.AtomicSkillReference import AtomicSkillReference
from pysarl.io.sarl.lang.core.DynamicSkillProvider import DynamicSkillProvider
from pysarl.io.sarl.lang.core.DynamicSkillProvider import EmptyDynamicSkillProvider
from pysarl.io.sarl.lang.core.Capacity import Capacity
from pysarl.io.sarl.lang.core.Identifiable import Identifiable
from pysarl.io.sarl.lang.core.Skill import Skill
from pysarl.io.sarl.lang.core.UnimplementedCapacityException import UnimplementedCapcityException

C = TypeVar('C', bound=Capacity)
S = TypeVar('S', bound=Skill)


class AbstractSkillContainer(AgentProtectedAPIObject, Identifiable):
    __skillRepository: Dict[Capacity, AtomicSkillReference]
    __skillProvider: DynamicSkillProvider = None

    def __init__(self, skillProvider: DynamicSkillProvider = None):
        self.__skillRepository = dict()

        if skillProvider is None:
            self.__skillProvider = EmptyDynamicSkillProvider()
        else:
            self.__skillProvider = skillProvider

    def _setDynamicSkillProvider(self, provider: DynamicSkillProvider) -> None:
        if provider is None:
            self.__skillProvider = EmptyDynamicSkillProvider()
        else:
            self.__skillProvider = provider

    def _getSkillRepository(self) -> dict:
        return self.__skillRepository

    def setSkill(self, skill, *capacities) -> S:
        self._setSkill(skill, False, *capacities)
        return skill

    def setSkillIfAbsent(self, skill: Skill, *capacities: C) -> None:
        self._setSkill(skill, True, *capacities)

    def _setSkill(self, skill: Skill, ifabsent: bool, *capacities: C) -> AtomicSkillReference:
        assert skill is not None
        self._attachOwner(skill)
        newRef: AtomicSkillReference = None
        if capacities is None or len(capacities) == 0:
            for cls in type(skill).__mro__:
                if cls != Capacity and cls != skill.__class__ and issubclass(cls, Capacity) and not issubclass(cls, Skill):
                    newRef = self.__registerSkill(skill, ifabsent, cls, newRef)
        else:
            for cap in capacities:
                assert cap is not None
                assert not issubclass(cap, Skill)
                newRef = self.__registerSkill(skill, ifabsent, cap, newRef)
        return newRef

    @abc.abstractmethod
    def _attachOwner(self, skill: Skill) -> None:
        pass

    def __registerSkill(self, skill: Skill, ifabsent: bool, capacity: Capacity.__class__, firstRef: AtomicSkillReference) -> AtomicSkillReference:
        newReference: AtomicSkillReference = None
        if ifabsent:
            if capacity in self._getSkillRepository():
                newReference = self._getSkillRepository()[capacity]
            else:
                newReference = AtomicSkillReference(skill)
                self._getSkillRepository()[capacity] = newReference
        else:
            newReference = AtomicSkillReference(skill)
            oldReference: AtomicSkillReference = self._getSkillRepository().get(capacity)
            self._getSkillRepository()[capacity] = newReference
            if oldReference is not None:
                oldReference.clear()

        if firstRef is None:
            return newReference

        return firstRef

    def getSkill(self, capacity: C) -> C:
        assert capacity is not None and issubclass(capacity, Capacity) and not issubclass(capacity, Skill)
        skill: AtomicSkillReference = self._getSkill(capacity)
        assert skill is not None
        return self._castSkill(capacity, skill)

    def _castSkill(self, capacity: Capacity.__class__, skillReference: AtomicSkillReference) -> C:
        return skillReference.get()

    def _getSkill(self, capacity: C) -> AtomicSkillReference:
        return self.__createSkillDynamically(capacity, self._getSkillRepository().get(capacity))

    def __createSkillDynamically(self, capacity: C, existingSkill: AtomicSkillReference) -> AtomicSkillReference:
        # Check if the stored skill is still not empty
        if existingSkill is not None:
            s: Skill = existingSkill.get()
            if s is not None:
                return existingSkill

        # Try to load dynamically the skill
        skill: Skill = self.__skillProvider.createSkill(capacity)
        if skill is not None:
            self._attachOwner(skill)
            return AtomicSkillReference(skill)

        # Use the default skill declaration if present
        raise UnimplementedCapcityException(capacity, self.getID())

    def hasSkill(self, capacity: C) -> bool:
        assert capacity is not None

        if capacity not in self.__skillRepository.keys():
            if self.__skillProvider is not None and self.__skillProvider.isSkillProviding(capacity):
                return True
            return False
        return True

    def clearSkill(self, capacity: Capacity.__class__) -> C:
        assert capacity is not None

        if capacity in self._getSkillRepository():
            reference: AtomicSkillReference = self._getSkillRepository().pop(capacity)
            if reference is not None:
                skill: Skill = reference.clear()
                return skill
        return None