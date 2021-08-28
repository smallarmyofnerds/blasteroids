import threading
from blasteroids.lib.client_messages.input import InputMessage
import pygame
from .screen import Screen
from .sprite_library import SpriteLibrary
from .world import World
from blasteroids.lib import log, PlayerInputs

logger = log.get_logger(__name__)


class Game:
    def __init__(self, server_connection, config):
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.screen = Screen(config.screen_width, config.screen_height)
        server_connection.game = self
        self.server_connection = server_connection
        self.something_pressed_last_time = False

        sprite_library = SpriteLibrary()
        sprite_library.load_all()
        self.world = World(sprite_library)

        self.lock = threading.Lock()
        self.world_buffer = None
        self.counter_delete_me = 0

    def update_world(self, server_world):
        self.lock.acquire()
        self.world_buffer = server_world
        self.lock.release()

    def _update(self):
        if self.world_buffer:
            self.world.update(self.world_buffer)
            if self.world.my_ship:
                self.screen.move_camera_to(self.world.my_ship.position)

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

        if inputs.is_anything_pressed():
            self.server_connection.queue_message(InputMessage.from_player_inputs(inputs))
            self.something_pressed_last_time = True
        else:
            if self.something_pressed_last_time:
                self.server_connection.queue_message(InputMessage.from_player_inputs(inputs))
                self.something_pressed_last_time = False
            else:
                pass

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
        if self.running:
            logger.info('Shutting down...')
            self.running = False
