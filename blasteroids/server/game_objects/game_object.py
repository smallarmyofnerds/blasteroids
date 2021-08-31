import pygame


class GameObject:
    MIN_VELOCITY = 0.5
    MIN_ROTATIONAL_VELOCITY = 0.001
    MAX_ROTATIONAL_VELOCITY = 190

    def __init__(self, id, name, position, orientation, velocity, rotational_velocity, rotational_velocity_friction):
        self.id = id
        self.name = name
        self.position = position
        self.orientation = orientation
        self.velocity = velocity
        self.acceleration = pygame.Vector2(0, 0)
        self.rotational_velocity = rotational_velocity
        self.rotational_velocity_friction = rotational_velocity_friction
        self.rotational_acceleration = 0  # dpsps

    def update(self, world, delta_time):
        self._before_update(world, delta_time)

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
        if self.velocity.length() < GameObject.MIN_VELOCITY:
            self.velocity = pygame.Vector2(0, 0)
        # if self.velocity.length() > GameObject.MAX_VELOCITY:
        #     self.velocity = self.velocity.normalize() * GameObject.MAX_VELOCITY

        # move object
        self.position = self.position + delta_time * self.velocity

        self._after_update(world, delta_time)

    def _before_update(self, world, delta_time):
        pass

    def _after_update(self, world, delta_time):
        if not world.is_in_bounds(self.position, 500):
            self.destroy()
