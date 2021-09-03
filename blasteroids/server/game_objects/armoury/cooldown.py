import pygame


class Cooldown:
    def __init__(self, cooldown):
        self.cooldown = cooldown
        self.last_shot = 0

    def set_cooldown(self, cooldown):
        self.cooldown = cooldown

    def can_shoot(self):
        return pygame.time.get_ticks() - self.last_shot > self.cooldown

    def update_last_shot(self):
        self.last_shot = pygame.time.get_ticks()
