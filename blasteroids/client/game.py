from blasteroids.client.sound_library import SoundLibrary
import threading
from blasteroids.lib.client_messages.input import InputMessage
import pygame
from .screen import Screen
from .world import World
from .sprite_library import SpriteLibrary
from blasteroids.lib import log, PlayerInputs

logger = log.get_logger(__name__)


class Game:
    def __init__(self, server_connection, config):
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.screen = Screen(config.client.screen_width, config.client.screen_height)
        server_connection.game = self
        self.server_connection = server_connection
        self.something_pressed_last_time = False

        self.sprite_library = SpriteLibrary()
        self.sprite_library.load_all()
        self.sound_library = SoundLibrary()
        self.world = World(self.sprite_library, self.sound_library)

        self.lock = threading.Lock()
        self.world_buffer = None
        self.counter_delete_me = 0

    def initialize_world(self, world_width, world_height):
        self.screen.initialize_world(world_width, world_height)

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
            if event.type == pygame.VIDEORESIZE:
                self.screen.set_window_size(event.w, event.h)

        is_key_pressed = pygame.key.get_pressed()

        inputs = PlayerInputs()
        inputs.right = is_key_pressed[pygame.K_RIGHT] or is_key_pressed[pygame.K_d]
        inputs.left = is_key_pressed[pygame.K_LEFT] or is_key_pressed[pygame.K_a]
        inputs.up = is_key_pressed[pygame.K_UP] or is_key_pressed[pygame.K_w]
        inputs.fire = is_key_pressed[pygame.K_SPACE]

        if inputs.is_anything_pressed():
            if self.world.my_ship:
                self.server_connection.queue_message(InputMessage.from_player_inputs(inputs))
            self.something_pressed_last_time = True
        else:
            if self.something_pressed_last_time:
                if self.world.my_ship:
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
            try:
                self._process_inputs()
                self._update()
                self._draw()
            except Exception as e:
                logger.exception(e)

    def stop(self):
        if self.running:
            logger.info('Shutting down...')
            self.running = False
