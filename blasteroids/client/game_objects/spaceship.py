import pygame
from pygame import Vector2
from blasteroids.client.game_object import GameObject
from blasteroids.client.static_sprite import StaticSprite
from blasteroids.client.animated_sprite import AnimatedSprite

class Spaceship(GameObject):
    MANEUVERABILITY = 3
    ACCELERATION = 0.15
    BULLET_SPEED = 4
    SHIELD = 2

    def __init__(self, position, static_sprite, animation_frames):
        super(Spaceship, self).__init__(position, Vector2(0, -1), (50, 80))
        self.static_sprite = StaticSprite(static_sprite, (50, 80))
        self.animation_frames = AnimatedSprite(animation_frames, (50, 80), 8)
        self.mask = pygame.mask.from_surface(static_sprite)
        self.is_accelerating = False
    
    def draw(self, screen):
        if self.is_accelerating:
            self.animation_frames.draw(screen, self.position, self.direction, self.size)
        else:
            self.static_sprite.draw(screen, self.position, self.direction, self.size)

    def rotate(self, clockwise = True):
        sign = 1 if clockwise else -1
        angle = self.MANEUVERABILITY * sign
        self.direction.rotate_ip(angle)

    def accelerate(self):
        self.velocity += self.direction * self.ACCELERATION
