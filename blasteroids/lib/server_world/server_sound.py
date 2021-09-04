from blasteroids.lib.constants import SOUND_OBJECT_ID
from .server_object import ServerObject


class ServerSound(ServerObject):
    def __init__(self, object_id, position, sound_id):
        super(ServerSound, self).__init__(SOUND_OBJECT_ID, object_id, position)
        self.sound_id = sound_id

    def from_sound(sound):
        return ServerSound(sound.id, sound.position, sound.sound_id)

    def encode(self, message_encoder):
        super(ServerSound, self).encode(message_encoder)
        message_encoder.push_byte(self.sound_id)

    def decode_body(encoded_message):
        object_id, position = ServerObject.decode_body(encoded_message)
        sound_id = encoded_message.pop_byte()
        return ServerSound(object_id, position, sound_id)
