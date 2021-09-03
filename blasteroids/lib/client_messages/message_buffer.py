from blasteroids.lib import log
from .encoded_message import EncodedMessage

logger = log.get_logger(__name__)


class MessageBuffer:
    def __init__(self, message_encoding):
        self.message_encoding = message_encoding
        self.buffer = b''
    
    def push(self, b):
        self.buffer = self.buffer + b
    
    def _pop_encoded_message(self):
        boundary = self.buffer.find(b'****')
        if boundary == -1:
            # not a complete message
            return None

        encoded_message = self.buffer[:boundary]
        self.buffer = self.buffer[boundary + 4:]

        return encoded_message

    def pop_all(self):
        messages = []
        while len(self.buffer) > 0:
            encoded_message = self._pop_encoded_message()
            if encoded_message is None:
                break

            try:
                messages.append(self.message_encoding.decode(EncodedMessage(encoded_message)))
            except Exception as e:
                logger.exception(e)

        return messages
