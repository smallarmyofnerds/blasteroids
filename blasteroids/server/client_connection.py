import select
import threading
from blasteroids.lib import log, WelcomeMessage, MessageEncoding, EncodedMessage
import blasteroids.lib.client_messages as client_messages
from blasteroids.lib.util import SynchronizedQueue

logger = log.get_logger(__name__)


class ClientConnectionState:
    def __init__(self, client_connection, hub):
        self.client_connection = client_connection
        self.hub = hub

    def _change_state(self, new_state):
        self.client_connection.set_state(new_state)

    def queue_client_message(self, message):
        self.client_connection.queue_message(message)

    def queue_game_message(self, message):
        self.hub.queue_message(message)

    def handle_message(self, message):
        message.dispatch(self)

    def handle_HELO(self):
        raise Exception('Unexpected HELO')

    def handle_INPT(self):
        raise Exception('Unexpected INPT')


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


class ConnectedState(ClientConnectionState):
    def __init__(self, client_connection, hub, player_name):
        super(ConnectedState, self).__init__(client_connection, hub)
        self.player = Player(client_connection, hub, player_name)

    def initialize(self):
        self.player.initialize()

    def handle_message(self, message):
        self.player.handle_message(message)

    def __repr__(self):
        return 'Connected'


class HandshakeState(ClientConnectionState):
    def __init__(self, client_connection, hub, server_name, welcome_message):
        super(HandshakeState, self).__init__(client_connection, hub)
        self.server_name = server_name
        self.welcome_message = welcome_message

    def initialize(self):
        self.queue_client_message(client_messages.WelcomeMessage(self.server_name, self.welcome_message))

    def handle_HELO(self, message):
        self._change_state(ConnectedState(self.client_connection, self.hub, message.player_name))

    def __repr__(self):
        return 'Handshake'


client_message_encoders = {
    client_messages.HelloMessage.TYPE: client_messages.HelloMessageEncoder(),
    client_messages.WelcomeMessage.TYPE: client_messages.WelcomeMessageEncoder(),
    client_messages.ReadyMessage.TYPE: client_messages.ReadyMessageEncoder(),
}


class ClientConnection(threading.Thread):
    def __init__(self, id, socket, address, config, hub, game_server):
        super(ClientConnection, self).__init__()
        self.id = id
        self.socket = socket
        self.is_running = True
        self.address = address
        self.server_name = config.server_name
        self.welcome_message = config.welcome_message
        self.hub = hub
        self.game_server = game_server
        self.message_encoding = MessageEncoding(client_message_encoders)
        self.state = None
        self.outgoing_messages = SynchronizedQueue()

    def queue_message(self, message):
        self.outgoing_messages.push(message)

    def _send_message(self, message):
        self.socket.send(self.message_encoding.encode(message))

    def _receive_message(self):
        encoded_bytes = self.socket.recv(8192)
        return self.message_encoding.decode(EncodedMessage(encoded_bytes))

    def set_state(self, state):
        self.state = state
        logger.info(f'Set state to {state}')
        state.initialize()

    def _flush_outgoing_messages(self):
        while not self.outgoing_messages.is_empty():
            message = self.outgoing_messages.pop()
            logger.info(f'Sending {message}')
            self._send_message(message)

    def run(self):
        logger.info('Running client connection')

        try:
            self.set_state(HandshakeState(self, self.hub, self.id, self.server_name, self.welcome_message))

            while self.is_running:
                readable, writable, exceptional = select.select([self.socket], [self.socket] if not self.outgoing_messages.is_empty() else [], [self.socket])

                for _ in readable:
                    message = self._receive_message()
                    logger.info(f'Received {message}')
                    self.state.handle_message(message)

                for _ in writable:
                    self._flush_outgoing_messages()

                for _ in exceptional:
                    self.socket.close()
                    self.is_running = False
                    self.game_server.remove_connection(self)

        except Exception as e:
            logger.error(e)
