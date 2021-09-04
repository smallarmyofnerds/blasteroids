import pygame


class GameObject:
    MIN_VELOCITY = 0.5
    MIN_ROTATIONAL_VELOCITY = 0.001
    MAX_ROTATIONAL_VELOCITY = 190

    def __init__(self, id, position, orientation, velocity, **kwargs):
        self.id = id

        self.position = position

        self.orientation = orientation

        self.velocity = velocity
        self.max_speed = kwargs.get('max_speed', 1000)
        self.acceleration = pygame.Vector2(0, 0)

        self.rotational_velocity = kwargs.get('rotational_velocity', 0)
        self.rotational_acceleration = 0  # dpsps

        self.destroyed = False

    def update(self, world, delta_time):
        self._set_accelerations(world)

        # update rotational velocity from rotational acceleration
        self.rotational_velocity = self.rotational_velocity + self.rotational_acceleration
        if abs(self.rotational_velocity) < GameObject.MIN_ROTATIONAL_VELOCITY:
            self.rotational_velocity = 0
        self.rotational_velocity = max(-1 * GameObject.MAX_ROTATIONAL_VELOCITY, min(GameObject.MAX_ROTATIONAL_VELOCITY, self.rotational_velocity))

        # rotate orientation based on rotational velocity
        self.orientation = self.orientation.rotate(-1 * delta_time * self.rotational_velocity)

        # update velocity from acceleration
        self.velocity = self.velocity + 0.5 * self.acceleration
        if self.velocity.length() < GameObject.MIN_VELOCITY:
            self.velocity = pygame.Vector2(0, 0)
        # if self.velocity.length() > GameObject.MAX_VELOCITY:
        #     self.velocity = self.velocity.normalize() * GameObject.MAX_VELOCITY

        # move object
        self.position = self.position + delta_time * self.velocity

    def destroy(self):
        self.destroyed = True

    def on_removed(self, world):
        pass

    def _set_accelerations(self, world):
        pass

    def is_in_bounds(self, world):
        return world.is_object_in_bounds(self.position)
