from blasteroids.server.game_objects.power_up import PowerUp


class ProximityMine(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(ProximityMine, self).__init__(id, "proximity_mine", position, lifespan)
