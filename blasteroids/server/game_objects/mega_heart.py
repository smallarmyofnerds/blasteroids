from blasteroids.server.game_objects.power_up import PowerUp


class MegaHeart(PowerUp):
    def __init__(self, id, position, **kwargs):
        super(MegaHeart, self).__init__(id, "mega_heart", position)

    def apply_power_up_to(self, ship):
        ship.heal_full()