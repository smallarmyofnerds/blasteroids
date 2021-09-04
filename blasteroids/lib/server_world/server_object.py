class ServerObject:
    def __init__(self, type_id, object_id, position):
        self.type_id = type_id
        self.object_id = object_id
        self.position = position

    def __repr__(self):
        return f'{self.type_id} id={self.object_id} position={self.position}'

    def encode(self, message_encoder):
        message_encoder.push_byte(self.type_id)
        message_encoder.push_long(self.object_id)
        message_encoder.push_vector(self.position)

    def decode_body(encoded_message):
        object_id = encoded_message.pop_long()
        position = encoded_message.pop_vector()
        return object_id, position
