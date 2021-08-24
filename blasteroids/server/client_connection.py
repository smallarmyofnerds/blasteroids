import select
import threading
from blasteroids.lib import log, WelcomeMessage, HelloMessage, MessageFactory, EncodedMessage

logger = log.get_logger(__name__)

class ClientConnectionState:
    def __init__(self, send_message):
        self.send_message = send_message

class ReadyState(ClientConnectionState):
    def __init__(self, send_message, player_name):
        super(ReadyState, self).__init__(send_message)
        self.player_name = player_name
    
class HandshakeState(ClientConnectionState):
    def __init__(self, send_message, server_name, welcome_message):
        super(HandshakeState, self).__init__(send_message)
        self.server_name = server_name
        self.welcome_message = welcome_message

    def initialize(self):
        self.send_message(WelcomeMessage(self.server_name, self.welcome_message))

    def handle_HELO(self, message):
        self.set_state(ReadyState(message.player_name))

class ClientConnection(threading.Thread):
    def __init__(self, id, socket, address, config, game, message_factory = MessageFactory()):
        super(ClientConnection, self).__init__()
        self.id = id
        self.socket = socket
        self.address = address
        self.server_name = config.server_name
        self.welcome_message = config.welcome_message
        self.game = game
        self.message_factory = message_factory
        self.state = None
        self.outgoing_messages = []
        self.outgoing_messages_lock = threading.Lock()
        self.outgoing_messages_waiting = False
    
    def queue_message(self, message):
        self.outgoing_messages_lock.acquire()
        self.outgoing_messages.append(message)
        self.outgoing_messages_waiting = True
        self.outgoing_messages_lock.release()

    def _send_message(self, message):
        logger.info(f'Sending {message}')
        self.socket.send(message.encode())
    
    def _receive_message(self):
        encoded_bytes = self.socket.recv(8192)
        decoded_message = self.message_factory.decode(EncodedMessage(encoded_bytes))
        logger.info(f'Received {decoded_message}')
        return decoded_message
    
    def _set_state(self, state):
        self.state = state
        state.initialize()
    
    def run(self):
        logger.info('Running client connection')
        
        try:
            self._set_state(HandshakeState(self.server_name, self.welcome_message, self._send_message, self._set_state))

            while True:
                readable, writable, _ = select.select([self.socket], [self.socket] if len(self.outgoing_messages) > 0 else [], [])

                for r in readable:
                    message = self._receive_message()
                    message.dispatch(self.state)

                for w in writable:
                    self.outgoing_messages_lock.acquire()
                    for message in self.outgoing_messages:
                        self._send_message(message)
                    self.outgoing_messages_lock.release()
        except Exception as e:
            logger.error(e)

