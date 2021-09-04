from blasteroids.lib.constants import WORLD_MESSAGE_ID
from blasteroids.lib.server_world.server_world import ServerWorld
from .message import Message
from .message_encoder import MessageEncoder


class WorldMessage(Message):
    def __init__(self, objects, ship_id, health, shield, active_weapon_id, is_engine_on):
        super(WorldMessage, self).__init__(WORLD_MESSAGE_ID)
        self.objects = objects
        self.ship_id = ship_id
        self.health = health
        self.shield = shield
        self.active_weapon_id = active_weapon_id
        self.is_engine_on = is_engine_on

    def to_server_world(self):
        return ServerWorld(self.objects, self.ship_id, self.health, self.shield, self.active_weapon_id, self.is_engine_on)

    def __repr__(self):
        return f'{super(WorldMessage, self).__repr__()}:...'


class WorldMessageEncoder(MessageEncoder):
    def __init__(self):
        super(WorldMessageEncoder, self).__init__(WORLD_MESSAGE_ID)

    def encode(self, message):
        buffer = bytearray()
        buffer += self._encode_byte(WORLD_MESSAGE_ID)
        buffer += self._encode_short(len(message.objects))
        for object in message.objects:
            buffer += self._encode_server_object(object)
        buffer += self._encode_long(message.ship_id)
        buffer += self._encode_short(message.health)
        buffer += self._encode_short(message.shield)
        buffer += self._encode_byte(message.active_weapon_id)
        buffer += self._encode_boolean(message.is_engine_on)
        return bytes(buffer) + b'****'

    def decode(self, encoded_message):
        count = encoded_message.pop_short()
        objects = []
        for i in range(count):
            objects.append(encoded_message.pop_object())
        ship_id = encoded_message.pop_long()
        health = encoded_message.pop_short()
        shield = encoded_message.pop_short()
        active_weapon_id = encoded_message.pop_byte()
        is_engine_on = encoded_message.pop_boolean()
        return WorldMessage(objects, ship_id, health, shield, active_weapon_id, is_engine_on)
