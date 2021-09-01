from blasteroids.server.game_objects.power_up import PowerUp


class RocketSalvoPickup(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(RocketSalvoPickup, self).__init__(id, "rocket_salvo_pickup", position, lifespan)
