from blasteroids.lib.constants import MEGA_PICKUP_SOUND_ID, MEGA_SHIELD_PICKUP_ID, SHIELDING_PICKUP_SOUND_ID
from blasteroids.server.game_objects.pickup import Pickup


class MegaShieldPickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(MegaShieldPickup, self).__init__(id, position, MEGA_SHIELD_PICKUP_ID, lifespan)

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect(SHIELDING_PICKUP_SOUND_ID, self.position)
        world.create_sound_effect(MEGA_PICKUP_SOUND_ID, self.position)
        ship.shield_full()
