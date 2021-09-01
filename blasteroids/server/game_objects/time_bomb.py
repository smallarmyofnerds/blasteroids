from blasteroids.server.game_objects.power_up import PowerUp


class TimeBomb(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(TimeBomb, self).__init__(id, "time_bomb", position, lifespan)
