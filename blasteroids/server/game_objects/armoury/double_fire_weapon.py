from blasteroids.lib.constants import DOUBLE_FIRE_SHOT_SOUND_ID
from .laser_weapon import LaserWeapon


class DoubleFireWeapon(LaserWeapon):
    def __init__(self, speed, collision_radius, damage, lifespan, cooldown, offset):
        super(DoubleFireWeapon, self).__init__(speed, collision_radius, damage, lifespan, cooldown)
        self.offset = offset

    def shoot(self, ship, world):
        if self.cooldown.can_shoot():
            self._generate_laser(ship, world, ship.position + self.offset * ship.orientation.rotate(90).normalize(), ship.orientation)
            self._generate_laser(ship, world, ship.position + self.offset * ship.orientation.rotate(-90).normalize(), ship.orientation)
            world.create_sound_effect(DOUBLE_FIRE_SHOT_SOUND_ID, ship.position)
            self.cooldown.update_last_shot()
