import pygame
from pygame.mixer import Sound

class SoundLibrary:
    def __init__(self):
        self.sounds = {}
        pygame.mixer.init()
        pygame.mixer.set_num_channels(16)

        self.sounds['laser'] = Sound('assets/sounds/laser.wav')
        self.sounds['impact'] = Sound('assets/sounds/impact.wav')
        self.sounds['shipimpact'] = Sound('assets/sounds/shipimpact.wav')
        self.sounds['healing_pickup'] = Sound('assets/sounds/healing_pickup.wav')
        self.sounds['shielding_pickup'] = Sound('assets/sounds/shielding_pickup.wav')
        self.sounds['rapid_fire_pickup'] = Sound('assets/sounds/rapid_fire_pickup.wav')
        self.sounds['spread_fire_pickup'] = Sound('assets/sounds/spread_fire_pickup.wav')
        self.sounds['double_fire_pickup'] = Sound('assets/sounds/double_fire_pickup.wav')
        self.sounds['rocket_pickup'] = Sound('assets/sounds/rocket_pickup.wav')
        self.sounds['rocket_salvo_pickup'] = Sound('assets/sounds/rocket_salvo_pickup.wav')
        self.sounds['time_bomb_pickup'] = Sound('assets/sounds/time_bomb_pickup.wav')
        self.sounds['proximity_mine_pickup'] = Sound('assets/sounds/proximity_mine_pickup.wav')
        self.sounds['mega_pickup'] = Sound('assets/sounds/mega_pickup.wav')
        self.sounds['rocket_shot'] = Sound('assets/sounds/rocket_shot.wav')
        self.sounds['time_bomb_shot'] = Sound('assets/sounds/time_bomb_shot.wav')
        self.sounds['rocket_salvo_shot'] = Sound('assets/sounds/rocket_salvo_shot.wav')
        self.sounds['rocket_explosion'] = Sound('assets/sounds/rocket_explosion.wav')
        self.sounds['rocket_salvo_explosion'] = Sound('assets/sounds/rocket_salvo_explosion.wav')

    def get_sound(self, name):
        return self.sounds[name]
