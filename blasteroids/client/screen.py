import pygame


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = None

    def init(self):
        self.surface = pygame.display.set_mode((self.width, self.height))

    def reset(self):
        self.surface.fill((0, 0, 0))
    
    def draw_sprite(self, sprite, position):
        pass
