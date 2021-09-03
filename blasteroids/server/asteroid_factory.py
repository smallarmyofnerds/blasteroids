import random
from pygame import Vector2
from blasteroids.server.game_objects import Asteroid


class AsteroidFactory:
    def __init__(self, config, id_generator):
        self.id_generator = id_generator
        self.min_speed = config.asteroid.min_speed
        self.max_speed = config.asteroid.max_speed
        self.damage = {}
        self.health = {}
        self.collision_radius = {}
        for i in range(3):
            self.damage[i + 1] = int(pow(3, i) * config.asteroid.base_damage)
            self.health[i + 1] = int(pow(3, i) * config.asteroid.base_health)
            self.collision_radius[i + 1] = int((i + 1) * config.asteroid.base_radius)

    def create(self, level, position):
        return Asteroid(
            level,
            self.id_generator.get_next_id(),
            position,
            Vector2(0, 1).rotate(random.random() * 360.0),
            Vector2(0, 1).rotate(random.random() * 360.0) * min(self.min_speed, random.random() * self.max_speed),
            self.collision_radius[level],
            self.damage[level],
            self.health[level],
        )
