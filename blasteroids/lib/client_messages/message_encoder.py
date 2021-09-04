import struct


class MessageEncoder:
    def __init__(self):
        self.buffer = bytearray()

    def push_byte(self, n):
        self.buffer += n.to_bytes(1, byteorder='little')

    def push_short(self, n):
        self.buffer += n.to_bytes(2, byteorder='little')

    def push_long(self, n):
        self.buffer += n.to_bytes(4, byteorder='little')

    def push_boolean(self, b):
        n = 1 if b else 0
        self.buffer += n.to_bytes(1, byteorder='little')

    def push_string(self, s):
        self.push_short(len(s))
        self.buffer += bytes(s, 'utf-8')

    def push_vector(self, v):
        self.buffer += struct.pack('ff', float(v.x), float(v.y))

    def get_bytes(self):
        return bytes(self.buffer)
