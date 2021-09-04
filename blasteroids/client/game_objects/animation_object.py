from .orientable_game_object import OrientableGameObject


class AnimationObject(OrientableGameObject):
    def __init__(self, server_animation, sprite_library):
        super(AnimationObject, self).__init__(server_animation)
        self.animation = sprite_library.animations[server_animation.animation_id]

    def draw(self, screen, my_position):
        self.animation.draw(screen, self.position, self.orientation)

    def update(self, server_animation):
        super(AnimationObject, self).update(server_animation)
