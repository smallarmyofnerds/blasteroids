class MessageEncoder:
    def __init__(self, type):
        self.type = type

    def _encode_type(self):
        return bytes(self.type, 'utf-8')

    def _encode_short(self, n):
        return n.to_bytes(2, byteorder='little')

    def _encode_string(self, s):
        return self._encode_short(len(s)) + bytes(s, 'utf-8')

    def _encode_string_array(self, a):
        encoded_array = ''.join(map(self._encode_string, a))
        return self._encode_short(len(a)) + encoded_array

    def encode(self, message):
        raise Exception('Unimplemented')

    def decode(self, encoded_message):
        raise Exception('Unimplemented')
