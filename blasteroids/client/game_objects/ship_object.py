from blasteroids.lib.constants import SHIP_EXHAUST_ANIMATION_ID
from .orientable_game_object import OrientableGameObject


class ShipObject(OrientableGameObject):
    def __init__(self, server_ship, sprite_library):
        super(ShipObject, self).__init__(server_ship)
        self.health = server_ship.health
        self.shield = server_ship.shield
        self.active_weapon_id = server_ship.active_weapon_id
        self.is_engine_on = server_ship.is_engine_on

        self.sprite = sprite_library.ship_sprites[server_ship.ship_id]
        self.exhaust_animation = sprite_library.animations[SHIP_EXHAUST_ANIMATION_ID]

    def update(self, server_ship):
        super(ShipObject, self).update(server_ship)
        self.health = server_ship.health
        self.shield = server_ship.shield
        self.active_weapon_id = server_ship.active_weapon_id
        self.is_engine_on = server_ship.is_engine_on

    def draw(self, screen, my_position):
        screen.draw_sprite(self.sprite, self.position, self.orientation)
        if self.is_engine_on:
            self.exhaust_animation.draw(screen, self.position - self.orientation * 30, self.orientation)
