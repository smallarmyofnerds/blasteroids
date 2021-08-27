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
        self.running = True
        self.fps = 30
        self.server_connection = server_connection
        self.world = World()
        self.world_buffer = RawWorld()

    def _update(self):
        self.world.update(self.world_buffer)

    def _process_inputs(self):
        # Read pygame inputs
        inputs = PlayerInputs()
        #inputs.left = asdflkj

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.stop()
                return

            

        
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if self.replay_rect.collidepoint(pos):
                    self.new_game()


        is_key_pressed = pygame.key.get_pressed()
        
        
        inputs.right = is_key_pressed[pygame.K_RIGHT]

        inputs.left = is_key_pressed[pygame.K_LEFT]

        inputs.up = is_key_pressed[pygame.K_UP]
        
        inputs.fire = is_key_pressed[pygame.K_SPACE]
        
        self.server_connection.send_inputs(inputs)

    def _draw(self):
        self.world.draw()

    def run(self):
        while self.running:
            pygame.clock.tick(self.fps)
            self.process_inputs()
            self.update()
            self.draw()

    def stop(self):
        self.running = False