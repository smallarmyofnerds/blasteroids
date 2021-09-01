from blasteroids.server.game_objects.power_up import PowerUp


class RocketPickup(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(RocketPickup, self).__init__(id, "rocket_pickup", position, lifespan)
