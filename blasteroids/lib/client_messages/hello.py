from .message import Message
from .message_decoder import MessageDecoder


class HelloMessage(Message):
    TYPE = 'HELO'

    def __init__(self, player_name):
        super(HelloMessage, self).__init__(HelloMessage.TYPE)
        self.player_name = player_name

    def encode(self):
        return super(HelloMessage, self).encode() + self.encode_string(self.player_name)

    def dispatch(self, state):
        return state.handle_HELO(self)

    def __repr__(self):
        return f'{super(HelloMessage, self).__repr__()}:{self.player_name}'


class HelloMessageDecoder(MessageDecoder):
    def decode(self, encoded_message):
        player_name = encoded_message.pop_string()
        return HelloMessage(player_name)
