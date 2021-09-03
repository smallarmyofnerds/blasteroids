from blasteroids.server.game_objects.power_up import PowerUp


class MegaHeartPickup(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(MegaHeartPickup, self).__init__(id, "mega_heart_pickup", position, lifespan)

    def apply_power_up_to(self, ship, world):
        world.create_sound_effect('healing_pickup', self.position)
        world.create_sound_effect('mega_pickup', self.position)
        ship.heal_full()
