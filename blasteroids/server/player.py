import threading
from blasteroids.lib.client_messages import WorldMessage


class Player:
    def __init__(self, ship, client_connection):
        self.ship = ship
        self.client_connection = client_connection
        self.inputs = None
        self.lock = threading.Lock()

    def update_inputs(self, inputs):
        self.lock.acquire()
        self.inputs = inputs
        self.lock.release()

    def process_input(self):
        self.ship.zero_accelerations()

        self.lock.acquire()

        if self.inputs:
            if self.inputs.left:
                if self.inputs.right:
                    pass
                else:
                    self.ship.set_rotating_left()
            elif self.inputs.right:
                self.ship.set_rotating_right()
            if self.inputs.up:
                self.ship.set_accelerating()
            if self.inputs.fire:
                self.shoot()

        self.inputs = None

        self.lock.release()

    def send_world(self, server_objects):
        self.client_connection.queue_message(WorldMessage(server_objects, self.ship.id))
