from blasteroids.lib.server_world import server_object
from blasteroids.lib import log
import threading
import pygame
from .player import Player
from .world import World
from blasteroids.lib.client_messages import WelcomeMessage

logger = log.get_logger(__name__)


class Game(threading.Thread):
    def __init__(self, config):
        super(Game, self).__init__()
        self.running = False
        self.clock = pygame.time.Clock()
        self.players = [None] * 2
        self.world = World(config)
        self.fps = 60
        self.respawn_delay = 5000
        self.lock = threading.Lock()

    def _get_next_player_id(self):
        if self.players[0] is None:
            return 1
        if self.players[1] is None:
            return 2
        raise Exception('Too many players')
    
    def _get_next_player(self):
        player_id = self._get_next_player_id()
        player_name = f'player_{player_id}'
        return player_id, player_name

    def create_player(self, client_connection):
        self.lock.acquire()

        player_id, player_name = self._get_next_player()

        player = Player(player_name, client_connection)
        self.players[player_id - 1] = player
        
        client_connection.queue_message(WelcomeMessage(self.world.width, self.world.height))

        self.lock.release()

        return player

    def remove_player(self, player):
        self.lock.acquire()

        if player.ship:
            self.world.remove_ship(player.ship)

        if self.players[0] == player:
            self.players[0] = None
        elif self.players[1] == player:
            self.players[1] = None
        else:
            logger.error('Removing unknown player')
        
        self.lock.release()

    def _spawn_players(self):
        for player in self.players:
            if player and player.ship is None:
                if pygame.time.get_ticks() - player.get_died_at() > self.respawn_delay:
                    player.respawn(self.world)

    def _broadcast_updates(self):
        server_objects = self.world.to_server_objects()
        for player in self.players:
            if player:
                player.send_world(server_objects)

    def run(self):
        self.running = True
        while self.running:
            self.clock.tick(self.fps)
            self.lock.acquire()
            try:
                self.world.update(self.clock.get_time() / 1000.0)
                self._spawn_players()
                self._broadcast_updates()
            except Exception as e:
                logger.exception(e)
            finally:
                self.lock.release()

    def stop(self):
        if self.running:
            logger.info('Game shutting down')
            self.running = False
            self.join(2)
            logger.info('Done')
