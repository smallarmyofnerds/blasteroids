import threading
from blasteroids.lib.client_messages import WorldMessage


class Player:
    def __init__(self, name, ship, client_connection):
        self.name = name
        self.ship = ship
        self.client_connection = client_connection
        self.inputs = None
        self.lock = threading.Lock()

    def update_inputs(self, inputs):
        self.lock.acquire()
        self.inputs = inputs
        self.lock.release()

    def get_inputs(self):
        self.lock.acquire()
        inputs = self.inputs
        self.lock.release()
        return inputs

    def remove_ship(self):
        self.lock.acquire()
        self.ship = None
        self.lock.release()

    def send_world(self, server_objects):
        self.client_connection.queue_message(WorldMessage(server_objects, self.ship.id if self.ship is not None else 0))
