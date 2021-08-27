class PlayerState:
    def __init__(self, player):
        self.player = player


class LobbyState(PlayerState):
    def __init__(self, player, lobby):
        super(LobbyState, self).__init__(player)
        self.lobby = lobby

    def initialize(self):
        self.lobby.add_player(self.player)

    def handle_ENTR(self, message):
        self.player.queue_outgoing_message(message)

    def handle_REDY(self, message):
        self.lobby.add_player_to_hopper(self.player)


class Player:
    def __init__(self, client_connection, hub, name):
        self.client_connection = client_connection
        self.hub = hub
        self.name = name
        self.state = None

    def initialize(self):
        self.state = LobbyState(self.hub.lobby)
        self.state.initialize()

    def handle_message(self, message):
        message.dispatch(self.state)

    def queue_outgoing_message(self, message):
        self.client_connection.queue_message(message)
