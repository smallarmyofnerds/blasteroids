from .game_object import GameObject


class MyShipObject(GameObject):
    def __init__(self, server_object, sprite_library, is_engine_on):
        super(MyShipObject, self).__init__(server_object)
        self.static_sprite = sprite_library.get(f'{server_object.name}_static')
        self.exhaust_animation = sprite_library.animations['exhaust']
        self.is_engine_on = is_engine_on

    def update(self, raw_ship, is_engine_on):
        super(MyShipObject, self)._update(raw_ship.position, raw_ship.orientation)
        self.is_engine_on = is_engine_on

    def draw(self, screen, my_position):
        screen.draw_sprite(self.static_sprite, self.position, self.orientation)
        if self.is_engine_on:
            self.exhaust_animation.draw(screen, self.position - self.orientation * 30, self.orientation)
