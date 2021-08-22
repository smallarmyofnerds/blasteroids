import logging

levels = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
}

def initialize_logging(config):
    logging.basicConfig(level=levels.get(config.logging_level, 'INFO'))

def get_logger(name):
    return logging.getLogger(name)
