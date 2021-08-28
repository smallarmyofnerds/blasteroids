from .game_object import GameObject


class DestroyableGameObject(GameObject):
    def __init__(self, id, position, orientation, velocity, rotational_velocity, damage, health):
        super(DestroyableGameObject, self).__init__(id, position, orientation, velocity, rotational_velocity)
        self.damage = damage
        self.health = health

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def apply_damage_to(self, other):
        other.take_damage(self.damage)

    def destroy(self, remove_object, world):
        remove_object(self)
