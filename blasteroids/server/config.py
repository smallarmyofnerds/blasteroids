import configparser


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
        self.safe_respawn_distance = int(config['SafeRespawnDistance'])


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
        self.min_speed = int(config['MinSpeed'])
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


class LootConfig:
    def __init__(self, config):
        self.level_1_chance = int(config['Level1Chance'])
        self.level_1_drops = list(filter(lambda d: len(d) > 0, config['Level1Drops'].split(',')))
        self.level_2_chance = int(config['Level2Chance'])
        self.level_2_drops = list(filter(lambda d: len(d) > 0, config['Level2Drops'].split(',')))
        self.level_3_chance = int(config['Level3Chance'])
        self.level_3_drops = list(filter(lambda d: len(d) > 0, config['Level3Drops'].split(',')))


class Config:
    def __init__(self, filename):
        config = configparser.ConfigParser()
        config.read(filename)

        self.server = ServerConfig(config['Server'])
        self.misc = MiscConfig(config['Misc'])
        self.world = WorldConfig(config['World'])
        self.asteroid = AsteroidConfig(config['Asteroid'])
        self.loot = LootConfig(config['Loot'])

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
