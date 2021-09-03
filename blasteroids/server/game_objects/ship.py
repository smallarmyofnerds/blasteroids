from blasteroids.server.game_objects.rocket_projectile import RocketProjectile
from .time_bomb_projectile import TimeBombProjectile
from .proximity_mine_projectile import ProximityMineProjectile
from blasteroids.server.game_objects.laser import Laser
import pygame
from .physical_object import PhysicalGameObject


class Weapon:
    def __init__(self):
        pass

    def shoot(self, ship, world):
        pass


class Cooldown(Weapon):
    def __init__(self, cooldown):
        self.cooldown = cooldown
        self.last_shot = 0

    def set_cooldown(self, cooldown):
        self.cooldown = cooldown

    def can_shoot(self):
        return pygame.time.get_ticks() - self.last_shot > self.cooldown

    def update_last_shot(self):
        self.last_shot = pygame.time.get_ticks()


class LaserWeapon(Weapon):
    def __init__(self, speed, collision_radius, damage, lifespan, cooldown):
        self.cooldown = Cooldown(cooldown)
        self.speed = speed
        self.collision_radius = collision_radius
        self.damage = damage
        self.lifespan = lifespan
    
    def _generate_laser(self, ship, world, position, orientation):
        world.create_projectile(Laser(ship, None, position, orientation, self.speed, self.collision_radius, self.damage, self.lifespan))

    def shoot(self, ship, world):
        if self.cooldown.can_shoot():
            self._generate_laser(ship, world, ship.position, ship.orientation)
            world.create_sound_effect('laser', ship.position)
            self.cooldown.update_last_shot()


class DoubleFireWeapon(LaserWeapon):
    def __init__(self, speed, collision_radius, damage, lifespan, cooldown, offset):
        super(DoubleFireWeapon, self).__init__(speed, collision_radius, damage, lifespan, cooldown)
        self.offset = offset
    
    def shoot(self, ship, world):
        if self.cooldown.can_shoot():
            self._generate_laser(ship, world, ship.position + self.offset * ship.orientation.rotate(90).normalize(), ship.orientation)
            self._generate_laser(ship, world, ship.position + self.offset * ship.orientation.rotate(-90).normalize(), ship.orientation)
            world.create_sound_effect('laser', ship.position)
            self.cooldown.update_last_shot()


class SpreadFireWeapon(LaserWeapon):
    def __init__(self, speed, collision_radius, damage, lifespan, cooldown, spread):
        super(SpreadFireWeapon, self).__init__(speed, collision_radius, damage, lifespan, cooldown)
        self.spread = spread
    
    def shoot(self, ship, world):
        if self.cooldown.can_shoot():
            self._generate_laser(ship, world, ship.position, ship.orientation)
            self._generate_laser(ship, world, ship.position, ship.orientation.rotate(self.spread))
            self._generate_laser(ship, world, ship.position, ship.orientation.rotate(-1 * self.spread))
            world.create_sound_effect('laser', ship.position)
            self.cooldown.update_last_shot()


class RocketWeapon(Weapon):
    def __init__(self, speed, collision_radius, damage, lifespan, name = 'rocket_projectile'):
        self.speed = speed
        self.collision_radius = collision_radius
        self.damage = damage
        self.lifespan = lifespan
        self.name = name
    
    def _generate_rocket(self, ship, world, position, orientation):
        world.create_projectile(RocketProjectile(ship, None, position, orientation, self.speed, self.collision_radius, self.damage, self.lifespan, self.name))

    def shoot(self, ship, world):
        self._generate_rocket(ship, world, ship.position, ship.orientation)
        ship.reset_weapon()
        world.create_sound_effect('rocket_shot', ship.position)


