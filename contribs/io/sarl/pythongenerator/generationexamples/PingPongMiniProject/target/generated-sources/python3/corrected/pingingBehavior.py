#!/usr/bin/env python3
# Generated by the SARL compiler the Thu Oct 13 11:30:30 CEST 2022. Do not change this file.

from io.sarl.core import OpenEventSpace
from io.sarl.lang.core import Agent
from io.sarl.lang.core import Behavior

from pingSkill import pingSkill
from pingCapacity import pingCapacity


class pingingBehavior(Behavior, object):
    def __on_Initialize__(self, occurrence):
        class __Jclosure_Procedure1(object):
            def apply(self, it):
                self.sendping()

        tsk = self.task(u"ping")
        self.every(tsk, 1000, __Jclosure_Procedure1())

    def __on_Destroy__(self, occurrence):
        pass

    def __guard_io_sarl_core_Initialize__(self, occurrence):
        it = occurrence
        __event_handles = list()
        __event_handles.append(self.__on_Initialize__)
        return __event_handles

    def __guard_io_sarl_core_Destroy__(self, occurrence):
        it = occurrence
        __event_handles_1 = list()
        __event_handles_1.append(self.__on_Destroy__)
        return __event_handles_1

    def __init__(self, owner: Agent, spc: OpenEventSpace):
        super().__init__(owner)
        pingSk = pingSkill(spc)
        self.setSkill(pingSk, pingCapacity)