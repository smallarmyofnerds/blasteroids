import random
from pygame import Vector2
import pygame
from blasteroids.server.game_objects import Obstacle, Ship, PowerUp, Asteroid
from blasteroids.lib.server_world import ServerShip, ServerPowerUp, ServerProjectile, ServerObstacle


class AsteroidFactory:
    def __init__(self, config):
        self.max_speed = config.asteroid_max_speed
        self.damage = {}
        self.health = {}
        self.collision_radius = {}
        for i in range(3):
            self.damage[i + 1] = int(pow(3, i) * config.asteroid_base_damage)
            self.health[i + 1] = int(pow(3, i) * config.asteroid_base_health)
            self.collision_radius[i + 1] = int((i + 1) * config.asteroid_base_collision_radius)

    def create(self, level, id, position):
        return Asteroid(
            level,
            id,
            position,
            Vector2(0, 1).rotate(random.random() * 360.0),
            Vector2(0, 1).rotate(random.random() * 360.0) * random.random() * self.max_speed,
            self.collision_radius[level],
            self.damage[level],
            self.health[level],
        )


class World:
    def __init__(self, config):
        self.config = config
        self.width = config.world_width
        self.height = config.world_height
        self.ships = []
        self.projectiles = []
        self.power_ups = []
        self.obstacles = []
        self.next_id = 1

        self.asteroid_factory = AsteroidFactory(config)

        self._top_up_asteroids()

    def is_in_bounds(self, p, padding = 0):
        return (p.x + padding) > 0 and (p.x - padding) < self.width and (p.y + padding) > 0 and (p.y - padding) < self.height
    
    def get_return_vector(self, p, v):
        if p.x < 0:
            if p.y < 0:
                return Vector2(1, 1).normalize() * v.length()
            elif p.y > self.height:
                return Vector2(1, -1).normalize() * v.length()
            else:
                return Vector2(1, 0).normalize() * v.length()
        elif p.x > self.width:
            if p.y < 0:
                return Vector2(-1, 1).normalize() * v.length()
            elif p.y > self.height:
                return Vector2(-1, -1).normalize() * v.length()
            else:
                return Vector2(-1, 0).normalize() * v.length()
        else:
            if p.y < 0:
                return Vector2(0, 1).normalize() * v.length()
            elif p.y > self.height:
                return Vector2(0, -1).normalize() * v.length()
            else:
                return Vector2(0, 0).normalize() * v.length()

    def _top_up_asteroids(self):
        asteroids_to_generate = max(0, self.config.min_asteroids - len(self.obstacles))
        for _ in range(asteroids_to_generate):
            self.add_new_asteroid(3, Vector2(random.randint(0, self.width), random.randint(0, self.height)))

    def add_new_asteroid(self, level, position):
        self.obstacles.append(self.asteroid_factory.create(level, self._get_next_id(), position))

    def _get_next_id(self):
        id = self.next_id
        self.next_id += 1
        return id

    def create_ship(self, name):
        ship = Ship(self.config, self._get_next_id(), Vector2(random.randint(0, self.width), random.randint(0, self.height)), Vector2(0, 1), name)
        self.ships.append(ship)
        return ship

    def create_projectile(self, projectile):
        projectile.id = self._get_next_id()
        self.projectiles.append(projectile)

    def remove_projectile(self, projectile):
        self.projectiles.remove(projectile)

    def create_obstacle(self, name):
        self.obstacles.append(Obstacle(self._get_next_id(), Vector2(0, 0), Vector2(0, 1), 10000))

    def remove_obstacle(self, obstacle):
        self.obstacles.remove(obstacle)

    def create_power_up(self, name):
        self.power_ups.append(PowerUp(self._get_next_id(), Vector2(0, 0), Vector2(0, 1)))

    def _remove_destroyed_objects(self, object_list):
        objects_to_remove = []
        for o in object_list:
            if o.destroyed:
                objects_to_remove.append(o)
        for o in objects_to_remove:
            object_list.remove(o)
            o.on_removed(self)

    def _remove_destroyed(self):
        self._remove_destroyed_objects(self.ships)
        self._remove_destroyed_objects(self.obstacles)
        self._remove_destroyed_objects(self.power_ups)
        self._remove_destroyed_objects(self.projectiles)

    def _update_all(self, delta_time):
        objects_to_update = [*self.ships, *self.projectiles, *self.power_ups, *self.obstacles]
        for o in objects_to_update:
            o.update(self, delta_time)
            if not o.is_in_bounds(self):
                o.destroy()

    def _test_ship_collisions(self):
        for ship in self.ships:
            for other in [*self.ships, *self.obstacles]:
                if ship == other:
                    continue
                if ship.collides_with(other):
                    ship.apply_damage_to(other)
                    other.apply_damage_to(ship)

    def _test_projectile_collisions(self):
        for projectile in self.projectiles:
            for other in [*self.ships, *self.obstacles]:
                if projectile.collides_with(other):
                    projectile.apply_damage_to(other)
                    projectile.destroy()

    def _test_power_up_collisions(self):
        for ship in self.ships:
            for power_up in self.power_ups:
                if ship.collides_with(power_up):
                    power_up.apply_power_up_to(ship)
                    power_up.destroy()

    def update(self, delta_time):
        self._remove_destroyed()
        self._update_all(delta_time)
        self._test_ship_collisions()
        self._test_projectile_collisions()
        self._test_power_up_collisions()
        self._top_up_asteroids()

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
