import logging
import sys

from contribs.io.sarl.pythongenerator.api.agent.skill import Skill
from contribs.io.sarl.pythongenerator.vm.builtin.capacity.Logging import Logging
from contribs.io.sarl.pythongenerator.vm.builtin.service.LoggingService import LoggingService


class LoggingSkill(Skill, Logging, object):

    def __init__(self):
        super().__init__()
        self.__loggingService = LoggingService()

    def debug(self, message):
        self.__loggingService.log(logging.DEBUG, message)

    def info(self, message):
        self.__loggingService.log(logging.WARNING, message)

    def warning(self, message):
        self.__loggingService.log(logging.WARNING, message, sys.stderr)

    def error(self, message):
        self.__loggingService.log(logging.ERROR, message, sys.stderr)
