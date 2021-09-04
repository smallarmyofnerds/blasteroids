from blasteroids.lib.constants import RAPID_FIRE_PICKUP_ID, RAPID_FIRE_PICKUP_SOUND_ID, RAPID_FIRE_WEAPON_ID
from blasteroids.server.game_objects.pickup import Pickup


class RapidFirePickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(RapidFirePickup, self).__init__(id, position, RAPID_FIRE_PICKUP_ID, lifespan)

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect(RAPID_FIRE_PICKUP_SOUND_ID, self.position)
        ship.set_active_weapon(RAPID_FIRE_WEAPON_ID)
