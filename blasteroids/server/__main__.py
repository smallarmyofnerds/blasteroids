import signal
from .config import Config
from blasteroids.lib import log
from .game_server import GameServer

config = Config('server.ini')

log.initialize_logging(config)
logger = log.get_logger(__name__)

server = GameServer(config.server_address, config.server_port, config)
signal.signal(signal.SIGINT, lambda sig, frame : server.stop())
server.start()
