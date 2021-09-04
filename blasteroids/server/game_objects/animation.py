from pygame import Vector2
import pygame
from .game_object import GameObject


class Animation(GameObject):
    def __init__(self, id, position, velocity, animation_id, duration):
        super(Animation, self).__init__(id, position, Vector2(0, 1), velocity)
        self.animation_id = animation_id
        self.duration = duration
        self.started_at = pygame.time.get_ticks()

    def update(self, world, delta_time):
        if pygame.time.get_ticks() - self.started_at > self.duration:
            self.destroy()
        else:
            super(Animation, self).update(world, delta_time)

    def is_in_bounds(self, world):
        return world.is_player_in_bounds(self.position, 200)
