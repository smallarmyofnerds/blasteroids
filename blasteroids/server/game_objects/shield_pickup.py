from blasteroids.server.game_objects.pickup import Pickup


class ShieldPickup(Pickup):
    def __init__(self, id, position, amount, lifespan, **kwargs):
        super(ShieldPickup, self).__init__(id, "shield_pickup", position, lifespan)
        self.amount = amount

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect('shielding_pickup', self.position)
        ship.shield_by(self.amount)
