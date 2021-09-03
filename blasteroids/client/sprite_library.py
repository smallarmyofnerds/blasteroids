import pygame
from .animation import Animation


class SpriteLibrary:
    def __init__(self, convert=True):
        self.sprites = {}
        self.convert = convert
        self.animations = {}

    def _load_sprite(self, filename, size=None):
        if size:
            return pygame.transform.scale(pygame.image.load(f'assets/sprites/{filename}'), size)
        return pygame.image.load(f'assets/sprites/{filename}')

    def load_all(self):
        self.sprites['player_1_static'] = self._load_sprite('player_1_static.png', (48, 48))
        # self.sprites['player_1_flying'] = self._load_sprite('player_1_flying.png')
        # self.sprites['player_1_exploding'] = self._load_sprite('player_1_exploding.png')
        self.sprites['player_2_static'] = self._load_sprite('player_2_static.png', (48, 48))
        self.sprites['asteroid_3'] = self._load_sprite('asteroid.png', (96, 96))
        self.sprites['asteroid_2'] = self._load_sprite('asteroid.png', (64, 64))
        self.sprites['asteroid_1'] = self._load_sprite('asteroid.png', (32, 32))
        self.sprites['laser'] = self._load_sprite('laser.png', (15, 60))
        self.sprites['heart_pickup'] = self._load_sprite('heart.png', (48, 48))
        self.sprites['mega_heart_pickup'] = self._load_sprite('mega_heart.png', (48, 48))
        self.sprites['shield_pickup'] = self._load_sprite('shield.png', (48, 48))
        self.sprites['mega_shield_pickup'] = self._load_sprite('mega_shield.png', (48, 48))
        self.sprites['rapid_fire_pickup'] = self._load_sprite('rapid_fire.png', (48, 48))
        self.sprites['spread_fire_pickup'] = self._load_sprite('spread_fire.png', (48, 48))
        self.sprites['double_fire_pickup'] = self._load_sprite('double_fire.png', (48, 48))
        self.sprites['rocket_pickup'] = self._load_sprite('rocket_pickup.png', (48, 48))
        self.sprites['rocket_salvo_pickup'] = self._load_sprite('rocket_salvo_pickup.png', (48, 48))
        self.sprites['proximity_mine_pickup'] = self._load_sprite('proximity_mine_pickup.png', (48, 48))
        self.sprites['time_bomb_pickup'] = self._load_sprite('time_bomb_pickup.png', (48, 48))
        self.sprites['rocket_projectile'] = self._load_sprite('rocket_projectile.png', (15, 60))
        self.sprites['rocket_salvo_projectile'] = self._load_sprite('rocket_salvo_projectile.png', (12, 24))
        self.sprites['time_bomb_projectile'] = self._load_sprite('time_bomb_projectile.png', (12, 24))
        self.sprites['proximity_mine_projectile'] = self._load_sprite('proximity_mine_projectile.png', (24, 24))

        frames = []
        for i in range(10):
            frames.append(self._load_sprite(f'exhaust_{i}.png', (32, 32)))
        self.animations['exhaust'] = Animation(frames, 100)

        sprite_sheet = self._load_sprite('explosion_1.png')
        frames = []
        for row in range(13):
            for column in range(5):
                frame = pygame.Surface((192, 192), pygame.SRCALPHA, 32)
                frame.blit(sprite_sheet, (0, 0), pygame.Rect(column * 192, row * 192, 192, 192))
                # frame.convert_alpha()
                # frame.set_colorkey(pygame.Color(0, 0, 0))
                frames.append(frame)
        self.animations['explosion'] = Animation(frames, 20)

    def get(self, name):
        return self.sprites.get(name)
