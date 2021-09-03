from .weapon import Weapon
from ..rocket_projectile import RocketProjectile


class RocketWeapon(Weapon):
    def __init__(self, speed, collision_radius, damage, lifespan, name = 'rocket_projectile'):
        self.speed = speed
        self.collision_radius = collision_radius
        self.damage = damage
        self.lifespan = lifespan
        self.name = name
    
    def _generate_rocket(self, ship, world, position, orientation):
        world.create_projectile(RocketProjectile(ship, None, position, orientation, self.speed, self.collision_radius, self.damage, self.lifespan, self.name))

    def shoot(self, ship, world):
        self._generate_rocket(ship, world, ship.position, ship.orientation)
        ship.reset_weapon()
        world.create_sound_effect('rocket_shot', ship.position)
