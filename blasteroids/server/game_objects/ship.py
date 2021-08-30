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
        self.laser_cool_down = 100

    def destroy(self, world):
        world.remove_ship(self)

    def zero_accelerations(self):
        self.acceleration = pygame.Vector2(0, 0)
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
            world.create_projectile(Laser(self.config, None, self.position, self.orientation, self.orientation.normalize() * 1000, 100))
            self.last_shot = now
