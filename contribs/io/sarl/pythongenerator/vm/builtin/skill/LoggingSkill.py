import logging
import sys

from pysarl.io.sarl.core.Logging import Logging
from pysarl.io.sarl.lang.core.Skill import Skill
from vm.builtin.service.LoggingService import LoggingService


class LoggingSkill(Skill, Logging):
    __logService: LoggingService

    def __init__(self):
        super().__init__()
        self.__logService = LoggingService()

    def debug(self, message: object, *parameters: object) -> None:
        self.__logService.log(logging.DEBUG, message, self.getOwnerClassName())

    def error(self, message: object, exception: BaseException = None, *parameters: object) -> None:
        self.__logService.log(logging.ERROR, message, sys.stderr, self.getOwnerClassName())

    def getLogger(self) -> logging.Logger:
        # TODO: Write this method
        pass

    def getLoggerLevel(self) -> int:
        # TODO: Write this method
        pass

    def info(self, message: object, *parameters: object) -> None:
        self.__logService.log(logging.INFO, message, self.getOwnerClassName())

    def isDebugLogEnabled(self) -> bool:
        # TODO: Write this method
        pass

    def isErrorLogEnabled(self) -> bool:
        # TODO: Write this method
        pass

    def isInfoLogEnabled(self) -> bool:
        # TODO: Write this method
        pass

    def isWarningLogEnabled(self) -> bool:
        # TODO: Write this method
        pass

    def println(self, message: object) -> None:
        # TODO: Write this method
        pass

    def setLoggingName(self, name: str) -> None:
        # TODO: Write this method
        pass

    def setLogLevel(self, level: int) -> None:
        # TODO: Write this method
        pass

    def warning(self, message: object, exception: BaseException = None, *parameters: object) -> None:
        self.__logService.log(logging.WARNING, message, self.getOwnerClassName(), sys.stderr)

