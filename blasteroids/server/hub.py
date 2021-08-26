from blasteroids.lib.client_messages.entry import EntryMessage
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
        player.handle_message(EntryMessage(self.get_player_list()))

    def remove_player(self, player):
        self.players.remove(player)

    def get_player_list(self):
        return list(map(lambda p: p.name, self.players))

    def add_player_to_hopper(self, player):
        if player not in self.players:
            raise Exception('Player not found')

        if self.hopper.is_full():
            return

        self.hopper.add(player)
        if self.hopper.is_full():
            self.hub.start_game(self.hopper)
            self.hopper = Hopper(2)


class Hub(threading.Thread):
    def __init__(self):
        self.lobby = Lobby(self)
        self.game = None

    def start_game(self, hopper):
        if self.game is not None:
            raise Exception('Game already running')

        game = Game(hopper.players)
        game.start()
        self.game = game

    def run(self):
        self.running = True
        while self.running:
            pass
