from .server_object import ServerObject


class ServerPowerUp(ServerObject):
    def __init__(self, id, position, orientation, name):
        super(ServerPowerUp, self).__init__('POWERUP', id, position, orientation, name)

    def from_power_up(power_up):
        return ServerPowerUp(power_up.id, power_up.position, power_up.orientation, power_up.name)
