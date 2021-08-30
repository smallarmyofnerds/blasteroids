import pygame


class SpriteLibrary:
    def __init__(self, convert=True):
        self.sprites = {}
        self.convert = convert

    def _load_sprite(self, filename):
        image = pygame.image.load(f'assets/sprites/{filename}')
        if self.convert:
            return image.convert()
        return image

    def load_all(self):
        self.sprites['player_1_static'] = pygame.transform.scale(self._load_sprite('player_1_static.png'), (48, 48))
        # self.sprites['player_1_flying'] = self._load_sprite('player_1_flying.png')
        # self.sprites['player_1_exploding'] = self._load_sprite('player_1_exploding.png')
        self.sprites['player_2_static'] = pygame.transform.scale(self._load_sprite('player_2_static.png'), (48, 48))
        self.sprites['asteroid_3'] = pygame.transform.scale(self._load_sprite('asteroid.png'), (96, 96))
        self.sprites['asteroid_2'] = pygame.transform.scale(self._load_sprite('asteroid.png'), (64, 64))
        self.sprites['asteroid_1'] = pygame.transform.scale(self._load_sprite('asteroid.png'), (32, 32))
        self.sprites['laser'] = pygame.transform.scale(self._load_sprite('laser.png'), (15, 60))

    def get(self, name):
        return self.sprites.get(name)
