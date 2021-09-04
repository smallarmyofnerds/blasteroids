from blasteroids.lib.constants import EXPLOSION_ANIMATION_ID, IMPACT_SOUND_ID
import random
from .physical_object import PhysicalGameObject


class Asteroid(PhysicalGameObject):
    def __init__(self, id, position, orientation, velocity, collision_radius, damage, health, level):
        super(Asteroid, self).__init__(
            id,
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
        return random.randint(-10, 10) * 5

    def on_removed(self, world):
        world.create_sound_effect(IMPACT_SOUND_ID, self.position)
        world.create_animation(EXPLOSION_ANIMATION_ID, self.position, self.velocity, 800)
        world.create_random_drop(self.level, self.position)
        if self.level > 1:
            for i in range(3):
                world.add_new_asteroid(self.level - 1, self.position)
