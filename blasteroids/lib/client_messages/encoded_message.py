import struct
from pygame.math import Vector2


class EncodedMessage:
    def __init__(self, msg):
        self.msg = msg

    def push(self, b):
        self.msg = self.msg + b

    def pop(self, length):
        b = self.msg[:length]
        self.msg = self.msg[length:]
        return b

    def pop_raw_string(self, length):
        return str(self.pop(length), 'utf-8')

    def pop_boolean(self):
        value = int.from_bytes(self.pop(1), 'little')
        return True if value == 1 else False

    def pop_byte(self):
        return int.from_bytes(self.pop(1), 'little')

    def pop_short(self):
        return int.from_bytes(self.pop(2), 'little')

    def pop_long(self):
        return int.from_bytes(self.pop(4), 'little')

    def pop_string(self):
        length = self.pop_short()
        return self.pop_raw_string(length)

    def pop_vector(self):
        x, y = struct.unpack('ff', self.pop(8))
        return Vector2(x, y)
