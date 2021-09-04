class MessageEncoding:
    def __init__(self, encoders):
        self.encoders = encoders

    def decode(self, encoded_message):
        message_id = encoded_message.pop_byte()
        encoder = self.encoders.get(message_id)
        if encoder is None:
            raise Exception(f'Unhandled message type {message_id}')
        return encoder.decode_body(encoded_message)
