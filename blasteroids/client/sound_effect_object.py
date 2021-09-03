from .game_object import GameObject


class SoundEffectObject(GameObject):
    def __init__(self, server_object, sound_library):
        super(SoundEffectObject, self).__init__(server_object)
        self.sound = sound_library.get_sound(server_object.name)
        self.has_played = False

    def draw(self, screen, my_position):
        if not self.has_played:
            if my_position is None:
                volume = 1.0
            else:
                distance_to_sound = self.position.distance_squared_to(my_position)
                if distance_to_sound == 0:
                    volume = 1.0
                else:
                    volume = min(1.0, 200000 * 1 / self.position.distance_squared_to(my_position))
            self.sound.set_volume(volume)
            self.sound.play()
            self.has_played = True

    def update(self, raw_effect):
        super(SoundEffectObject, self)._update(raw_effect.position, raw_effect.orientation)
