#!/usr/bin/env python3
# Generated by the SARL compiler the Thu Oct 13 11:30:30 CEST 2022. Do not change this file.

from io.sarl.lang.core import Capacity
from io.sarl.lang.core import Event


class pingCapacity(Capacity, object):
    def sendping(self):
        raise Exception("Unimplemented function")

    def replyPing(self, occ: Event):
        raise Exception("Unimplemented function")

    def __init__(self):
        pass
