import configparser
import socket

DEFAULT_SERVER_ADDRESS = ''
DEFAULT_SERVER_PORT = 19999
DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600


class Config:
    def __init__(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)

        self.server_address = config['Server'].get('Address', DEFAULT_SERVER_ADDRESS)
        self.server_port = int(config['Server'].get('Port', DEFAULT_SERVER_PORT))
        self.logging_level = config['Misc'].get('LoggingLevel', 'INFO')

        self.screen_width = int(config['Client'].get('Width', DEFAULT_SCREEN_WIDTH))
        self.screen_height = int(config['Client'].get('Height', DEFAULT_SCREEN_HEIGHT))
