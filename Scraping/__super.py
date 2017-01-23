import logging


class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info('Setting %r' % (key, value))
        super().__setitem__(key, value)
