from .server_orientable_object import ServerOrientableObject
from ..constants import ASTEROID_OBJECT_ID


class ServerAsteroid(ServerOrientableObject):
    def __init__(self, object_id, position, orientation, level):
        super(ServerAsteroid, self).__init__(ASTEROID_OBJECT_ID, object_id, position, orientation)
        self.level = level

    def from_asteroid(asteroid):
        return ServerAsteroid(asteroid.id, asteroid.position, asteroid.orientation, asteroid.level)

    def encode(self, message_encoder):
        super(ServerAsteroid, self).encode(message_encoder)
        message_encoder.push_byte(self.level)

    def decode_body(encoded_message):
        object_id, position, orientation = ServerOrientableObject.decode_body(encoded_message)
        level = encoded_message.pop_byte()
        return ServerAsteroid(object_id, position, orientation, level)
