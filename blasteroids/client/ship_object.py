from .game_object import GameObject


class ShipObject(GameObject):
    def __init__(self, server_object, sprite_library):
        super(ShipObject, self).__init__(server_object)
        self.static_sprite = sprite_library.get(f'{server_object.name}_static')
        # self.flying_sprites = sprite_library.get(f'{server_object.name}_flying')
        # self.exploding_sprites = sprite_library.get(f'{server_object.name}_exploding')

    def update(self, raw_ship):
        super(ShipObject, self)._update(raw_ship.position, raw_ship.orientation)

    def draw(self, screen):
        screen.draw_sprite(self.static_sprite, self.position, self.orientation)

    def destroy(self):
        print('Oh noes')
