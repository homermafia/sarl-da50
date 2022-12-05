import logging
import sys

from pysarl.io.sarl.lang.core.Skill import Skill
from vm.builtin.capacity.Logging import Logging
from vm.builtin.service.LoggingService import LoggingService


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
