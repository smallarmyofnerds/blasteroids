import configparser
import socket

DEFAULT_SERVER_ADDRESS = ''
DEFAULT_SERVER_PORT = 19999

class Config:
    def __init__(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)

        self.server_address = config['Server'].get('Address', DEFAULT_SERVER_ADDRESS)
        self.server_port = int(config['Server'].get('Port', DEFAULT_SERVER_PORT))
        self.server_name = config['Server'].get('Name', socket.gethostname())
        self.welcome_message = config['Server'].get('WelcomeMessage', f'Welcome to the {socket.gethostname()} server!')
        self.logging_level = config['Misc'].get('LoggingLevel', 'INFO')
