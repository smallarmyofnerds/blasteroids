from blasteroids.server.game_objects.pickup import Pickup


class ProximityMinePickup(Pickup):
    def __init__(self, id, position, lifespan, **kwargs):
        super(ProximityMinePickup, self).__init__(id, "proximity_mine_pickup", position, lifespan)

    def apply_power_up_to(self, ship, world):
        world.create_sound_effect('proximity_mine_pickup', self.position)
        ship.set_active_weapon('proximity_mine')
