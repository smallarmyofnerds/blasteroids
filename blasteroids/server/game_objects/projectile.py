from .physical_object import PhysicalGameObject


class Projectile(PhysicalGameObject):
    def __init__(self, id, position, orientation, velocity, collision_radius, damage, projectile_id, owner):
        super(Projectile, self).__init__(id, position, orientation, velocity, collision_radius, damage, 0)
        self.projectile_id = projectile_id
        self.owner = owner

    def collides_with(self, other):
        if other == self.owner:
            return False
        return super(Projectile, self).collides_with(other)

    def can_hit_projectile(self, other):
        return False
