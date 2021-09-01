import pygame
from .game_object import GameObject


class EffectObject(GameObject):
    def __init__(self, server_object, sound_library):
        super(EffectObject, self).__init__(server_object)
        self.sound = pygame.mixer.Sound(sound_library.get_sound(server_object.name).get_raw())
        self.has_played = False

    def draw(self, screen, my_position):
        if not self.has_played:
            distance_to_sound = self.position.distance_squared_to(my_position)
            if distance_to_sound == 0:
                volume = 1.0
            else:
                volume = min(1.0, 200000 * 1 / self.position.distance_squared_to(my_position))
            self.sound.set_volume(volume)
            self.sound.play()
            self.has_played = True

    def update(self, raw_effect):
        super(EffectObject, self)._update(raw_effect.position, raw_effect.orientation)
