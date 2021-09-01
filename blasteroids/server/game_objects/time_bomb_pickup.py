from blasteroids.server.game_objects.power_up import PowerUp


class TimeBombPickup(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(TimeBombPickup, self).__init__(id, "time_bomb_pickup", position, lifespan)
