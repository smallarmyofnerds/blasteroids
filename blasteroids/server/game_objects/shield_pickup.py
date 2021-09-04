from blasteroids.lib.constants import SHIELDING_PICKUP_SOUND_ID, SHIELD_PICKUP_ID
from blasteroids.server.game_objects.pickup import Pickup


class ShieldPickup(Pickup):
    def __init__(self, id, position, amount, lifespan, **kwargs):
        super(ShieldPickup, self).__init__(id, position, SHIELD_PICKUP_ID, lifespan)
        self.amount = amount

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect(SHIELDING_PICKUP_SOUND_ID, self.position)
        ship.shield_by(self.amount)
