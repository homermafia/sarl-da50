from pysarl.io.sarl.lang.core.Capacity import Capacity


class Time(Capacity):
    """
    @param : timeDuration
    """

    def fromOSDuration(self, timeDuration):
        pass

    """
        @param : timeValue
    """

    def fromOSTime(self, timeValue):
        pass

    def getOSTimeFactor(self):
        pass

    def getTime(self):
        pass

    """
        @param : timeDuration
    """

    def toOSDuration(self, timeDuration):
        pass

    """
        @param : timeValue
   """

    def toOSTime(self, timeValue):
        pass
