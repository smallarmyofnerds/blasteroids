import threading
import pygame
from .game_player import GamePlayer


class World:
    def __init__(self):
        self.ships = []
        self.projectiles = []
        self.power_ups = []
        self.obstacles = []

    def add_ship(self, ship):
        self.ships.append(ship)

    def remove_ship(self, ship):
        self.ships.remove(ship)

    def _update_all(self):
        for o in [*self.ships, *self.projectiles, *self.power_ups, *self.obstacles]:
            o.update()

    def _test_ship_collisions(self):
        for ship in self.ships:
            for other in [*self.ships, *self.obstacles]:
                if ship == other:
                    continue
                if ship.collides_with(other):
                    ship.apply_damage_to(other)
                    other.apply_damage_to(ship)
                    if ship.health == 0:
                        ship.destroy(self)
                    if other.health == 0:
                        other.destroy(self)

    def _test_projectile_collisions(self):
        for projectile in self.projectiles:
            for other in [*self.ships, *self.obstacles]:
                if projectile.collides_with(other):
                    projectile.apply_damage_to(other)
                    projectile.destroy(self)
                    if other.health == 0:
                        other.destroy(self)

    def _test_power_up_collisions(self):
        for ship in self.ships:
            for power_up in self.power_ups:
                if ship.collides_with(power_up):
                    power_up.apply_power_up_to(ship)
                    power_up.destroy(self)

    def update(self):
        self._update_all()
        self._test_ship_collisions()
        self._test_projectile_collisions()
        self._test_power_up_collisions()


class Game(threading.Thread):
    def __init__(self):
        self.running = False
        self.players = []
        self.world = World()
        self.fps = 30

    def add_player(self, player):
        self.players.append(GamePlayer(player))

    def _process_inputs(self):
        for player in self.players:
            player.process_input()

    def _broadcast_updates(self):
        for player in self.players:
            player.send_world(self.world)

    def run(self):
        self.running = True
        while self.running:
            pygame.clock.tick(self.fps)
            self._process_inputs()
            self.world.update()
            self._broadcast_updates()
