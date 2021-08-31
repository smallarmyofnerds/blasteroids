from blasteroids.server.game_objects.power_up import PowerUp


class SpreadFire(PowerUp):
    def __init__(self, id, position, **kwargs):
        super(SpreadFire, self).__init__(id, "spread_fire", position)

    def apply_power_up_to(self, ship):
        ship.set_active_weapon('spread_fire')
