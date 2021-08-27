from .game_object import GameObject


class ObstacleObject(GameObject):
    def __init__(self, server_object, sprite_library):
        super(ObstacleObject, self).__init__(server_object)
        self.sprite = sprite_library.get('player_1_static')

    def draw(self, screen):
        screen.draw_sprite(self.sprite, self.position, self.orientation)

    def update(self, raw_obstacle):
        super(ObstacleObject, self)._update(raw_obstacle.position, raw_obstacle.orientation)

    def destroy(self):
        pass