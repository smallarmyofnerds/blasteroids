from blasteroids.lib.constants import ROCKET_WEAPON_ID
from blasteroids.server.game_objects.pickup import Pickup


class RocketPickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(RocketPickup, self).__init__(id, "rocket_pickup", position, lifespan)

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect('rocket_pickup', self.position)
        ship.set_active_weapon(ROCKET_WEAPON_ID)
