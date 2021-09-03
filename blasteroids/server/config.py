import configparser
import socket

DEFAULT_SERVER_ADDRESS = ''
DEFAULT_SERVER_PORT = 19999

DEFAULT_SHIP_ACCELERATION_RATE = 1
DEFAULT_SHIP_ROTATIONAL_ACCELERATION_RATE = 2
DEFAULT_SHIP_ROTATIONAL_VELOCITY_FRICTION = 0.1
DEFAULT_SHIP_LINEAR_FRICTION = 0.1
DEFAULT_SHIP_RADIUS = 20
DEFAULT_SHIP_DAMAGE = 100
DEFAULT_SHIP_HEALTH = 100
DEFAULT_SHIP_MAX_SHIELDS = 1000

DEFAULT_LASER_SPEED = 1000
DEFAULT_LASER_RADIUS = 5
DEFAULT_LASER_DAMAGE = 200
DEFAULT_LASER_LIFESPAN = 1000
DEFAULT_LASER_COOLDOWN = 200

DEFAULT_RAPID_FIRE_SPEED = 1500
DEFAULT_RAPID_FIRE_RADIUS = 2
DEFAULT_RAPID_FIRE_DAMAGE = 80
DEFAULT_RAPID_FIRE_LIFESPAN = 1000
DEFAULT_RAPID_FIRE_COOLDOWN = 80

DEFAULT_MIN_ASTEROIDS = 40
DEFAULT_ASTEROID_MAX_SPEED = 50
DEFAULT_ASTEROID_BASE_DAMAGE = 800
DEFAULT_ASTEROID_BASE_HEALTH = 200
DEFAULT_ASTEROID_BASE_COLLISION_RADIUS = 12

DEFAULT_HEART_HEALTH = 400
DEFAULT_SHIELD_AMOUNT = 400

DEFAULT_DOUBLE_FIRE_LIFESPAN = 6000
DEFAULT_HEART_LIFESPAN = 6000
DEFAULT_MEGA_HEART_LIFESPAN = 3000
DEFAULT_MEGA_SHIELD_LIFESPAN = 3000
DEFAULT_PROXIMITY_MINE_LIFESPAN = 3000
DEFAULT_RAPID_FIRE_LIFESPAN = 6000
DEFAULT_ROCKET_SALVO_LIFESPAN = 3000
DEFAULT_ROCKET_LIFESPAN = 3000
DEFAULT_SHIELD_LIFESPAN = 6000
DEFAULT_SPREAD_FIRE_LIFESPAN = 6000
DEFAULT_TIME_BOMB_LIFESPAN = 3000

DEFAULT_WORLD_WIDTH = 10000
DEFAULT_WORLD_HEIGHT = 10000
DEFAULT_WORLD_EDGE_ACCELERATION_FACTOR = 2


class ServerConfig:
    def __init__(self, config):
        self.address = config['Address']
        self.port = int(config['Port'])

class MiscConfig:
    def __init__(self, config):
        self.logging_level = config['LoggingLevel']

class WorldConfig:
    def __init__(self, config):
        self.width = int(config['Width'])
        self.height = int(config['Height'])
        self.edge_acceleration_factor = float(config['EdgeAccelerationFactor'])
        self.min_obstacles = int(config['MinObstacles'])

class ShipConfig:
    def __init__(self, config):
        self.linear_acceleration = int(config['LinearAcceleration'])
        self.linear_friction = float(config['LinearFriction'])
        self.angular_acceleration = int(config['AngularAcceleration'])
        self.angular_friction = float(config['AngularFriction'])
        self.radius = int(config['Radius'])
        self.damage = int(config['Damage'])
        self.max_health = int(config['MaxHealth'])
        self.max_shields = int(config['MaxShields'])

class LaserConfig:
    def __init__(self, config):
        self.projectile_speed = int(config['ProjectileSpeed'])
        self.projectile_radius = float(config['ProjectileRadius'])
        self.projectile_damage = int(config['ProjectileDamage'])
        self.projectile_lifespan = int(config['ProjectileLifespan'])
        self.cooldown = int(config['Cooldown'])

