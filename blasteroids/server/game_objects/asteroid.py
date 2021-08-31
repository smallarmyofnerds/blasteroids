import random
from pygame.math import Vector2
from blasteroids.server.game_objects.obstacle import Obstacle


class Asteroid(Obstacle):
    def __init__(self, level, id, position, orientation, velocity, collision_radius, damage, health):
        name = f'asteroid_{level}'
        super(Asteroid, self).__init__(
            id,
            name,
            position,
            orientation,
            velocity,
            collision_radius,
            damage,
            health,
            rotational_velocity=self._random_rotational_velocity(),
        )
        self.level = level

    def _random_rotational_velocity(self):
        return random.randint(-10, 10) * 2

    def on_removed(self, world):
        if self.level > 1:
            for i in range(3):
                world.add_new_asteroid(self.level - 1, self.position)
