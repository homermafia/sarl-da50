#!/usr/bin/env python3
# Generated by the SARL compiler the Thu Oct 13 19:59:28 CEST 2022. Do not change this file.

class SpecialAgent(,object):
	def __on_Initialize__(self, occurrence):
		.println(u"inited")
		self.spawn()
	def __guard_io_sarl_core_Initialize__(self, occurrence):
		it = occurrence
		__event_handles = list
		__event_handles.add(__on_Initialize__)
		return __event_handles
	def __init__(self):
		pass