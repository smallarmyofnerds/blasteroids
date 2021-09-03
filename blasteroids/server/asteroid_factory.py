import random
from pygame import Vector2
from blasteroids.server.game_objects import Asteroid


class AsteroidFactory:
    def __init__(self, config):
        self.max_speed = config.asteroid.max_speed
        self.damage = {}
        self.health = {}
        self.collision_radius = {}
        for i in range(3):
            self.damage[i + 1] = int(pow(3, i) * config.asteroid.base_damage)
            self.health[i + 1] = int(pow(3, i) * config.asteroid.base_health)
            self.collision_radius[i + 1] = int((i + 1) * config.asteroid.base_radius)

    def create(self, level, id, position):
        return Asteroid(
            level,
            id,
            position,
            Vector2(0, 1).rotate(random.random() * 360.0),
            Vector2(0, 1).rotate(random.random() * 360.0) * random.random() * self.max_speed,
            self.collision_radius[level],
            self.damage[level],
            self.health[level],
        )
