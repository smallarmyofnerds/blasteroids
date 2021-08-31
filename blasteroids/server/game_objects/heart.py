from pygame import Vector2
from blasteroids.server.game_objects.power_up import PowerUp


class Heart(PowerUp):
    def __init__(self, id, position, **kwargs):
        super(Heart, self).__init__(id, "heart", position)
