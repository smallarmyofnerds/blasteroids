from .server_object import ServerObject


class ServerOrientableObject(ServerObject):
    def __init__(self, type_id, object_id, position, orientation):
        super(ServerOrientableObject, self).__init__(type_id, object_id, position)
        self.orientation = orientation

    def encode(self, message_encoder):
        super(ServerOrientableObject, self).encode(message_encoder)
        message_encoder.push_vector(self.orientation)

    def decode_body(encoded_message):
        object_id, position = ServerObject.decode_body(encoded_message)
        orientation = encoded_message.pop_vector()
        return object_id, position, orientation
