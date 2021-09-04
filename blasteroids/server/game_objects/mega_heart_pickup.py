from blasteroids.lib.constants import HEALING_PICKUP_SOUND_ID, MEGA_HEALTH_PICKUP_ID, MEGA_PICKUP_SOUND_ID
from blasteroids.server.game_objects.pickup import Pickup


class MegaHeartPickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(MegaHeartPickup, self).__init__(id, position, MEGA_HEALTH_PICKUP_ID, lifespan)

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect(HEALING_PICKUP_SOUND_ID, self.position)
        world.create_sound_effect(MEGA_PICKUP_SOUND_ID, self.position)
        ship.heal_full()
