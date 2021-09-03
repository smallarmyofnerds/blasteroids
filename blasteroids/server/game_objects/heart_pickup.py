from blasteroids.server.game_objects.pickup import Pickup


class HeartPickup(Pickup):
    def __init__(self, id, position, amount, lifespan, **kwargs):
        super(HeartPickup, self).__init__(id, "heart_pickup", position, lifespan)
        self.amount = amount

    def apply_power_up_to(self, ship, world):
        world.create_sound_effect('healing_pickup', self.position)
        ship.heal_by(self.amount)
