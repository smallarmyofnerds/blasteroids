from .game_object import GameObject


class PowerUpObject(GameObject):
    def __init__(self, server_object, sprite_library):
        super(PowerUpObject, self).__init__(server_object)
        self.sprite = sprite_library.get(server_object.name)

    def draw(self, screen, my_position):
        screen.draw_sprite(self.sprite, self.position, self.orientation)

    def update(self, raw_obstacle):
        super(PowerUpObject, self)._update(raw_obstacle.position, raw_obstacle.orientation)
