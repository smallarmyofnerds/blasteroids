from .destroyable_game_object import DestroyableGameObject


class Projectile(DestroyableGameObject):
    def __init__(self, id, name, position, orientation, velocity, damage):
        super(Projectile, self).__init__(id, name, position, orientation, velocity, 0, 0, None, damage, 0)
    
    def destroy(self, world):
        return world.remove_projectile(self)
