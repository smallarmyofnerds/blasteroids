from .drawable_object import DrawableObject

class StaticSprite(DrawableObject):
    def __init__(self, sprite, size):
        super(StaticSprite, self).__init__(size)
        self.sprite = sprite
    
    def draw(self, surface, position, direction):
        self._scale_rotate_and_blit(self.sprite, surface, position, direction)
