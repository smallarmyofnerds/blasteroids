from blasteroids.server.game_objects.power_up import PowerUp


class Rocket(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(Rocket, self).__init__(id, "rocket", position, lifespan)
