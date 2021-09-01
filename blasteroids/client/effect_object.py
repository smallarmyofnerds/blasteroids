from .game_object import GameObject


class EffectObject(GameObject):
    def __init__(self, server_object, sound_library):
        super(EffectObject, self).__init__(server_object)
        self.sound = sound_library.get_sound(server_object.name)
        self.has_played = False

    def draw(self, screen):
        if not self.has_played:
            self.sound.play()
            self.has_played = True

    def update(self, raw_effect):
        super(EffectObject, self)._update(raw_effect.position, raw_effect.orientation)
