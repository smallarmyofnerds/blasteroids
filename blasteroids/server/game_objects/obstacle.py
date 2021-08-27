from .destroyable_game_object import DestroyableGameObject


class Obstacle(DestroyableGameObject):
    def __init__(self, position, orientation, velocity, rotational_velocity, damage, health):
        super(Obstacle, self).__init__(position, orientation, velocity, rotational_velocity, damage, health)
