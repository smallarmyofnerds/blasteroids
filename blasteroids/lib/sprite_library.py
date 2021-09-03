import pygame


class SpriteLibrary:
    def __init__(self, convert=True):
        self.sprites = {}
        self.convert = convert

    def _load_sprite(self, filename):
        image = pygame.image.load(f'assets/sprites/{filename}')
        # if self.convert:
        #     return image.convert()
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
        self.sprites['heart_pickup'] = pygame.transform.scale(self._load_sprite('heart.png'), (48, 48))
        self.sprites['mega_heart_pickup'] = pygame.transform.scale(self._load_sprite('mega_heart.png'), (48, 48))
        self.sprites['shield_pickup'] = pygame.transform.scale(self._load_sprite('shield.png'), (48, 48))
        self.sprites['mega_shield_pickup'] = pygame.transform.scale(self._load_sprite('mega_shield.png'), (48, 48))
        self.sprites['rapid_fire_pickup'] = pygame.transform.scale(self._load_sprite('rapid_fire.png'), (48, 48))
        self.sprites['spread_fire_pickup'] = pygame.transform.scale(self._load_sprite('spread_fire.png'), (48, 48))
        self.sprites['double_fire_pickup'] = pygame.transform.scale(self._load_sprite('double_fire.png'), (48, 48))
        self.sprites['rocket_pickup'] = pygame.transform.scale(self._load_sprite('rocket_pickup.png'), (48, 48))
        self.sprites['rocket_salvo_pickup'] = pygame.transform.scale(self._load_sprite('rocket_salvo_pickup.png'), (48, 48))
        self.sprites['proximity_mine_pickup'] = pygame.transform.scale(self._load_sprite('proximity_mine_pickup.png'), (48, 48))
        self.sprites['time_bomb_pickup'] = pygame.transform.scale(self._load_sprite('time_bomb_pickup.png'), (48, 48))
        self.sprites['rocket_projectile'] = pygame.transform.scale(self._load_sprite('rocket_projectile.png'), (15, 60))
        self.sprites['rocket_salvo_projectile'] = pygame.transform.scale(self._load_sprite('rocket_salvo_projectile.png'), (12, 24))
        self.sprites['time_bomb_projectile'] = pygame.transform.scale(self._load_sprite('rocket_salvo_projectile.png'), (12, 24))
        self.sprites['proximity_mine_projectile'] = pygame.transform.scale(self._load_sprite('rocket_salvo_projectile.png'), (12, 24))

    def get(self, name):
        return self.sprites.get(name)
