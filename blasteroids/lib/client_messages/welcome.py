from .message import Message
from .message_encoder import MessageEncoder


class WelcomeMessage(Message):
    TYPE = 'WELC'

    def __init__(self, world_width, world_height):
        super(WelcomeMessage, self).__init__(WelcomeMessage.TYPE)
        self.world_width = world_width
        self.world_height = world_height

    def __repr__(self):
        return f'{super(WelcomeMessage, self).__repr__()}:{self.world_width}:{self.world_height}'


class WelcomeMessageEncoder(MessageEncoder):
    def __init__(self):
        super(WelcomeMessageEncoder, self).__init__(WelcomeMessage.TYPE)

    def encode(self, message):
        return super(WelcomeMessageEncoder, self)._encode_type() + self._encode_short(message.world_width) + self._encode_short(message.world_height)

    def decode(self, encoded_message):
        world_width = encoded_message.pop_short()
        world_height = encoded_message.pop_short()
        return WelcomeMessage(world_width, world_height)
