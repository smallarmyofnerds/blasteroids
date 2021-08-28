from blasteroids.lib import log
import threading
import pygame
from .player import Player
from .world import World

logger = log.get_logger(__name__)


class Game(threading.Thread):
    def __init__(self):
        super(Game, self).__init__()
        self.running = False
        self.clock = pygame.time.Clock()
        self.players = [None] * 2
        self.world = World()
        self.fps = 30

    def _get_next_player_id(self):
        if self.players[0] is None:
            return 1
        if self.players[1] is None:
            return 2
        raise Exception('Too many players')

    def create_player(self, client_connection):
        player_id = self._get_next_player_id()
        ship = self.world.create_ship(f'player_{player_id}')
        player = Player(ship, client_connection)
        self.players[player_id - 1] = player
        return player

    def remove_player(self, player):
        if self.players[0] == player:
            self.players[0] = None
        elif self.players[1] == player:
            self.players[1] = None
        raise Exception('Unknown player')

    def _process_inputs(self):
        for player in self.players:
            if player:
                player.process_input()

    def _broadcast_updates(self):
        server_objects = self.world.to_server_objects()
        for player in self.players:
            if player:
                player.send_world(server_objects)

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(self.fps)
            self._process_inputs()
            self.world.update()
            self._broadcast_updates()

    def stop(self):
        if self.running:
            logger.info('Game shutting down')
            self.running = False
            self.join(2)
            logger.info('Done')
