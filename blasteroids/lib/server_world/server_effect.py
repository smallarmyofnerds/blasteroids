from .server_object import ServerObject


class ServerEffect(ServerObject):
    def __init__(self, id, position, orientation, name):
        super(ServerEffect, self).__init__('EFFECT', id, position, orientation, name)

    def from_effect(effect):
        return ServerEffect(effect.id, effect.position, effect.orientation, effect.name)
