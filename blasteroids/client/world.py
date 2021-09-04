from blasteroids.lib.constants import ANIMATION_OBJECT_ID, ASTEROID_OBJECT_ID, PICKUP_OBJECT_ID, PROJECTILE_OBJECT_ID, SHIP_OBJECT_ID, SOUND_OBJECT_ID
from .game_objects import AnimationObject, ProjectileObject, AsteroidObject, PickupObject, ShipObject, SoundEffectObject
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
            server_object = server_world.objects_by_id.get(object.object_id)
            if server_object:
                pass
            else:
                objects_to_remove.append(object)
        for object in objects_to_remove:
            self.game_objects.remove(object)
            del self.game_objects_by_id[object.object_id]

    def _create_new_objects(self, server_world):
        for object in server_world.objects:
            existing_object = self.game_objects_by_id.get(object.object_id)
            if existing_object:
                existing_object.update(object)
            else:
                if object.type_id == SHIP_OBJECT_ID:
                    new_object = ShipObject(object, self.sprite_library)
                elif object.type_id == PROJECTILE_OBJECT_ID:
                    new_object = ProjectileObject(object, self.sprite_library)
                elif object.type_id == ASTEROID_OBJECT_ID:
                    new_object = AsteroidObject(object, self.sprite_library)
                elif object.type_id == PICKUP_OBJECT_ID:
                    new_object = PickupObject(object, self.sprite_library)
                elif object.type_id == SOUND_OBJECT_ID:
                    new_object = SoundEffectObject(object, self.sound_library)
                elif object.type_id == ANIMATION_OBJECT_ID:
                    new_object = AnimationObject(object, self.sprite_library)
                else:
                    raise Exception(f'Unrecognized object type {object.type_id} from server')

                self.game_objects.append(new_object)
                self.game_objects_by_id[new_object.object_id] = new_object

    def _sync_my_ship(self, server_world):
        if self.my_ship:
            if server_world.my_ship:
                self.my_ship.update(server_world.my_ship)
            else:
                self.my_ship = None
        else:
            if server_world.my_ship:
                self.my_ship = ShipObject(server_world.my_ship, self.sprite_library)
            else:
                pass

    def _sync_hud(self, server_world):
        if server_world.my_ship:
            self.hud.update(server_world.my_ship.health, server_world.my_ship.shield, server_world.my_ship.active_weapon_id)

    def update(self, server_world):
        self._sync_hud(server_world)
        self._destroy_objects(server_world)
        self._create_new_objects(server_world)
        self._sync_my_ship(server_world)
