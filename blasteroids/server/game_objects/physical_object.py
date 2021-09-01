from .game_object import GameObject


class PhysicalGameObject(GameObject):
    def __init__(self, id, name, position, orientation, velocity, collision_radius, damage, max_health, **kwargs):
        super(PhysicalGameObject, self).__init__(id, name, position, orientation, velocity, **kwargs)

        self.damage = damage

        self.max_health = max_health
        self.health = max_health

        self.collision_radius = collision_radius

    def take_damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.destroy()

    def apply_damage_to(self, other):
        other.take_damage(self.damage)

    def collides_with(self, other):
        vector_between = self.position - other.position
        distance_between = vector_between.length()
        min_distance = self.collision_radius + other.collision_radius
        return distance_between <= min_distance
