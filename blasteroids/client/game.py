import pygame
import threading


class PlayerInputs:
    def __init__(self):
        self.left = False
        self.right = False
        self.up = False
        self.fire = False


class World:
    def __init__(self):
        self.players = []
        self.asteroids = []
        self.bullets = []
        self.powerups = []

    def draw(self):
        pass

    def update(self, buffer):
        pass


class RawWorld:
    def __init__(self) -> None:
        pass


class Game(threading.Thread):
    def __init__(self, server_connection):
        super(Game, self).__init__()
        pygame.init()
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.width = 300
        self.height = 300
        self.server_connection = server_connection
        self.world = World()
        self.world_buffer = RawWorld()

    def _update(self):
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
        self.world.draw()
        pygame.display.flip()

    def _init_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))

    def run(self):
        self._init_screen()
        while self.running:
            self.clock.tick(self.fps)
            self._process_inputs()
            self._update()
            self._draw()

    def stop(self):
        self.running = False
