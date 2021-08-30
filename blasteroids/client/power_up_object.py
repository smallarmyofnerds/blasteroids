from .game_object import GameObject


class PowerUpObject(GameObject):
    def __init__(self, id, position, orientation):
        super(PowerUpObject, self).__init__(id, position, orientation)
