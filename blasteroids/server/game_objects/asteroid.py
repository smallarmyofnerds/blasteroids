import random
from pygame.math import Vector2
from blasteroids.server.game_objects.obstacle import Obstacle


class Asteroid(Obstacle):
    def __init__(self, level, id, position, orientation, velocity, damage, health):
        name = f'asteroid_{level}'
        super(Asteroid, self).__init__(
            id,
            name,
            position,
            self._random_orientation(),
            velocity,
            self._random_rotational_velocity(),
            0,
            damage,
            health,
        )
        self.level = level

    def _random_orientation(self):
        return Vector2(0, 1).rotate(random.random() * 360.0)

    def _random_rotational_velocity(self):
        return random.randint(-10, 10) * 2

    def destroy(self, world):
        world.remove_obstacle(self)
        if self.level > 1:
            for i in range(3):
                world.add_new_asteroid(self.level - 1, self.position)
