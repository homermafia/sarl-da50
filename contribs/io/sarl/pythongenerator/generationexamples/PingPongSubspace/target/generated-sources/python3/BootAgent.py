#!/usr/bin/env python3
# Generated by the SARL compiler the Sun Oct 23 23:39:11 CEST 2022. Do not change this file.

from io.sarl.core import Lifecycle
from io.sarl.lang.core import Agent

class BootAgent(Agent,object):
	def __on_Initialize__(self, occurrence):
		self.getSkill(Lifecycle).spawn(PingAgent, occurrence.parameters)
		self.getSkill(Lifecycle).spawn(PongAgent, occurrence.parameters)
		self.getSkill(Lifecycle).killMe_1()
	def __guard_io_sarl_core_Initialize__(self, occurrence):
		it = occurrence
		__event_handles = list
		__event_handles.add(__on_Initialize__)
		return __event_handles
	def __init__(self):
		pass