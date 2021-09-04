from blasteroids.lib.constants import PICKUP_OBJECT_ID
from .server_object import ServerObject


class ServerPickup(ServerObject):
    def __init__(self, object_id, position, pickup_id):
        super(ServerPickup, self).__init__(PICKUP_OBJECT_ID, object_id, position)
        self.pickup_id = pickup_id

    def from_pickup(pickup):
        return ServerPickup(pickup.id, pickup.position, pickup.pickup_id)

    def encode(self, message_encoder):
        super(ServerPickup, self).encode(message_encoder)
        message_encoder.push_byte(self.pickup_id)

    def decode_body(encoded_message):
        object_id, position = ServerObject.decode_body(encoded_message)
        pickup_id = encoded_message.pop_byte()
        return ServerPickup(object_id, position, pickup_id)
