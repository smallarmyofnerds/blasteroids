from .destroyable_game_object import DestroyableGameObject


class Projectile(DestroyableGameObject):
    def __init__(self, id, name, position, orientation, velocity, collision_radius, damage):
        super(Projectile, self).__init__(id, name, position, orientation, velocity, 0, 0, collision_radius, damage, 0)

    def destroy(self, world):
        world.remove_projectile(self)
