#!/usr/bin/env python3
# Generated by the SARL compiler the Sat Oct 22 13:20:32 CEST 2022. Do not change this file.

from io.sarl.lang.core import Event
from io.sarl.lang.core import EventListener

class FilteringEventListener(EventListener,object):
	def receiveEvent(self, occ : Event) -> :
		if self.parent.acceptedType.isInstance(occ):
			self.parent.behaviorDelegate.asEventListener().receiveEvent(occ)
	def getID(self) -> :
		return self.parent.getID()
	def __init__(self, parent : ) -> :
		(self.parent = parent)