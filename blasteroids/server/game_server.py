import socket
from blasteroids.lib import log
from .client_connection import ClientConnection

logger = log.get_logger(__name__)

class GameServer:
    def __init__(self, address, port, config):
        self.address = address
        self.port = port
        self.server_name = config.server_name
        self.welcome_message = config.welcome_message
        pass
    
    def _bind_socket(self, address, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((address, port))
        return server

    def start(self):
        server = self._bind_socket(self.address, self.port)
        logger.info(f'Server listening on {self.address}:{self.port}')

        while True:
            server.listen(1)
            client_socket, client_address = server.accept()
            logger.info(f'Accepted connection from {client_address}')
            connection = ClientConnection(client_socket, client_address, self.server_name, self.welcome_message)
            connection.start()

