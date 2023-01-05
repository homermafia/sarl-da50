import sys
import logging
import time

from vm.utils.singleton import singleton


@singleton
class LoggingService:

    def __init__(self):
        self.__streamHandler = logging.StreamHandler()
        self.__logger = logging.getLogger("Logger")
        self.__logger.addHandler(self.__streamHandler)

    def log(self, level, message, source="SARL Run-time Environment", stream=sys.stdout):
        self.__streamHandler.setStream(stream)
        self.__logger.setLevel(level)
        formattedMessage = "[" + logging.getLevelName(level) + ", " + time.strftime("%I:%M%p") + ", " + source + "] " + message
        self.__logger.log(level, formattedMessage)
        self.__streamHandler.flush()