class RapidFireConfig:
    def __init__(self, config):
        self.pickup_lifespan = int(config['PickupLifespan'])
        self.projectile_speed = int(config['ProjectileSpeed'])
        self.projectile_radius = int(config['ProjectileRadius'])
        self.projectile_damage = int(config['ProjectileDamage'])
        self.projectile_lifespan = int(config['ProjectileLifespan'])
        self.cooldown = int(config['Cooldown'])

class DoubleFireConfig:
    def __init__(self, config):
        self.pickup_lifespan = int(config['PickupLifespan'])
        self.offset = int(config['Offset'])

class SpreadFireConfig:
    def __init__(self, config):
        self.pickup_lifespan = int(config['PickupLifespan'])
        self.spread = int(config['Spread'])

class HeartConfig:
    def __init__(self, config):
        self.pickup_lifespan = int(config['PickupLifespan'])
        self.health_amount = int(config['HealthAmount'])

class MegaHeartConfig:
    def __init__(self, config):
        self.pickup_lifespan = int(config['PickupLifespan'])

class ShieldConfig:
    def __init__(self, config):
        self.pickup_lifespan = int(config['PickupLifespan'])
        self.shield_amount = int(config['ShieldAmount'])

class MegaShieldConfig:
    def __init__(self, config):
        self.pickup_lifespan = int(config['PickupLifespan'])

class AsteroidConfig:
    def __init__(self, config):
        self.max_speed = int(config['MaxSpeed'])
        self.base_damage = int(config['BaseDamage'])
        self.base_health = int(config['BaseHealth'])
        self.base_radius = int(config['BaseRadius'])

class ProximityMineConfig:
    def __init__(self, config):
        self.pickup_lifespan = int(config['PickupLifespan'])
        self.projectile_radius = int(config['ProjectileRadius'])
        self.projectile_damage = int(config['ProjectileDamage'])
        self.detection_range = int(config['DetectionRange'])
        self.timer_duration = int(config['TimerDuration'])
        self.explosion_radius = int(config['ExplosionRadius'])
        self.explosion_damage = int(config['ExplosionDamage'])

class TimeBombConfig:
    def __init__(self, config):
        self.pickup_lifespan = int(config['PickupLifespan'])
        self.projectile_radius = int(config['ProjectileRadius'])
        self.projectile_damage = int(config['ProjectileDamage'])
        self.timer_duration = int(config['TimerDuration'])
        self.explosion_radius = int(config['ExplosionRadius'])
        self.explosion_damage = int(config['ExplosionDamage'])

class RocketConfig:
    def __init__(self, config):
        self.pickup_lifespan = int(config['PickupLifespan'])
        self.projectile_speed = int(config['ProjectileSpeed'])
        self.projectile_radius = int(config['ProjectileRadius'])
        self.projectile_damage = int(config['ProjectileDamage'])
        self.projectile_lifespan = int(config['ProjectileLifespan'])

class RocketSalvoConfig:
    def __init__(self, config):
        self.pickup_lifespan = int(config['PickupLifespan'])
        self.projectile_speed = int(config['ProjectileSpeed'])
        self.projectile_radius = int(config['ProjectileRadius'])
        self.projectile_damage = int(config['ProjectileDamage'])
        self.projectile_lifespan = int(config['ProjectileLifespan'])
        self.spread = int(config['Spread'])

class Config:
    def __init__(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)

        self.server = ServerConfig(config['Server'])
        self.misc = MiscConfig(config['Misc'])
        self.world = WorldConfig(config['World'])
        self.asteroid = AsteroidConfig(config['Asteroid'])

        self.ship = ShipConfig(config['Ship'])
        self.laser = LaserConfig(config['Laser'])
        self.rapid_fire = RapidFireConfig(config['RapidFire'])
        self.double_fire = DoubleFireConfig(config['DoubleFire'])
        self.spread_fire = SpreadFireConfig(config['SpreadFire'])
        self.heart = HeartConfig(config['Heart'])
        self.mega_heart = MegaHeartConfig(config['MegaHeart'])
        self.shield = ShieldConfig(config['Shield'])
        self.mega_shield = MegaShieldConfig(config['MegaShield'])
        self.rocket = RocketConfig(config['Rocket'])
        self.rocket_salvo = RocketSalvoConfig(config['RocketSalvo'])
        self.proximity_mine = ProximityMineConfig(config['ProximityMine'])
        self.time_bomb = TimeBombConfig(config['TimeBomb'])
