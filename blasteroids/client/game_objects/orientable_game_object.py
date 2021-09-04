from .game_object import GameObject


class OrientableGameObject(GameObject):
    def __init__(self, server_object):
        super(OrientableGameObject, self).__init__(server_object)
        self.orientation = server_object.orientation

    def update(self, server_object):
        super(OrientableGameObject, self).update(server_object)
        self.orientation = server_object.orientation

    def draw(self, screen, my_position):
        pass
