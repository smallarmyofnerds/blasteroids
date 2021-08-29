from .ship_object import ShipObject
from .projectile_object import ProjectileObject
from .obstacle_object import ObstacleObject
from .power_up_object import PowerUpObject


class World:
    def __init__(self, sprite_library):
        self.sprite_library = sprite_library
        self.my_ship = None
        self.game_objects = []
        self.game_objects_by_id = {}

    def draw(self, screen):
        if self.my_ship:
            self.my_ship.draw(screen)
        for object in self.game_objects:
            object.draw(screen)

    def _destroy_objects(self, server_world):
        for object in self.game_objects:
            server_object = server_world.objects_by_id.get(object.id)
            if server_object:
                pass
            else:
                object.destroy()

    def _create_new_objects(self, server_world):
        for object in server_world.objects:
            existing_object = self.game_objects_by_id.get(object.id)
            if existing_object:
                existing_object.update(object)
            else:
                if object.type == 'SHIP':
                    new_object = ShipObject(object, self.sprite_library)
                elif object.type == 'PROJECTILE':
                    new_object = ProjectileObject(object, self.sprite_library)
                elif object.type == 'OBSTACLE':
                    new_object = ObstacleObject(object, self.sprite_library)
                elif object.type == 'POWERUP':
                    new_object = PowerUpObject(object, self.sprite_library)
                else:
                    raise Exception(f'Unrecognized object type {object.type} from server')

                self.game_objects.append(new_object)
                self.game_objects_by_id[new_object.id] = new_object

    def _sync_my_ship(self, server_world):
        if self.my_ship:
            if server_world.my_ship:
                self.my_ship.update(server_world.my_ship)
            else:
                self.my_ship.destroy()
                self.my_ship = None
        else:
            if server_world.my_ship:
                self.my_ship = ShipObject(server_world.my_ship, self.sprite_library)
            else:
                pass

    def update(self, server_world):
        self._sync_my_ship(server_world)
        self._destroy_objects(server_world)
        self._create_new_objects(server_world)
