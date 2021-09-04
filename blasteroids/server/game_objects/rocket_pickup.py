from blasteroids.lib.constants import ROCKET_PICKUP_ID, ROCKET_PICKUP_SOUND_ID, ROCKET_WEAPON_ID
from blasteroids.server.game_objects.pickup import Pickup


class RocketPickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(RocketPickup, self).__init__(id, position, ROCKET_PICKUP_ID, lifespan)

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect(ROCKET_PICKUP_SOUND_ID, self.position)
        ship.set_active_weapon(ROCKET_WEAPON_ID)
