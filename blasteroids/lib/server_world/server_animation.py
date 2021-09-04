from .server_orientable_object import ServerOrientableObject
from ..constants import ANIMATION_OBJECT_ID


class ServerAnimation(ServerOrientableObject):
    def __init__(self, object_id, position, orientation, animation_id):
        super(ServerAnimation, self).__init__(ANIMATION_OBJECT_ID, object_id, position, orientation)
        self.animation_id = animation_id

    def from_animation(animation):
        return ServerAnimation(animation.id, animation.position, animation.orientation, animation.animation_id)

    def encode(self, message_encoder):
        super(ServerAnimation, self).encode(message_encoder)
        message_encoder.push_byte(self.animation_id)

    def decode_body(encoded_message):
        object_id, position, orientation = ServerOrientableObject.decode_body(encoded_message)
        animation_id = encoded_message.pop_byte()
        return ServerAnimation(object_id, position, orientation, animation_id)
