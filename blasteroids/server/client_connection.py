import threading
from blasteroids.lib import log, WelcomeMessage, HelloMessage, MessageFactory, EncodedMessage

logger = log.get_logger(__name__)

class ClientConnection(threading.Thread):
    def __init__(self, socket, address, server_name, welcome_message, message_factory = MessageFactory()):
        super(ClientConnection, self).__init__()
        self.socket = socket
        self.address = address
        self.server_name = server_name
        self.welcome_message = welcome_message
        self.message_factory = message_factory
    
    def _send_message(self, message):
        logger.info(f'Sending {message}')
        self.socket.send(message.encode())
    
    def _receive_message(self):
        encoded_bytes = self.socket.recv(8192)
        decoded_message = self.message_factory.decode(EncodedMessage(encoded_bytes))
        logger.info(f'Received {decoded_message}')
        return decoded_message
    
    def run(self):
        logger.info('Running client connection')
        try:
            self._send_message(WelcomeMessage(self.server_name, self.welcome_message))
            message = self._receive_message()
            if message.type != HelloMessage.TYPE:
                raise Exception(f'Expecting HELO, got {message.type}')
        except Exception as e:
            logger.error(e)

