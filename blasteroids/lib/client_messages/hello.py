from .message import Message
from .message_encoder import MessageEncoder


class HelloMessage(Message):
    TYPE = 'HELO'

    def __init__(self, player_name):
        super(HelloMessage, self).__init__(HelloMessage.TYPE)
        self.player_name = player_name

    def __repr__(self):
        return f'{super(HelloMessage, self).__repr__()}:{self.player_name}'


class HelloMessageEncoder(MessageEncoder):
    def __init__(self):
        super(HelloMessageEncoder, self).__init__(HelloMessage.TYPE)

    def encode(self, message):
        return super(HelloMessageEncoder, self)._encode_type() + self._encode_string(message.player_name)

    def decode(self, encoded_message):
        player_name = encoded_message.pop_string()
        return HelloMessage(player_name)
