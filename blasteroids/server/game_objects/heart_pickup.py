from blasteroids.lib.constants import HEALING_PICKUP_SOUND_ID, HEALTH_PICKUP_ID
from blasteroids.server.game_objects.pickup import Pickup


class HeartPickup(Pickup):
    def __init__(self, id, position, amount, lifespan, **kwargs):
        super(HeartPickup, self).__init__(id, position, HEALTH_PICKUP_ID, lifespan)
        self.amount = amount

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect(HEALING_PICKUP_SOUND_ID, self.position)
        ship.heal_by(self.amount)
