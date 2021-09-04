from blasteroids.lib.constants import ROCKET_PROJECTILE_ID, ROCKET_SHOT_SOUND_ID
from .weapon import Weapon
from ..rocket_projectile import RocketProjectile


class RocketWeapon(Weapon):
    def __init__(self, speed, collision_radius, damage, lifespan, projectile_id=ROCKET_PROJECTILE_ID):
        self.speed = speed
        self.collision_radius = collision_radius
        self.damage = damage
        self.lifespan = lifespan
        self.projectile_id = projectile_id

    def _generate_rocket(self, ship, world, position, orientation):
        world.create_projectile(RocketProjectile(None, position, orientation, orientation.normalize() * self.speed, self.collision_radius, self.damage, self.projectile_id, ship, self.lifespan))

    def shoot(self, ship, world):
        self._generate_rocket(ship, world, ship.position, ship.orientation)
        ship.reset_weapon()
        world.create_sound_effect(ROCKET_SHOT_SOUND_ID, ship.position)
