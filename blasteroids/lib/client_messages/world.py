from blasteroids.lib.server_world.server_sound import ServerSound
from blasteroids.lib.server_world.server_ship import ServerShip
from blasteroids.lib.server_world.server_projectile import ServerProjectile
from blasteroids.lib.server_world.server_pickup import ServerPickup
from blasteroids.lib.server_world.server_asteroid import ServerAsteroid
from blasteroids.lib.server_world.server_animation import ServerAnimation
from blasteroids.lib.constants import ANIMATION_OBJECT_ID, ASTEROID_OBJECT_ID, PICKUP_OBJECT_ID, PROJECTILE_OBJECT_ID, SHIP_OBJECT_ID, SOUND_OBJECT_ID, WORLD_MESSAGE_ID
from blasteroids.lib.server_world.server_world import ServerWorld
from .message import Message


class WorldMessage(Message):
    def __init__(self, objects, ship_object_id):
        super(WorldMessage, self).__init__(WORLD_MESSAGE_ID)
        self.objects = objects
        self.ship_object_id = ship_object_id

    def to_server_world(self):
        return ServerWorld(self.objects, self.ship_object_id)

    def __repr__(self):
        return f'{super(WorldMessage, self).__repr__()}:...'

    def encode(self, message_encoder):
        super(WorldMessage, self).encode(message_encoder)
        message_encoder.push_short(len(self.objects))
        for object in self.objects:
            object.encode(message_encoder)
        message_encoder.push_long(self.ship_object_id)

    def decode_body(encoded_message):
        count = encoded_message.pop_short()
        objects = []
        for i in range(count):
            type_id = encoded_message.pop_byte()
            if type_id == ANIMATION_OBJECT_ID:
                objects.append(ServerAnimation.decode_body(encoded_message))
            elif type_id == ASTEROID_OBJECT_ID:
                objects.append(ServerAsteroid.decode_body(encoded_message))
            elif type_id == PICKUP_OBJECT_ID:
                objects.append(ServerPickup.decode_body(encoded_message))
            elif type_id == PROJECTILE_OBJECT_ID:
                objects.append(ServerProjectile.decode_body(encoded_message))
            elif type_id == SHIP_OBJECT_ID:
                objects.append(ServerShip.decode_body(encoded_message))
            elif type_id == SOUND_OBJECT_ID:
                objects.append(ServerSound.decode_body(encoded_message))
            else:
                raise Exception('Unrecognized object type {type_id}')
        ship_object_id = encoded_message.pop_long()
        return WorldMessage(objects, ship_object_id)
