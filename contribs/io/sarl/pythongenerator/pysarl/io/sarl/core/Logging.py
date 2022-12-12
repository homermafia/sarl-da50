from __future__ import annotations
import abc
from logging import Logger

from pysarl.io.sarl.lang.core.Capacity import Capacity


class Logging(Capacity, abc.ABC):

    @abc.abstractmethod
    def debug(self, message: object, *parameters: object) -> None:
        pass

    #void debug(messageProvider: Supplier < String >)

    @abc.abstractmethod
    def error(self, message: object, exception: BaseException = None, *parameters: object) -> None:
        pass

    # void error(messageProvider: Supplier < String >)

    @abc.abstractmethod
    def getLogger(self) -> Logger:
        pass

    @abc.abstractmethod
    def getLoggerLevel(self) -> int:
        pass

    @abc.abstractmethod
    def info(self, message: object, *parameters: object) -> None:
        pass

    # void info(messageProvider: Supplier < String >)

    @abc.abstractmethod
    def isDebugLogEnabled(self) -> bool:
        pass

    @abc.abstractmethod
    def isErrorLogEnabled(self) -> bool:
        pass

    @abc.abstractmethod
    def isInfoLogEnabled(self) -> bool:
        pass

    @abc.abstractmethod
    def isWarningLogEnabled(self) -> bool:
        pass

    @abc.abstractmethod
    def println(self, message: object) -> None:
        pass

    @abc.abstractmethod
    def setLoggingName(self, name: str) -> None:
        pass

    @abc.abstractmethod
    def setLogLevel(self, level: int) -> None:
        pass

    @abc.abstractmethod
    def warning(self, message: object, exception: BaseException = None, *parameters: object) -> None:
        pass

    # void warning(messageProvider: Supplier < String >)
