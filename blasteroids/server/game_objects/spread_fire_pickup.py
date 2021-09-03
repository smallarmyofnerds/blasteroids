from blasteroids.server.game_objects.power_up import PowerUp


class SpreadFirePickup(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(SpreadFirePickup, self).__init__(id, "spread_fire_pickup", position, lifespan)

    def apply_power_up_to(self, ship, world):
        world.create_sound_effect('spread_fire_pickup', self.position)
        ship.set_active_weapon('spread_fire')
