import pygame


class GameObject:
    def __init__(self, server_object):
        self.id = server_object.id
        self.position = server_object.position
        self.orientation = server_object.orientation
        self.name = server_object.name
        self.destroyed_at = None
        self.death_duration = 500

    def _update(self, position, orientation):
        self.position = position
        self.orientation = orientation

    def destroy(self):
        self.destroyed_at = pygame.time.get_ticks()

    def should_be_removed(self):
        return self.destroyed_at is not None and (pygame.time.get_ticks() - self.destroyed_at > self.death_duration)

    def draw(self, screen):
        pass
