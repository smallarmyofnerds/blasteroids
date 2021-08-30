import signal

import pygame
from .config import Config
from blasteroids.lib import log, SpriteLibrary
from .game_server import GameServer
from .game import Game

pygame.init()

config = Config('server.ini')

log.initialize_logging(config)
logger = log.get_logger(__name__)

game = Game(config)
game.start()

server = GameServer(config, game)


def tear_down(sig, frame):
    game.stop()
    server.stop()


signal.signal(signal.SIGINT, tear_down)

server.start()
logger.info('Stopped')
