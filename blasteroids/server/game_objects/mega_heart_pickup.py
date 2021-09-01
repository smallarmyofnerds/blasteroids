from blasteroids.server.game_objects.power_up import PowerUp


class MegaHeartPickup(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(MegaHeartPickup, self).__init__(id, "mega_heart_pickup", position, lifespan)

    def apply_power_up_to(self, ship):
        ship.heal_full()
