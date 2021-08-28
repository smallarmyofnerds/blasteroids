from .server_object import ServerObject


class ServerProjectile(ServerObject):
    def __init__(self, id, position, orientation, name):
        super(ServerProjectile, self).__init__('PROJECTILE', id, position, orientation, name)

    def from_projectile(projectile):
        return ServerProjectile(projectile.id, projectile.position, projectile.orientation, projectile.name)
