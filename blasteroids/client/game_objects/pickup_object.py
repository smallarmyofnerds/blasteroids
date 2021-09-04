from pygame import Vector2
from .game_object import GameObject


class PickupObject(GameObject):
    def __init__(self, server_pickup, sprite_library):
        super(PickupObject, self).__init__(server_pickup)
        self.sprite = sprite_library.pickup_sprites[server_pickup.pickup_id]

    def draw(self, screen, my_position):
        screen.draw_sprite(self.sprite, self.position, Vector2(0, 1))

    def update(self, server_pickup):
        super(PickupObject, self).update(server_pickup)
