import struct


class MessageEncoder:
    def __init__(self, type):
        self.type = type

    def _encode_type(self):
        return bytes(self.type, 'utf-8')

    def _encode_short(self, n):
        return n.to_bytes(2, byteorder='little')

    def _encode_boolean(self, b):
        n = 1 if b else 0
        return n.to_bytes(1, byteorder='little')

    def _encode_string(self, s):
        return self._encode_short(len(s)) + bytes(s, 'utf-8')

    def _encode_string_array(self, a):
        encoded_array = ''.join(map(self._encode_string, a))
        return self._encode_short(len(a)) + encoded_array

    def _encode_vector(self, v):
        return struct.pack('ff', float(v.x), float(v.y))

    def _encode_server_object(self, server_object):
        buffer = bytearray()
        buffer += self._encode_string(server_object.type)
        buffer += self._encode_short(server_object.id)
        buffer += self._encode_vector(server_object.position)
        buffer += self._encode_vector(server_object.orientation)
        buffer += self._encode_string(server_object.name)
        return bytes(buffer)

    def encode(self, message):
        raise Exception('Unimplemented')

    def decode(self, encoded_message):
        raise Exception('Unimplemented')
