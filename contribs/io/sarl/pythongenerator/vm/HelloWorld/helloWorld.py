#!/usr/bin/env python3
# Generated by the SARL compiler the Thu Oct 13 19:57:44 CEST 2022. Do not change this file.


#### GENERATED PYTHON CODE OF THE FIRST VERSION OF HELLOWORLD
""""
from io.sarl.lang.core import Agent
from org.eclipse.xtext.xbase.lib import InputOutput

class BootAgent(Agent,object):
	def __on_Initialize__(self, occurrence):
		InputOutput.println(u"Hello World!")
	def __guard_io_sarl_core_Initialize__(self, occurrence):
		it = occurrence
		__event_handles = list
		__event_handles.add(__on_Initialize__)
		return __event_handles
	def __init__(self):
		pass
"""

#### GENERATED PYTHON CODE OF THE FIRST VERSION OF HELLOWORLD
"""
from io.sarl.core import Lifecycle
from io.sarl.lang.core import Agent

class BootAgent(Agent,object):
	def __on_Initialize__(self, occurrence):
		self.info(u"Hello World!")
		self.getSkill(Lifecycle).killMe()
	def __guard_io_sarl_core_Initialize__(self, occurrence):
		it = occurrence
		__event_handles = list
		__event_handles.add(__on_Initialize__)
		return __event_handles
	def __init__(self):
		pass
"""

#### PYTHON CODE WITH NECESSARY MODIFICATIONS

from contribs.io.sarl.pythongenerator.api.agent.agent import Agent
from contribs.io.sarl.pythongenerator.vm.builtin.capacity.Logging import Logging
from contribs.io.sarl.pythongenerator.vm.builtin.capacity.Lifecycle import Lifecycle


class HelloWorldAgent(Agent, object):

    def __on_Initialize__(self, occurrence):
        self.getSkill(Logging).debug(u"Hello World!d")
        self.getSkill(Logging).info(u"Hello World!i")
        # print(str(5/0))
        self.getSkill(Lifecycle).killMe()
        print("after killMe nothing should be executed")

    def __guard_io_sarl_core_Initialize__(self, occurrence):
        it = occurrence
        __event_handles = list()
        __event_handles.append(self.__on_Initialize__)
        return __event_handles

    def __on_Destroy__(self, occurrence):
        self.getSkill(Logging).debug(u"Goodbye World!d")

    def __guard_io_sarl_core_Destroy__(self, occurrence):
        it = occurrence
        __event_handles = list()
        __event_handles.append(self.__on_Destroy__)
        return __event_handles

    def __on_AgentSpawned__(self, occurrence):
        skill = self.getSkill(Logging)
        skill.info("Agent " + str(occurrence.getAgentId()) + " of type " + occurrence.getAgentType()
                   + " has spawned")

    def __guard_io_sarl_core_AgentSpawned__(self, occurrence):
        it = occurrence
        __event_handles = list()
        __event_handles.append(self.__on_AgentSpawned__)
        return __event_handles

    def __on_AgentKilled__(self, occurrence):
        skill = self.getSkill(Logging)
        skill.info("Agent of type " + occurrence.getAgentType() + " has been killed")

    def __guard_io_sarl_core_AgentKilled__(self, occurrence):
        it = occurrence
        __event_handles = list()
        __event_handles.append(self.__on_AgentKilled__)
        return __event_handles

    def __init__(self, parentID, agentID, dynamicSkillProvider=None):
        super().__init__(parentID, agentID, dynamicSkillProvider)
