#!/usr/bin/env python3
# Generated by the SARL compiler the Wed Oct 19 16:25:56 CEST 2022. Do not change this file.

from io.sarl.lang.core import Agent

class SecondAgent(Agent,object):
	def __on_Initialize__(self, occurrence):
		(self.myVar = 10)
		self.printstate(self.getstate())
		self.printstate(self.getstate2())
		self.printstate2(self.getstate())
	def getstate(self) -> :
		return self.myVar
	def getstate2(self) -> :
		return self.myVar
	def printstate(self, s : ) -> int:
		return .println(self.myVar)
	def printstate2(self, s_1 : ):
		.println(self.myVar)
	def __guard_io_sarl_core_Initialize__(self, occurrence):
		it = occurrence
		__event_handles = list
		__event_handles.add(__on_Initialize__)
		return __event_handles
	def __init__(self):
		self.myVar = 0