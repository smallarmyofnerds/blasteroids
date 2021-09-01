from blasteroids.server.game_objects.power_up import PowerUp


class Shield(PowerUp):
    def __init__(self, id, position, amount, lifespan, **kwargs):
        super(Shield, self).__init__(id, "shield", position, lifespan)
        self.amount = amount

    def apply_power_up_to(self, ship):
        ship.shield_by(self.amount)
