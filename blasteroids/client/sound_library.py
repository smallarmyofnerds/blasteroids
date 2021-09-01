from pygame.mixer import Sound

class SoundLibrary:
    def __init__(self):
        self.sounds = {}

        self.sounds['laser'] = Sound('assets/sounds/laser.wav')
        self.sounds['impact'] = Sound('assets/sounds/impact.wav')
        self.sounds['shipimpact'] = Sound('assets/sounds/shipimpact.wav')

    def get_sound(self, name):
        return self.sounds[name]
