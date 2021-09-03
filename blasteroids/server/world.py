from .game_objects.animation import Animation
from blasteroids.lib.server_world.server_animation import ServerAnimation
import random
from pygame import Vector2
from blasteroids.server.game_objects import Obstacle, Ship, Asteroid
from blasteroids.lib.server_world import ServerShip, ServerPickup, ServerProjectile, ServerObstacle, ServerSound, ServerAnimation
from blasteroids.server.game_objects.sound_effect import SoundEffect
from .asteroid_factory import AsteroidFactory
from .loot_factory import LootFactory

class IdGenerator:
    def __init__(self):
        self.next_id = 1
    
    def get_next_id(self):
        id = self.next_id
        self.next_id += 1
        return id


class World:
    def __init__(self, config):
        self.config = config
        self.width = config.world.width
        self.height = config.world.height
        self.ships = []
        self.projectiles = []
        self.power_ups = []
        self.obstacles = []
        self.sounds = []
        self.animations = []
        self.id_generator = IdGenerator()
        self.edge_acceleration_factor = config.world.edge_acceleration_factor

        self.asteroid_factory = AsteroidFactory(config, self.id_generator)
        self.loot_factory = LootFactory(config, self.id_generator)
        self._top_up_asteroids()

    def is_in_bounds(self, p, padding=0):
        return (p.x + padding) > 0 and (p.x - padding) < self.width and (p.y + padding) > 0 and (p.y - padding) < self.height

    def get_return_vector(self, p, v):
        if p.x < 0:
            if p.y < 0:
                return Vector2(1, 1).normalize() * self.edge_acceleration_factor
            elif p.y > self.height:
                return Vector2(1, -1).normalize() * self.edge_acceleration_factor
            else:
                return Vector2(1, 0).normalize() * self.edge_acceleration_factor
        elif p.x > self.width:
            if p.y < 0:
                return Vector2(-1, 1).normalize() * self.edge_acceleration_factor
            elif p.y > self.height:
                return Vector2(-1, -1).normalize() * self.edge_acceleration_factor
            else:
                return Vector2(-1, 0).normalize() * self.edge_acceleration_factor
        else:
            if p.y < 0:
                return Vector2(0, 1).normalize() * self.edge_acceleration_factor
            elif p.y > self.height:
                return Vector2(0, -1).normalize() * self.edge_acceleration_factor
            else:
                return Vector2(0, 0).normalize() * self.edge_acceleration_factor

    def _top_up_asteroids(self):
        asteroids_to_generate = max(0, self.config.world.min_obstacles - len(self.obstacles))
        for _ in range(asteroids_to_generate):
            self.add_new_asteroid(3, Vector2(random.randint(0, self.width), random.randint(0, self.height)))

    def add_new_asteroid(self, level, position):
        self.obstacles.append(self.asteroid_factory.create(level, position))

    def _get_safe_position(self):
        while True:
            position = Vector2(random.randint(0, self.width), random.randint(0, self.height))
            for o in [*self.ships, *self.obstacles, *self.projectiles, *self.power_ups]:
                if position.distance_squared_to(o.position) > 10000:
                    return position

    def create_ship(self, player):
        position = self._get_safe_position()
        ship = Ship(self.config, self.id_generator.get_next_id(), position, Vector2(0, 1), player)
        self.ships.append(ship)
        return ship
    
    def remove_ship(self, ship):
        self.ships.remove(ship)

    def create_projectile(self, projectile):
        projectile.id = self.id_generator.get_next_id()
        self.projectiles.append(projectile)

    def create_obstacle(self, name):
        self.obstacles.append(Obstacle(self.id_generator.get_next_id(), Vector2(0, 0), Vector2(0, 1), 10000))

    def create_sound_effect(self, name, position):
        self.sounds.append(SoundEffect(self.id_generator.get_next_id(), position, name))
    
    def create_animation(self, name, position, velocity, duration):
        self.animations.append(Animation(self.id_generator.get_next_id(), position, velocity, name, duration))

    def create_random_drop(self, level, position):
        random_drop = self.loot_factory.create(level, position)
        if random_drop:
            self.power_ups.append(random_drop)
    
    def ship_closest_to(self, position, ignore):
        closest = None
        for ship in self.ships:
            if ignore is not None and ship == ignore:
                continue
            if closest is None:
                closest = ship
            else:
                if position.distance_squared_to(ship.position) < position.distance_squared_to(closest.position):
                    closest = ship
        return closest

    def all_objects_in_range(self, position, range, ignore):
        targets = []
        range_squared = range * range
        for o in [*self.ships, *self.obstacles, *self.projectiles]:
            if o == ignore:
                continue
            if position.distance_squared_to(o.position) < range_squared:
                targets.append(o)
        return targets

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
        self._remove_destroyed_objects(self.sounds)
        self._remove_destroyed_objects(self.animations)

    def _update_all(self, delta_time):
        objects_to_update = [*self.ships, *self.projectiles, *self.power_ups, *self.obstacles, *self.sounds, *self.animations]
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
                    ship.apply_damage_to(other, self)
                    other.apply_damage_to(ship, self)

    def _test_projectile_collisions(self):
        for projectile in self.projectiles:
            for other in [*self.ships, *self.obstacles]:
                if projectile.collides_with(other):
                    projectile.apply_damage_to(other, self)
                    projectile.destroy()
            for other in [*self.projectiles]:
                if other == projectile:
                    continue
                if projectile.can_hit_projectile(other):
                    if projectile.collides_with(other):
                        projectile.apply_damage_to(other, self)
                        projectile.destroy()

    def _test_power_up_collisions(self):
        for ship in self.ships:
            for pickup in self.power_ups:
                if ship.collides_with(pickup):
                    pickup.apply_pickup_to(ship, self)
                    pickup.destroy()

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
        for pickup in self.power_ups:
            objects.append(ServerPickup.from_power_up(pickup))
        for obstacle in self.obstacles:
            objects.append(ServerObstacle.from_obstacle(obstacle))
        for sound in self.sounds:
            objects.append(ServerSound.from_sound(sound))
        for animation in self.animations:
            objects.append(ServerAnimation.from_animation(animation))
        return objects
