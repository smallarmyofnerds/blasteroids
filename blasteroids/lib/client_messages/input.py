from blasteroids.lib.constants import INPUT_MESSAGE_ID
from .message import Message
from .message_encoder import MessageEncoder
from blasteroids.lib.player_inputs import PlayerInputs


class InputMessage(Message):
    def __init__(self, left, right, up, fire):
        super(InputMessage, self).__init__(INPUT_MESSAGE_ID)
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
        super(InputMessageEncoder, self).__init__(INPUT_MESSAGE_ID)

    def encode(self, message):
        buffer = bytearray()
        buffer += self._encode_byte(INPUT_MESSAGE_ID)
        buffer += self._encode_boolean(message.left)
        buffer += self._encode_boolean(message.right)
        buffer += self._encode_boolean(message.up)
        buffer += self._encode_boolean(message.fire)
        buffer += b'****'
        return bytes(buffer)

    def decode(self, encoded_message):
        left = encoded_message.pop_boolean()
        right = encoded_message.pop_boolean()
        up = encoded_message.pop_boolean()
        fire = encoded_message.pop_boolean()
        return InputMessage(left, right, up, fire)
