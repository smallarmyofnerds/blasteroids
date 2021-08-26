from .message import Message
from .message_encoder import MessageEncoder


class InputMessage(Message):
    TYPE = 'INPT'

    def __init__(self, player_name):
        super(InputMessage, self).__init__(InputMessage.TYPE)
        self.player_name = player_name

    def dispatch(self, handler):
        return handler.handle_INPT(self)

    def __repr__(self):
        return f'{super(InputMessage, self).__repr__()}:{self.player_name}'


class InputMessageEncoder(MessageEncoder):
    def __init__(self):
        super(InputMessageEncoder, self).__init__(InputMessage.TYPE)

    def encode(self, message):
        return super(InputMessageEncoder, self)._encode_type() + self._encode_string(message.player_name)

    def decode(self, encoded_message):
        player_name = encoded_message.pop_string()
        return InputMessage(player_name)
