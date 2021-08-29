import random
import threading
from pygame import Vector2
import pygame
from blasteroids.server.game_objects import Obstacle, Ship, PowerUp, Asteroid
from blasteroids.lib.server_world import ServerShip, ServerPowerUp, ServerProjectile, ServerObstacle


class World:
    def __init__(self, config, sprite_library):
        self.config = config
        self.width = config.world_width
        self.height = config.world_height
        self.sprite_library = sprite_library
        self.ships = []
        self.projectiles = []
        self.power_ups = []
        self.obstacles = []
        self.next_id = 0

        self.lock = threading.Lock()

        self.last_obstacle_at = None
        self._generate_initial_obstacles()

    def _generate_initial_obstacles(self):
        for i in range(10):
            obstacle = Asteroid(
                self._get_next_id(),
                Vector2(
                    # random.randint(0, self.width),
                    # random.randint(0, self.height)
                    0, 0
                ),
                Vector2(0, 1).rotate(random.random() * 360.0),
                Vector2(0, 1).rotate(random.random() * 360.0) * random.random() * 50,
                10000,
                1000,
            )
            self.obstacles.append(obstacle)
        self.last_obstacle_at = pygame.time.get_ticks()

    def _get_next_id(self):
        id = self.next_id
        self.next_id += 1
        return id

    def create_ship(self, name):
        self.lock.acquire()
        ship = Ship(self.config, self.sprite_library, self._get_next_id(), Vector2(0, 0), Vector2(0, 1), name)
        self.ships.append(ship)
        self.lock.release()
        return ship

    def create_projectile(self, projectile):
        self.lock.acquire()
        projectile.id = self._get_next_id()
        self.projectiles.append(projectile)
        self.lock.release()

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

    def _update_all(self, delta_time):
        # self.lock.acquire()
        all_objects = [*self.ships, *self.projectiles, *self.power_ups, *self.obstacles]
        # self.lock.release()
        for o in all_objects:
            o.update(self, delta_time)

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

    def update(self, delta_time):
        self.lock.acquire()
        self._update_all(delta_time)
        self.lock.release()
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
