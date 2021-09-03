from .server_object import ServerObject


class ServerAnimation(ServerObject):
    def __init__(self, id, position, orientation, name):
        super(ServerAnimation, self).__init__('ANIM', id, position, orientation, name)

    def from_animation(animation):
        return ServerAnimation(animation.id, animation.position, animation.orientation, animation.name)
