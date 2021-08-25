from .message import Message
from .message_decoder import MessageDecoder


class InputMessage(Message):
    TYPE = 'INPT'

    def __init__(self, player_name):
        super(InputMessage, self).__init__(InputMessage.TYPE)
        self.player_name = player_name

    def encode(self):
        return super(InputMessage, self).encode() + self.encode_string(self.player_name)

    def dispatch(self, state):
        return state.handle_INPT(self)

    def __repr__(self):
        return f'{super(InputMessage, self).__repr__()}:{self.player_name}'


class InputMessageDecoder(MessageDecoder):
    def decode(self, encoded_message):
        player_name = encoded_message.pop_string()
        return InputMessage(player_name)
