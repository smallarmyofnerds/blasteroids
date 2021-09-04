from .message import Message
from ..constants import WELCOME_MESSAGE_ID


class WelcomeMessage(Message):
    def __init__(self, world_width, world_height, boundary):
        super(WelcomeMessage, self).__init__(WELCOME_MESSAGE_ID)
        self.world_width = world_width
        self.world_height = world_height
        self.boundary = boundary

    def __repr__(self):
        return f'{super(WelcomeMessage, self).__repr__()}:{self.world_width}:{self.world_height}'

    def encode(self, message_encoder):
        super(WelcomeMessage, self).encode(message_encoder)
        message_encoder.push_short(self.world_width)
        message_encoder.push_short(self.world_height)
        message_encoder.push_short(self.boundary)

    def decode_body(encoded_message):
        world_width = encoded_message.pop_short()
        world_height = encoded_message.pop_short()
        boundary = encoded_message.pop_short()
        return WelcomeMessage(world_width, world_height, boundary)
