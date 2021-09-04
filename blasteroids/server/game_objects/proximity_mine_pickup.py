from blasteroids.lib.constants import PROXIMITY_MINE_PICKUP_ID, PROXIMITY_MINE_PICKUP_SOUND_ID, PROXIMITY_MINE_WEAPON_ID
from blasteroids.server.game_objects.pickup import Pickup


class ProximityMinePickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(ProximityMinePickup, self).__init__(id, position, PROXIMITY_MINE_PICKUP_ID, lifespan)

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect(PROXIMITY_MINE_PICKUP_SOUND_ID, self.position)
        ship.set_active_weapon(PROXIMITY_MINE_WEAPON_ID)
