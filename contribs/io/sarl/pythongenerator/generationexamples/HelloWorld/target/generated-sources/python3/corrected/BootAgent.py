
from io.sarl.core import Lifecycle
from io.sarl.core import Logging
from io.sarl.lang.core import Agent

class BootAgent(Agent,object):
	def __on_Initialize__(self, occurrence):
		self.getSkill(Logging).info(u"Hello World!")
		self.getSkill(Lifecycle).killMe()

	def __guard_io_sarl_core_Initialize__(self, occurrence):
		it = occurrence
		__event_handles = list()
		__event_handles.append(self.__on_Initialize__)
		return __event_handles

	def __init__(self):
		pass
