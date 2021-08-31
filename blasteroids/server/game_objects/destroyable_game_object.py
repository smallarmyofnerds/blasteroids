from .game_object import GameObject


class DestroyableGameObject(GameObject):
    def __init__(self, id, name, position, orientation, velocity, rotational_velocity, rotational_velocity_friction, collision_radius, damage, health):
        super(DestroyableGameObject, self).__init__(id, name, position, orientation, velocity, rotational_velocity, rotational_velocity_friction)
        self.damage = damage
        self.health = health
        self.destroyed = False
        self.collision_radius = collision_radius

    def take_damage(self, damage):
        self.health -= damage

        if self.health <= 0:
            self.destroy()

    def apply_damage_to(self, other):
        other.take_damage(self.damage)

    def destroy(self):
        self.destroyed = True

    def on_removed(self, world):
        pass

    def collides_with(self, other):
        vector_between = self.position - other.position
        distance_between = vector_between.length()
        min_distance = self.collision_radius + other.collision_radius
        return distance_between <= min_distance
