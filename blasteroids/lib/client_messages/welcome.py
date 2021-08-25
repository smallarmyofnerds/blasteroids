from .message import Message
from .message_decoder import MessageDecoder


class WelcomeMessage(Message):
    TYPE = 'WELC'

    def __init__(self, server_name, welcome_message):
        super(WelcomeMessage, self).__init__(WelcomeMessage.TYPE)
        self.server_name = server_name
        self.welcome_message = welcome_message

    def encode(self):
        return super(WelcomeMessage, self).encode() + self.encode_string(self.server_name) + self.encode_string(self.welcome_message)

    def __repr__(self):
        return f'{super(WelcomeMessage, self).__repr__()}:{self.server_name}:{self.welcome_message}'


class WelcomeMessageDecoder(MessageDecoder):
    def decode(self, encoded_message):
        player_name = encoded_message.pop_string()
        return WelcomeMessage(player_name)
