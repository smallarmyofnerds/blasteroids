import configparser
import socket


class ServerConfig:
    def __init__(self, config):
        self.address = config['Address']
        self.port = int(config['Port'])

class MiscConfig:
    def __init__(self, config):
        self.logging_level = config['LoggingLevel']

class ClientConfig:
    def __init__(self, config):
        self.screen_width = int(config['Width'])
        self.screen_height = int(config['Height'])

class Config:
    def __init__(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)

        self.server = ServerConfig(config['Server'])
        self.misc = MiscConfig(config['Misc'])
        self.client = ClientConfig(config['Client'])
