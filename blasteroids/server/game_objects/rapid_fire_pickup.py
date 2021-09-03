from blasteroids.server.game_objects.power_up import PowerUp


class RapidFirePickup(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(RapidFirePickup, self).__init__(id, "rapid_fire_pickup", position, lifespan)

    def apply_power_up_to(self, ship, world):
        world.create_sound_effect('rapid_fire_pickup', self.position)
        ship.set_active_weapon('rapid_fire')
