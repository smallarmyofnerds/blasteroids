from server_object import ServerObject


class ServerShip(ServerObject):
    def __init__(self, id, position, orientation, name):
        super(ServerShip, self).__init__('SHIP', id, position, orientation, name)