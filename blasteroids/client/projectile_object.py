from .game_object import GameObject


class ProjectileObject(GameObject):
    def __init__(self, server_object, sprite_library):
        super(ProjectileObject, self).__init__(server_object)
        self.sprite = sprite_library.get(server_object.name)

    def draw(self, screen):
        screen.draw_sprite(self.sprite, self.position, self.orientation)

    def update(self, raw_obstacle):
        super(ProjectileObject, self)._update(raw_obstacle.position, raw_obstacle.orientation)

    def on_create(self, sound_library):
        if self.name == 'laser':
            sound_library.get_sound('laser').play()
