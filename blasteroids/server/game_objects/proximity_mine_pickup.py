from blasteroids.server.game_objects.power_up import PowerUp


class ProximityMinePickup(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(ProximityMinePickup, self).__init__(id, "proximity_mine_pickup", position, lifespan)
