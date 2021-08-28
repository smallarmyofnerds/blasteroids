import signal
from .config import Config
from blasteroids.lib import log
from .game_server import GameServer
from .game import Game

config = Config('server.ini')

log.initialize_logging(config)
logger = log.get_logger(__name__)

game = Game()
game.start()

server = GameServer(config, game)


def tear_down(sig, frame):
    game.stop()
    server.stop()


signal.signal(signal.SIGINT, tear_down)

server.start()
logger.info('Stopped')
