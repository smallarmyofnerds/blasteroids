import random
from blasteroids.server.game_objects.obstacle import Obstacle


class Asteroid(Obstacle):
    def __init__(self, id, position, orientation, velocity, damage, health):
        super(Asteroid, self).__init__(id, 'asteroid', position, orientation, velocity, self._random_rotational_velocity(), 0, damage, health)

    def _random_rotational_velocity(self):
        return random.randint(-10, 10) * 2
