from .game_object import GameObject


class ProjectileObject(GameObject):
    def __init__(self, id, position, orientation):
        super(ProjectileObject, self).__init__(id, position, orientation)

    def destroy(self):
        pass