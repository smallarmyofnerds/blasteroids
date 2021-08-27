from .server_object import ServerObject


class ServerObstacle(ServerObject):
    def __init__(self, id, position, orientation, name):
        super(ServerObstacle, self).__init__('OBSTACLE', id, position, orientation, name)
