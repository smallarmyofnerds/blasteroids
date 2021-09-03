from .laser_weapon import LaserWeapon
from .double_fire_weapon import DoubleFireWeapon
from .spread_fire_weapon import SpreadFireWeapon
from .rocket_weapon import RocketWeapon
from .rocket_salvo_weapon import RocketSalvoWeapon
from .time_bomb_weapon import TimeBombWeapon
from .proximity_mine_weapon import ProximityMineWeapon
from .cooldown import Cooldown


def build_weapons(config):
    return {
        'laser': LaserWeapon(
            config.laser.projectile_speed,
            config.laser.projectile_radius,
            config.laser.projectile_damage,
            config.laser.projectile_lifespan,
            config.laser.cooldown,
        ),
        'double_fire': DoubleFireWeapon(
            config.laser.projectile_speed,
            config.laser.projectile_radius,
            config.laser.projectile_damage,
            config.laser.projectile_lifespan,
            config.laser.cooldown,
            config.double_fire.offset,
        ),
        'spread_fire': SpreadFireWeapon(
            config.laser.projectile_speed,
            config.laser.projectile_radius,
            config.laser.projectile_damage,
            config.laser.projectile_lifespan,
            config.laser.cooldown,
            config.spread_fire.spread,
        ),
        'rapid_fire': LaserWeapon(
            config.rapid_fire.projectile_speed,
            config.rapid_fire.projectile_radius,
            config.rapid_fire.projectile_damage,
            config.rapid_fire.projectile_lifespan,
            config.rapid_fire.cooldown,
        ),
        'rocket': RocketWeapon(
            config.rocket.projectile_speed,
            config.rocket.projectile_radius,
            config.rocket.projectile_damage,
            config.rocket.projectile_lifespan,
        ),
        'rocket_salvo': RocketSalvoWeapon(
            config.rocket_salvo.projectile_speed,
            config.rocket_salvo.projectile_radius,
            config.rocket_salvo.projectile_damage,
            config.rocket_salvo.projectile_lifespan,
            config.rocket_salvo.spread,
        ),
        'time_bomb': TimeBombWeapon(
            config.time_bomb.projectile_radius,
            config.time_bomb.projectile_damage,
            config.time_bomb.timer_duration,
            config.time_bomb.explosion_radius,
            config.time_bomb.explosion_damage,
        ),
        'proximity_mine': ProximityMineWeapon(
            config.proximity_mine.projectile_radius,
            config.proximity_mine.projectile_damage,
            config.proximity_mine.detection_range,
            config.proximity_mine.timer_duration,
            config.proximity_mine.explosion_radius,
            config.proximity_mine.explosion_damage,
        ),
    }


class Armoury:
    def __init__(self, config):
        self.weapons = build_weapons(config)
        self.active_weapon_name = 'rocket'
        self.cooldown = Cooldown(0)
    
    def set_active_weapon(self, weapon_name):
        self.active_weapon_name = weapon_name
    
    def reset_weapon(self):
        self.set_active_weapon('rocket_salvo')
        self.cooldown.set_cooldown(500)
    
    def shoot_active_weapon(self, ship, world):
        if self.cooldown.can_shoot():
            self.cooldown.set_cooldown(0)
            self.weapons[self.active_weapon_name].shoot(ship, world)
            self.cooldown.update_last_shot()
