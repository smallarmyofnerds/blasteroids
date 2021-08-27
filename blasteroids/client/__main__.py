from game import Game


class ServerConnection:
    def send_inputs(self, inputs):
        pass


server_connection = ServerConnection()

game = Game(server_connection)

game.start()
