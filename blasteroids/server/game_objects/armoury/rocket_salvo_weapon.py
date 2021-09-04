from blasteroids.lib.constants import ROCKET_SALVO_PROJECTILE_ID, ROCKET_SALVO_SHOT_SOUND_ID
from .rocket_weapon import RocketWeapon


class RocketSalvoWeapon(RocketWeapon):
    def __init__(self, speed, collision_radius, damage, lifespan, spread):
        super(RocketSalvoWeapon, self).__init__(speed, collision_radius, damage, lifespan, ROCKET_SALVO_PROJECTILE_ID)
        self.spread = spread

    def shoot(self, ship, world):
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(-1 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(-2 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(-3 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(-4 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(-5 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(1 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(2 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(3 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(4 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(5 * self.spread))

        ship.reset_weapon()

        world.create_sound_effect(ROCKET_SALVO_SHOT_SOUND_ID, ship.position)
