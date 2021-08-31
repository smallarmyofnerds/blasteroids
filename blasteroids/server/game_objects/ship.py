from blasteroids.server.game_objects.laser import Laser
import pygame
from .physical_object import PhysicalGameObject


class Weapon:
    def __init__(self):
        pass

    def shoot(self, ship, world):
        pass


class LaserWeapon(Weapon):
    def __init__(self, speed, collision_radius, damage, lifespan, cooldown):
        self.speed = speed
        self.collision_radius = collision_radius
        self.damage = damage
        self.lifespan = lifespan
        self.cooldown = cooldown
        self.last_shot = 0
    
    def _generate_laser(self, ship, world, position, orientation):
        world.create_projectile(Laser(ship, None, position, orientation, self.speed, self.collision_radius, self.damage, self.lifespan))

    def shoot(self, ship, world):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.cooldown:
            self._generate_laser(ship, world, ship.position, ship.orientation)
            self.last_shot = now


class DoubleFireWeapon(LaserWeapon):
    def __init__(self, speed, collision_radius, damage, lifespan, cooldown):
        super(DoubleFireWeapon, self).__init__(speed, collision_radius, damage, lifespan, cooldown)
    
    def shoot(self, ship, world):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.cooldown:
            self._generate_laser(ship, world, ship.position + 10 * ship.orientation.rotate(90).normalize(), ship.orientation)
            self._generate_laser(ship, world, ship.position + 10 * ship.orientation.rotate(-90).normalize(), ship.orientation)
            self.last_shot = now


class SpreadFireWeapon(LaserWeapon):
    def __init__(self, speed, collision_radius, damage, lifespan, cooldown):
        super(SpreadFireWeapon, self).__init__(speed, collision_radius, damage, lifespan, cooldown)
    
    def shoot(self, ship, world):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.cooldown:
            self._generate_laser(ship, world, ship.position, ship.orientation)
            self._generate_laser(ship, world, ship.position, ship.orientation.rotate(20))
            self._generate_laser(ship, world, ship.position, ship.orientation.rotate(-20))
            self.last_shot = now


class Armoury:
    def __init__(self, config):
        self.weapons = {
            'laser': LaserWeapon(config.laser_speed, config.laser_radius, config.laser_damage, config.laser_lifespan, config.laser_cooldown),
            'double_fire': DoubleFireWeapon(config.laser_speed, config.laser_radius, config.laser_damage, config.laser_lifespan, config.laser_cooldown),
            'spread_fire': SpreadFireWeapon(config.laser_speed, config.laser_radius, config.laser_damage, config.laser_lifespan, config.laser_cooldown),
            'rapid_fire': LaserWeapon(config.rapid_fire_speed, config.rapid_fire_radius, config.rapid_fire_damage, config.rapid_fire_lifespan, config.rapid_fire_cooldown),
        }
        self.active_weapon_name = 'laser'
    
    def set_active_weapon(self, weapon_name):
        self.active_weapon_name = weapon_name
    
    def shoot_active_weapon(self, ship, world):
        self.weapons[self.active_weapon_name].shoot(ship, world)


class Ship(PhysicalGameObject):
    def __init__(self, config, id, position, orientation, player):
        super(Ship, self).__init__(
            id,
            player.name,
            position,
            orientation,
            pygame.Vector2(0, 0),
            config.ship_radius,
            config.ship_damage,
            config.ship_health,
        )
        self.config = config
        self.player = player
        self.acceleration_rate = config.ship_acceleration_rate
        self.rotational_acceleration_rate = config.ship_rotational_acceleration_rate
        self.rotational_velocity_friction = config.ship_rotational_velocity_friction
        self.linear_friction = config.ship_linear_friction

        self.armoury = Armoury(config)

        self.shield = 0
        self.max_shields = config.ship_max_shields

    def on_removed(self, world):
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
