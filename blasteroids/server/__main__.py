import signal
from .config import Config
from blasteroids.lib import log
from .game_server import GameServer
from .hub import Hub

config = Config('server.ini')

log.initialize_logging(config)
logger = log.get_logger(__name__)

hub = Hub()
hub.start()

server = GameServer(config, hub)


def tear_down(sig, frame):
    server.stop()
    hub.stop()


signal.signal(signal.SIGINT, tear_down)

server.start()
