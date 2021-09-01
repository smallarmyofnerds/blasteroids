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


class Config:
    def __init__(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)

        self.server_address = config['Server'].get('Address', DEFAULT_SERVER_ADDRESS)
        self.server_port = int(config['Server'].get('Port', DEFAULT_SERVER_PORT))
        self.server_name = config['Server'].get('Name', socket.gethostname())
        self.welcome_message = config['Server'].get('WelcomeMessage', f'Welcome to the {socket.gethostname()} server!')

        self.logging_level = config['Misc'].get('LoggingLevel', 'INFO')

        self.ship_acceleration_rate = int(config['Game'].get('ShipAccelerationRate', DEFAULT_SHIP_ACCELERATION_RATE))
        self.ship_rotational_acceleration_rate = int(config['Game'].get('ShipRotationalAccelerationRate', DEFAULT_SHIP_ROTATIONAL_ACCELERATION_RATE))
        self.ship_rotational_velocity_friction = float(config['Game'].get('ShipRotationalVelocityFriction', DEFAULT_SHIP_ROTATIONAL_VELOCITY_FRICTION))
        self.ship_linear_friction = float(config['Game'].get('ShipLinearFriction', DEFAULT_SHIP_LINEAR_FRICTION))
        self.ship_radius = float(config['Game'].get('ShipRadius', DEFAULT_SHIP_RADIUS))
        self.ship_damage = int(config['Game'].get('ShipDamage', DEFAULT_SHIP_DAMAGE))
        self.ship_health = int(config['Game'].get('ShipHealth', DEFAULT_SHIP_HEALTH))
        self.ship_max_shields = int(config['Game'].get('ShipMaxShields', DEFAULT_SHIP_MAX_SHIELDS))

        self.laser_speed = int(config['Game'].get('LaserSpeed', DEFAULT_LASER_SPEED))
        self.laser_radius = float(config['Game'].get('LaserRadius', DEFAULT_LASER_RADIUS))
        self.laser_damage = int(config['Game'].get('LaserDamage', DEFAULT_LASER_DAMAGE))
        self.laser_lifespan = int(config['Game'].get('LaserLifespan', DEFAULT_LASER_LIFESPAN))
        self.laser_cooldown = int(config['Game'].get('LaserCooldown', DEFAULT_LASER_COOLDOWN))

        self.rapid_fire_speed = int(config['Game'].get('RapidFireSpeed', DEFAULT_RAPID_FIRE_SPEED))
        self.rapid_fire_radius = float(config['Game'].get('RapidFireRadius', DEFAULT_RAPID_FIRE_RADIUS))
        self.rapid_fire_damage = int(config['Game'].get('RapidFireDamage', DEFAULT_RAPID_FIRE_DAMAGE))
        self.rapid_fire_lifespan = int(config['Game'].get('RapidFireLifespan', DEFAULT_RAPID_FIRE_LIFESPAN))
        self.rapid_fire_cooldown = int(config['Game'].get('RapidFireCooldown', DEFAULT_RAPID_FIRE_COOLDOWN))

        self.min_asteroids = int(config['Game'].get('MinAsteroids', DEFAULT_MIN_ASTEROIDS))
        self.asteroid_max_speed = int(config['Game'].get('AsteroidMaxSpeed', DEFAULT_ASTEROID_MAX_SPEED))
        self.asteroid_base_damage = int(config['Game'].get('AsteroidBaseDamage', DEFAULT_ASTEROID_BASE_DAMAGE))
        self.asteroid_base_health = int(config['Game'].get('AsteroidBaseHealth', DEFAULT_ASTEROID_BASE_HEALTH))
        self.asteroid_base_collision_radius = int(config['Game'].get('AsteroidBaseCollisionRadius', DEFAULT_ASTEROID_BASE_COLLISION_RADIUS))

        self.heart_health = int(config['Game'].get('HeartHealth', DEFAULT_HEART_HEALTH))
        self.shield_amount = int(config['Game'].get('ShieldAmount', DEFAULT_SHIELD_AMOUNT))

        self.double_fire_lifespan = int(config['Game'].get('DoubleFireLifespan', DEFAULT_DOUBLE_FIRE_LIFESPAN))
        self.heart_lifespan = int(config['Game'].get('HeartLifespan', DEFAULT_HEART_LIFESPAN))
        self.mega_heart_lifespan = int(config['Game'].get('MegaHeartLifespan', DEFAULT_MEGA_HEART_LIFESPAN))
        self.mega_shield_lifespan = int(config['Game'].get('MegaShieldLifespan', DEFAULT_MEGA_SHIELD_LIFESPAN))
        self.proximity_mine_lifespan = int(config['Game'].get('ProximityMineLifespan', DEFAULT_PROXIMITY_MINE_LIFESPAN))
        self.rapid_fire_lifespan = int(config['Game'].get('RapidFireLifespan', DEFAULT_RAPID_FIRE_LIFESPAN))
        self.rocket_salvo_lifespan = int(config['Game'].get('RocketSalvoLifespan', DEFAULT_ROCKET_SALVO_LIFESPAN))
        self.rocket_lifespan = int(config['Game'].get('RocketLifespan', DEFAULT_ROCKET_LIFESPAN))
        self.shield_lifespan = int(config['Game'].get('ShieldLifespan', DEFAULT_SHIELD_LIFESPAN))
        self.spread_fire_lifespan = int(config['Game'].get('SpreadFireLifespan', DEFAULT_SPREAD_FIRE_LIFESPAN))
        self.time_bomb_lifespan = int(config['Game'].get('TimeBombLifespan', DEFAULT_TIME_BOMB_LIFESPAN))

        self.world_width = int(config['Game'].get('WorldWidth', DEFAULT_WORLD_WIDTH))
        self.world_height = int(config['Game'].get('WorldHeight', DEFAULT_WORLD_HEIGHT))
        self.world_edge_acceleration_factor = float(config['Game'].get('WorldEdgeAccelerationFactor', DEFAULT_WORLD_EDGE_ACCELERATION_FACTOR))
