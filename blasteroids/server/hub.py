import threading


class Hopper:
    def __init__(self, slots):
        self.slots = slots
        self.players = []

    def is_full(self):
        return len(self.players) == self.slots

    def add(self, player):
        if self.is_full():
            raise Exception('Hopper is full')

        self.players.append(player)

    def remove(self, player):
        self.players.remove(player)


class Lobby:
    def __init__(self, hub):
        self.hub = hub
        self.hopper = Hopper(2)
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, player):
        self.players.remove(player)

    def add_player_to_hopper(self, player):
        if player not in self.players:
            raise Exception('Player not found')

        if self.hopper.is_full():
            return

        self.hopper.add(player)


class Hub(threading.Thread):
    def __init__(self):
        self.lobby = Lobby(self)
        self.client_connections = []
        self.client_connections_lock = threading.Lock()

    def add_client_connection(self, client_connection):
        self.client_connections_lock.acquire()
        self.client_connections.append(client_connection)
        self.client_connections_lock.release()

    def run(self):
        self.running = True
        while self.running:
            pass
