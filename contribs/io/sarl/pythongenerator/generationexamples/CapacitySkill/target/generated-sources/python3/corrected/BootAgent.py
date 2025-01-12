#!/usr/bin/env python3
# Generated by the SARL compiler the Thu Oct 13 19:57:43 CEST 2022. Do not change this file.

from io.sarl.lang.core import Agent

from ConsoleLogging import ConsoleLogging
from ConsoleErrorLogging import ConsoleErrorLogging


class BootAgent(Agent, object):
    def __on_Initialize__(self, occurrence):
        s = ConsoleLogging()
        self.setSkill(s)
        s.info(u"Hello World !")
        se = ConsoleErrorLogging()
        self.setSkill(se)
        self.getSkill().info(u"A message 2")
        se.error(u"ERROR")

    def __guard_io_sarl_core_Initialize__(self, occurrence):
        it = occurrence
        __event_handles = list()
        __event_handles.append(self.__on_Initialize__)
        return __event_handles

    def __init__(self):
        pass
