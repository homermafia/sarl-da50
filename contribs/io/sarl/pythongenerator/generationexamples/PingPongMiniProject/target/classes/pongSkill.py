#!/usr/bin/env python3
# Generated by the SARL compiler the Thu Oct 13 11:30:30 CEST 2022. Do not change this file.

from io.sarl.core import OpenEventSpace
from io.sarl.lang.core import Address
from io.sarl.lang.core import Event

class pongSkill(,object):
	def sendpong(self) -> :
		if (self.spc.getNumberOfStrongParticipants() > 1):
			e = PongEvent(0)
			.println(u"Sending pong event")
			self.spc.emit(self.getID(), e)
		else:
			.println(u"I am alone in this event")
	def replyPong(self, occ : Event) -> :
		class __Jclosure_(Address)=>boolean((Address)=>bool,object):
			def matches(self, it):
				(it == occ.getSource())
		if (self.spc.getNumberOfStrongParticipants() > 1):
			e = PongEvent(0)
			.println(u"Replying with pong event")
			self.spc.emit(self.getID(), e, __Jclosure_(Address)=>boolean())
		else:
			.println(u"I am alone in this event")
	def __init__(self, pongSpace : OpenEventSpace) -> :
		(self.spc = pongSpace)