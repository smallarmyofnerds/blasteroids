from blasteroids.lib.constants import DOUBLE_FIRE_WEAPON_ID, LASER_WEAPON_ID, PROXIMITY_MINE_WEAPON_ID, RAPID_FIRE_WEAPON_ID, ROCKET_SALVO_WEAPON_ID, ROCKET_WEAPON_ID, SPREAD_FIRE_WEAPON_ID, TIME_BOMB_WEAPON_ID
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
        LASER_WEAPON_ID: LaserWeapon(
            config.laser.projectile_speed,
            config.laser.projectile_radius,
            config.laser.projectile_damage,
            config.laser.projectile_lifespan,
            config.laser.cooldown,
        ),
        DOUBLE_FIRE_WEAPON_ID: DoubleFireWeapon(
            config.laser.projectile_speed,
            config.laser.projectile_radius,
            config.laser.projectile_damage,
            config.laser.projectile_lifespan,
            config.laser.cooldown,
            config.double_fire.offset,
        ),
        SPREAD_FIRE_WEAPON_ID: SpreadFireWeapon(
            config.laser.projectile_speed,
            config.laser.projectile_radius,
            config.laser.projectile_damage,
            config.laser.projectile_lifespan,
            config.laser.cooldown,
            config.spread_fire.spread,
        ),
        RAPID_FIRE_WEAPON_ID: LaserWeapon(
            config.rapid_fire.projectile_speed,
            config.rapid_fire.projectile_radius,
            config.rapid_fire.projectile_damage,
            config.rapid_fire.projectile_lifespan,
            config.rapid_fire.cooldown,
        ),
        ROCKET_WEAPON_ID: RocketWeapon(
            config.rocket.projectile_speed,
            config.rocket.projectile_radius,
            config.rocket.projectile_damage,
            config.rocket.projectile_lifespan,
        ),
        ROCKET_SALVO_WEAPON_ID: RocketSalvoWeapon(
            config.rocket_salvo.projectile_speed,
            config.rocket_salvo.projectile_radius,
            config.rocket_salvo.projectile_damage,
            config.rocket_salvo.projectile_lifespan,
            config.rocket_salvo.spread,
        ),
        TIME_BOMB_WEAPON_ID: TimeBombWeapon(
            config.time_bomb.projectile_radius,
            config.time_bomb.projectile_damage,
            config.time_bomb.timer_duration,
            config.time_bomb.explosion_radius,
            config.time_bomb.explosion_damage,
        ),
        PROXIMITY_MINE_WEAPON_ID: ProximityMineWeapon(
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
        self.active_weapon_id = LASER_WEAPON_ID
        self.cooldown = Cooldown(0)

    def set_active_weapon(self, weapon_id):
        self.active_weapon_id = weapon_id

    def reset_weapon(self):
        self.set_active_weapon(LASER_WEAPON_ID)
        self.cooldown.set_cooldown(500)

    def get_active_weapon(self):
        return self.active_weapon_id

    def shoot_active_weapon(self, ship, world):
        if self.cooldown.can_shoot():
            self.cooldown.set_cooldown(0)
            self.weapons[self.active_weapon_id].shoot(ship, world)
            self.cooldown.update_last_shot()
