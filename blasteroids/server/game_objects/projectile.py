from .destroyable_game_object import DestroyableGameObject


class Projectile(DestroyableGameObject):
    def __init__(self, owner, id, name, position, orientation, velocity, collision_radius, damage):
        super(Projectile, self).__init__(id, name, position, orientation, velocity, 0, 0, collision_radius, damage, 0)
        self.owner = owner

    def collides_with(self, other):
        if other == self.owner:
            return False
        return super(Projectile, self).collides_with(other)
