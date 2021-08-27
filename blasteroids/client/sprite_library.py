import pygame


class SpriteLibrary:
    def __init__(self):
        self.sprites = {}

    def _load_sprite(self, filename):
        return pygame.image.load(f'assets/sprites/{filename}')

    def load_all(self):
        self.sprites['player_1_static'] = self._load_sprite('player_1_static.png')
        # self.sprites['player_1_flying'] = self._load_sprite('player_1_flying.png')
        # self.sprites['player_1_exploding'] = self._load_sprite('player_1_exploding.png')
        self.sprites['player_2_static'] = self._load_sprite('player_2_static.png')

    def get(self, name):
        return self.sprites.get(name)
