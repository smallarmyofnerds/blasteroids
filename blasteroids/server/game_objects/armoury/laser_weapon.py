from blasteroids.lib.constants import LASER_SOUND_ID
from .weapon import Weapon
from .cooldown import Cooldown
from ..laser import Laser


class LaserWeapon(Weapon):
    def __init__(self, speed, collision_radius, damage, lifespan, cooldown):
        self.cooldown = Cooldown(cooldown)
        self.speed = speed
        self.collision_radius = collision_radius
        self.damage = damage
        self.lifespan = lifespan

    def _generate_laser(self, ship, world, position, orientation):
        world.create_projectile(Laser(None, position, orientation, self.speed, self.collision_radius, self.damage, ship, self.lifespan))

    def shoot(self, ship, world):
        if self.cooldown.can_shoot():
            self._generate_laser(ship, world, ship.position, ship.orientation)
            world.create_sound_effect(LASER_SOUND_ID, ship.position)
            self.cooldown.update_last_shot()
