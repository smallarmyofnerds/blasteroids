from blasteroids.client.spacegame_utils import load_sprite
from pygame.math import Vector2
from blasteroids.client.game_object import GameObject2
from blasteroids.client.static_sprite import StaticSprite

class Bullet(GameObject2):
    def __init__(self, position, velocity):
        super(Bullet, self).__init__(position, Vector2(0, -1), velocity, (40, 40))
        self.sprite = StaticSprite(load_sprite('bullet'), (40, 40))

    def draw(self, screen):
        self.sprite.draw(screen, self.position, self.direction)
