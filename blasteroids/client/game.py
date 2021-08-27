from pygame.math import Vector2
from blasteroids.client.game_object import GameObject
import pygame
import threading
from .screen import Screen


class PlayerInputs:
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.fire = False


class ShipObject(GameObject):
    def __init__(self, id, position, orientation):
        super(ShipObject, self).__init__(id, position, orientation)

    def update(self, raw_ship):
        super(ShipObject, self)._update(raw_ship.position, raw_ship.orientation)

    def draw(self, screen):
        pygame.draw.rect(screen.surface, (0, 0, 255), (self.position.x, self.position.y, 100, 100))

    def destroy(self):
        print('Oh noes')


class ProjectileObject(GameObject):
    def __init__(self, id, position, orientation):
        super(ProjectileObject, self).__init__(id, position, orientation)
    
    def destroy(self):
        pass


class ObstacleObject(GameObject):
    def __init__(self, id, position, orientation):
        super(ObstacleObject, self).__init__(id, position, orientation)

    def draw(self, screen):
        pygame.draw.rect(screen.surface, (0, 255, 0), (self.position.x, self.position.y, 100, 100))

    def update(self, raw_obstacle):
        super(ObstacleObject, self)._update(raw_obstacle.position, raw_obstacle.orientation)

    def destroy(self):
        pass


class PowerUpObject(GameObject):
    def __init__(self, id, position, orientation):
        super(PowerUpObject, self).__init__(id, position, orientation)
    
    def destroy(self):
        pass


class World:
    def __init__(self):
        self.my_ship = None
        self.game_objects = []
        self.game_objects_by_id = {}

    def draw(self, screen):
        if self.my_ship:
            self.my_ship.draw(screen)
        for object in self.game_objects:
            object.draw(screen)

    def _destroy_objects(self, buffer):
        for object in self.game_objects:
            server_object = buffer.objects_by_id.get(object.id)
            if server_object:
                pass
            else:
                object.destroy()

    def _create_new_objects(self, buffer):
        for object in buffer.objects:
            existing_object = self.game_objects_by_id.get(object.id)
            if existing_object:
                existing_object.update(object)
            else:
                if object.type == 'SHIP':
                    new_object = ShipObject(object.id, object.position, object.orientation)
                elif object.type == 'PROJECTILE':
                    new_object = ProjectileObject(object.id, object.position, object.orientation)
                elif object.type == 'OBSTACLE':
                    new_object = ObstacleObject(object.id, object.position, object.orientation)
                elif object.type == 'POWERUP':
                    new_object = PowerUpObject(object.id, object.position, object.orientation)
                else:
                    raise Exception(f'Unrecognized object type {object.type} from server')

                self.game_objects.append(new_object)
                self.game_objects_by_id[new_object.id] = new_object

    def _sync_my_ship(self, buffer):
        if self.my_ship:
            if buffer.my_ship:
                self.my_ship.update(buffer.my_ship)
            else:
                self.my_ship.destroy()
                self.my_ship = None
        else:
            if buffer.my_ship:
                self.my_ship = ShipObject(buffer.my_ship.id, buffer.my_ship.position, buffer.my_ship.orientation)
            else:
                pass

    def update(self, buffer):
        self._sync_my_ship(buffer)
        self._destroy_objects(buffer)
        self._create_new_objects(buffer)


class RawObject:
    def __init__(self, type, id, position, orientation):
        self.type = type
        self.id = id
        self.position = position
        self.orientation = orientation


class RawShip(RawObject):
    def __init__(self, id, position, orientation):
        super(RawShip, self).__init__('SHIP', id, position, orientation)


class RawObstacle(RawObject):
    def __init__(self, id, position, orientation):
        super(RawObstacle, self).__init__('OBSTACLE', id, position, orientation)


class RawWorld:
    def __init__(self) -> None:
        self.my_ship = RawShip(12, Vector2(100, 200), Vector2(0, 1))
        o = RawObstacle(129, Vector2(246, 456), Vector2(0, 3))
        self.objects = [o]
        self.objects_by_id = {
            o.id: o
        }


class Game(threading.Thread):
    def __init__(self, server_connection, config):
        super(Game, self).__init__()
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.screen = Screen(config.screen_width, config.screen_height)
        self.server_connection = server_connection
        self.world = World()
        self.world_buffer = RawWorld()
        self.counter_delete_me = 0

    def _update(self):
        self.counter_delete_me += 1
        if self.counter_delete_me > 200:
            if self.counter_delete_me < 300:
                self.world_buffer.my_ship = None
            elif self.counter_delete_me == 300:
                self.world_buffer.my_ship = RawShip(12, Vector2(100, 100), Vector2(0, 1))
            else:
                self.world_buffer.my_ship.position = self.world_buffer.my_ship.position + Vector2(1, 0)
        else:
            self.world_buffer.my_ship.position = self.world_buffer.my_ship.position + Vector2(1, 0)
        self.world.update(self.world_buffer)

    def _process_inputs(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.stop()
                return

        is_key_pressed = pygame.key.get_pressed()

        inputs = PlayerInputs()
        inputs.right = is_key_pressed[pygame.K_RIGHT]
        inputs.left = is_key_pressed[pygame.K_LEFT]
        inputs.up = is_key_pressed[pygame.K_UP]
        inputs.fire = is_key_pressed[pygame.K_SPACE]

        self.server_connection.send_inputs(inputs)

    def _draw(self):
        self.screen.reset()
        self.world.draw(self.screen)
        pygame.display.flip()

    def run(self):
        self.screen.init()
        while self.running:
            self.clock.tick(self.fps)
            self._process_inputs()
            self._update()
            self._draw()

    def stop(self):
        print('Shutting down...')
        self.running = False
