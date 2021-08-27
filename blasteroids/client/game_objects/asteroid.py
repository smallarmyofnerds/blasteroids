from blasteroids.client.game_object import GameObject
from blasteroids.client.static_sprite import StaticSprite

class Asteroid(GameObject):
    def __init__(self, position, direction, sprite):
        super(Asteroid, self).__init__(position, direction, (130, 130))
        self.sprite = StaticSprite(sprite, (130, 130))
    
    def draw(self, screen):
        self.sprite.draw(screen, self.position, self.direction, self.size)
