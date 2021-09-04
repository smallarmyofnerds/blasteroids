from blasteroids.lib.constants import SPREAD_FIRE_SHOT_SOUND_ID
from .laser_weapon import LaserWeapon


class SpreadFireWeapon(LaserWeapon):
    def __init__(self, speed, collision_radius, damage, lifespan, cooldown, spread):
        super(SpreadFireWeapon, self).__init__(speed, collision_radius, damage, lifespan, cooldown)
        self.spread = spread

    def shoot(self, ship, world):
        if self.cooldown.can_shoot():
            self._generate_laser(ship, world, ship.position, ship.orientation)
            self._generate_laser(ship, world, ship.position, ship.orientation.rotate(self.spread))
            self._generate_laser(ship, world, ship.position, ship.orientation.rotate(-1 * self.spread))
            world.create_sound_effect(SPREAD_FIRE_SHOT_SOUND_ID, ship.position)
            self.cooldown.update_last_shot()
