#!/usr/bin/env python3
# Generated by the SARL compiler the Thu Oct 13 20:12:36 CEST 2022. Do not change this file.

from io.sarl.core import Schedules
from io.sarl.lang.core import Agent

class BootAgent(Agent,object):
	def __on_Initialize__(self, occurrence):
		self.spawn(PingAgent, occurrence.parameters)
		self.spawn(PongAgent, occurrence.parameters)
		self.killMe()
	def __guard_io_sarl_core_Initialize__(self, occurrence):
		it = occurrence
		__event_handles = list
		__event_handles.add(__on_Initialize__)
		return __event_handles
	def __init__(self):
		pass