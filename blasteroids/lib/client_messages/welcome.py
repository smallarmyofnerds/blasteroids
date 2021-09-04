from .message import Message
from .message_encoder import MessageEncoder
from ..constants import WELCOME_MESSAGE_ID


class WelcomeMessage(Message):
    def __init__(self, world_width, world_height):
        super(WelcomeMessage, self).__init__(WELCOME_MESSAGE_ID)
        self.world_width = world_width
        self.world_height = world_height

    def __repr__(self):
        return f'{super(WelcomeMessage, self).__repr__()}:{self.world_width}:{self.world_height}'


class WelcomeMessageEncoder(MessageEncoder):
    def __init__(self):
        super(WelcomeMessageEncoder, self).__init__(WELCOME_MESSAGE_ID)

    def encode(self, message):
        buffer = bytearray()
        buffer += self._encode_byte(WELCOME_MESSAGE_ID)
        buffer += self._encode_short(message.world_width)
        buffer += self._encode_short(message.world_height)
        buffer += b'****'
        return bytes(buffer)

    def decode(self, encoded_message):
        world_width = encoded_message.pop_short()
        world_height = encoded_message.pop_short()
        return WelcomeMessage(world_width, world_height)
