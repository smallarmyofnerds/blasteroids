from blasteroids.server.game_objects.power_up import PowerUp


class RapidFire(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(RapidFire, self).__init__(id, "rapid_fire", position, lifespan)

    def apply_power_up_to(self, ship):
        ship.set_active_weapon('rapid_fire')
