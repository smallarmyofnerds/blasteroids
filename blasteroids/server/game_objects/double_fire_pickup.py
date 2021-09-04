from blasteroids.lib.constants import DOUBLE_FIRE_PICKUP_ID, DOUBLE_FIRE_PICKUP_SOUND_ID, DOUBLE_FIRE_WEAPON_ID
from blasteroids.server.game_objects.pickup import Pickup


class DoubleFirePickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(DoubleFirePickup, self).__init__(id, position, DOUBLE_FIRE_PICKUP_ID, lifespan)

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect(DOUBLE_FIRE_PICKUP_SOUND_ID, self.position)
        ship.set_active_weapon(DOUBLE_FIRE_WEAPON_ID)
