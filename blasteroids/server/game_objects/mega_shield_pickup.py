from blasteroids.server.game_objects.power_up import PowerUp


class MegaShieldPickup(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(MegaShieldPickup, self).__init__(id, "mega_shield_pickup", position, lifespan)

    def apply_power_up_to(self, ship):
        ship.shield_full()
