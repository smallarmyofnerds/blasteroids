from .server_object import ServerObject


class ServerPickup(ServerObject):
    def __init__(self, id, position, orientation, name):
        super(ServerPickup, self).__init__('PICKUP', id, position, orientation, name)

    def from_power_up(pickup):
        return ServerPickup(pickup.id, pickup.position, pickup.orientation, pickup.name)
