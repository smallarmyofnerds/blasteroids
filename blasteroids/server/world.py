from blasteroids.server.game_objects.time_bomb_pickup import TimeBombPickup
from blasteroids.server.game_objects.proximity_mine_pickup import ProximityMinePickup
from blasteroids.server.game_objects.mega_shield_pickup import MegaShieldPickup
from blasteroids.server.game_objects.rocket_pickup import RocketPickup
from blasteroids.server.game_objects.rocket_salvo_pickup import RocketSalvoPickup
from blasteroids.server.game_objects.spread_fire_pickup import SpreadFirePickup
from blasteroids.server.game_objects.double_fire_pickup import DoubleFirePickup
from blasteroids.server.game_objects.mega_heart_pickup import MegaHeartPickup
import random
from pygame import Vector2
from blasteroids.server.game_objects import Obstacle, Ship, PowerUp, Asteroid
from blasteroids.lib.server_world import ServerShip, ServerPowerUp, ServerProjectile, ServerObstacle, ServerEffect
from blasteroids.server.game_objects.heart_pickup import HeartPickup
from blasteroids.server.game_objects.shield_pickup import ShieldPickup
from blasteroids.server.game_objects.rapid_fire_pickup import RapidFirePickup
from blasteroids.server.game_objects.sound_effect import SoundEffect


class AsteroidFactory:
    def __init__(self, config):
        self.max_speed = config.asteroid.max_speed
        self.damage = {}
        self.health = {}
        self.collision_radius = {}
        for i in range(3):
            self.damage[i + 1] = int(pow(3, i) * config.asteroid.base_damage)
            self.health[i + 1] = int(pow(3, i) * config.asteroid.base_health)
            self.collision_radius[i + 1] = int((i + 1) * config.asteroid.base_radius)

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
        self.width = config.world.width
        self.height = config.world.height
        self.ships = []
        self.projectiles = []
        self.power_ups = []
        self.obstacles = []
        self.effects = []
        self.next_id = 1
        self.edge_acceleration_factor = config.world.edge_acceleration_factor

        self.asteroid_factory = AsteroidFactory(config)

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
        self.obstacles.append(self.asteroid_factory.create(level, self._get_next_id(), position))

    def _get_next_id(self):
        id = self.next_id
        self.next_id += 1
        return id

    def _get_safe_position(self):
        while True:
            position = Vector2(random.randint(0, self.width), random.randint(0, self.height))
            for o in [*self.ships, *self.obstacles, *self.projectiles, *self.power_ups]:
                if position.distance_squared_to(o.position) > 10000:
                    return position

    def create_ship(self, player):
        position = self._get_safe_position()
        ship = Ship(self.config, self._get_next_id(), position, Vector2(0, 1), player)
        self.ships.append(ship)
        return ship
    
    def remove_ship(self, ship):
        self.ships.remove(ship)

    def create_projectile(self, projectile):
        projectile.id = self._get_next_id()
        self.projectiles.append(projectile)

    def remove_projectile(self, projectile):
        self.projectiles.remove(projectile)

    def create_obstacle(self, name):
        self.obstacles.append(Obstacle(self._get_next_id(), Vector2(0, 0), Vector2(0, 1), 10000))

    def remove_obstacle(self, obstacle):
        self.obstacles.remove(obstacle)
    
    def create_sound_effect(self, name, position):
        self.effects.append(SoundEffect(self._get_next_id(), position, name))

    def add_new_power_up(self, name, position):
        if name == 'heart':
            self.power_ups.append(HeartPickup(self._get_next_id(), position, self.config.heart.health_amount, self.config.heart.pickup_lifespan))
        elif name == 'mega_heart':
            self.power_ups.append(MegaHeartPickup(self._get_next_id(), position, self.config.mega_heart.pickup_lifespan))
        elif name == 'shield':
            self.power_ups.append(ShieldPickup(self._get_next_id(), position, self.config.shield.shield_amount, self.config.shield.pickup_lifespan))
        elif name == 'mega_shield':
            self.power_ups.append(MegaShieldPickup(self._get_next_id(), position, self.config.mega_shield.pickup_lifespan))
        elif name == 'double_fire':
            self.power_ups.append(DoubleFirePickup(self._get_next_id(), position, self.config.double_fire.pickup_lifespan))
        elif name == 'spread_fire':
            self.power_ups.append(SpreadFirePickup(self._get_next_id(), position, self.config.spread_fire.pickup_lifespan))
        elif name == 'rapid_fire':
            self.power_ups.append(RapidFirePickup(self._get_next_id(), position, self.config.rapid_fire.pickup_lifespan))
        elif name == 'rocket':
            self.power_ups.append(RocketPickup(self._get_next_id(), position, self.config.rocket.pickup_lifespan))
        elif name == 'rocket_salvo':
            self.power_ups.append(RocketSalvoPickup(self._get_next_id(), position, self.config.rocket_salvo.pickup_lifespan))
        elif name == 'proximity_mine':
            self.power_ups.append(ProximityMinePickup(self._get_next_id(), position, self.config.proximity_mine.pickup_lifespan))
        elif name == 'time_bomb':
            self.power_ups.append(TimeBombPickup(self._get_next_id(), position, self.config.time_bomb.pickup_lifespan))

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

    def all_objects_in_range(self, position, range):
        targets = []
        range_squared = range * range
        for o in [*self.ships, *self.obstacles, *self.projectiles]:
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
        self._remove_destroyed_objects(self.effects)

    def _update_all(self, delta_time):
        objects_to_update = [*self.ships, *self.projectiles, *self.power_ups, *self.obstacles, *self.effects]
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

    def _test_power_up_collisions(self):
        for ship in self.ships:
            for power_up in self.power_ups:
                if ship.collides_with(power_up):
                    power_up.apply_power_up_to(ship, self)
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
        for effect in self.effects:
            objects.append(ServerEffect.from_effect(effect))
        return objects