class RocketSalvoWeapon(RocketWeapon):
    def __init__(self, speed, collision_radius, damage, lifespan, spread):
        super(RocketSalvoWeapon, self).__init__(speed, collision_radius, damage, lifespan, 'rocket_salvo_projectile')
        self.spread = spread
    
    def shoot(self, ship, world):
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(-1 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(-2 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(-3 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(-4 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(-5 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(1 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(2 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(3 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(4 * self.spread))
        self._generate_rocket(ship, world, ship.position, ship.orientation.rotate(5 * self.spread))

        ship.reset_weapon()

        world.create_sound_effect('rocket_shot', ship.position)


class TimeBombWeapon(Weapon):
    def __init__(self, collision_radius, damage, timer_duration, explosion_radius, explosion_damage):
        self.collision_radius = collision_radius
        self.damage = damage
        self.timer_duration = timer_duration
        self.explosion_radius = explosion_radius
        self.explosion_damage = explosion_damage
    
    def shoot(self, ship, world):
        world.create_projectile(TimeBombProjectile(ship, None, ship.position, ship.velocity, self.collision_radius, self.damage, self.timer_duration, self.explosion_radius, self.explosion_damage))
        ship.reset_weapon()

class ProximityMineWeapon(Weapon):
    def __init__(self, collision_radius, damage, detection_range, timer_duration, explosion_radius, explosion_damage):
        self.collision_radius = collision_radius
        self.damage = damage
        self.detection_range = detection_range
        self.timer_duration = timer_duration
        self.explosion_radius = explosion_radius
        self.explosion_damage = explosion_damage
    
    def shoot(self, ship, world):
        world.create_projectile(ProximityMineProjectile(ship, None, ship.position, ship.velocity, self.collision_radius, self.damage, self.detection_range, self.timer_duration, self.explosion_radius, self.explosion_damage))
        ship.reset_weapon()

class Armoury:
    def __init__(self, config):
        self.weapons = {
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
        self.active_weapon_name = 'laser'
        self.cooldown = Cooldown(0)
    
    def set_active_weapon(self, weapon_name):
        self.active_weapon_name = weapon_name
    
    def reset_weapon(self):
        self.set_active_weapon('laser')
        self.cooldown.set_cooldown(500)
    
    def shoot_active_weapon(self, ship, world):
        if self.cooldown.can_shoot():
            self.cooldown.set_cooldown(0)
            self.weapons[self.active_weapon_name].shoot(ship, world)
            self.cooldown.update_last_shot()


class Ship(PhysicalGameObject):
    def __init__(self, config, id, position, orientation, player):
        super(Ship, self).__init__(
            id,
            player.name,
            position,
            orientation,
            pygame.Vector2(0, 0),
            config.ship.radius,
            config.ship.damage,
            config.ship.max_health,
        )
        self.config = config
        self.player = player
        self.acceleration_rate = config.ship.linear_acceleration
        self.rotational_acceleration_rate = config.ship.angular_acceleration
        self.rotational_velocity_friction = config.ship.angular_friction
        self.linear_friction = config.ship.linear_friction

        self.armoury = Armoury(config)

        self.shield = 0
        self.max_shields = config.ship.max_shields

    def on_removed(self, world):
        world.create_sound_effect('shipimpact', self.position)
        self.player.kill()

    def shoot(self, world):
        self.armoury.shoot_active_weapon(self, world)

    def take_damage(self, amount):
        if amount >= self.shield:
            super(Ship, self).take_damage(amount - self.shield)
            self.shield = 0
        else:
            self.shield -= amount

    def heal_by(self, amount):
        self.health = min(self.health + amount, self.max_health)
    
    def heal_full(self):
        self.health = self.max_health

    def shield_by(self, amount):
        self.shield = min(self.shield + amount, self.max_shields)
    
    def shield_full(self):
        self.shield = self.max_shields
    
    def set_active_weapon(self, weapon_name):
        self.armoury.set_active_weapon(weapon_name)
    
    def reset_weapon(self):
        self.armoury.reset_weapon()
    
    def get_active_weapon(self):
        return self.armoury.active_weapon_name

    def _set_rotating_left(self):
        self.rotational_acceleration = -1 * self.rotational_acceleration_rate
    
    def _set_rotating_right(self):
        self.rotational_acceleration = self.rotational_acceleration_rate

    def _set_slowing_rotation(self):
        self.rotational_acceleration = -1 * self.rotational_velocity_friction * self.rotational_velocity

    def _set_rotations(self, inputs):
        if inputs:
            if inputs.left:
                if inputs.right:
                    self._set_slowing_rotation()
                else:
                    self._set_rotating_left()
            elif inputs.right:
                self._set_rotating_right()
            else:
                self._set_slowing_rotation()
        else:
            self._set_slowing_rotation()

    def _set_accelerating(self):
        self.acceleration = self.orientation.normalize() * self.acceleration_rate
    
    def _set_slowing(self):
        self.acceleration = -1 * self.linear_friction * self.velocity

    def _set_linear(self, inputs):
        if inputs:
            if inputs.up:
                self._set_accelerating()
            else:
                self._set_slowing()
        else:
            self._set_slowing()

    def _set_accelerations(self, world):
        inputs = self.player.get_inputs()

        self._set_rotations(inputs)

        if world.is_in_bounds(self.position):
            self._set_linear(inputs)
        else:
            # pull back into world
            self.acceleration = world.get_return_vector(self.position, self.velocity) * self.acceleration_rate

        if inputs and inputs.fire:
            self.shoot(world)
