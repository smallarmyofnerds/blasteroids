from blasteroids.server.game_objects.power_up import PowerUp


class MegaShield(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(MegaShield, self).__init__(id, "mega_shield", position, lifespan)

    def apply_power_up_to(self, ship):
        ship.shield_full()
