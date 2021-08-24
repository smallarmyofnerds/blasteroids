import socket
import select
import threading
from blasteroids.lib import log
from .client_connection import ClientConnection

logger = log.get_logger(__name__)

class GameServer:
    def __init__(self, config, game):
        self.address = config.server_address
        self.port = config.server_port
        self.server_name = config.server_name
        self.welcome_message = config.welcome_message
        self.game = game
        self.running = False
        self.client_connections = []
        self.client_connections_lock = threading.Lock()
    
    def _bind_socket(self, address, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((address, port))
        return server
    
    def _register_client_connection(self, client_socket, client_address):
        self.client_connections_lock.acquire()
        connection = ClientConnection(len(self.client_connections), client_socket, client_address, self.config, self.game)
        self.client_connections.append(connection)
        self.client_connections_lock.release()
        connection.start()

    def start(self):
        server = self._bind_socket(self.address, self.port)

        server.listen(1)
        logger.info(f'Server listening on {self.address}:{self.port}')


        self.running = True
        while self.running:
            readable, _, _ = select.select([server], [], [], 0.1)
            for r in readable:
                if r is server:
                    client_socket, client_address = server.accept()
                    logger.info(f'Accepted connection from {client_address}')
                    self._register_client_connection(client_socket, client_address)
        
        logger.info('Server shutting down')

    def stop(self):
        self.running = False
        threading.join(self)
