from blasteroids.server.game_objects.power_up import PowerUp


class Heart(PowerUp):
    def __init__(self, id, position, amount, **kwargs):
        super(Heart, self).__init__(id, "heart", position)
        self.amount = amount

    def apply_power_up_to(self, ship):
        ship.heal_by(self.amount)
