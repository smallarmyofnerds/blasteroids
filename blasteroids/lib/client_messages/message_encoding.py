class MessageEncoding:
    def __init__(self, encoders):
        self.encoders = encoders

    def decode(self, encoded_message):
        type = encoded_message.pop_raw_string(4)
        encoder = self.encoders.get(type)
        if encoder is None:
            raise Exception(f'Unhandled message type {type}')
        return encoder.decode(encoded_message)

    def encode(self, message):
        encoder = self.encoders.get(message.type)
        if encoder is None:
            raise Exception(f'Unhandled message type {type}')
        return encoder.encode(message)
