import pygame
from pygame import surface

from pygame.math import Vector2
from pygame.transform import rotozoom

from blasteroids.client.spacegame_utils import get_random_velocity, load_sound, load_sprite, wrap_position
from blasteroids.client.game_object import GameObject
from blasteroids.client.game_objects.bullet import Bullet


s = Spaceship(
    position,
    load_sprite('static_ship'),
    [load_sprite('frame_1'), load_sprite('frame_2'), load_sprite('frame_3'), load_sprite('frame_2')]
)



UP = Vector2(0, -1)
        

class Spaceship(GameObject):
    MANEUVERABILITY = 3
    ACCELERATION = 0.15
    BULLET_SPEED = 4
    SHIELD = 2

    def __init__(self, position, sprite, moving_sprite, create_bullet_callback):
        self.create_bullet_callback = create_bullet_callback
        self.laser_sound = load_sound("laser")
        self.direction = Vector2(UP)
        self.sprite = pygame.transform.scale(sprite, (50, 70))
        self.move_counter = 0
        self.moving_sprite = moving_sprite
        self.is_moving = False
        self.engine = load_sound("engine")
        super().__init__(position, self.sprite, Vector2(0))
    
    def rotate(self, clockwise = True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)
    
    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION
    
    def shoot(self):
        bullet_velocity = self.direction * self.BULLET_SPEED + self.velocity
        bullet = Bullet(self.position, bullet_velocity)
        self.create_bullet_callback(bullet)
        self.create_bullet_callback(bullet)
        self.create_bullet_callback(bullet)
        self.create_bullet_callback(bullet)
        self.laser_sound.play()

    def set_moving(self, is_moving):
        self.is_moving = is_moving
        if self.is_moving:
            self.engine.play()
            self.move_counter = (self.move_counter + 1) % 32
        else:
            self.engine.stop()
            self.move_counter = 0
    
    def explode(self, surface):
        self.ship_explosion = load_sprite("shipexplosion")
        self.re_ship_explosion = pygame.transform.scale(self.ship_explosion, (80, 80))
        surface.blit(self.re_ship_explosion, self.position)

    def draw(self, surface):
        angle = self.direction.angle_to(UP)
        if self.is_moving:
            frame_to_draw = self.moving_sprite[self.move_counter//8]
            thing_to_draw = pygame.transform.scale(frame_to_draw, (50, 80))
            rotated_surface = rotozoom(thing_to_draw, angle, 1.0)
        else:
            rotated_surface = rotozoom(self.sprite, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size * 0.5
        surface.blit(rotated_surface, blit_position)
