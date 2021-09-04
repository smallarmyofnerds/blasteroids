from blasteroids.lib.constants import RAPID_FIRE_WEAPON_ID
from blasteroids.server.game_objects.pickup import Pickup


class RapidFirePickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(RapidFirePickup, self).__init__(id, "rapid_fire_pickup", position, lifespan)

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect('rapid_fire_pickup', self.position)
        ship.set_active_weapon(RAPID_FIRE_WEAPON_ID)
