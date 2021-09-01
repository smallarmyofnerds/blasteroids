import random
from pygame.math import Vector2
from blasteroids.server.game_objects.obstacle import Obstacle

random_drops = {
    3: [
        (20, 'heart'),
        (20, 'shield'),
        (10, 'mega_heart'),
        (10, 'mega_shield'),
    ],
    2: [
        (5, 'heart'),
        (5, 'shield'),
        (5, 'mega_heart'),
        (5, 'mega_shield'),
        (10, 'double_fire'),
        (10, 'spread_fire'),
        (10, 'rapid_fire'),
    ],
    1: [
        (2, 'heart'),
        (2, 'shield'),
        (2, 'mega_heart'),
        (2, 'mega_shield'),
        (2, 'double_fire'),
        (2, 'spread_fire'),
        (2, 'rapid_fire'),
        (5, 'rocket'),
        (5, 'rocket_salvo'),
        (5, 'proximity_mine'),
        (5, 'time_bomb'),
    ]
}

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

    def _generate_random_drop(self, world):
        roll = 100 * random.random()
        current_chance = 0
        for (chance, drop) in random_drops[self.level]:
            current_chance += chance
            if roll < current_chance:
                world.add_new_power_up(drop, self.position)
                break
                
    def on_removed(self, world):
        self._generate_random_drop(world)
        if self.level > 1:
            for i in range(3):
                world.add_new_asteroid(self.level - 1, self.position)
