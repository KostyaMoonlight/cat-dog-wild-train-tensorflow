import logging

class Logger:
    def __init__(self, _class):
        self._class = _class
        self.debug_logger = logging.Logger("debug.log", logging.DEBUG)
        self.info_logger = logging.Logger("info.log", logging.INFO)
        self.error_logger = logging.Logger("error.log", logging.ERROR)

    def info(self, message):
        self.info_logger.info(f"{self._class.__class__.__name__} {message}")

    def warning(self, message):
        self.info_logger.warning(f"{self._class.__class__.__name__} {message}")

    def error(self, message):
        self.error_logger.error(f"{self._class.__class__.__name__} {message}")
    
    def debug(self, message):
        self.debug_logger.debug(f"{self._class.__class__.__name__} {message}")