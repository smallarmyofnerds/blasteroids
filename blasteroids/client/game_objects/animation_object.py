from pygame import Vector2
from .game_object import GameObject


class AnimationObject(GameObject):
    def __init__(self, server_object, sprite_library):
        super(AnimationObject, self).__init__(server_object)
        self.animation = sprite_library.animations[server_object.name]

    def draw(self, screen, my_position):
        self.animation.draw(screen, self.position, Vector2(0, 1))

    def update(self, raw_animation):
        super(AnimationObject, self)._update(raw_animation.position, raw_animation.orientation)
