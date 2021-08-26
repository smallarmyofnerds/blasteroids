from .message import Message
from .message_encoder import MessageEncoder


class WelcomeMessage(Message):
    TYPE = 'WELC'

    def __init__(self, server_name, welcome_message):
        super(WelcomeMessage, self).__init__(WelcomeMessage.TYPE)
        self.server_name = server_name
        self.welcome_message = welcome_message

    def __repr__(self):
        return f'{super(WelcomeMessage, self).__repr__()}:{self.server_name}:{self.welcome_message}'


class WelcomeMessageEncoder(MessageEncoder):
    def __init__(self):
        super(WelcomeMessageEncoder, self).__init__(WelcomeMessage.TYPE)

    def encode(self, message):
        return super(WelcomeMessageEncoder, self)._encode_type() + self._encode_string(message.server_name) + self._encode_string(message.welcome_message)

    def decode(self, encoded_message):
        player_name = encoded_message.pop_string()
        return WelcomeMessage(player_name)
