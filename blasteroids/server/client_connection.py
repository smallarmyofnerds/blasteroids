from blasteroids.lib.client_messages.message_encoder import MessageEncoder
from blasteroids.lib.constants import INPUT_MESSAGE_ID, WELCOME_MESSAGE_ID, WORLD_MESSAGE_ID
import select
import threading
from blasteroids.lib import log
from blasteroids.lib.client_messages import InputMessage, WorldMessage, MessageEncoding, WelcomeMessage, MessageBuffer

logger = log.get_logger(__name__)


client_message_encoders = {
    WELCOME_MESSAGE_ID: WelcomeMessage,
    INPUT_MESSAGE_ID: InputMessage,
    WORLD_MESSAGE_ID: WorldMessage,
}


class ClientConnection(threading.Thread):
    def __init__(self, id, socket, address, game, game_server):
        super(ClientConnection, self).__init__()
        self.id = id
        self.socket = socket
        self.is_running = True
        self.address = address
        self.game = game
        self.player = None
        self.game_server = game_server
        self.message_buffer = MessageBuffer(MessageEncoding(client_message_encoders))

        self.outgoing_messages = []
        self.lock = threading.Lock()

    def queue_message(self, message):
        self.lock.acquire()
        self.outgoing_messages.append(message)
        self.lock.release()

    def _receive_bytes(self):
        encoded_bytes = self.socket.recv(8192)
        self.game_server.record_bytes_received(len(encoded_bytes))
        self.message_buffer.push(encoded_bytes)

    def _process_messages(self):
        messages = self.message_buffer.pop_all()
        for message in messages:
            logger.debug(f'Received {message}')
            self._handle_message(message)

    def _handle_message(self, message):
        if message.message_id != INPUT_MESSAGE_ID:
            raise Exception(f'Unexpected message type "{message.message_id}"')

        self.player.update_inputs(message.to_player_inputs())

    def _flush_outgoing_messages(self):
        self.lock.acquire()
        for message in self.outgoing_messages:
            self._send_message(message)
        self.outgoing_messages = []
        self.lock.release()

    def _send_message(self, message):
        encoder = MessageEncoder()
        message.encode(encoder)
        encoded_message = encoder.get_bytes()
        self.socket.send(encoded_message + b'****')
        self.game_server.record_bytes_sent(len(encoded_message) + 4)

    def run(self):
        logger.info('Running client connection')

        self.player = self.game.create_player(self)
        logger.info(f'{self.player.name} connected')

        try:
            while self.is_running:
                self.lock.acquire()
                messages_to_send = len(self.outgoing_messages) > 0
                self.lock.release()

                readable, writable, exceptional = select.select([self.socket], [self.socket] if messages_to_send else [], [self.socket], 0.001)

                for _ in exceptional:
                    self.socket.close()
                    self.is_running = False
                    self.game_server.remove_connection(self)

                if self.is_running:
                    for _ in readable:
                        self._receive_bytes()
                        self._process_messages()

                    for _ in writable:
                        self._flush_outgoing_messages()

        except Exception as e:
            if e.errno == 54:
                logger.info('Player disconnected')
            else:
                logger.exception(e)
        finally:
            logger.info('Removing player from game')
            self.game.remove_player(self.player)
            logger.info('Closing socket')
            self.socket.close()
            logger.info('Removing client connection')
            self.game_server.remove_connection(self)

    def stop(self):
        if self.is_running:
            logger.info(f'Shutting down connection {self.id}')
            self.is_running = False
            self.join(2)
            logger.info(f'Done ({self.id})')
