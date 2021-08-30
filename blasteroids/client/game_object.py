import pygame


class GameObject:
    def __init__(self, server_object):
        self.id = server_object.id
        self.position = server_object.position
        self.orientation = server_object.orientation
        self.name = server_object.name
        self.destroyed_at = None
        self.death_duration = 100

    def _update(self, position, orientation):
        self.position = position
        self.orientation = orientation

    def destroy(self):
        self.destroyed_at = pygame.time.get_ticks()

    def should_be_removed(self):
        dead_for = pygame.time.get_ticks() - self.destroyed_at
        return dead_for > self.death_duration

    def draw(self, screen):
        pass

    def on_create(self, sound_library):
        pass
