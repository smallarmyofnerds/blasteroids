from .destroyable_game_object import DestroyableGameObject


class Obstacle(DestroyableGameObject):
    def __init__(self, id, name, position, orientation, velocity, rotational_velocity, rotational_velocity_friction, collision_radius, damage, health):
        super(Obstacle, self).__init__(id, name, position, orientation, velocity, rotational_velocity, rotational_velocity_friction, collision_radius, damage, health)

    def destroy(self, world):
        world.remove_obstacle(self)
