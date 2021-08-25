from blasteroids.lib.log import get_logger

logger = get_logger(__name__)


class MessageFactory:
    def __init__(self, decoders):
        self.decoders = decoders

    def decode(self, encoded_message):
        type = encoded_message.pop_raw_string(4)
        logger.info(type)
        decoder = self.decoders.get(type)
        if decoder is None:
            raise Exception(f'Unhandled message type {type}')
        return decoder.decode(encoded_message)

