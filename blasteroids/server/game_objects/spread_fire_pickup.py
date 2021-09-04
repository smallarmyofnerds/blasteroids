from blasteroids.lib.constants import SPREAD_FIRE_PICKUP_ID, SPREAD_FIRE_PICKUP_SOUND_ID, SPREAD_FIRE_WEAPON_ID
from blasteroids.server.game_objects.pickup import Pickup


class SpreadFirePickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(SpreadFirePickup, self).__init__(id, position, SPREAD_FIRE_PICKUP_ID, lifespan)

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect(SPREAD_FIRE_PICKUP_SOUND_ID, self.position)
        ship.set_active_weapon(SPREAD_FIRE_WEAPON_ID)
