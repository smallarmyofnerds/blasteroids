from .hello_message import HelloMessage
from .hello_message_decoder import HelloMessageDecoder
from .log import get_logger

logger = get_logger(__name__)

class MessageFactory:
    def __init__(self):
        self.decoders = {
            HelloMessage.TYPE: HelloMessageDecoder(),
        }

    def decode(self, encoded_message):
        type = encoded_message.pop_raw_string(4)
        logger.info(type)
        decoder = self.decoders.get(type)
        if decoder is None:
            raise Exception(f'Unhandled message type {type}')
        return decoder.decode(encoded_message)

