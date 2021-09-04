from .orientable_game_object import OrientableGameObject


class AsteroidObject(OrientableGameObject):
    def __init__(self, server_asteroid, sprite_library):
        super(AsteroidObject, self).__init__(server_asteroid)
        self.sprite = sprite_library.asteroid_sprites[server_asteroid.level]

    def draw(self, screen, my_position):
        screen.draw_sprite(self.sprite, self.position, self.orientation)

    def update(self, server_asteroid):
        super(AsteroidObject, self).update(server_asteroid)
