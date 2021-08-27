import pygame
import threading
from pygame.math import Vector2
from .screen import Screen
from .sprite_library import SpriteLibrary
from .world import World
from .server_world import ServerWorld
from .server_ship import ServerShip
from .player_inputs import PlayerInputs


class Game(threading.Thread):
    def __init__(self, server_connection, config):
        super(Game, self).__init__()
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.screen = Screen(config.screen_width, config.screen_height)
        self.server_connection = server_connection

        sprite_library = SpriteLibrary()
        sprite_library.load_all()
        self.world = World(sprite_library)

        self.world_buffer = ServerWorld()
        self.counter_delete_me = 0

    def _update(self):
        self.counter_delete_me += 1
        if self.counter_delete_me > 200:
            if self.counter_delete_me < 300:
                self.world_buffer.my_ship = None
            elif self.counter_delete_me == 300:
                self.world_buffer.my_ship = ServerShip(12, Vector2(100, 100), Vector2(0, 1), 'player_1')
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
