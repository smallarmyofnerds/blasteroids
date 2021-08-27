import pygame
from game_object import GameObject


class ObstacleObject(GameObject):
    def __init__(self, server_object, sprite_library):
        super(ObstacleObject, self).__init__(server_object)
        self.sprite = sprite_library.get('player_1_static')

    def draw(self, screen):
        pygame.draw.rect(screen.surface, (0, 255, 0), (self.position.x, self.position.y, 100, 100))

    def update(self, raw_obstacle):
        super(ObstacleObject, self)._update(raw_obstacle.position, raw_obstacle.orientation)

    def destroy(self):
        pass