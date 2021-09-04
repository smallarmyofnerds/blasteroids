import pygame
from .physical_object import PhysicalGameObject
from blasteroids.server.game_objects.armoury import Armoury


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

        self.is_engine_on = False
        self.shield = 0
        self.max_shields = config.ship.max_shields

    def on_removed(self, world):
        world.create_sound_effect('shipimpact', self.position)
        world.create_animation('explosion', self.position, self.velocity, 2000)
        self.player.kill()

    def shoot(self, world):
        self.armoury.shoot_active_weapon(self, world)

    def take_damage(self, amount, world):
        if amount >= self.shield:
            super(Ship, self).take_damage(amount - self.shield, world)
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
    
    def set_active_weapon(self, weapon_id):
        self.armoury.set_active_weapon(weapon_id)
    
    def reset_weapon(self):
        self.armoury.reset_weapon()
    
    def get_active_weapon(self):
        return self.armoury.get_active_weapon()

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

        self.is_engine_on = inputs.up

        self._set_rotations(inputs)

        if world.is_in_bounds(self.position):
            self._set_linear(inputs)
        else:
            # pull back into world
            self.acceleration = world.get_return_vector(self.position, self.velocity) * self.acceleration_rate

        if inputs and inputs.fire:
            self.shoot(world)
