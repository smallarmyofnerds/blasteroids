from .physical_object import PhysicalGameObject


class Obstacle(PhysicalGameObject):
    def __init__(self, id, name, position, orientation, velocity, collision_radius, damage, health, **kwargs):
        super(Obstacle, self).__init__(id, name, position, orientation, velocity, collision_radius, damage, health, **kwargs)
