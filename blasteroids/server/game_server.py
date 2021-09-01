import socket
import select
import threading
from blasteroids.lib import log
from .client_connection import ClientConnection

logger = log.get_logger(__name__)


class ConnectionFactory:
    def __init__(self, game_server, game):
        self.game_server = game_server
        self.game = game
        self.next_id = 0

    def get_next_id(self):
        id = self.next_id
        self.next_id += 1
        return id

    def create(self, client_socket, client_address):
        logger.info('Creating new client connection')
        return ClientConnection(self.get_next_id(), client_socket, client_address, self.game, self.game_server)


class GameServer:
    def __init__(self, config, game):
        self.address = config.server.address
        self.port = config.server.port
        self.connection_factory = ConnectionFactory(self, game)
        self.client_connections = []
        self.client_connections_lock = threading.Lock()
        self.running = False

    def _bind_socket(self, address, port):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((address, port))
        return server

    def _register_client_connection(self, client_socket, client_address):
        connection = self.connection_factory.create(client_socket, client_address)
        connection.start()
        self.client_connections_lock.acquire()
        self.client_connections.append(connection)
        self.client_connections_lock.release()

    def remove_connection(self, client_connection):
        self.client_connections_lock.acquire()
        self.client_connections.remove(client_connection)
        self.client_connections_lock.release()

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

        logger.info('Closing client connections')
        self.client_connections_lock.acquire()
        for client_connection in self.client_connections:
            client_connection.stop()
        self.client_connections_lock.release()

        logger.info('Shutting down')

    def stop(self):
        self.running = False
