from blasteroids.lib.server_world.server_world import ServerWorld
from .message import Message
from .message_encoder import MessageEncoder


class WorldMessage(Message):
    TYPE = 'WRLD'

    def __init__(self, objects, ship_id, health, shield, active_weapon):
        super(WorldMessage, self).__init__(WorldMessage.TYPE)
        self.objects = objects
        self.ship_id = ship_id
        self.health = health
        self.shield = shield
        self.active_weapon = active_weapon

    def to_server_world(self):
        return ServerWorld(self.objects, self.ship_id, self.health, self.shield, self.active_weapon)

    def __repr__(self):
        return f'{super(WorldMessage, self).__repr__()}:...'


class WorldMessageEncoder(MessageEncoder):
    def __init__(self):
        super(WorldMessageEncoder, self).__init__(WorldMessage.TYPE)

    def encode(self, message):
        buffer = bytearray()
        buffer += super(WorldMessageEncoder, self)._encode_type()
        buffer += self._encode_short(len(message.objects))
        for object in message.objects:
            buffer += self._encode_server_object(object)
        buffer += self._encode_short(message.ship_id)
        buffer += self._encode_short(message.health)
        buffer += self._encode_short(message.shield)
        buffer += self._encode_string(message.active_weapon)
        return bytes(buffer) + b'****'

    def decode(self, encoded_message):
        count = encoded_message.pop_short()
        objects = []
        for i in range(count):
            objects.append(encoded_message.pop_object())
        ship_id = encoded_message.pop_short()
        health = encoded_message.pop_short()
        shield = encoded_message.pop_short()
        active_weapon = encoded_message.pop_string()
        return WorldMessage(objects, ship_id, health, shield, active_weapon)
