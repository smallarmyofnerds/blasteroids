from blasteroids.server.game_objects.power_up import PowerUp


class DoubleFirePickup(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(DoubleFirePickup, self).__init__(id, "double_fire_pickup", position, lifespan)

    def apply_power_up_to(self, ship, world):
        world.create_instant_effect('double_fire_pickup', self.position)
        ship.set_active_weapon('double_fire')
