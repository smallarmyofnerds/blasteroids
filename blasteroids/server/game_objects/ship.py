from blasteroids.server.game_objects.laser import Laser
import pygame
from .destroyable_game_object import DestroyableGameObject


class Ship(DestroyableGameObject):
    def __init__(self, config, id, position, orientation, name):
        super(Ship, self).__init__(
            id,
            name,
            position,
            orientation,
            pygame.Vector2(0, 0),
            0,
            config.ship_rotational_velocity_friction,
            config.ship_radius,
            config.ship_damage,
            config.ship_health,
        )
        self.config = config
        self.player = None
        self.acceleration_rate = config.ship_acceleration_rate
        self.rotational_acceleration_rate = config.ship_rotational_acceleration_rate
        self.last_shot = 0
        self.laser_cool_down = 200
        self.shield = 0

    def on_removed(self, world):
        self.player.remove_ship()

    def zero_accelerations(self, delta_time):
        self.acceleration = -1 * delta_time * self.velocity
        self.rotational_acceleration = 0

    def set_rotating_left(self):
        self.rotational_acceleration = -1 * self.rotational_acceleration_rate

    def set_rotating_right(self):
        self.rotational_acceleration = self.rotational_acceleration_rate

    def set_accelerating(self):
        self.acceleration = self.orientation.normalize() * self.acceleration_rate

    def shoot(self, world):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.laser_cool_down:
            world.create_projectile(Laser(self.config, self, None, self.position, self.orientation, self.orientation.normalize() * 1000, self.config.laser_damage))
            self.last_shot = now

    def take_damage(self, damage):
        damage_to_shield = max(self.shield, self.shield - damage)
        damage_to_health = damage - damage_to_shield
        self.shield -= damage_to_shield
        self.health -= damage_to_health

        if self.health <= 0:
            self.destroy()

    def _before_update(self, world, delta_time):
        self.zero_accelerations(delta_time)
        inputs = self.player.get_inputs()
        if world.is_in_bounds(self.position):
            if inputs:
                if inputs.left:
                    if inputs.right:
                        pass
                    else:
                        self.set_rotating_left()
                elif inputs.right:
                    self.set_rotating_right()
                if inputs.up:
                    self.set_accelerating()
                if inputs.fire:
                    self.shoot(world)
        else:
            self.acceleration = world.get_return_vector(self.position).normalize() * self.acceleration_rate * 2
            if inputs:
                if inputs.left:
                    if inputs.right:
                        pass
                    else:
                        self.set_rotating_left()
                elif inputs.right:
                    self.set_rotating_right()
                if inputs.fire:
                    self.shoot(world)
