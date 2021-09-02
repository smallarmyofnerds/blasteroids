from blasteroids.server.game_objects.power_up import PowerUp


class HeartPickup(PowerUp):
    def __init__(self, id, position, amount, lifespan, **kwargs):
        super(HeartPickup, self).__init__(id, "heart_pickup", position, lifespan)
        self.amount = amount

    def apply_power_up_to(self, ship, world):
        world.create_instant_effect('healing_pickup', self.position)
        ship.heal_by(self.amount)
