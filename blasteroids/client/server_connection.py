from blasteroids.lib.client_messages.message_encoder import MessageEncoder
from blasteroids.lib.constants import INPUT_MESSAGE_ID, WELCOME_MESSAGE_ID, WORLD_MESSAGE_ID
from blasteroids.lib.client_messages.welcome import WelcomeMessage
from blasteroids.lib.client_messages.input import InputMessage
from blasteroids.lib.client_messages.world import WorldMessage
import threading
import socket
import select
from blasteroids.lib import log
from blasteroids.lib.client_messages import MessageEncoding, MessageBuffer

logger = log.get_logger(__name__)

server_message_encoders = {
    WELCOME_MESSAGE_ID: WelcomeMessage,
    INPUT_MESSAGE_ID: InputMessage,
    WORLD_MESSAGE_ID: WorldMessage,
}


class ServerConnection(threading.Thread):
    def __init__(self, config):
        super(ServerConnection, self).__init__()
        self.server_address = config.server.address
        self.server_port = config.server.port
        self.socket = None
        self.running = False
        self.message_buffer = MessageBuffer(MessageEncoding(server_message_encoders))
        self.outgoing_messages = []
        self.lock = threading.Lock()
        self.game = None

    def queue_message(self, message):
        self.lock.acquire()
        self.outgoing_messages.append(message)
        self.lock.release()

    def _receive_bytes(self):
        encoded_bytes = self.socket.recv(8192)
        self.message_buffer.push(encoded_bytes)

    def _process_messages(self):
        messages = self.message_buffer.pop_all()
        for message in messages:
            logger.debug(f'Received {message}')
            self._handle_message(message)

    def _handle_message(self, message):
        if message.message_id == WELCOME_MESSAGE_ID:
            self.game.initialize_world(message.world_width, message.world_height, message.boundary)
            return
        if message.message_id != WORLD_MESSAGE_ID:
            raise Exception(f'Unexpected message type {message.message_id}')

        self.game.update_world(message.to_server_world())

    def _flush_outgoing_messages(self):
        self.lock.acquire()
        for message in self.outgoing_messages:
            try:
                logger.debug(f'Sending {message}')
                self._send_message(message)
            except Exception as e:
                logger.error(e)
        self.outgoing_messages = []
        self.lock.release()

    def _send_message(self, message):
        encoder = MessageEncoder()
        message.encode(encoder)
        self.socket.send(encoder.get_bytes() + b'****')

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server_address, self.server_port))

        self.running = True
        while self.running:
            self.lock.acquire()
            messages_to_send = len(self.outgoing_messages) > 0
            self.lock.release()

            readable, writable, exceptional = select.select([self.socket], [self.socket] if messages_to_send else [], [self.socket], 0.001)

            for _ in readable:
                self._receive_bytes()
                self._process_messages()

            for _ in writable:
                self._flush_outgoing_messages()

            for _ in exceptional:
                self.socket.close()
                self.running = False

        logger.info('Closing server connection')
        self.socket.shutdown(1)
        self.socket.close()

    def stop(self):
        if self.running:
            logger.info('Shutting down')
            self.running = False
            self.join(2)
            logger.info('Done')
