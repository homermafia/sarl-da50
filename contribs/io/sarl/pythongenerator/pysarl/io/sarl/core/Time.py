import abc

from pysarl.io.sarl.lang.core.Capacity import Capacity


class Time(Capacity, abc.ABC):

    """
    @param : timeDuration
    """
    @abc.abstractmethod
    def fromOSDuration(self, timeDuration: float) -> float:
        pass

    """
        @param : timeValue
    """
    @abc.abstractmethod
    def fromOSTime(self, timeValue: float) -> float:
        pass

    @abc.abstractmethod
    def getOSTimeFactor(self) -> float:
        pass

    """
        @param : timeDuration
    """
    @abc.abstractmethod
    def getTime(self, timeUnit = None) -> float:
        pass

    """
        @param : timeDuration
    """
    @abc.abstractmethod
    def toOSDuration(self, timeDuration: float) -> float:
        pass

    """
        @param : timeValue
   """
    @abc.abstractmethod
    def toOSTime(self, timeValue: float) -> float:
        pass
