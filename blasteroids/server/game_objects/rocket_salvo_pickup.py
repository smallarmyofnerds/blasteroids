from blasteroids.server.game_objects.power_up import PowerUp


class RocketSalvoPickup(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(RocketSalvoPickup, self).__init__(id, "rocket_salvo_pickup", position, lifespan)

    def apply_power_up_to(self, ship, world):
        world.create_sound_effect('rocket_salvo_pickup', self.position)
        ship.set_active_weapon('rocket_salvo')