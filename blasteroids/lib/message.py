class Message:
    def __init__(self, type):
        self.type = type

    def encode(self):
        return self.encode_type()

    def encode_type(self):
        return bytes(self.type, 'utf-8')
    
    def encode_string(self, s):
        return len(s).to_bytes(2, byteorder='little') + bytes(s, 'utf-8')

    def __repr__(self):
        return self.type
