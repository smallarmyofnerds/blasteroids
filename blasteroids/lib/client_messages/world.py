from blasteroids.lib.server_world.server_world import ServerWorld
from .message import Message
from .message_encoder import MessageEncoder


class WorldMessage(Message):
    TYPE = 'WRLD'

    def __init__(self, objects, player_id):
        super(WorldMessage, self).__init__(WorldMessage.TYPE)
        self.objects = objects
        self.player_id = player_id

    def to_server_world(self):
        return ServerWorld(self.objects, self.player_id)

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
        buffer += self._encode_short(message.player_id)
        return bytes(buffer) + b'****'

    def decode(self, encoded_message):
        count = encoded_message.pop_short()
        objects = []
        for i in range(count):
            objects.append(encoded_message.pop_object())
        player_id = encoded_message.pop_short()
        return WorldMessage(objects, player_id)
