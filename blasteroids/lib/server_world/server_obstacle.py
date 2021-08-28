from .server_object import ServerObject


class ServerObstacle(ServerObject):
    def __init__(self, id, position, orientation, name):
        super(ServerObstacle, self).__init__('OBSTACLE', id, position, orientation, name)

    def from_obstacle(self, obstacle):
        return ServerObstacle(obstacle.id, obstacle.position, obstacle.orientation, obstacle.name)
