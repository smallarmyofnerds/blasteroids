from blasteroids.server.game_objects.laser import Laser
import pygame
from .physical_object import PhysicalGameObject


class Ship(PhysicalGameObject):
    def __init__(self, config, id, position, orientation, name):
        super(Ship, self).__init__(
            id,
            name,
            position,
            orientation,
            pygame.Vector2(0, 0),
            config.ship_radius,
            config.ship_damage,
            config.ship_health,
        )
        self.config = config
        self.player = None
        self.acceleration_rate = config.ship_acceleration_rate
        self.rotational_acceleration_rate = config.ship_rotational_acceleration_rate
        self.rotational_velocity_friction = config.ship_rotational_velocity_friction
        self.linear_friction = 0.1
        self.last_shot = 0
        self.laser_cool_down = 200
        self.shield = 0
        self.max_shields = config.ship_max_shields

    def on_removed(self, world):
        self.player.remove_ship()

    def shoot(self, world):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.laser_cool_down:
            world.create_projectile(Laser(self.config, self, None, self.position, self.orientation, self.orientation.normalize() * 1000, self.config.laser_damage))
            self.last_shot = now

    def take_damage(self, amount):
        damage_to_shield = max(self.shield, self.shield - amount)
        damage_to_health = amount - damage_to_shield
        self.shield -= damage_to_shield
        self.health -= damage_to_health

        if self.health <= 0:
            self.destroy()

    def heal_by(self, amount):
        self.health = min(self.health + amount, self.max_health)
    
    def heal_full(self):
        self.health = self.max_health

    def shield_by(self, amount):
        self.shield = min(self.shield + amount, self.max_shields)
    
    def shield_full(self):
        self.shield = self.max_shields

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
