from blasteroids.lib.constants import INPUT_MESSAGE_ID
from .message import Message
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

    def encode(self, message_encoder):
        super(InputMessage, self).encode(message_encoder)
        flags = 0
        flags |= (1 << 3) if self.left else 0
        flags |= (1 << 2) if self.right else 0
        flags |= (1 << 1) if self.up else 0
        flags |= 1 if self.fire else 0
        message_encoder.push_byte(flags)

    def decode_body(encoded_message):
        flags = encoded_message.pop_byte()
        left = flags & (1 << 3)
        right = flags & (1 << 2)
        up = flags & (1 << 1)
        fire = flags & 1
        return InputMessage(left, right, up, fire)
