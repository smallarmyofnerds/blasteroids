import pygame


class GameObject:
    MIN_VELOCITY = 0.5
    MIN_ROTATIONAL_VELOCITY = 0.1

    def __init__(self, id, position, orientation, velocity, rotational_velocity):
        self.id = id
        self.position = position
        self.orientation = orientation
        self.velocity = velocity
        self.acceleration = pygame.Vector2(0, 0)
        self.rotational_velocity = rotational_velocity
        self.rotational_acceleration = 0  # dpsps

    def zero_accelerations(self):
        self.acceleration = pygame.Vector2(0, 0)
        self.rotational_acceleration = 0

    def set_rotating_left(self, rotational_acceleration_rate):
        self.rotational_acceleration = -1 * rotational_acceleration_rate

    def set_rotating_right(self, rotational_acceleration_rate):
        self.rotational_acceleration = rotational_acceleration_rate

    def set_accelerating(self, acceleration_rate):
        self.acceleration = self.orientation.normalize() * acceleration_rate

    def update(self):
        # update rotational velocity from rotational acceleration
        self.rotational_velocity = self.rotational_velocity + self.rotational_acceleration
        if abs(self.rotational_velocity) < GameObject.MIN_ROTATIONAL_VELOCITY:
            self.rotational_velocity = 0

        # rotate orientation based on rotational velocity
        self.orientation = self.orientation.rotate(-1 * self.rotational_velocity)

        # update velocity from acceleration
        self.velocity = self.velocity + self.acceleration
        if abs(self.velocity.length()) < GameObject.MIN_VELOCITY:
            self.velocity = pygame.Vector2(0, 0)

        # move object
        self.position = self.position + self.velocity
