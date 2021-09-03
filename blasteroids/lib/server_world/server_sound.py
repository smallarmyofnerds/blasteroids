from .server_object import ServerObject


class ServerSound(ServerObject):
    def __init__(self, id, position, orientation, name):
        super(ServerSound, self).__init__('SOUND', id, position, orientation, name)

    def from_sound(sound):
        return ServerSound(sound.id, sound.position, sound.orientation, sound.name)
