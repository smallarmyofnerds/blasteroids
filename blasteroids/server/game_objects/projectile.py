from .physical_object import PhysicalGameObject


class Projectile(PhysicalGameObject):
    def __init__(self, owner, id, name, position, orientation, velocity, collision_radius, damage):
        super(Projectile, self).__init__(id, name, position, orientation, velocity, collision_radius, damage, 0)
        self.owner = owner

    def collides_with(self, other):
        if other == self.owner:
            return False
        return super(Projectile, self).collides_with(other)

    def can_hit_projectile(self, other):
        return False
