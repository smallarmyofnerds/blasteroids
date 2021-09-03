from blasteroids.server.game_objects.pickup import Pickup


class DoubleFirePickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(DoubleFirePickup, self).__init__(id, "double_fire_pickup", position, lifespan)

    def apply_pickup_to(self, ship, world):
        world.create_sound_effect('double_fire_pickup', self.position)
        ship.set_active_weapon('double_fire')
