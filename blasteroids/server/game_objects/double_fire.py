from blasteroids.server.game_objects.power_up import PowerUp


class DoubleFire(PowerUp):
    def __init__(self, id, position, **kwargs):
        super(DoubleFire, self).__init__(id, "double_fire", position)
