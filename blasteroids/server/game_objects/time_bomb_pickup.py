from blasteroids.server.game_objects.power_up import PowerUp


class TimeBombPickup(PowerUp):
    def __init__(self, id, position, lifespan, **kwargs):
        super(TimeBombPickup, self).__init__(id, "time_bomb_pickup", position, lifespan)

    def apply_power_up_to(self, ship, world):
        world.create_sound_effect('time_bomb_pickup', self.position)
        ship.set_active_weapon('time_bomb')
