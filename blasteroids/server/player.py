from blasteroids.lib.player_inputs import PlayerInputs
import threading

import pygame
from blasteroids.lib.client_messages import WorldMessage
from blasteroids.lib import log

logger = log.get_logger(__name__)


class Player:
    def __init__(self, name, client_connection):
        self.name = name
        self.ship = None
        self.client_connection = client_connection
        self.inputs = PlayerInputs()
        self.died_at = 0
        self.lock = threading.Lock()

    def respawn(self, world):
        logger.info(f'Spawning {self.name}')
        self.lock.acquire()
        self.ship = world.create_ship(self)
        self.died_at = 0
        self.lock.release()

    def update_inputs(self, inputs):
        self.lock.acquire()
        if self.ship:
            self.inputs = inputs
        self.lock.release()

    def get_inputs(self):
        self.lock.acquire()
        inputs = self.inputs
        self.lock.release()
        return inputs

    def kill(self):
        self.lock.acquire()
        self.ship = None
        self.inputs = PlayerInputs()
        self.died_at = pygame.time.get_ticks()
        self.lock.release()
    
    def get_died_at(self):
        self.lock.acquire()
        died_at = self.died_at
        self.lock.release()
        return died_at

    def send_world(self, server_objects):
        self.client_connection.queue_message(
            WorldMessage(
                server_objects,
                self.ship.id if self.ship is not None else 0,
                self.ship.health if self.ship is not None else 0,
                self.ship.shield if self.ship is not None else 0,
                self.ship.get_active_weapon() if self.ship is not None else '',
            ),
        )
