from pygame import Vector2
from server_ship import ServerShip
from server_obstacle import ServerObstacle


class ServerWorld:
    def __init__(self) -> None:
        self.my_ship = ServerShip(12, Vector2(100, 200), Vector2(0, 1), 'player_1')
        o = ServerObstacle(129, Vector2(246, 456), Vector2(0, 3), 'asteroid')
        self.objects = [o]
        self.objects_by_id = {
            o.id: o
        }
