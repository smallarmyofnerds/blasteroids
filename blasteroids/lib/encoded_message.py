class EncodedMessage:
    def __init__(self, msg):
        self.msg = msg

    def pop(self, length):
        b = self.msg[:length]
        self.msg = self.msg[length:]
        return b

    def pop_raw_string(self, length):
        return str(self.pop(length), 'utf-8')

    def pop_short(self):
        return int.from_bytes(self.pop(2), 'little')

    def pop_string(self):
        length = self.pop_short()
        return self.pop_raw_string(length)
