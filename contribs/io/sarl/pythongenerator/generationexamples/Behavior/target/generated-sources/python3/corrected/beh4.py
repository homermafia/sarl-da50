#!/usr/bin/env python3
# Generated by the SARL compiler the Sat Oct 22 12:19:50 CEST 2022. Do not change this file.

from io.sarl.lang.core import Agent
from io.sarl.lang.core import Behavior

from s import s


class beh4(Behavior, object):
    def __on_Initialize__(self, occurrence):
        print(u"behaviour initialized")

    def __guard_io_sarl_core_Initialize__(self, occurrence):
        it = occurrence
        __event_handles = list()
        __event_handles.append(self.__on_Initialize__)
        return __event_handles

    def __init__(self, owner: Agent):
        super().__init__(owner)
        sk = s()
        print(u"setting skill")
        self.setSkill(sk)
        print(u"skill set")
