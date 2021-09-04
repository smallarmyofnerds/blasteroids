from .game_objects import AnimationObject, ProjectileObject, ObstacleObject, PickupObject, ProjectileObject, ShipObject, SoundEffectObject, MyShipObject
from .hud import Hud


class World:
    def __init__(self, sprite_library, sound_library):
        self.sprite_library = sprite_library
        self.sound_library = sound_library
        self.my_ship = None
        self.game_objects = []
        self.game_objects_by_id = {}
        self.hud = Hud(sprite_library)

    def draw(self, screen):
        for object in self.game_objects:
            object.draw(screen, self.my_ship.position if self.my_ship is not None else None)
        if self.my_ship:
            self.my_ship.draw(screen, None)
            self.hud.draw(screen)

    def _destroy_objects(self, server_world):
        objects_to_remove = []
        for object in self.game_objects:
            server_object = server_world.objects_by_id.get(object.id)
            if server_object:
                pass
            else:
                objects_to_remove.append(object)
        for object in objects_to_remove:
            self.game_objects.remove(object)
            del self.game_objects_by_id[object.id]

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
                elif object.type == 'PICKUP':
                    new_object = PickupObject(object, self.sprite_library)
                elif object.type == 'SOUND':
                    new_object = SoundEffectObject(object, self.sound_library)
                elif object.type == 'ANIM':
                    new_object = AnimationObject(object, self.sprite_library)
                else:
                    raise Exception(f'Unrecognized object type {object.type} from server')

                self.game_objects.append(new_object)
                self.game_objects_by_id[new_object.id] = new_object

    def _sync_my_ship(self, server_world):
        if self.my_ship:
            if server_world.my_ship:
                self.my_ship.update(server_world.my_ship, server_world.is_engine_on)
            else:
                self.my_ship = None
        else:
            if server_world.my_ship:
                self.my_ship = MyShipObject(server_world.my_ship, self.sprite_library, server_world.is_engine_on)
            else:
                pass

    def _sync_hud(self, server_world):
        self.hud.update(server_world.health, server_world.shield, server_world.active_weapon)

    def update(self, server_world):
        self._sync_hud(server_world)
        self._sync_my_ship(server_world)
        self._destroy_objects(server_world)
        self._create_new_objects(server_world)
