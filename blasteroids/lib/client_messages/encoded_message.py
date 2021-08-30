import struct
from pygame.math import Vector2
from blasteroids.lib.server_world import ServerShip, ServerObstacle, ServerProjectile, ServerPowerUp


class EncodedMessage:
    def __init__(self, msg):
        self.msg = msg

    def push(self, b):
        self.msg = self.msg + b

    def pop(self, length):
        b = self.msg[:length]
        self.msg = self.msg[length:]
        return b

    def pop_raw_string(self, length):
        return str(self.pop(length), 'utf-8')

    def pop_boolean(self):
        value = int.from_bytes(self.pop(1), 'little')
        return True if value == 1 else False

    def pop_short(self):
        return int.from_bytes(self.pop(2), 'little')

    def pop_string(self):
        length = self.pop_short()
        return self.pop_raw_string(length)

    def pop_vector(self):
        x, y = struct.unpack('ff', self.pop(8))
        return Vector2(x, y)

    def pop_object(self):
        type = self.pop_string()
        id = self.pop_short()
        position = self.pop_vector()
        orientation = self.pop_vector()
        name = self.pop_string()
        if type == 'SHIP':
            return ServerShip(id, position, orientation, name)
        elif type == 'PROJECTILE':
            return ServerProjectile(id, position, orientation, name)
        elif type == 'OBSTACLE':
            return ServerObstacle(id, position, orientation, name)
        elif type == 'POWERUP':
            return ServerPowerUp(id, position, orientation, name)
        else:
            raise Exception(f'Unrecognized object type {type}')

    def pop_string_array(self):
        length = self.pop_short()
        a = []
        for i in range(length):
            a.append(self.pop_string())
        return a
