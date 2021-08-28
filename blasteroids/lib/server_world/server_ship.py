from .server_object import ServerObject


class ServerShip(ServerObject):
    def __init__(self, id, position, orientation, name):
        super(ServerShip, self).__init__('SHIP', id, position, orientation, name)

    def from_ship(ship):
        return ServerShip(ship.id, ship.position, ship.orientation, ship.name)
