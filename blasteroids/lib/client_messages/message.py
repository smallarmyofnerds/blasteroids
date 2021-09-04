class Message:
    def __init__(self, message_id):
        self.message_id = message_id

    def encode(self, message_encoder):
        message_encoder.push_byte(self.message_id)

    def __repr__(self):
        return self.message_id
