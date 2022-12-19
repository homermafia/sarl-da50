import sys
import logging

from vm.utils.singleton import singleton


@singleton
class LoggingService:

    def __init__(self):
        self.__streamHandler = logging.StreamHandler()
        self.__logger = logging.getLogger("Logger")
        self.__logger.addHandler(self.__streamHandler)

    def log(self, level, message, stream=sys.stdout):
        self.__streamHandler.setStream(stream)
        self.__logger.setLevel(level)
        self.__logger.log(level, message)
        self.__streamHandler.flush()
