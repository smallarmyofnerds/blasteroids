from blasteroids.server.game_objects.pickup import Pickup


class MegaHeartPickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(MegaHeartPickup, self).__init__(id, "mega_heart_pickup", position, lifespan)

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect('healing_pickup', self.position)
        world.create_sound_effect('mega_pickup', self.position)
        ship.heal_full()
