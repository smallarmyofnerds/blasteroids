from .rocket_weapon import RocketWeapon


class RocketSalvoWeapon(RocketWeapon):
    def __init__(self, speed, collision_radius, damage, lifespan, spread):
        super(RocketSalvoWeapon, self).__init__(speed, collision_radius, damage, lifespan, 'rocket_salvo_projectile')
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

        world.create_sound_effect('rocket_salvo_shot', ship.position)
