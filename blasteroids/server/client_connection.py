from blasteroids.lib.client_messages.input import InputMessageEncoder
import select
import threading
from blasteroids.lib import log
from blasteroids.lib.client_messages import InputMessage, WorldMessage, WorldMessageEncoder, MessageEncoding, EncodedMessage, WelcomeMessage, WelcomeMessageEncoder

logger = log.get_logger(__name__)


client_message_encoders = {
    WelcomeMessage.TYPE: WelcomeMessageEncoder(),
    InputMessage.TYPE: InputMessageEncoder(),
    WorldMessage.TYPE: WorldMessageEncoder()
}


class ClientConnection(threading.Thread):
    def __init__(self, id, socket, address, config, game, game_server):
        super(ClientConnection, self).__init__()
        self.id = id
        self.socket = socket
        self.is_running = True
        self.address = address
        self.server_name = config.server_name
        self.welcome_message = config.welcome_message
        self.game = game
        self.player = None
        self.game_server = game_server
        self.message_encoding = MessageEncoding(client_message_encoders)

        self.outgoing_messages = []
        self.outgoing_messages_lock = threading.Lock()

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
            self._send_message(message)
        self.outgoing_messages = []
        self.outgoing_messages_lock.release()

    def _handle_message(self, message):
        if message.type != InputMessage.TYPE:
            raise Exception(f'Unexpected message type "{message.type}"')

        self.player.update_inputs(message.to_player_inputs())

    def run(self):
        logger.info('Running client connection')

        self.player = self.game.create_player(self)

        try:
            while self.is_running:
                self.outgoing_messages_lock.acquire()
                messages_to_send = len(self.outgoing_messages) > 0
                self.outgoing_messages_lock.release()

                readable, writable, exceptional = select.select([self.socket], [self.socket] if messages_to_send else [], [self.socket], 0.001)

                for _ in exceptional:
                    self.socket.close()
                    self.is_running = False
                    self.game_server.remove_connection(self)

                if self.is_running:
                    for _ in readable:
                        # logger.info('Socket is readable')
                        message = self._receive_message()
                        if message:
                            logger.info(f'Received {message}')
                            self._handle_message(message)

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
