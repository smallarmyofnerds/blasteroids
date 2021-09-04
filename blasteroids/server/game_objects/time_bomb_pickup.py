from blasteroids.lib.constants import TIME_BOMB_PICKUP_ID, TIME_BOMB_PICKUP_SOUND_ID, TIME_BOMB_WEAPON_ID
from blasteroids.server.game_objects.pickup import Pickup


class TimeBombPickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(TimeBombPickup, self).__init__(id, position, TIME_BOMB_PICKUP_ID, lifespan)

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect(TIME_BOMB_PICKUP_SOUND_ID, self.position)
        ship.set_active_weapon(TIME_BOMB_WEAPON_ID)
