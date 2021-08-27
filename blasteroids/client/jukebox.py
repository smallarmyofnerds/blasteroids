import pygame

class Jukebox():
    def __init__(self):
        self.songs = ['battle_1.wav', 'battle_1.wav', 'battle_1.wav']
        self.current_song = 0

    def play(self):
        pygame.mixer.music.load(f"assets/sounds/{self.songs[self.current_song]}")
        pygame.mixer.music.play(-1)
        
    def skip(self):
        self.current_song = (self.current_song + 1) % len(self.songs)
        self.play()