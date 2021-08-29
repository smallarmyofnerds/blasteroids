from blasteroids.lib.client_messages.input import InputMessage, InputMessageEncoder
from blasteroids.lib.client_messages.world import WorldMessage, WorldMessageEncoder
from blasteroids.lib.util.synchronized_queue import SynchronizedQueue
import threading
import socket
import select
from blasteroids.lib import log
from blasteroids.lib.client_messages import MessageEncoding, EncodedMessage

logger = log.get_logger(__name__)

server_message_encoders = {
    InputMessage.TYPE: InputMessageEncoder(),
    WorldMessage.TYPE: WorldMessageEncoder()
}


class ServerConnection(threading.Thread):
    def __init__(self, config):
        super(ServerConnection, self).__init__()
        self.server_address = config.server_address
        self.server_port = config.server_port
        self.socket = None
        self.running = False
        self.message_encoding = MessageEncoding(server_message_encoders)
        self.outgoing_messages = []
        self.outgoing_messages_lock = threading.Lock()
        self.game = None

    def queue_message(self, message):
        self.outgoing_messages_lock.acquire()
        self.outgoing_messages.append(message)
        self.outgoing_messages_lock.release()

    def _send_message(self, message):
        self.socket.send(self.message_encoding.encode(message))

    def _receive_message(self):
        encoded_bytes = self.socket.recv(8192)
        return self.message_encoding.decode(EncodedMessage(encoded_bytes))

    def _flush_outgoing_messages(self):
        self.outgoing_messages_lock.acquire()
        for message in self.outgoing_messages:
            try:
                logger.info(f'Sending {message}')
                self._send_message(message)
            except Exception as e:
                logger.error(e)
        self.outgoing_messages = []
        self.outgoing_messages_lock.release()

    def _handle_message(self, message):
        if message.type != WorldMessage.TYPE:
            raise Exception(f'Unexpected message type {message.type}')

        self.game.update_world(message.to_server_world())

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server_address, self.server_port))

        self.running = True
        while self.running:
            self.outgoing_messages_lock.acquire()
            messages_to_send = len(self.outgoing_messages) > 0
            self.outgoing_messages_lock.release()

            readable, writable, exceptional = select.select([self.socket], [self.socket] if messages_to_send else [], [self.socket], 0.001)

            for _ in readable:
                message = self._receive_message()
                logger.info(f'Received {message}')
                self._handle_message(message)

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
