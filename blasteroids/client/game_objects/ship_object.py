from .game_object import GameObject


class ShipObject(GameObject):
    def __init__(self, server_object, sprite_library):
        super(ShipObject, self).__init__(server_object)
        self.static_sprite = sprite_library.get(f'{server_object.name}_static')

    def update(self, raw_ship):
        super(ShipObject, self)._update(raw_ship.position, raw_ship.orientation)

    def draw(self, screen, my_position):
        screen.draw_sprite(self.static_sprite, self.position, self.orientation)
