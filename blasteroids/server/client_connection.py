import select
import threading
from blasteroids.lib import log, WelcomeMessage, MessageFactory, EncodedMessage
import blasteroids.lib.client_messages as client_messages

logger = log.get_logger(__name__)


class ClientConnectionState:
    def __init__(self, client_connection, game):
        self.client_connection = client_connection
        self.game = game

    def queue_client_message(self, message):
        self.client_connection.queue_message(message)

    def queue_game_message(self, message):
        self.game.queue_message(message)

    def handle_HELO(self):
        raise Exception('Unexpected HELO')

    def handle_INPT(self):
        raise Exception('Unexpected INPT')


class ReadyState(ClientConnectionState):
    def __init__(self, client_connection, game, player_name):
        super(ReadyState, self).__init__(client_connection, game)
        self.player_name = player_name

    def handle_INPT(self, message):
        self.queue_game_message(InputGameMessage(self.player_name, message))


class HandshakeState(ClientConnectionState):
    def __init__(self, client_connection, game, server_name, welcome_message):
        super(HandshakeState, self).__init__(client_connection, game)
        self.server_name = server_name
        self.welcome_message = welcome_message

    def initialize(self):
        self.queue_client_message(WelcomeMessage(self.server_name, self.welcome_message))

    def handle_HELO(self, message):
        return ReadyState(self.client_connection, self.game, message.player_name)


client_message_decoders = {
    client_messages.HelloMessage.TYPE: client_messages.HelloMessageDecoder(),
}

from collections import deque

class SynchronizedQueue:
    def __init__(self):
        self.items = deque([])
        self.lock = threading.Lock()

    def push(self, item):
        self.lock.acquire()
        self.items.append(item)
        self.lock.release()
    
    def pop(self):
        self.lock.acquire()
        item = self.items.popleft()
        self.lock.release()
        return item
    
    def is_empty(self):
        self.lock.acquire()
        is_empty = len(self.items) == 0
        self.lock.release()
        return is_empty
    
    def __iter__(self):


class ClientConnection(threading.Thread):
    def __init__(self, id, socket, address, config, hub, game_server, message_factory=MessageFactory(client_message_decoders)):
        super(ClientConnection, self).__init__()
        self.id = id
        self.socket = socket
        self.is_running = True
        self.address = address
        self.server_name = config.server_name
        self.welcome_message = config.welcome_message
        self.hub = hub
        self.game_server = game_server
        self.message_factory = message_factory
        self.state = None
        self.outgoing_messages = SynchronizedQueue()

    def queue_message(self, message):
        self.outgoing_messages_lock.acquire()
        self.outgoing_messages.append(message)
        self.outgoing_messages_waiting = True
        self.outgoing_messages_lock.release()

    def _send_message(self, message):
        self.socket.send(message.encode())

    def _receive_message(self):
        encoded_bytes = self.socket.recv(8192)
        return self.message_factory.decode(EncodedMessage(encoded_bytes))

    def _set_state(self, state):
        self.state = state
        state.initialize()

    def _flush_outgoing_messages(self):
        self.outgoing_messages_lock.acquire()
        for message in self.outgoing_messages:
            logger.info(f'Sending {message}')
            self._send_message(message)
        self.outgoing_messages_waiting = False
        self.outgoing_messages_lock.release()

    def run(self):
        logger.info('Running client connection')

        try:
            self._set_state(HandshakeState(self, self.id, self.server_name, self.welcome_message))

            while self.is_running:
                readable, writable, exceptional = select.select([self.socket], [self.socket] if not self.outgoing_messages.is_empty() else [], [self.socket])

                for _ in readable:
                    message = self._receive_message()
                    logger.info(f'Received {message}')
                    next_state = message.dispatch(self.state)
                    if next_state is not None:
                        self._set_state(next_state)

                for _ in writable:
                    self._flush_outgoing_messages()

                for _ in exceptional:
                    self.socket.close()
                    self.is_running = False
                    self.game_server.remove_connection(self)

        except Exception as e:
            logger.error(e)
