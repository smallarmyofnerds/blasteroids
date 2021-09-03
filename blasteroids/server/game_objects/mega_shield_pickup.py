from blasteroids.server.game_objects.pickup import Pickup


class MegaShieldPickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(MegaShieldPickup, self).__init__(id, "mega_shield_pickup", position, lifespan)

    def apply_power_up_to(self, ship, world):
        world.create_sound_effect('shielding_pickup', self.position)
        world.create_sound_effect('mega_pickup', self.position)
        ship.shield_full()
