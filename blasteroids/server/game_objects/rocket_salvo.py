from blasteroids.server.game_objects.power_up import PowerUp


class RocketSalvo(PowerUp):
    def __init__(self, id, position, **kwargs):
        super(RocketSalvo, self).__init__(id, "rocket_salvo", position)
