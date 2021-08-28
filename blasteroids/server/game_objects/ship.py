import pygame
from .destroyable_game_object import DestroyableGameObject


class Ship(DestroyableGameObject):
    def __init__(self, sprite_library, id, position, orientation, name):
        img = sprite_library.get(f'{name}_static')
        collision_mask = pygame.mask.from_surface(img)
        super(Ship, self).__init__(id, position, orientation, pygame.Vector2(0, 0), 0, collision_mask, 100, 100)
        self.name = name
        self.player = None

    def destroy(self, remove_object, world):
        super(Ship, self).destroy(remove_object, world)
        world.remove_player(self.player)
