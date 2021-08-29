import pygame


class GameObject:
    MIN_VELOCITY = 0.5
    MIN_ROTATIONAL_VELOCITY = 0.001
    MAX_ROTATIONAL_VELOCITY = 190

    def __init__(self, id, name, position, orientation, velocity, rotational_velocity, rotational_velocity_friction, collision_mask):
        self.id = id
        self.name = name
        self.position = position
        self.orientation = orientation
        self.velocity = velocity
        self.acceleration = pygame.Vector2(0, 0)
        self.rotational_velocity = rotational_velocity
        self.rotational_velocity_friction = rotational_velocity_friction
        self.rotational_acceleration = 0  # dpsps
        self.collision_mask = collision_mask

    def update(self, world, delta_time):
        # update rotational velocity from rotational acceleration
        rotational_friction = -1 * self.rotational_velocity_friction * self.rotational_velocity
        self.rotational_velocity = self.rotational_velocity + rotational_friction + self.rotational_acceleration
        if abs(self.rotational_velocity) < GameObject.MIN_ROTATIONAL_VELOCITY:
            self.rotational_velocity = 0
        self.rotational_velocity = max(-1 * GameObject.MAX_ROTATIONAL_VELOCITY, min(GameObject.MAX_ROTATIONAL_VELOCITY, self.rotational_velocity))

        # rotate orientation based on rotational velocity
        self.orientation = self.orientation.rotate(-1 * delta_time * self.rotational_velocity)

        # update velocity from acceleration
        self.velocity = self.velocity + self.acceleration
        if abs(self.velocity.length()) < GameObject.MIN_VELOCITY:
            self.velocity = pygame.Vector2(0, 0)

        # move object
        self.position = self.position + delta_time * self.velocity

    def collides_with(self, other):
        # if pygame.sprite.spritecollide(self.collision_mask, [other.collision_mask], False, pygame.sprite.collide_mask):
        #     return True
        return False
