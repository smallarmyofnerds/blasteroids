from pygame import Vector2
from blasteroids.server.game_objects import Obstacle, Projectile, Ship, PowerUp
from blasteroids.lib.server_world import ServerShip, ServerPowerUp, ServerProjectile, ServerObstacle


class World:
    def __init__(self):
        self.ships = []
        self.projectiles = []
        self.power_ups = []
        self.obstacles = []
        self.next_id = 0

    def _get_next_id(self):
        id = self.next_id
        self.next_id += 1
        return id

    def create_ship(self, name):
        ship = Ship(self._get_next_id(), Vector2(0, 0), Vector2(0, 1), name)
        self.ships.append(ship)
        return ship

    def create_projectile(self, name):
        self.projectiles.append(Projectile(self._get_next_id(), Vector2(0, 0), Vector2(0, 1), 1000))

    def remove_projectile(self, projectile):
        self.projectiles.remove(projectile)

    def create_obstacle(self, name):
        self.obstacles.append(Obstacle(self._get_next_id(), Vector2(0, 0), Vector2(0, 1), 10000))

    def remove_obstacle(self, obstacle):
        self.obstacles.remove(obstacle)

    def create_power_up(self, name):
        self.power_ups.append(PowerUp(self._get_next_id(), Vector2(0, 0), Vector2(0, 1)))

    def remove_ship(self, ship):
        self.ships.remove(ship)

    def _update_all(self):
        for o in [*self.ships, *self.projectiles, *self.power_ups, *self.obstacles]:
            o.update()

    def _test_ship_collisions(self):
        for ship in self.ships:
            for other in [*self.ships, *self.obstacles]:
                if ship == other:
                    continue
                if ship.collides_with(other):
                    ship.apply_damage_to(other)
                    other.apply_damage_to(ship)
                    if ship.health == 0:
                        ship.destroy(self)
                    if other.health == 0:
                        other.destroy(self)

    def _test_projectile_collisions(self):
        for projectile in self.projectiles:
            for other in [*self.ships, *self.obstacles]:
                if projectile.collides_with(other):
                    projectile.apply_damage_to(other)
                    projectile.destroy(self)
                    if other.health == 0:
                        other.destroy(self)

    def _test_power_up_collisions(self):
        for ship in self.ships:
            for power_up in self.power_ups:
                if ship.collides_with(power_up):
                    power_up.apply_power_up_to(ship)
                    power_up.destroy(self)

    def update(self):
        self._update_all()
        self._test_ship_collisions()
        self._test_projectile_collisions()
        self._test_power_up_collisions()

    def to_server_objects(self):
        objects = []
        for ship in self.ships:
            objects.append(ServerShip.from_ship(ship))
        for projectile in self.projectiles:
            objects.append(ServerProjectile.from_projectile(projectile))
        for power_up in self.power_ups:
            objects.append(ServerPowerUp.from_power_up(power_up))
        for obstacle in self.obstacles:
            objects.append(ServerObstacle.from_obstacle(obstacle))
        return objects
