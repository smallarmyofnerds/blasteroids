import signal
from blasteroids.client.game import Game
from blasteroids.client.server_connection import ServerConnection
from blasteroids.client.config import Config


config = Config('client.ini')

server_connection = ServerConnection()

game = Game(server_connection, config)


def tear_down(sig, frame):
    game.stop()


signal.signal(signal.SIGINT, tear_down)

game.start()
