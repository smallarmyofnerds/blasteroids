import signal
from blasteroids.lib import log
from blasteroids.client.game import Game
from blasteroids.client.server_connection import ServerConnection
from blasteroids.client.config import Config


config = Config('client.ini')

log.initialize_logging(config)
logger = log.get_logger(__name__)

server_connection = ServerConnection(config)
game = Game(server_connection, config)


def tear_down(sig, frame):
    game.stop()
    server_connection.stop()


signal.signal(signal.SIGINT, tear_down)

server_connection.start()
game.run()
server_connection.stop()
