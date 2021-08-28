from .message import Message
from .message_encoder import MessageEncoder
from blasteroids.lib.player_inputs import PlayerInputs


class InputMessage(Message):
    TYPE = 'INPT'

    def __init__(self, left, right, up, fire):
        super(InputMessage, self).__init__(InputMessage.TYPE)
        self.left = left
        self.right = right
        self.up = up
        self.fire = fire

    def from_player_inputs(player_inputs):
        return InputMessage(player_inputs.left, player_inputs.right, player_inputs.up, player_inputs.fire)

    def to_player_inputs(self):
        inputs = PlayerInputs()
        inputs.left = self.left
        inputs.right = self.right
        inputs.up = self.up
        inputs.fire = self.fire
        return inputs

    def __repr__(self):
        return f'{super(InputMessage, self).__repr__()}:{self.left}:{self.right}:{self.up}:{self.fire}'


class InputMessageEncoder(MessageEncoder):
    def __init__(self):
        super(InputMessageEncoder, self).__init__(InputMessage.TYPE)

    def encode(self, message):
        return super(InputMessageEncoder, self)._encode_type() + self._encode_boolean(message.left) + self._encode_boolean(message.right) + self._encode_boolean(message.up) + self._encode_boolean(message.fire)

    def decode(self, encoded_message):
        left = encoded_message.pop_boolean()
        right = encoded_message.pop_boolean()
        up = encoded_message.pop_boolean()
        fire = encoded_message.pop_boolean()
        return InputMessage(left, right, up, fire)
