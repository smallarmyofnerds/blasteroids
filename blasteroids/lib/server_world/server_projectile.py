from .server_orientable_object import ServerOrientableObject
from ..constants import PROJECTILE_OBJECT_ID


class ServerProjectile(ServerOrientableObject):
    def __init__(self, object_id, position, orientation, projectile_id):
        super(ServerProjectile, self).__init__(PROJECTILE_OBJECT_ID, object_id, position, orientation)
        self.projectile_id = projectile_id

    def from_projectile(projectile):
        return ServerProjectile(projectile.id, projectile.position, projectile.orientation, projectile.projectile_id)

    def encode(self, message_encoder):
        super(ServerProjectile, self).encode(message_encoder)
        message_encoder.push_byte(self.projectile_id)

    def decode_body(encoded_message):
        object_id, position, orientation = ServerOrientableObject.decode_body(encoded_message)
        projectile_id = encoded_message.pop_byte()
        return ServerProjectile(object_id, position, orientation, projectile_id)
