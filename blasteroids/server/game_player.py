import threading
from .player_input_state import PlayerInputState
from .ship_object import ShipObject


class GamePlayer:
    def __init__(self, player):
        self.player = player
        self.ship = ShipObject(player)
        self.input_state = PlayerInputState()
        self.input_state_lock = threading.Lock()
        self.acceleration_rate = 1
        self.rotational_acceleration_rate = 2

    def process_input(self):
        self.ship.zero_accelerations()

        self.input_state_lock.acquire()

        if self.input_state.left:
            if self.input_state.right:
                pass
            else:
                self.ship.set_rotating_left(self.rotational_acceleration_rate)
        elif self.input_state.right:
            self.ship.set_rotating_right(self.rotational_acceleration_rate)
        if self.input_state.up:
            self.ship.set_accelerating(self.acceleration_rate)
        if self.input_state.fire:
            self.shoot()

        self.input_state_lock.release()

    def update(self):
        self.ship.update()
