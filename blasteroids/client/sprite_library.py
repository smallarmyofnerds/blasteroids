from blasteroids.lib.constants import DOUBLE_FIRE_PICKUP_ID, EXPLOSION_ANIMATION_ID, HEALTH_PICKUP_ID, LASER_PROJECTILE_ID, MEGA_HEALTH_PICKUP_ID, MEGA_SHIELD_PICKUP_ID, PROXIMITY_MINE_PICKUP_ID, PROXIMITY_MINE_PROJECTILE_ID, RAPID_FIRE_PICKUP_ID, ROCKET_PICKUP_ID, ROCKET_PROJECTILE_ID, ROCKET_SALVO_PICKUP_ID, ROCKET_SALVO_PROJECTILE_ID, SHIELD_PICKUP_ID, SHIP_EXHAUST_ANIMATION_ID, SPREAD_FIRE_PICKUP_ID, TIME_BOMB_PICKUP_ID, TIME_BOMB_PROJECTILE_ID
import pygame
from .animation import Animation


class SpriteLibrary:
    def __init__(self, convert=True):
        self.ship_sprites = {}
        self.asteroid_sprites = {}
        self.pickup_sprites = {}
        self.projectile_sprites = {}
        self.animations = {}

    def _load_sprite(self, filename, size=None):
        if size:
            return pygame.transform.scale(pygame.image.load(f'assets/sprites/{filename}'), size)
        return pygame.image.load(f'assets/sprites/{filename}')

    def load_all(self):
        self.ship_sprites[1] = self._load_sprite('player_1_static.png', (48, 48))
        self.ship_sprites[2] = self._load_sprite('player_2_static.png', (48, 48))

        self.asteroid_sprites[3] = self._load_sprite('asteroid.png', (96, 96))
        self.asteroid_sprites[2] = self._load_sprite('asteroid.png', (64, 64))
        self.asteroid_sprites[1] = self._load_sprite('asteroid.png', (32, 32))

        self.pickup_sprites[HEALTH_PICKUP_ID] = self._load_sprite('heart.png', (48, 48))
        self.pickup_sprites[MEGA_HEALTH_PICKUP_ID] = self._load_sprite('mega_heart.png', (48, 48))
        self.pickup_sprites[SHIELD_PICKUP_ID] = self._load_sprite('shield.png', (48, 48))
        self.pickup_sprites[MEGA_SHIELD_PICKUP_ID] = self._load_sprite('mega_shield.png', (48, 48))
        self.pickup_sprites[DOUBLE_FIRE_PICKUP_ID] = self._load_sprite('double_fire.png', (48, 48))
        self.pickup_sprites[SPREAD_FIRE_PICKUP_ID] = self._load_sprite('spread_fire.png', (48, 48))
        self.pickup_sprites[RAPID_FIRE_PICKUP_ID] = self._load_sprite('rapid_fire.png', (48, 48))
        self.pickup_sprites[ROCKET_PICKUP_ID] = self._load_sprite('rocket_pickup.png', (48, 48))
        self.pickup_sprites[ROCKET_SALVO_PICKUP_ID] = self._load_sprite('rocket_salvo_pickup.png', (48, 48))
        self.pickup_sprites[TIME_BOMB_PICKUP_ID] = self._load_sprite('time_bomb_pickup.png', (48, 48))
        self.pickup_sprites[PROXIMITY_MINE_PICKUP_ID] = self._load_sprite('proximity_mine_pickup.png', (48, 48))

        self.projectile_sprites[LASER_PROJECTILE_ID] = self._load_sprite('laser.png', (15, 60))
        self.projectile_sprites[ROCKET_PROJECTILE_ID] = self._load_sprite('rocket_projectile.png', (15, 60))
        self.projectile_sprites[ROCKET_SALVO_PROJECTILE_ID] = self._load_sprite('rocket_salvo_projectile.png', (12, 24))
        self.projectile_sprites[TIME_BOMB_PROJECTILE_ID] = self._load_sprite('time_bomb_projectile.png', (12, 24))
        self.projectile_sprites[PROXIMITY_MINE_PROJECTILE_ID] = self._load_sprite('proximity_mine_projectile.png', (24, 24))

        frames = []
        for i in range(10):
            frames.append(self._load_sprite(f'exhaust_{i}.png', (32, 32)))
        self.animations[SHIP_EXHAUST_ANIMATION_ID] = Animation(frames, 100)

        sprite_sheet = self._load_sprite('explosion_1.png')
        frames = []
        for row in range(13):
            for column in range(5):
                frame = pygame.Surface((192, 192), pygame.SRCALPHA, 32)
                frame.blit(sprite_sheet, (0, 0), pygame.Rect(column * 192, row * 192, 192, 192))
                # frame.convert_alpha()
                # frame.set_colorkey(pygame.Color(0, 0, 0))
                frames.append(frame)
        self.animations[EXPLOSION_ANIMATION_ID] = Animation(frames, 20)
