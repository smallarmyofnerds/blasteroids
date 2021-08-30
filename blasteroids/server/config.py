import configparser
import socket

DEFAULT_SERVER_ADDRESS = ''
DEFAULT_SERVER_PORT = 19999

DEFAULT_SHIP_ACCELERATION_RATE = 1
DEFAULT_SHIP_ROTATIONAL_ACCELERATION_RATE = 2
DEFAULT_SHIP_ROTATIONAL_VELOCITY_FRICTION = 0.1
DEFAULT_SHIP_RADIUS = 20
DEFAULT_SHIP_DAMAGE = 100
DEFAULT_SHIP_HEALTH = 100

DEFAULT_LASER_RADIUS = 5

DEFAULT_ASTEROID_MAX_SPEED = 50
DEFAULT_ASTEROID_BASE_DAMAGE = 10000
DEFAULT_ASTEROID_BASE_HEALTH = 1000
DEFAULT_ASTEROID_BASE_COLLISION_RADIUS = 28

DEFAULT_WORLD_WIDTH = 10000
DEFAULT_WORLD_HEIGHT = 10000


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
        self.ship_radius = float(config['Game'].get('ShipRadius', DEFAULT_SHIP_RADIUS))
        self.ship_damage = int(config['Game'].get('ShipDamage', DEFAULT_SHIP_DAMAGE))
        self.ship_health = int(config['Game'].get('ShipHealth', DEFAULT_SHIP_HEALTH))

        self.laser_radius = float(config['Game'].get('LaserRadius', DEFAULT_LASER_RADIUS))

        self.asteroid_max_speed = int(config['Game'].get('AsteroidMaxSpeed', DEFAULT_ASTEROID_MAX_SPEED))
        self.asteroid_base_damage = int(config['Game'].get('AsteroidBaseDamage', DEFAULT_ASTEROID_BASE_DAMAGE))
        self.asteroid_base_health = int(config['Game'].get('AsteroidBaseHealth', DEFAULT_ASTEROID_BASE_HEALTH))
        self.asteroid_base_collision_radius = int(config['Game'].get('AsteroidBaseCollisionRadius', DEFAULT_ASTEROID_BASE_COLLISION_RADIUS))

        self.world_width = int(config['Game'].get('WorldWidth', DEFAULT_WORLD_WIDTH))
        self.world_height = int(config['Game'].get('WorldHeight', DEFAULT_WORLD_HEIGHT))
