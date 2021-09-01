from blasteroids.lib.client_messages.input import InputMessageEncoder
import select
import threading
from blasteroids.lib import log
from blasteroids.lib.client_messages import InputMessage, WorldMessage, WorldMessageEncoder, MessageEncoding, WelcomeMessage, WelcomeMessageEncoder, MessageBuffer

logger = log.get_logger(__name__)


client_message_encoders = {
    WelcomeMessage.TYPE: WelcomeMessageEncoder(),
    InputMessage.TYPE: InputMessageEncoder(),
    WorldMessage.TYPE: WorldMessageEncoder()
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
        self.message_encoding = MessageEncoding(client_message_encoders)
        self.message_buffer = MessageBuffer(self.message_encoding)

        self.outgoing_messages = []
        self.lock = threading.Lock()

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
            logger.info(f'Received {message}')
            self._handle_message(message)

    def _handle_message(self, message):
        if message.type != InputMessage.TYPE:
            raise Exception(f'Unexpected message type "{message.type}"')

        self.player.update_inputs(message.to_player_inputs())

    def _flush_outgoing_messages(self):
        self.lock.acquire()
        for message in self.outgoing_messages:
            self._send_message(message)
        self.outgoing_messages = []
        self.lock.release()

    def _send_message(self, message):
        self.socket.send(self.message_encoding.encode(message))

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
            logger.error(e)
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
